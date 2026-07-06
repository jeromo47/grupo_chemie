# MANUAL EJECUTABLE — PARTE B (Fases 3–4: Extracción y DuckDB)

**Pipeline Grupo Chemie: Firebird 2.5 → Python → Parquet → DuckDB → Informe → Drive**
**Versión 1.0 — 2026-07-05. Parte B de 3. Cubre los puntos 8–10 del encargo.**

**Estado de verificación:** todo el código Python y todo el SQL de esta parte se ha **ejecutado en vivo hoy** con datos sintéticos que replican la estructura esperada: conversión de tipos (Decimal→DECIMAL(18,4) exacto, fechas, bytes cp1252 → "MUÑOZ"/"GARCÍA" correctos, columnas todo-NULL), carga de Parquet a DuckDB, ejecución multi-sentencia de archivos SQL, las 5 vistas canónicas y las 7 vistas de alerta con sus umbrales. Lo único que NO se puede verificar sin estar en el PC de la empresa es la conexión fdb real (eso lo cubre `test_conexion.py` de la Parte A) y los nombres de columna reales de MasterSQL (eso lo cierra la capa de mapeo, sección 4.3).

**Requisito de entrada:** checklist de cierre de la Parte A completa, en particular `config.json` con charset y `tablas_objetivo` rellenados.

---

## FASE 3 — EXTRACCIÓN A PARQUET (punto 8 del encargo)

### 3.1 El script completo

Crea `C:\grupo_chemie\scripts\extract.py`:

```python
#!/usr/bin/env python3
"""Extraccion Firebird 2.5 -> Parquet tipado. Una carpeta por fecha, una subcarpeta por empresa."""
import os, sys, json, time, logging, datetime, decimal
from pathlib import Path
import fdb
import pyarrow as pa
import pyarrow.parquet as pq

BASE = Path(__file__).resolve().parent.parent
cfg = json.loads((BASE / "config" / "config.json").read_text(encoding="utf-8"))
HOY = datetime.date.today().isoformat()
DEST = BASE / "extracts" / HOY
LOGD = BASE / "logs"; LOGD.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler(LOGD / f"extract_{HOY}.log", encoding="utf-8"),
              logging.StreamHandler()])
log = logging.getLogger("extract")

os.add_dll_directory(str(Path(cfg["fbclient_dll"]).parent))
fdb.load_api(cfg["fbclient_dll"])

def tpb_solo_lectura():
    # READ ONLY + CONCURRENCY (snapshot) + WAIT: vista consistente de todas
    # las tablas, cero bloqueo a escritores, impacto GC despreciable en minutos.
    tpb = fdb.TPB()
    tpb.access_mode = fdb.isc_tpb_read
    tpb.isolation_level = fdb.isc_tpb_concurrency
    tpb.lock_resolution = fdb.isc_tpb_wait
    return tpb

CS = cfg["charset_conexion"]

def a_arrow(nombre, valores):
    """Convierte una columna (lista Python) a pyarrow con tipo estable.
    Verificado: Decimal, datetime, date, bool, int, float, bytes(cp1252), todo-NULL."""
    muestra = next((v for v in valores if v is not None), None)
    if muestra is None:
        return pa.array([None] * len(valores), pa.string())
    if isinstance(muestra, decimal.Decimal):
        q = decimal.Decimal("0.0001")
        vals = [None if v is None else decimal.Decimal(v).quantize(q) for v in valores]
        return pa.array(vals, pa.decimal128(18, 4))
    if isinstance(muestra, datetime.datetime):
        return pa.array(valores, pa.timestamp("us"))
    if isinstance(muestra, datetime.date):
        return pa.array(valores, pa.date32())
    if isinstance(muestra, bool):
        return pa.array(valores, pa.bool_())
    if isinstance(muestra, int):
        return pa.array(valores, pa.int64())
    if isinstance(muestra, float):
        return pa.array(valores, pa.float64())
    if isinstance(muestra, bytes):   # charset NONE: decodificar cp1252
        vals = [None if v is None else v.decode("cp1252", "replace") for v in valores]
        return pa.array(vals, pa.string())
    return pa.array([None if v is None else str(v) for v in valores], pa.string())

def extrae_tabla(cur, tabla, destino):
    t0 = time.time()
    cur.execute(f"SELECT * FROM {tabla}")
    nombres = [d[0].strip() for d in cur.description]
    filas = cur.fetchall()   # volúmenes de este grupo: cabe en memoria de sobra
    cols = list(zip(*filas)) if filas else [[] for _ in nombres]
    arrays = [a_arrow(n, list(c)) for n, c in zip(nombres, cols)]
    tab = pa.table(dict(zip(nombres, arrays)))
    pq.write_table(tab, destino / f"{tabla}.parquet", compression="zstd")
    return {"tabla": tabla, "filas": len(filas), "columnas": len(nombres),
            "segundos": round(time.time() - t0, 2)}

def main():
    manifest = {"fecha": HOY, "empresas": {}}
    fallo_critico = False
    for emp, e in cfg["empresas"].items():
        d = DEST / emp; d.mkdir(parents=True, exist_ok=True)
        dsn = f"{cfg['host']}/{cfg['puerto']}:{e['fdb']}"
        log.info(f"[{emp}] conectando {dsn}")
        try:
            con = fdb.connect(dsn=dsn, user=cfg["usuario"],
                              password=cfg["password"], charset=CS)
        except Exception as ex:
            log.error(f"[{emp}] SIN CONEXION -> {ex}")
            manifest["empresas"][emp] = [{"error_conexion": str(ex)}]
            fallo_critico = True
            continue
        tr = con.trans(default_tpb=tpb_solo_lectura()); cur = tr.cursor()
        res = []
        for tabla in cfg["tablas_objetivo"]:
            try:
                r = extrae_tabla(cur, tabla, d)
                log.info(f"[{emp}] {tabla}: {r['filas']} filas en {r['segundos']}s")
                res.append(r)
            except Exception as ex:
                log.error(f"[{emp}] {tabla}: FALLO -> {ex}")
                res.append({"tabla": tabla, "error": str(ex)})
                if tabla in cfg.get("tablas_criticas", []):
                    fallo_critico = True
        tr.commit(); con.close()
        manifest["empresas"][emp] = res
    (DEST / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info(f"manifest -> {DEST / 'manifest.json'}")
    sys.exit(1 if fallo_critico else 0)

if __name__ == "__main__":
    main()
```

Lanzador manual para el verano — `C:\grupo_chemie\run_extraccion.bat` (doble clic vía AnyDesk):

```bat
@echo off
cd /d C:\grupo_chemie
venv\Scripts\python.exe scripts\extract.py
pause
```

### 3.2 Notas exactas de comportamiento

- **Convención de salida:** `extracts\AAAA-MM-DD\EMPRESA\TABLA.parquet` + `manifest.json` con filas/columnas/segundos por tabla. El manifest es tu detector de deriva: si VTOSCLIENTES pasa de 90 filas a 0 de una semana a otra, algo ha cambiado en el ERP.
- **Nombres de tabla sin comillas** en el SELECT: MasterSQL crea identificadores sin comillas, Firebird los guarda en mayúsculas y el SQL sin comillas los resuelve solo.
- **Tabla que no existe en alguna empresa** (posible: las 3 bases pueden diferir): se registra el fallo en log y manifest y **se sigue con el resto**. Solo las tablas listadas en `tablas_criticas` provocan exit code 1.
- **Doble ejecución el mismo día:** sobrescribe los mismos ficheros — idempotente, sin efectos raros.
- **BLOB de texto** llegan como `str` con fdb por defecto; un BLOB binario caería al caso `str(v)` (feo pero inofensivo). Si alguna tabla objetivo tuviera BLOB binarios molestos, se excluye esa columna en la capa de mapeo, no aquí: la extracción es deliberadamente tonta (SELECT * siempre), toda la inteligencia va en DuckDB.
- **Horario:** en verano, al lanzarlo tú a mano, da igual la hora (la transacción de solo lectura no molesta). Cuando pase a tarea programada (Parte C), correrá a las 09:10, antes del pico de oficina.

---

## FASE 4 — DUCKDB: RECONSTRUCCIÓN, CONTRATO, MAPEO, VISTAS Y ALERTAS (puntos 9 y 10)

### 4.1 Reconstrucción idempotente (punto 9)

Crea `C:\grupo_chemie\scripts\build_duckdb.py`:

```python
#!/usr/bin/env python3
"""Reconstruye data/grupo_chemie.duckdb desde el extracto mas reciente (o la fecha dada como argumento).
Idempotencia por demolicion: borra la base y la recrea entera. Un solo comando."""
import sys
from pathlib import Path
import duckdb

BASE = Path(__file__).resolve().parent.parent
EX = BASE / "extracts"
fechas = sorted(p.name for p in EX.iterdir() if p.is_dir() and not p.name.startswith("_"))
if not fechas:
    print("No hay extractos en", EX); sys.exit(1)
fecha = sys.argv[1] if len(sys.argv) > 1 else fechas[-1]
SRC = EX / fecha
DB = BASE / "data" / "grupo_chemie.duckdb"
DB.parent.mkdir(exist_ok=True)
DB.unlink(missing_ok=True)

con = duckdb.connect(str(DB))
con.execute(f"CREATE TABLE _meta AS SELECT '{fecha}' AS fecha_extraccion, current_timestamp AS construido")

# 1) Capa raw: una tabla por parquet, prefijada por empresa
for empresa_dir in sorted(p for p in SRC.iterdir() if p.is_dir()):
    emp = empresa_dir.name.lower()
    for pqf in sorted(empresa_dir.glob("*.parquet")):
        tname = f"raw_{emp}_{pqf.stem.lower()}"
        con.execute(f"CREATE OR REPLACE TABLE {tname} AS SELECT * FROM read_parquet('{pqf.as_posix()}')")
        n = con.execute(f"SELECT COUNT(*) FROM {tname}").fetchone()[0]
        print(f"{tname}: {n} filas")

# 2) Capas SQL en orden: mapping -> vistas -> alertas.
#    Cada archivo puede contener varias sentencias (verificado en duckdb 1.5.4).
#    Un archivo que falle (p.ej. mapeo aun sin rellenar) NO tumba el build:
#    se avisa y se sigue, para que el informe funcione parcialmente desde la semana 1.
errores = []
for carpeta in ("mapping", "vistas", "alertas"):
    for f in sorted((BASE / "sql" / carpeta).glob("*.sql")):
        try:
            con.execute(f.read_text(encoding="utf-8"))
            print(f"SQL OK: {carpeta}/{f.name}")
        except Exception as ex:
            errores.append(f"{carpeta}/{f.name}: {ex}")
            print(f"SQL AVISO: {carpeta}/{f.name} -> {str(ex)[:150]}")

con.close()
print(f"\nBase reconstruida -> {DB} (extracto {fecha})")
if errores:
    print(f"{len(errores)} capa(s) SQL pendientes o con error (ver arriba). El resto funciona.")
```

Un solo comando lo reconstruye todo:

```bat
C:\grupo_chemie\venv\Scripts\python.exe C:\grupo_chemie\scripts\build_duckdb.py
```

### 4.2 Contrato canónico (fijo desde hoy)

Las vistas y alertas de 4.4 y 4.5 son **finales** y están escritas contra este contrato. Lo único que se adapta a MasterSQL es la capa de mapeo (4.3), que traduce nombres reales → contrato.

| Vista staging (la produce el mapeo) | Columnas exactas que debe entregar |
|---|---|
| `stg_ventas_linea` | empresa, fecha (DATE), factura, cliente_id, cliente, comercial, familia_id, familia, referencia, descripcion, cantidad, importe (sin IVA), coste |
| `stg_cartera_cobros` | empresa, cliente_id, cliente, factura, efecto, fecha_vto (DATE), importe_vto, cobrado, estado |
| `stg_cartera_pagos` | empresa, proveedor_id, proveedor, factura, efecto, fecha_vto (DATE), importe_vto, pagado, estado |
| `stg_compras_linea` | empresa, fecha (DATE), proveedor_id, proveedor, referencia, cantidad, importe |

Las canónicas (`v_*`) añaden lo derivado: margen_calc, flag_ref_generica, pendiente, dias_vencido, tramo.

### 4.3 Capa de mapeo — lo ÚNICO abierto, y cómo se cierra en 10 minutos por tabla

Un archivo `.sql` por vista staging en `C:\grupo_chemie\sql\mapping\`:

```text
sql\mapping\00_ventas_linea.sql
sql\mapping\10_cartera_cobros.sql
sql\mapping\20_compras_linea.sql
sql\mapping\30_cartera_pagos.sql
```

**Procedimiento de relleno (mecánico):** (1) abre el `esquema_EMPRESA.csv` de la Fase 2.7 filtrado por la tabla en cuestión; (2) identifica qué columna real corresponde a cada columna del contrato (los nombres de MasterSQL son autoexplicativos en español); (3) sustituye los marcadores `<<...>>`. Alternativa más rápida: **súbeme los tres `esquema_*.csv` y te entrego los cuatro archivos de mapeo ya rellenos.**

Plantilla de `10_cartera_cobros.sql` sobre `VTOSCLIENTES` (tabla real confirmada; columnas por confirmar — los nombres de ejemplo del bloque comentado son los que se usaron en la validación en vivo, NO los reales de MasterSQL):

```sql
-- CARTERA DE COBROS desde VTOSCLIENTES (tabla confirmada en tu descubrimiento previo).
-- Rellena los <<MARCADORES>> con la salida de esquema_*.csv para VTOSCLIENTES.
-- Tu export previo 07B demuestra que el ERP tiene exactamente estos conceptos:
-- FACTURA, EFECTO, FECHA_VTO, IMPORTE_VTO, IMPORTE_COBRO, ESTADO.
CREATE OR REPLACE VIEW stg_cartera_cobros AS
SELECT 'CHEMIE' AS empresa,
       <<COL_CODIGO_CLIENTE>>            AS cliente_id,
       <<COL_NOMBRE_CLIENTE_O_JOIN>>     AS cliente,
       <<COL_FACTURA>>                   AS factura,
       <<COL_EFECTO>>                    AS efecto,
       <<COL_FECHA_VTO>>                 AS fecha_vto,
       <<COL_IMPORTE_VTO>>               AS importe_vto,
       COALESCE(<<COL_IMPORTE_COBRADO>>, 0) AS cobrado,
       <<COL_ESTADO>>                    AS estado
FROM raw_chemie_vtosclientes
UNION ALL
SELECT 'ACI', <<...mismas columnas...>> FROM raw_aci_vtosclientes
UNION ALL
SELECT 'ECOCLEAN', <<...mismas columnas...>> FROM raw_ecoclean_vtosclientes;
```

Si el nombre del cliente no viene en VTOSCLIENTES, se trae con join al maestro (patrón para cualquier mapeo):

```sql
SELECT 'CHEMIE' AS empresa, v.<<COL_CODIGO_CLIENTE>> AS cliente_id,
       c.<<COL_NOMBRE>> AS cliente, ...
FROM raw_chemie_vtosclientes v
LEFT JOIN raw_chemie_clientes c ON c.<<COL_CODIGO>> = v.<<COL_CODIGO_CLIENTE>>
```

`00_ventas_linea.sql` sigue el mismo patrón sobre la tabla de líneas de venta que salga en 2.5 (cabecera + líneas: cuidado con el join, ver la advertencia anti fan-out en la validación de la Parte C). `20_compras_linea.sql` y `30_cartera_pagos.sql` (sobre la homóloga de proveedores, probablemente `VTOSPROVEEDORES`), ídem.

**Regla de oro de esta capa:** es el ÚNICO sitio de todo el sistema donde aparecen nombres de columnas de MasterSQL. Si Tecnimática cambia algo en una actualización del ERP, solo se toca aquí.

### 4.4 Vistas canónicas (punto 10 — SQL final, sintaxis verificada en duckdb 1.5.4)

Crea `C:\grupo_chemie\sql\vistas\00_canonicas.sql`:

```sql
CREATE OR REPLACE VIEW v_ventas_linea AS
SELECT *,
       importe - coste AS margen_calc,
       (referencia IN ('999999','000000') OR referencia IS NULL OR trim(referencia) = '') AS flag_ref_generica
FROM stg_ventas_linea;

CREATE OR REPLACE VIEW v_cartera_cobros AS
SELECT *,
       importe_vto - cobrado AS pendiente,
       datediff('day', fecha_vto, current_date) AS dias_vencido,
       CASE
         WHEN datediff('day', fecha_vto, current_date) <= 0  THEN '0_no_vencido'
         WHEN datediff('day', fecha_vto, current_date) <= 30 THEN '1_vencido_0_30'
         WHEN datediff('day', fecha_vto, current_date) <= 60 THEN '2_vencido_31_60'
         ELSE '3_vencido_mas_60'
       END AS tramo
FROM stg_cartera_cobros
WHERE importe_vto - cobrado > 0.005;

CREATE OR REPLACE VIEW v_cartera_pagos AS
SELECT *,
       importe_vto - pagado AS pendiente,
       datediff('day', fecha_vto, current_date) AS dias_vencido,
       CASE
         WHEN datediff('day', fecha_vto, current_date) <= 0  THEN '0_no_vencido'
         WHEN datediff('day', fecha_vto, current_date) <= 30 THEN '1_vencido_0_30'
         WHEN datediff('day', fecha_vto, current_date) <= 60 THEN '2_vencido_31_60'
         ELSE '3_vencido_mas_60'
       END AS tramo
FROM stg_cartera_pagos
WHERE importe_vto - pagado > 0.005;

CREATE OR REPLACE VIEW v_compras_linea AS
SELECT * FROM stg_compras_linea;

CREATE OR REPLACE VIEW v_margen_familia AS
SELECT empresa, familia, date_trunc('month', fecha) AS mes,
       SUM(importe) AS ventas, SUM(coste) AS coste,
       SUM(importe - coste) AS margen,
       ROUND(100.0 * SUM(importe - coste) / NULLIF(SUM(importe), 0), 2) AS margen_pct
FROM v_ventas_linea
WHERE NOT flag_ref_generica
GROUP BY 1, 2, 3;

CREATE OR REPLACE VIEW v_concentracion_clientes AS
WITH v AS (
  SELECT empresa, cliente, SUM(importe) AS imp
  FROM v_ventas_linea
  WHERE fecha >= date_trunc('year', current_date)
  GROUP BY 1, 2),
r AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY empresa ORDER BY imp DESC) AS rn,
         SUM(imp) OVER (PARTITION BY empresa) AS total
  FROM v)
SELECT empresa,
       ROUND(100 * SUM(CASE WHEN rn <= 3 THEN imp END) / MAX(total), 2) AS pct_top3,
       ROUND(100 * SUM(CASE WHEN rn <= 5 THEN imp END) / MAX(total), 2) AS pct_top5,
       MAX(total) AS ventas_ytd
FROM r GROUP BY 1;
```

Decisiones incorporadas: el margen por familia **excluye siempre** las referencias genéricas 999999/000000/vacías (la contaminación de ACI no ensucia el KPI); el umbral `> 0.005` en cartera evita que redondeos a céntimo generen falsos "pendientes".

### 4.5 Alertas (punto 10 — SQL final con umbrales, verificado)

Crea `C:\grupo_chemie\sql\alertas\00_alertas.sql`:

```sql
-- A1a: linea con margen negativo en referencia NO generica (contaminacion o venta a perdida).
--      Umbral: cualquier ocurrencia.
CREATE OR REPLACE VIEW a_margen_negativo AS
SELECT empresa, fecha, factura, cliente, referencia, descripcion, importe, coste, margen_calc
FROM v_ventas_linea
WHERE margen_calc < 0 AND NOT flag_ref_generica;

-- A1b: linea facturada con coste cero (detector de maestro contaminado).
--      Umbral: cualquier ocurrencia.
CREATE OR REPLACE VIEW a_coste_cero AS
SELECT empresa, fecha, factura, cliente, referencia, descripcion, importe
FROM v_ventas_linea
WHERE coste = 0 AND importe > 0;

-- A2: cliente con margen agregado NEGATIVO (la firma del caso ACI/EJIDOMAR).
CREATE OR REPLACE VIEW a_cliente_margen_negativo AS
SELECT empresa, cliente, SUM(importe) AS ventas, SUM(margen_calc) AS margen
FROM v_ventas_linea
GROUP BY 1, 2
HAVING SUM(margen_calc) < 0;

-- A3: concentracion top-3 > 50 % (Chemie 2025 cerro en 46,93 %; vigilancia).
CREATE OR REPLACE VIEW a_concentracion AS
SELECT * FROM v_concentracion_clientes WHERE pct_top3 > 50;

-- A4: DSO. Formula fija: pendiente_total / ventas_ultimos_365d * 365. Umbral: 75 dias.
CREATE OR REPLACE VIEW a_dso AS
WITH p AS (SELECT empresa, SUM(pendiente) AS pendiente FROM v_cartera_cobros GROUP BY 1),
     v AS (SELECT empresa, SUM(importe) AS ventas_365
           FROM v_ventas_linea
           WHERE fecha >= current_date - INTERVAL 365 DAY
           GROUP BY 1)
SELECT p.empresa, p.pendiente, v.ventas_365,
       ROUND(p.pendiente / NULLIF(v.ventas_365, 0) * 365, 1) AS dso_dias
FROM p JOIN v USING (empresa)
WHERE p.pendiente / NULLIF(v.ventas_365, 0) * 365 > 75;

-- A5: cartera vencida por tramos (siempre visible en el informe; el umbral en euros
--     del tramo >60d se fija tras ver la primera foto real).
CREATE OR REPLACE VIEW a_vencida_tramos AS
SELECT empresa, tramo, COUNT(*) AS efectos, ROUND(SUM(pendiente), 2) AS pendiente
FROM v_cartera_cobros
GROUP BY 1, 2
ORDER BY 1, 2;

-- A6: cliente del top-10 YTD con efecto vencido > 30 dias.
CREATE OR REPLACE VIEW a_top_cliente_vencido AS
WITH top10 AS (
  SELECT empresa, cliente_id FROM (
    SELECT empresa, cliente_id,
           ROW_NUMBER() OVER (PARTITION BY empresa ORDER BY SUM(importe) DESC) AS rn
    FROM v_ventas_linea
    WHERE fecha >= date_trunc('year', current_date)
    GROUP BY 1, 2) WHERE rn <= 10)
SELECT c.empresa, c.cliente, c.factura, c.fecha_vto, c.pendiente, c.dias_vencido
FROM v_cartera_cobros c
JOIN top10 t USING (empresa, cliente_id)
WHERE c.dias_vencido > 30;
```

Umbral aplazado a v2 (deliberadamente): caída de margen de una familia > 5 p.p. interanual. Requiere dos ejercicios comparables en datos **tipados**; se activa cuando el pipeline lleve corriendo lo suficiente o cuando se cargue el histórico 2024–2025 re-extraído con este mismo extract.py (recomendado: hacerlo, es gratis — mismas tablas, la extracción trae todo el histórico de la tabla, no solo el año en curso).

### 4.6 Prueba de humo de la Fase 3+4 (secuencia exacta)

```bat
cd C:\grupo_chemie
venv\Scripts\python.exe scripts\extract.py
venv\Scripts\python.exe scripts\build_duckdb.py
venv\Scripts\python.exe -c "import duckdb; con=duckdb.connect('data/grupo_chemie.duckdb', read_only=True); print(con.execute('SELECT * FROM _meta').fetchall()); print(con.execute(\"SELECT table_name FROM information_schema.tables WHERE table_name LIKE 'raw_%' ORDER BY 1\").fetchall())"
```

Comprobaciones mínimas tras el primer build con mapeo relleno:

```sql
SELECT empresa, COUNT(*), MIN(fecha), MAX(fecha) FROM v_ventas_linea GROUP BY 1;
SELECT * FROM a_vencida_tramos;
SELECT * FROM a_cliente_margen_negativo ORDER BY margen LIMIT 10;   -- aqui debe asomar EJIDOMAR en ACI
SELECT * FROM v_concentracion_clientes;
```

Si `a_cliente_margen_negativo` no muestra EJIDOMAR en ACI con margen fuertemente negativo, sospecha del mapeo de coste antes que celebrar que el problema no existe: ese cliente es tu caso de control conocido.

---

## CIERRE DE LA PARTE B — checklist antes de pasar a la Parte C

1. ☐ `extract.py`, `build_duckdb.py` y `run_extraccion.bat` creados tal cual.
2. ☐ Primera extracción real ejecutada: carpeta `extracts\AAAA-MM-DD\` con los Parquet de las 3 empresas y `manifest.json` sin errores en `tablas_criticas`.
3. ☐ `build_duckdb.py` ejecutado: tablas `raw_*` cargadas (los avisos de mapping pendiente son normales en este punto).
4. ☐ Los 4 archivos de mapeo creados (con marcadores o ya rellenos con los `esquema_*.csv`).
5. ☐ `sql\vistas\00_canonicas.sql` y `sql\alertas\00_alertas.sql` copiados tal cual (no se editan: son contrato).
6. ☐ Con el mapeo relleno: prueba de humo 4.6 pasada y EJIDOMAR visible en A2.

**Pendiente que cierro yo en cuanto subas los `esquema_*.csv`:** los cuatro archivos de mapeo con nombres de columna reales de MasterSQL, sin un solo marcador. Es el único hueco de toda la Parte B.

La Parte C (informe semanal, tarea programada como SYSTEM, rclone→Drive, retención y la validación final con las cifras de control 2025 y mayo 2026) cierra el manual.
