import os, json, sys
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
    sys.exit(
        f"ERROR: no existe la DLL {dll}\n"
        "Revisa bitness y ruta: Python x64 necesita fbclient x64."
    )
os.add_dll_directory(str(dll.parent))
fdb.load_api(str(dll))


def tpb_solo_lectura():
    tpb = fdb.TPB()
    tpb.access_mode = fdb.isc_tpb_read
    tpb.isolation_level = fdb.isc_tpb_concurrency
    tpb.lock_resolution = fdb.isc_tpb_wait
    return tpb


def txt(v):
    if isinstance(v, bytes):
        v = v.decode("cp1252", "replace")
    return v.strip() if isinstance(v, str) else v


cs = str(cfg["charset_conexion"])
charset_con = None if cs.upper().startswith("PENDIENTE") else cs

fallo = False
for emp, e in cfg["empresas"].items():
    ruta = Path(e["fdb"])
    if not ruta.exists():
        print(emp, f"FALLO -> no existe {ruta} en este PC")
        fallo = True
        continue
    dsn = f"{cfg['host']}/{cfg['puerto']}:{e['fdb']}"
    try:
        con = fdb.connect(
            dsn=dsn,
            user=cfg["usuario"],
            password=cfg["password"],
            charset=charset_con,
        )
        tr = con.trans(default_tpb=tpb_solo_lectura())
        cur = tr.cursor()
        cur.execute("SELECT rdb$get_context('SYSTEM','ENGINE_VERSION') FROM rdb$database")
        print(emp, "OK -> motor", txt(cur.fetchone()[0]))
        tr.commit()
        con.close()
    except Exception as ex:
        print(emp, "FALLO ->", ex)
        fallo = True

if fallo:
    sys.exit(1)
print("CONEXION VERIFICADA EN LAS 3 BASES")
