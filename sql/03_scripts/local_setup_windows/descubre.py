import os, json, csv, sys
from pathlib import Path
import fdb

BASE = Path(__file__).resolve().parent


def carga_config():
    for c in (BASE / "config.json", BASE / "config" / "config.json"):
        if c.exists():
            return json.loads(c.read_text(encoding="utf-8"))
    sys.exit("ERROR: no encuentro config.json ni config\\config.json junto al script.")


cfg = carga_config()


def valida(clave):
    v = str(cfg.get(clave, ""))
    if not v or "RELLENAR" in v.upper() or "PENDIENTE_FASE" in v.upper():
        sys.exit(f"ERROR: config.json -> '{clave}' sin rellenar (valor actual: {v!r})")


valida("fbclient_dll")
valida("password")

dll = Path(cfg["fbclient_dll"])
if not dll.exists():
    sys.exit(f"ERROR: no existe la DLL {dll} (bitness/ruta)")
os.add_dll_directory(str(dll.parent))
fdb.load_api(str(dll))

Q_VERSION = "SELECT rdb$get_context('SYSTEM','ENGINE_VERSION') FROM rdb$database"
Q_CHARSET = """
SELECT TRIM(cs.RDB$CHARACTER_SET_NAME)
FROM RDB$DATABASE d
JOIN RDB$CHARACTER_SETS cs
  ON cs.RDB$CHARACTER_SET_ID = d.RDB$CHARACTER_SET_ID
"""
Q_TABLAS = """SELECT TRIM(RDB$RELATION_NAME) FROM RDB$RELATIONS
WHERE COALESCE(RDB$SYSTEM_FLAG,0)=0 AND RDB$VIEW_BLR IS NULL ORDER BY 1"""
Q_COLS = """SELECT TRIM(rf.RDB$FIELD_NAME), f.RDB$FIELD_TYPE, f.RDB$FIELD_SUB_TYPE,
f.RDB$FIELD_LENGTH, f.RDB$FIELD_SCALE FROM RDB$RELATION_FIELDS rf
JOIN RDB$FIELDS f ON f.RDB$FIELD_NAME=rf.RDB$FIELD_SOURCE
WHERE rf.RDB$RELATION_NAME=? ORDER BY rf.RDB$FIELD_POSITION"""


def tpb_ro():
    t = fdb.TPB()
    t.access_mode = fdb.isc_tpb_read
    t.isolation_level = fdb.isc_tpb_concurrency
    t.lock_resolution = fdb.isc_tpb_wait
    return t


def txt(v):
    if isinstance(v, bytes):
        v = v.decode("cp1252", "replace")
    return v.strip() if isinstance(v, str) else v


out = BASE / "esquema"
out.mkdir(parents=True, exist_ok=True)
cs = str(cfg["charset_conexion"])
charset_con = None if cs.upper().startswith("PENDIENTE") else cs

for emp, e in cfg["empresas"].items():
    ruta = Path(e["fdb"])
    if not ruta.exists():
        print(f"[{emp}] SALTADA: no existe {ruta} en este PC")
        continue

    con = fdb.connect(
        dsn=f"{cfg['host']}/{cfg['puerto']}:{e['fdb']}",
        user=cfg["usuario"],
        password=cfg["password"],
        charset=charset_con,
    )
    tr = con.trans(default_tpb=tpb_ro())
    cur = tr.cursor()

    cur.execute(Q_VERSION)
    version = txt(cur.fetchone()[0])

    try:
        cur.execute(Q_CHARSET)
        db_charset = txt(cur.fetchone()[0])
    except Exception as ex:
        db_charset = f"ERROR_LEYENDO_CHARSET: {ex}"

    muestras = []
    try:
        cur.execute("SELECT FIRST 300 RAZONSOCIAL FROM CLIENTES")
        for (rs,) in cur.fetchall():
            s = txt(rs)
            if s and any(ord(ch) > 127 for ch in s):
                muestras.append(s)
            if len(muestras) >= 8:
                break
    except Exception as ex:
        muestras = [f"(no se pudo muestrear CLIENTES: {ex})"]

    (out / f"charset_{emp}.txt").write_text(
        f"empresa: {emp}\n"
        f"version motor: {version}\n"
        f"charset por defecto de la BD: {db_charset}\n"
        f"charset de conexion usado: {charset_con or 'NONE (sin fijar aun)'}\n"
        f"muestras con caracteres especiales (deben leerse bien):\n"
        + "\n".join(f"  - {m}" for m in muestras) + "\n",
        encoding="utf-8",
    )
    print(f"[{emp}] motor {version} | charset BD: {db_charset} -> charset_{emp}.txt")

    cur.execute(Q_TABLAS)
    tablas = [txt(r[0]) for r in cur.fetchall()]
    with open(out / f"esquema_{emp}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["tabla", "filas", "columna", "tipo", "subtipo", "longitud", "escala"])
        for t in tablas:
            try:
                cur.execute(f"SELECT COUNT(*) FROM {t}")
                n = cur.fetchone()[0]
            except Exception:
                n = -1
            try:
                cur.execute(Q_COLS, (t,))
                colfilas = cur.fetchall()
            except Exception as ex:
                w.writerow([t, n, f"(error columnas: {ex})", "", "", "", ""])
                continue
            for c in colfilas:
                w.writerow([t, n] + [txt(x) for x in c])

    tr.commit()
    con.close()
    print(f"[{emp}] {len(tablas)} tablas -> esquema_{emp}.csv")

print("\nHecho. Revisa la carpeta 'esquema' y comparte los CSV/TXT para la siguiente fase.")
