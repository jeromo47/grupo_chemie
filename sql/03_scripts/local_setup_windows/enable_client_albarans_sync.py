#!/usr/bin/env python3
"""Activa la sincronización READ ONLY de albaranes de CLIENTE de MasterSQL.

Objetivo:
1. Validar que LINEASALBAC existe en CHEMIE, ACI y ECOCLEAN.
2. Comprobar columnas mínimas para construir el histórico comercial real.
3. Mostrar una prueba concreta del albarán 710 de CHEMIE / cliente 621.
4. Añadir LINEASALBAC (y GENERALALBAC si existe) a config.json -> tablas_objetivo.
5. Opcionalmente ejecutar el pipeline de producción.

No escribe nunca en Firebird/MasterSQL. Solo modifica config.json local con backup
cuando se usa --apply.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import fdb


ROOT = Path(r"C:\grupo_chemie")
CONFIG_CANDIDATES = (
    ROOT / "config.json",
    ROOT / "config" / "config.json",
)
PIPELINE = ROOT / "scripts" / "run_pipeline_produccion.py"
PYTHON = ROOT / "venv" / "Scripts" / "python.exe"

LINE_TABLE = "LINEASALBAC"
HEADER_TABLE = "GENERALALBAC"

REQUIRED_LINE_COLUMNS = {
    "CODIGOID",
    "TIENDA",
    "LINEA",
    "EJERCICIO",
    "SERIE",
    "FECHA",
    "CODIGOCLIENTE",
    "NUMERODOCUMENTO",
    "REFERENCIA1",
    "REFERENCIA2",
    "REFERENCIA3",
    "DESCRIPCION",
    "CANTIDAD",
    "PRECIOSINIVA",
    "TOTALLINEA",
}

OPTIONAL_LINE_COLUMNS = {
    "ANULADO",
    "TOTALLINEAREAL",
}


def load_config() -> tuple[Path, dict]:
    for path in CONFIG_CANDIDATES:
        if path.exists():
            return path, json.loads(path.read_text(encoding="utf-8"))
    checked = "\n".join(f"  - {path}" for path in CONFIG_CANDIDATES)
    raise FileNotFoundError(f"No se encontró config.json. Rutas comprobadas:\n{checked}")


def validate_config(config: dict) -> None:
    required = [
        "fbclient_dll",
        "host",
        "puerto",
        "usuario",
        "password",
        "empresas",
        "tablas_objetivo",
    ]
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"Faltan claves en config.json: {missing}")
    if not isinstance(config["tablas_objetivo"], list):
        raise TypeError("config.json -> tablas_objetivo debe ser una lista")
    if not config["empresas"]:
        raise ValueError("config.json -> empresas está vacío")


def load_firebird_api(config: dict) -> None:
    dll = Path(config["fbclient_dll"])
    if not dll.exists():
        raise FileNotFoundError(f"No existe fbclient: {dll}")
    os.add_dll_directory(str(dll.parent))
    fdb.load_api(str(dll))


def read_only_tpb() -> fdb.TPB:
    tpb = fdb.TPB()
    tpb.access_mode = fdb.isc_tpb_read
    tpb.isolation_level = fdb.isc_tpb_concurrency
    tpb.lock_resolution = fdb.isc_tpb_wait
    return tpb


def connect_company(config: dict, company_config: dict):
    charset_raw = str(config.get("charset_conexion", "")).strip()
    charset = None if not charset_raw or charset_raw.upper().startswith("PENDIENTE") else charset_raw
    dsn = f"{config['host']}/{config['puerto']}:{company_config['fdb']}"
    return fdb.connect(
        dsn=dsn,
        user=config["usuario"],
        password=config["password"],
        charset=charset,
    )


def user_tables(cursor) -> set[str]:
    cursor.execute(
        """
        SELECT TRIM(RDB$RELATION_NAME)
        FROM RDB$RELATIONS
        WHERE COALESCE(RDB$SYSTEM_FLAG,0)=0
          AND RDB$VIEW_BLR IS NULL
        """
    )
    return {str(row[0]).strip().upper() for row in cursor.fetchall()}


def table_columns(cursor, table_name: str) -> set[str]:
    cursor.execute(
        """
        SELECT TRIM(rf.RDB$FIELD_NAME)
        FROM RDB$RELATION_FIELDS rf
        JOIN RDB$RELATIONS r
          ON r.RDB$RELATION_NAME = rf.RDB$RELATION_NAME
        WHERE rf.RDB$RELATION_NAME = ?
          AND COALESCE(r.RDB$SYSTEM_FLAG,0)=0
          AND r.RDB$VIEW_BLR IS NULL
        ORDER BY rf.RDB$FIELD_POSITION
        """,
        (table_name,),
    )
    return {str(row[0]).strip().upper() for row in cursor.fetchall()}


def inspect_company(config: dict, company: str, company_config: dict) -> dict:
    db_path = Path(company_config["fdb"])
    if not db_path.exists():
        raise FileNotFoundError(f"[{company}] no existe la base: {db_path}")

    conn = connect_company(config, company_config)
    tr = conn.trans(default_tpb=read_only_tpb())
    cur = tr.cursor()

    try:
        tables = user_tables(cur)
        if LINE_TABLE not in tables:
            alba_candidates = sorted(t for t in tables if "ALBA" in t)
            raise RuntimeError(
                f"[{company}] no existe {LINE_TABLE}. "
                f"Tablas con 'ALBA': {alba_candidates}"
            )

        columns = table_columns(cur, LINE_TABLE)
        missing = sorted(REQUIRED_LINE_COLUMNS - columns)
        if missing:
            raise RuntimeError(
                f"[{company}] {LINE_TABLE} no tiene las columnas requeridas: {missing}"
            )

        cur.execute(f"SELECT COUNT(*) FROM {LINE_TABLE}")
        total_rows = int(cur.fetchone()[0] or 0)

        header_exists = HEADER_TABLE in tables
        optional = sorted(OPTIONAL_LINE_COLUMNS & columns)

        sample_710 = []
        if company.upper() == "CHEMIE":
            cur.execute(
                f"""
                SELECT
                    FECHA,
                    CODIGOCLIENTE,
                    NUMERODOCUMENTO,
                    REFERENCIA1,
                    DESCRIPCION,
                    CANTIDAD,
                    PRECIOSINIVA,
                    TOTALLINEA
                FROM {LINE_TABLE}
                WHERE CODIGOCLIENTE = ?
                  AND NUMERODOCUMENTO = ?
                ORDER BY LINEA
                """,
                (621, 710),
            )
            for row in cur.fetchall():
                sample_710.append(
                    {
                        "fecha": str(row[0]) if row[0] is not None else None,
                        "cliente": row[1],
                        "albaran": row[2],
                        "referencia": str(row[3]).strip() if row[3] is not None else None,
                        "descripcion": str(row[4]).strip() if row[4] is not None else None,
                        "cantidad": float(row[5]) if row[5] is not None else None,
                        "precio_sin_iva": float(row[6]) if row[6] is not None else None,
                        "total_linea": float(row[7]) if row[7] is not None else None,
                    }
                )

        tr.rollback()
        return {
            "company": company,
            "rows": total_rows,
            "header_exists": header_exists,
            "optional_columns": optional,
            "sample_710": sample_710,
        }
    except Exception:
        try:
            tr.rollback()
        except Exception:
            pass
        raise
    finally:
        conn.close()


def backup_and_patch_config(config_path: Path, config: dict, include_header: bool) -> Path | None:
    existing = [str(value).upper() for value in config["tablas_objetivo"]]
    targets = [LINE_TABLE]
    if include_header:
        targets.append(HEADER_TABLE)

    missing_targets = [table for table in targets if table not in existing]
    if not missing_targets:
        print("config.json ya contiene las tablas de albaranes de cliente.")
        return None

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = config_path.with_name(
        f"{config_path.stem}.backup_albaranes_cliente_{timestamp}{config_path.suffix}"
    )
    shutil.copy2(config_path, backup)

    updated = json.loads(json.dumps(config))
    updated["tablas_objetivo"].extend(missing_targets)
    config_path.write_text(
        json.dumps(updated, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"config.json actualizado: {config_path}")
    print(f"Copia de seguridad: {backup}")
    print("Añadidas: " + ", ".join(missing_targets))
    return backup


def run_pipeline() -> None:
    if not PYTHON.exists():
        raise FileNotFoundError(f"No existe Python del proyecto: {PYTHON}")
    if not PIPELINE.exists():
        raise FileNotFoundError(f"No existe pipeline: {PIPELINE}")

    print()
    print("=" * 96)
    print("EJECUTANDO PIPELINE DE PRODUCCIÓN")
    print("=" * 96)
    completed = subprocess.run(
        [str(PYTHON), str(PIPELINE)],
        cwd=str(ROOT),
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"El pipeline terminó con código {completed.returncode}.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Añade LINEASALBAC y, si existe en las 3 empresas, GENERALALBAC a config.json.",
    )
    parser.add_argument(
        "--run-pipeline",
        action="store_true",
        help="Ejecuta el pipeline de producción después de aplicar el cambio.",
    )
    args = parser.parse_args()

    if args.run_pipeline and not args.apply:
        parser.error("--run-pipeline requiere --apply")

    config_path, config = load_config()
    validate_config(config)
    load_firebird_api(config)

    print("=" * 96)
    print("VALIDACIÓN READ ONLY DE ALBARANES DE CLIENTE")
    print("=" * 96)
    print(f"Config: {config_path}")
    print("Firebird/MasterSQL: solo lectura")

    results = []
    for company, company_config in config["empresas"].items():
        print(f"Inspeccionando {company}...")
        result = inspect_company(config, company, company_config)
        results.append(result)
        print(
            f"  {LINE_TABLE}={result['rows']:,} líneas | "
            f"{HEADER_TABLE}={'sí' if result['header_exists'] else 'no'} | "
            f"opcionales={result['optional_columns']}"
        )

    chemie = next((r for r in results if r["company"].upper() == "CHEMIE"), None)
    if chemie is not None:
        print()
        print("PRUEBA CHEMIE · CLIENTE 621 · ALBARÁN 710")
        if not chemie["sample_710"]:
            print("  No se ha localizado el albarán 710 en LINEASALBAC.")
            print("  No se aplicará ningún cambio automáticamente.")
            return 2
        for row in chemie["sample_710"]:
            print(
                f"  {row['fecha']} | ref {row['referencia']} | "
                f"{row['descripcion']} | cantidad {row['cantidad']} | "
                f"{row['total_linea']:.2f} €"
            )

    include_header = all(result["header_exists"] for result in results)

    if not args.apply:
        print()
        print("MODO DIAGNÓSTICO: no se ha modificado ningún archivo.")
        print("Para activar y sincronizar:")
        print(
            rf'"{PYTHON}" "{Path(__file__)}" --apply --run-pipeline'
        )
        return 0

    backup = backup_and_patch_config(config_path, config, include_header)

    try:
        if args.run_pipeline:
            run_pipeline()
    except Exception:
        if backup is not None and backup.exists():
            shutil.copy2(backup, config_path)
            print()
            print(
                "El pipeline falló. Se ha restaurado config.json para no romper "
                "futuras ejecuciones."
            )
        raise

    print()
    print("=" * 96)
    print("ALBARANES DE CLIENTE ACTIVADOS")
    print("=" * 96)
    print(f"{LINE_TABLE} queda incluido en cada extracción normal.")
    if include_header:
        print(f"{HEADER_TABLE} también queda incluido.")
    print(
        "Supabase recibirá raw_<empresa>_lineasalbac. "
        "La app comercial la consumirá automáticamente en el siguiente refresh."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print()
        print("=" * 96)
        print("ERROR")
        print("=" * 96)
        print(f"{type(exc).__name__}: {exc}")
        raise SystemExit(1)
