#!/usr/bin/env python3
"""Activa la sincronización READ ONLY de CONTACTOS de MasterSQL.

Uso diagnóstico:
  C:\grupo_chemie\venv\Scripts\python.exe C:\grupo_chemie\sql\03_scripts\local_setup_windows\enable_contacts_sync.py

Activar y lanzar pipeline:
  C:\grupo_chemie\venv\Scripts\python.exe C:\grupo_chemie\sql\03_scripts\local_setup_windows\enable_contacts_sync.py --apply --run-pipeline

El script nunca escribe en Firebird/MasterSQL. Solo modifica config.json con copia
de seguridad cuando se usa --apply.
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
TARGET_TABLE = "CONTACTOS"

REQUIRED_CONTACT_COLUMNS = {
    "CODIGO",
    "PERSONACONTACTO",
    "CLIENTEPROVEEDOR",
    "RAZONSOCIAL",
    "NOMBRECOMERCIAL",
    "DEPARTAMENTO",
    "TELEFONO",
    "EXTENSION",
    "MOVIL",
    "FAX",
    "CORREOELECTRONICO",
}

REQUIRED_CLIENT_COLUMNS = {
    "CODIGOID",
    "CODIGO",
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


def table_columns(cursor, table_name: str) -> set[str]:
    cursor.execute(
        """
        SELECT TRIM(rf.RDB$FIELD_NAME)
        FROM RDB$RELATION_FIELDS rf
        JOIN RDB$RELATIONS r
          ON r.RDB$RELATION_NAME = rf.RDB$RELATION_NAME
        WHERE rf.RDB$RELATION_NAME = ?
          AND COALESCE(r.RDB$SYSTEM_FLAG, 0) = 0
          AND r.RDB$VIEW_BLR IS NULL
        ORDER BY rf.RDB$FIELD_POSITION
        """,
        (table_name,),
    )
    return {str(row[0]).strip().upper() for row in cursor.fetchall()}


def scalar(cursor, sql: str, params=()):
    cursor.execute(sql, params)
    row = cursor.fetchone()
    return None if row is None else row[0]


def inspect_company(config: dict, company: str, company_config: dict) -> dict:
    db_path = Path(company_config["fdb"])
    if not db_path.exists():
        raise FileNotFoundError(f"[{company}] no existe la base: {db_path}")

    conn = connect_company(config, company_config)
    transaction = conn.trans(default_tpb=read_only_tpb())
    cursor = transaction.cursor()

    try:
        contact_columns = table_columns(cursor, TARGET_TABLE)
        if not contact_columns:
            raise RuntimeError(f"[{company}] no existe la tabla física {TARGET_TABLE}")

        missing_contact = sorted(REQUIRED_CONTACT_COLUMNS - contact_columns)
        if missing_contact:
            raise RuntimeError(
                f"[{company}] {TARGET_TABLE} no tiene las columnas requeridas: {missing_contact}"
            )

        client_columns = table_columns(cursor, "CLIENTES")
        missing_client = sorted(REQUIRED_CLIENT_COLUMNS - client_columns)
        if missing_client:
            raise RuntimeError(
                f"[{company}] CLIENTES no tiene las columnas requeridas: {missing_client}"
            )

        contact_rows = int(scalar(cursor, "SELECT COUNT(*) FROM CONTACTOS") or 0)
        client_contact_rows = int(
            scalar(
                cursor,
                """
                SELECT COUNT(*)
                FROM CONTACTOS
                WHERE UPPER(COALESCE(TRIM(CLIENTEPROVEEDOR), '')) = 'C'
                  AND NULLIF(TRIM(PERSONACONTACTO), '') IS NOT NULL
                """,
            )
            or 0
        )
        unmatched_rows = int(
            scalar(
                cursor,
                """
                SELECT COUNT(*)
                FROM CONTACTOS co
                LEFT JOIN CLIENTES cl
                  ON cl.CODIGOID = co.CODIGO
                WHERE UPPER(COALESCE(TRIM(co.CLIENTEPROVEEDOR), '')) = 'C'
                  AND NULLIF(TRIM(co.PERSONACONTACTO), '') IS NOT NULL
                  AND cl.CODIGOID IS NULL
                """,
            )
            or 0
        )

        transaction.rollback()

        return {
            "company": company,
            "contact_rows": contact_rows,
            "client_contact_rows": client_contact_rows,
            "unmatched_rows": unmatched_rows,
            "contact_columns": len(contact_columns),
        }
    except Exception:
        try:
            transaction.rollback()
        except Exception:
            pass
        raise
    finally:
        conn.close()


def backup_and_patch_config(config_path: Path, config: dict) -> Path | None:
    existing = [str(value).upper() for value in config["tablas_objetivo"]]
    if TARGET_TABLE in existing:
        print(f"config.json ya contiene {TARGET_TABLE}.")
        return None

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = config_path.with_name(
        f"{config_path.stem}.backup_contactos_{timestamp}{config_path.suffix}"
    )
    shutil.copy2(config_path, backup)

    updated = json.loads(json.dumps(config))
    updated["tablas_objetivo"].append(TARGET_TABLE)
    config_path.write_text(
        json.dumps(updated, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"config.json actualizado: {config_path}")
    print(f"Copia de seguridad: {backup}")
    print(
        f"Tablas objetivo por sociedad: "
        f"{len(config['tablas_objetivo'])} -> {len(updated['tablas_objetivo'])}"
    )
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
        raise RuntimeError(
            f"El pipeline terminó con código {completed.returncode}."
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Añade CONTACTOS a config.json después de crear backup.",
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
    print("VALIDACIÓN READ ONLY DE CONTACTOS MASTER SQL")
    print("=" * 96)
    print(f"Config: {config_path}")
    print("Firebird/MasterSQL: solo lectura")

    results = []
    for company, company_config in config["empresas"].items():
        print(f"Inspeccionando {company}...")
        result = inspect_company(config, company, company_config)
        results.append(result)
        print(
            f"  CONTACTOS={result['contact_rows']:,} | "
            f"contactos cliente={result['client_contact_rows']:,} | "
            f"sin CLIENTES.CODIGOID={result['unmatched_rows']:,}"
        )

    if any(result["unmatched_rows"] for result in results):
        print()
        print(
            "AVISO: existen contactos de cliente sin correspondencia CLIENTES.CODIGOID. "
            "Se extraerá CONTACTOS completo, pero esos registros no podrán asociarse "
            "a una ficha comercial hasta corregir el origen."
        )

    if not args.apply:
        print()
        print("MODO DIAGNÓSTICO: no se ha modificado ningún archivo.")
        print("Para activar y sincronizar:")
        print(
            rf'"{PYTHON}" "{Path(__file__)}" --apply --run-pipeline'
        )
        return 0

    backup = backup_and_patch_config(config_path, config)

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
    print("CONTACTOS ACTIVADO")
    print("=" * 96)
    print("CONTACTOS queda incluido en cada extracción normal.")
    print(
        "El pipeline generará raw_<empresa>_contactos y Supabase lo convertirá "
        "en commercial.erp_contacts."
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
