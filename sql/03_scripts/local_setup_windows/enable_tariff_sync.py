#!/usr/bin/env python3
"""Activa la sincronización de la tabla de tarifas/PVP de MasterSQL.

Objetivo:
1. Conectar en READ ONLY a CHEMIE, ACI y ECOCLEAN.
2. Descubrir la tabla física que contiene las 5 tarifas/PVP de artículos.
3. Exigir que la misma tabla exista y tenga señales inequívocas en las 3 empresas.
4. Añadirla a config.json -> tablas_objetivo.
5. Opcionalmente ejecutar el pipeline de producción existente.

No escribe nunca en Firebird/MasterSQL. Solo modifica config.json si se usa --apply.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Iterable

import fdb


ROOT = Path(r"C:\grupo_chemie")
CONFIG_CANDIDATES = (
    ROOT / "config.json",
    ROOT / "config" / "config.json",
)
PIPELINE = ROOT / "scripts" / "run_pipeline_produccion.py"
PYTHON = ROOT / "venv" / "Scripts" / "python.exe"

EXCLUDED_PRICE_WORDS = {
    "COMPRA",
    "COSTE",
    "COSTO",
    "ENTRADA",
    "MEDIO",
    "COMBINADO",
    "COMBINABLE",
    "CHUPITO",
}

REFERENCE_TOKENS = {
    "REFE",
    "REFERENCIA",
    "REFERENCIA1",
    "CODIGOARTICULO",
    "ARTICULO",
}

WAREHOUSE_TOKENS = {
    "ALMACEN",
    "CODIGOALMACEN",
    "TIENDA",
}


def load_config() -> tuple[Path, dict]:
    for path in CONFIG_CANDIDATES:
        if path.exists():
            return path, json.loads(path.read_text(encoding="utf-8"))
    checked = "\n".join(f"  - {p}" for p in CONFIG_CANDIDATES)
    raise FileNotFoundError(f"No se encontró config.json. Rutas:\n{checked}")


def validate_config(config: dict) -> None:
    required = ["fbclient_dll", "host", "puerto", "usuario", "password", "empresas", "tablas_objetivo"]
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"Faltan claves en config.json: {missing}")
    if not isinstance(config["tablas_objetivo"], list):
        raise TypeError("config.json -> tablas_objetivo debe ser una lista")
    if not config["empresas"]:
        raise ValueError("config.json -> empresas está vacío")


def normalize(name: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", name.upper().strip())


def has_indexed_signal(column: str, index: int, tokens: Iterable[str]) -> bool:
    c = normalize(column)
    if not any(token in c for token in tokens):
        return False
    return bool(re.search(rf"(?<!\d){index}(?!\d)", c))


def is_price_column(column: str, index: int) -> bool:
    c = normalize(column)
    if any(word in c for word in EXCLUDED_PRICE_WORDS):
        return False
    return has_indexed_signal(c, index, ("PVP", "PRECIO", "VENTA"))


def is_reference_column(column: str) -> bool:
    c = normalize(column)
    return (
        c in REFERENCE_TOKENS
        or c.startswith("REFERENCIA")
        or c.startswith("REFE")
        or c == "CODARTICULO"
    )


def is_warehouse_column(column: str) -> bool:
    c = normalize(column)
    return any(token in c for token in WAREHOUSE_TOKENS)


def read_only_tpb() -> fdb.TPB:
    tpb = fdb.TPB()
    tpb.access_mode = fdb.isc_tpb_read
    tpb.isolation_level = fdb.isc_tpb_concurrency
    tpb.lock_resolution = fdb.isc_tpb_wait
    return tpb


def load_firebird_api(config: dict) -> None:
    dll = Path(config["fbclient_dll"])
    if not dll.exists():
        raise FileNotFoundError(f"No existe fbclient: {dll}")
    os.add_dll_directory(str(dll.parent))
    fdb.load_api(str(dll))


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


def read_user_tables(cursor) -> dict[str, list[str]]:
    cursor.execute(
        """
        SELECT
            TRIM(r.RDB$RELATION_NAME) AS TABLE_NAME,
            TRIM(rf.RDB$FIELD_NAME) AS COLUMN_NAME,
            rf.RDB$FIELD_POSITION
        FROM RDB$RELATIONS r
        JOIN RDB$RELATION_FIELDS rf
          ON rf.RDB$RELATION_NAME = r.RDB$RELATION_NAME
        WHERE COALESCE(r.RDB$SYSTEM_FLAG, 0) = 0
          AND r.RDB$VIEW_BLR IS NULL
        ORDER BY r.RDB$RELATION_NAME, rf.RDB$FIELD_POSITION
        """
    )
    result: dict[str, list[str]] = {}
    for table_name, column_name, _ in cursor.fetchall():
        table = str(table_name).strip()
        column = str(column_name).strip()
        result.setdefault(table, []).append(column)
    return result


def score_table(table_name: str, columns: list[str]) -> dict:
    price_slots = {
        i for i in range(1, 6)
        if any(is_price_column(column, i) for column in columns)
    }
    benefit_slots = {
        i for i in range(1, 6)
        if any(has_indexed_signal(column, i, ("BENEFICIO", "MARGEN")) for column in columns)
    }
    discount_slots = {
        i for i in range(1, 6)
        if any(has_indexed_signal(column, i, ("DESCUENTO", "DTO")) for column in columns)
    }
    has_reference = any(is_reference_column(column) for column in columns)
    has_warehouse = any(is_warehouse_column(column) for column in columns)

    score = 0
    score += 15 * len(price_slots)
    score += 30 if price_slots == {1, 2, 3, 4, 5} else 0
    score += 20 if has_reference else 0
    score += 10 if has_warehouse else 0
    score += 2 * len(benefit_slots)
    score += len(discount_slots)

    table_norm = normalize(table_name)
    if "ARTIC" in table_norm:
        score += 5
    if "ALMACEN" in table_norm:
        score += 5
    if "HISTOR" in table_norm:
        score -= 15

    relevant_columns = [
        col for col in columns
        if (
            is_reference_column(col)
            or is_warehouse_column(col)
            or any(is_price_column(col, i) for i in range(1, 6))
            or any(has_indexed_signal(col, i, ("BENEFICIO", "MARGEN", "DESCUENTO", "DTO")) for i in range(1, 6))
            or any(token in normalize(col) for token in ("STOCK", "COSTE", "COSTO", "COMPRA", "ENTRADA"))
        )
    ]

    return {
        "table": table_name,
        "score": score,
        "price_slots": sorted(price_slots),
        "benefit_slots": sorted(benefit_slots),
        "discount_slots": sorted(discount_slots),
        "has_reference": has_reference,
        "has_warehouse": has_warehouse,
        "relevant_columns": relevant_columns,
        "qualified": price_slots == {1, 2, 3, 4, 5} and has_reference,
    }


def discover_company(config: dict, company: str, company_config: dict) -> list[dict]:
    db_path = Path(company_config["fdb"])
    if not db_path.exists():
        raise FileNotFoundError(f"[{company}] no existe la base: {db_path}")

    conn = connect_company(config, company_config)
    transaction = conn.trans(default_tpb=read_only_tpb())
    cursor = transaction.cursor()
    try:
        tables = read_user_tables(cursor)
        candidates = [
            score_table(table_name, columns)
            for table_name, columns in tables.items()
        ]
        candidates.sort(key=lambda item: (-item["score"], item["table"]))
        transaction.rollback()
        return candidates
    except Exception:
        try:
            transaction.rollback()
        except Exception:
            pass
        raise
    finally:
        conn.close()


def choose_common_table(results: dict[str, list[dict]]) -> tuple[str, dict[str, dict]]:
    qualified_by_company: dict[str, dict[str, dict]] = {}
    for company, candidates in results.items():
        qualified_by_company[company] = {
            item["table"].upper(): item
            for item in candidates
            if item["qualified"]
        }

    common = set.intersection(
        *(set(items) for items in qualified_by_company.values())
    )
    if not common:
        raise RuntimeError(
            "No existe una tabla candidata inequívoca común a todas las empresas. "
            "No se modifica config.json."
        )

    ranked: list[tuple[int, str]] = []
    for table in common:
        total_score = sum(
            qualified_by_company[company][table]["score"]
            for company in qualified_by_company
        )
        ranked.append((total_score, table))
    ranked.sort(reverse=True)

    best_score, best_table = ranked[0]
    if len(ranked) > 1 and ranked[1][0] == best_score:
        tied = [table for score, table in ranked if score == best_score]
        raise RuntimeError(
            f"Hay varias tablas candidatas empatadas: {tied}. "
            "No se modifica config.json."
        )

    details = {
        company: qualified_by_company[company][best_table]
        for company in qualified_by_company
    }
    return best_table, details


def show_candidates(results: dict[str, list[dict]], limit: int = 8) -> None:
    print()
    print("=" * 100)
    print("CANDIDATOS DE TARIFAS/PVP")
    print("=" * 100)
    for company, candidates in results.items():
        print()
        print(f"[{company}]")
        shown = [item for item in candidates if item["score"] > 0][:limit]
        for item in shown:
            print(
                f"  {item['table']:<35} score={item['score']:>3} "
                f"PVP={item['price_slots']} "
                f"BEN={item['benefit_slots']} "
                f"DTO={item['discount_slots']} "
                f"ref={item['has_reference']} almacen={item['has_warehouse']}"
            )
            if item["relevant_columns"]:
                print("    columnas: " + ", ".join(item["relevant_columns"]))


def backup_and_patch_config(config_path: Path, config: dict, table_name: str) -> Path | None:
    existing = [str(value).upper() for value in config["tablas_objetivo"]]
    if table_name.upper() in existing:
        print(f"config.json ya contiene {table_name}.")
        return None

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = config_path.with_name(f"{config_path.stem}.backup_tarifas_{timestamp}{config_path.suffix}")
    shutil.copy2(config_path, backup)

    updated = json.loads(json.dumps(config))
    updated["tablas_objetivo"].append(table_name)
    config_path.write_text(
        json.dumps(updated, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"config.json actualizado: {config_path}")
    print(f"Copia de seguridad: {backup}")
    return backup


def run_pipeline() -> None:
    if not PYTHON.exists():
        raise FileNotFoundError(f"No existe Python del proyecto: {PYTHON}")
    if not PIPELINE.exists():
        raise FileNotFoundError(f"No existe pipeline: {PIPELINE}")

    print()
    print("=" * 100)
    print("EJECUTANDO PIPELINE DE PRODUCCIÓN")
    print("=" * 100)
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
        help="Añade la tabla detectada a config.json después de crear backup.",
    )
    parser.add_argument(
        "--run-pipeline",
        action="store_true",
        help="Ejecuta run_pipeline_produccion.py después de aplicar el cambio.",
    )
    args = parser.parse_args()

    if args.run_pipeline and not args.apply:
        parser.error("--run-pipeline requiere --apply")

    config_path, config = load_config()
    validate_config(config)
    load_firebird_api(config)

    print("=" * 100)
    print("DESCUBRIMIENTO READ ONLY DE TARIFAS MASTER SQL")
    print("=" * 100)
    print(f"Config: {config_path}")
    print("Firebird/MasterSQL: solo lectura")

    results: dict[str, list[dict]] = {}
    for company, company_config in config["empresas"].items():
        print(f"Inspeccionando {company}...")
        results[company] = discover_company(config, company, company_config)

    show_candidates(results)

    selected_table, details = choose_common_table(results)

    print()
    print("=" * 100)
    print("TABLA DETECTADA")
    print("=" * 100)
    print(f"Tabla física común: {selected_table}")
    for company, item in details.items():
        print(
            f"{company}: score={item['score']} | "
            f"PVP={item['price_slots']} | "
            f"almacén={item['has_warehouse']}"
        )
        print("  " + ", ".join(item["relevant_columns"]))

    if not args.apply:
        print()
        print("MODO DIAGNÓSTICO: no se ha modificado ningún archivo.")
        print("Para activar y sincronizar:")
        print(
            rf'"{PYTHON}" "{Path(__file__)}" --apply --run-pipeline'
        )
        return 0

    backup = backup_and_patch_config(config_path, config, selected_table)

    try:
        if args.run_pipeline:
            run_pipeline()
    except Exception:
        if backup is not None and backup.exists():
            shutil.copy2(backup, config_path)
            print()
            print(
                "El pipeline falló. Se ha restaurado config.json para no "
                "romper futuras ejecuciones."
            )
        raise

    print()
    print("=" * 100)
    print("TARIFAS ACTIVADAS")
    print("=" * 100)
    print(f"Tabla incluida permanentemente: {selected_table}")
    print("Se actualizará en cada ejecución normal del pipeline.")
    print(
        "Supabase recibirá una tabla raw por empresa con el patrón "
        f"<empresa>_{selected_table.lower()}."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print()
        print("=" * 100)
        print("ERROR")
        print("=" * 100)
        print(f"{type(exc).__name__}: {exc}")
        raise SystemExit(1)
