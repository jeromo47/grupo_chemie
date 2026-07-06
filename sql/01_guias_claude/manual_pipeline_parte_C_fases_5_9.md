# MANUAL EJECUTABLE — PARTE C (Fases 5–9: Informe, Orquestación, Drive y Validación)

**Pipeline Grupo Chemie: Firebird 2.5 → Python → Parquet → DuckDB → Informe → Drive**
**Versión 1.0 — 2026-07-05. Parte C de 3 (final). Cubre los puntos 11–15 del encargo.**

**Estado de verificación:** el generador de informe y la plantilla se han **ejecutado en vivo hoy** contra la base de validación de la Parte B: formato es-ES correcto ("121,00 €"), alertas EJIDOMAR/coste-cero/DSO/tramos renderizadas, y la ruta de degradación elegante comprobada (una capa sin mapear muestra "pendientes de mapeo" en vez de romper el informe). La función de retención también se ejecutó: conserva las 12 semanas configuradas, protege siempre las 4 carpetas más recientes y no toca `_esquema`. Lo NO verificable desde aquí: la sintaxis de `schtasks` y el flujo OAuth de rclone (se validan en el propio PC; se indica cómo).

---

## FASE 5 — INFORME SEMANAL (punto 11 del encargo)

Librería elegida: **jinja2** (única dependencia, ya instalada en la Parte A). Salida: HTML autocontenido con CSS inline, legible en el móvil desde Drive. No se generan gráficos en v1: tablas y alertas primero; Power BI local queda como capa exploratoria opcional sobre el mismo DuckDB.

### 5.1 Generador — `C:\grupo_chemie\scripts\report.py`

```python
#!/usr/bin/env python3
"""Genera el informe semanal HTML desde data/grupo_chemie.duckdb.
Cada seccion degrada con gracia si su capa aun no esta mapeada."""
import datetime
from pathlib import Path
import duckdb
from jinja2 import Template

BASE = Path(__file__).resolve().parent.parent
DB = BASE / "data" / "grupo_chemie.duckdb"
HOY = datetime.date.today().isoformat()

def eur(x):
    if x is None:
        return "—"
    s = f"{float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s + " €"

con = duckdb.connect(str(DB), read_only=True)

def q(sql):
    try:
        r = con.execute(sql)
        return [dict(zip([c[0] for c in r.description], f)) for f in r.fetchall()]
    except Exception as ex:
        return [{"SIN_DATOS": str(ex)[:120]}]

def sin(datos):
    return (not datos) or ("SIN_DATOS" in datos[0])

ctx = {
 "fecha": HOY, "eur": eur, "sin": sin,
 "alertas_coste_cero": q("SELECT * FROM a_coste_cero ORDER BY importe DESC LIMIT 20"),
 "alertas_margen_neg": q("SELECT * FROM a_margen_negativo ORDER BY margen_calc LIMIT 20"),
 "cliente_margen_neg": q("SELECT * FROM a_cliente_margen_negativo ORDER BY margen"),
 "concentracion":      q("SELECT * FROM v_concentracion_clientes ORDER BY empresa"),
 "dso":                q("SELECT * FROM a_dso"),
 "vencida":            q("SELECT * FROM a_vencida_tramos"),
 "top_vencido":        q("SELECT * FROM a_top_cliente_vencido ORDER BY pendiente DESC LIMIT 15"),
 "ventas_sem":         q("""SELECT empresa, ROUND(SUM(importe),2) AS ventas
                            FROM v_ventas_linea
                            WHERE fecha >= current_date - INTERVAL 7 DAY
                            GROUP BY 1 ORDER BY 1"""),
 "ventas_ytd":         q("""SELECT empresa, ROUND(SUM(importe),2) AS ventas,
                                   ROUND(SUM(margen_calc),2) AS margen
                            FROM v_ventas_linea
                            WHERE fecha >= date_trunc('year', current_date)
                            GROUP BY 1 ORDER BY 1"""),
 "margen_familia":     q("""SELECT empresa, familia, ROUND(SUM(ventas),2) AS v,
                                   ROUND(SUM(margen),2) AS m,
                                   ROUND(100*SUM(margen)/NULLIF(SUM(ventas),0),1) AS pct
                            FROM v_margen_familia
                            WHERE mes >= date_trunc('year', current_date)
                            GROUP BY 1,2 ORDER BY 1, v DESC"""),
 "compras_sem":        q("""SELECT empresa, proveedor, ROUND(SUM(importe),2) AS compras
                            FROM v_compras_linea
                            WHERE fecha >= current_date - INTERVAL 7 DAY
                            GROUP BY 1,2 ORDER BY compras DESC LIMIT 10"""),
}

tpl = Template((BASE / "scripts" / "informe.html.j2").read_text(encoding="utf-8"))
html = tpl.render(**ctx)

(BASE / "informes").mkdir(exist_ok=True)
(BASE / "publicar").mkdir(exist_ok=True)
(BASE / "informes" / f"informe_{HOY}.html").write_text(html, encoding="utf-8")
(BASE / "publicar" / "informe_semanal.html").write_text(html, encoding="utf-8")
print("informe ->", BASE / "publicar" / "informe_semanal.html")
```

### 5.2 Plantilla — `C:\grupo_chemie\scripts\informe.html.j2`

(Exactamente la validada. Copiar tal cual.)

```html
<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grupo Chemie — Informe {{ fecha }}</title>
<style>
 body{font-family:system-ui,Segoe UI,Arial;margin:16px;color:#222;max-width:900px}
 h1{font-size:1.3em} h2{font-size:1.05em;border-bottom:1px solid #ddd;padding-bottom:4px;margin-top:28px}
 table{border-collapse:collapse;width:100%;font-size:.85em;margin:8px 0}
 th,td{border:1px solid #ddd;padding:4px 6px;text-align:right} th{background:#f5f5f5}
 td:first-child,th:first-child,td:nth-child(2),th:nth-child(2){text-align:left}
 .alerta{background:#fff3f3;border-left:4px solid #c00;padding:8px 12px;margin:8px 0}
 .sin{color:#999;font-style:italic}
</style></head><body>
<h1>Grupo Chemie — Informe semanal {{ fecha }}</h1>

<h2>⚠ Alertas</h2>
{% if not sin(cliente_margen_neg) %}{% for a in cliente_margen_neg %}
<div class="alerta"><b>{{a.empresa}}</b> — cliente con margen agregado NEGATIVO: {{a.cliente}} ({{ eur(a.margen) }} sobre {{ eur(a.ventas) }} de ventas)</div>
{% endfor %}{% endif %}
{% if not sin(dso) %}{% for d in dso %}
<div class="alerta">DSO {{d.empresa}}: <b>{{d.dso_dias}} días</b> (pendiente {{ eur(d.pendiente) }}; umbral 75)</div>
{% endfor %}{% endif %}
{% if not sin(alertas_coste_cero) %}
<h3>Líneas con coste cero ({{ alertas_coste_cero|length }})</h3>
<table><tr><th>Emp</th><th>Cliente</th><th>Ref</th><th>Descripción</th><th>Importe</th></tr>
{% for a in alertas_coste_cero %}<tr><td>{{a.empresa}}</td><td>{{a.cliente}}</td><td>{{a.referencia}}</td><td>{{a.descripcion}}</td><td>{{ eur(a.importe) }}</td></tr>{% endfor %}</table>
{% endif %}
{% if not sin(alertas_margen_neg) %}
<h3>Líneas con margen negativo ({{ alertas_margen_neg|length }})</h3>
<table><tr><th>Emp</th><th>Cliente</th><th>Ref</th><th>Importe</th><th>Coste</th><th>Margen</th></tr>
{% for a in alertas_margen_neg %}<tr><td>{{a.empresa}}</td><td>{{a.cliente}}</td><td>{{a.referencia}}</td><td>{{ eur(a.importe) }}</td><td>{{ eur(a.coste) }}</td><td>{{ eur(a.margen_calc) }}</td></tr>{% endfor %}</table>
{% endif %}
{% if not sin(top_vencido) %}
<h3>Clientes top-10 con vencidos &gt; 30 días</h3>
<table><tr><th>Emp</th><th>Cliente</th><th>Factura</th><th>Vencimiento</th><th>Pendiente</th><th>Días</th></tr>
{% for t in top_vencido %}<tr><td>{{t.empresa}}</td><td>{{t.cliente}}</td><td>{{t.factura}}</td><td>{{t.fecha_vto}}</td><td>{{ eur(t.pendiente) }}</td><td>{{t.dias_vencido}}</td></tr>{% endfor %}</table>
{% endif %}

<h2>Ventas de la semana</h2>
{% if not sin(ventas_sem) %}
<table><tr><th>Empresa</th><th>Ventas 7d</th></tr>
{% for v in ventas_sem %}<tr><td>{{v.empresa}}</td><td>{{ eur(v.ventas) }}</td></tr>{% endfor %}</table>
{% else %}<p class="sin">Sin ventas registradas en los últimos 7 días o mapeo pendiente.</p>{% endif %}

<h2>Acumulado del año</h2>
{% if not sin(ventas_ytd) %}
<table><tr><th>Empresa</th><th>Ventas YTD</th><th>Margen YTD</th></tr>
{% for v in ventas_ytd %}<tr><td>{{v.empresa}}</td><td>{{ eur(v.ventas) }}</td><td>{{ eur(v.margen) }}</td></tr>{% endfor %}</table>
{% endif %}

<h2>Concentración de clientes (YTD)</h2>
{% if not sin(concentracion) %}
<table><tr><th>Empresa</th><th>% Top 3</th><th>% Top 5</th><th>Ventas YTD</th></tr>
{% for c in concentracion %}<tr><td>{{c.empresa}}</td><td>{{c.pct_top3}} %</td><td>{{c.pct_top5}} %</td><td>{{ eur(c.ventas_ytd) }}</td></tr>{% endfor %}</table>
{% endif %}

<h2>Tesorería — cartera de cobros</h2>
{% if not sin(vencida) %}
<table><tr><th>Empresa</th><th>Tramo</th><th>Efectos</th><th>Pendiente</th></tr>
{% for v in vencida %}<tr><td>{{v.empresa}}</td><td>{{v.tramo}}</td><td>{{v.efectos}}</td><td>{{ eur(v.pendiente) }}</td></tr>{% endfor %}</table>
{% else %}<p class="sin">Cartera pendiente de mapeo (Parte B, 4.3: VTOSCLIENTES).</p>{% endif %}

<h2>Compras de la semana (top proveedores)</h2>
{% if not sin(compras_sem) %}
<table><tr><th>Empresa</th><th>Proveedor</th><th>Compras 7d</th></tr>
{% for c in compras_sem %}<tr><td>{{c.empresa}}</td><td>{{c.proveedor}}</td><td>{{ eur(c.compras) }}</td></tr>{% endfor %}</table>
{% else %}<p class="sin">Compras pendientes de mapeo (Parte B, 4.3).</p>{% endif %}

<h2>Margen por familia (YTD, sin referencias genéricas)</h2>
{% if not sin(margen_familia) %}
<table><tr><th>Empresa</th><th>Familia</th><th>Ventas</th><th>Margen</th><th>%</th></tr>
{% for m in margen_familia %}<tr><td>{{m.empresa}}</td><td>{{m.familia}}</td><td>{{ eur(m.v) }}</td><td>{{ eur(m.m) }}</td><td>{{m.pct}} %</td></tr>{% endfor %}</table>
{% endif %}

<p style="color:#999;font-size:.8em">Generado automáticamente desde el extracto {{ fecha }} en el PC de la empresa.</p>
</body></html>
```

---

## FASE 6 — ORQUESTACIÓN Y TAREA PROGRAMADA (puntos 12 y 14)

### 6.1 Orquestador — `C:\grupo_chemie\scripts\run_pipeline.py`

```python
#!/usr/bin/env python3
"""Orquesta el ciclo completo: extraer -> DuckDB -> informe -> gbak (lunes) -> retencion -> Drive.
Guard anti doble ejecucion: si ya corrio hoy con exito, sale sin hacer nada."""
import sys, json, datetime, subprocess, shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PY = BASE / "venv" / "Scripts" / "python.exe"
HOY = datetime.date.today()
MARCA = BASE / "logs" / f"ok_{HOY.isoformat()}.flag"
cfg = json.loads((BASE / "config" / "config.json").read_text(encoding="utf-8"))

if MARCA.exists():
    print("Ya ejecutado hoy con exito. Fin."); sys.exit(0)

def paso(nombre, args, critico=True):
    print(f"== {nombre} ==", flush=True)
    r = subprocess.run(args, cwd=BASE)
    if r.returncode != 0 and critico:
        print(f"FALLO en {nombre} (rc={r.returncode}). Pipeline detenido."); sys.exit(r.returncode)
    return r.returncode

paso("extraccion", [str(PY), "scripts/extract.py"])
paso("duckdb",     [str(PY), "scripts/build_duckdb.py"])
paso("informe",    [str(PY), "scripts/report.py"])

# gbak semanal (dia_gbak: 0 = lunes)
if HOY.weekday() == cfg.get("dia_gbak", 0):
    for emp, e in cfg["empresas"].items():
        fbk = BASE / "backups" / f"{emp}_{HOY.isoformat()}.fbk"
        paso(f"gbak {emp}", [cfg["gbak_exe"], "-b", "-g", "-v",
             "-user", cfg["usuario"], "-password", cfg["password"],
             f"{cfg['host']}:{e['fdb']}", str(fbk),
             "-y", str(BASE / "logs" / f"gbak_{emp}_{HOY.isoformat()}.log")],
             critico=False)

# Retencion (punto 14 del encargo) — funcion validada en vivo
def retencion_dirs_fecha(carpeta, semanas, minimo=4):
    """Borra subcarpetas AAAA-MM-DD mas antiguas que 'semanas', conservando
    siempre las 'minimo' mas recientes y sin tocar carpetas con prefijo _."""
    limite = datetime.date.today() - datetime.timedelta(weeks=semanas)
    dirs = sorted((p for p in carpeta.iterdir()
                   if p.is_dir() and not p.name.startswith("_")), key=lambda p: p.name)
    proteger = {p.name for p in dirs[-minimo:]}
    for p in dirs:
        try:
            fecha = datetime.date.fromisoformat(p.name)
        except ValueError:
            continue
        if fecha < limite and p.name not in proteger:
            shutil.rmtree(p); print("retencion: borrado", p.name)

def retencion_ficheros(carpeta, patron, semanas, minimo=3):
    limite = datetime.date.today() - datetime.timedelta(weeks=semanas)
    fs = sorted(carpeta.glob(patron), key=lambda p: p.name)
    for p in fs[:-minimo] if len(fs) > minimo else []:
        # el nombre lleva la fecha: EMP_AAAA-MM-DD.fbk
        try:
            fecha = datetime.date.fromisoformat(p.stem.split("_", 1)[1])
        except (ValueError, IndexError):
            continue
        if fecha < limite:
            p.unlink(); print("retencion: borrado", p.name)

retencion_dirs_fecha(BASE / "extracts", cfg.get("retencion_semanas_extracts", 12))
for emp in cfg["empresas"]:
    retencion_ficheros(BASE / "backups", f"{emp}_*.fbk",
                       cfg.get("retencion_semanas_fbk", 8))

# Sincronizacion a Drive (Fase 7). No critico: si falla, el informe queda en local.
rclone = BASE / "rclone" / "rclone.exe"
if rclone.exists():
    paso("drive", [str(rclone), "copy", str(BASE / "publicar"), "gdrive:GrupoChemie/publicar",
                   "--config", str(BASE / "config" / "rclone.conf"),
                   "--log-file", str(BASE / "logs" / "rclone.log"),
                   "--log-level", "INFO"], critico=False)

MARCA.write_text(datetime.datetime.now().isoformat(), encoding="utf-8")
print("PIPELINE COMPLETO OK")
```

### 6.2 Lanzador — `C:\grupo_chemie\pipeline.bat`

```bat
@echo off
cd /d C:\grupo_chemie
venv\Scripts\python.exe scripts\run_pipeline.py >> logs\scheduler.log 2>&1
```

**Modo verano (julio–agosto):** NO crees todavía las tareas programadas. Ciclo manual semanal: AnyDesk → doble clic a `pipeline.bat` → informe en Drive. Así validas el sistema con supervisión antes de soltarlo.

### 6.3 Tarea programada (punto 12 — configuración exacta, se crea el 1–15 de septiembre)

Dos tareas complementarias, ambas como **SYSTEM** (evita el problema de contraseñas de usuario y corre sin sesión iniciada), y el guard del orquestador impide la doble ejecución si disparan las dos el mismo día:

```bat
:: 1) Al arrancar el PC (lo encienden a las 09:00), con retardo de 10 min
::    para que el servicio Firebird este levantado:
schtasks /Create /TN "GrupoChemie_ONSTART" /TR "C:\grupo_chemie\pipeline.bat" /SC ONSTART /DELAY 0010:00 /RU SYSTEM /RL HIGHEST /F

:: 2) Red de seguridad: si un dia el PC ya estaba encendido de antes (ONSTART no dispara),
::    la diaria de las 09:15 cubre el hueco:
schtasks /Create /TN "GrupoChemie_DIARIA" /TR "C:\grupo_chemie\pipeline.bat" /SC DAILY /ST 09:15 /RU SYSTEM /RL HIGHEST /F
```

Detalles exactos: `/RU SYSTEM` no pide `/RP` (sin contraseña); `/RL HIGHEST` ejecuta con elevación; `/F` sobrescribe si ya existe; el directorio de trabajo lo fija el `cd /d` del .bat (schtasks no tiene parámetro para ello); la redirección `>> logs\scheduler.log 2>&1` del .bat captura stdout y errores. El formato de `/DELAY` es `mmmm:ss` (0010:00 = 10 minutos) y solo es válido con ONSTART/ONLOGON/ONEVENT — **verifícalo en el propio PC con `schtasks /Create /?`**; si tu build de Windows lo rechazara, crea la tarea en la GUI del Programador de tareas: desencadenador "Al iniciar el equipo" → "Retrasar tarea durante: 10 minutos", ejecutar con la cuenta SYSTEM, "Ejecutar con los privilegios más altos".

Verificación tras crearlas:

```bat
schtasks /Query /TN "GrupoChemie_ONSTART" /V /FO LIST
schtasks /Run /TN "GrupoChemie_DIARIA"        :: prueba de fuego manual
type C:\grupo_chemie\logs\scheduler.log       :: debe terminar en PIPELINE COMPLETO OK
```

Nota SYSTEM + permisos: SYSTEM tiene acceso total a `C:\grupo_chemie`, ejecuta gbak y rclone sin problema **siempre que rclone use `--config` con ruta explícita** (ya lo hace el orquestador): sin ese flag, rclone buscaría su config en el perfil de SYSTEM (`C:\Windows\System32\config\systemprofile\...`) y no la encontraría.

### 6.4 Retención (punto 14 — ya resuelto arriba)

Integrada en `run_pipeline.py` y validada en vivo: extractos AAAA-MM-DD > 12 semanas se borran conservando siempre los 4 más recientes y sin tocar `_esquema`; los `.fbk` > 8 semanas se borran conservando los 3 más recientes por empresa. En Drive no hace falta retención: solo se sincroniza `publicar\` (el informe vigente), no los extractos.

---

## FASE 7 — SINCRONIZACIÓN A GOOGLE DRIVE (punto 13)

### 7.1 Comparación y decisión

| Criterio (tarea programada, sin usuario delante) | Google Drive for Desktop | rclone |
|---|---|---|
| ¿Corre sin sesión de usuario iniciada? | No: es una app de bandeja, necesita sesión interactiva | Sí: ejecutable de línea de comandos, invocable por SYSTEM |
| ¿Invocable por ejecución (al final del pipeline)? | No: sincroniza en continuo, sin control por-run | Sí: `rclone copy` explícito, exit code comprobable |
| Autenticación | Ligada al navegador/sesión | Token OAuth en fichero de config, refresco automático |
| Huella y mantenimiento | Pesada, se autoactualiza, fallos silenciosos | Un .exe portable, log propio por ejecución |
| Alcance sobre tu Drive | Ve todo el Drive | Con scope `drive.file`, solo ve/toca lo que él mismo crea |

**Ganador sin discusión para este caso: rclone.** El scope `drive.file` es además el aislamiento perfecto para tu situación: los datos de empresa que suba rclone quedan en tu Drive, visibles para ti con normalidad, pero rclone no puede leer nada más de tu Drive personal.

### 7.2 Instalación y configuración exacta

```bat
:: Descarga el zip de rclone para windows/amd64 desde rclone.org y extrae rclone.exe a:
mkdir C:\grupo_chemie\rclone
:: (copiar rclone.exe ahi)

:: Configuracion — UNA vez, interactiva, via AnyDesk (abre navegador para OAuth):
C:\grupo_chemie\rclone\rclone.exe config --config C:\grupo_chemie\config\rclone.conf
```

En el asistente: `n` (new remote) → nombre: `gdrive` → storage: `drive` (Google Drive) → client_id/secret: vacío (Enter; el compartido de rclone sobra para un informe semanal de KBs — si algún día notas throttling, se crea un client_id propio en Google Cloud Console, opcional) → scope: opción **`drive.file`** → root_folder_id y service_account: vacío → auto config: **yes** (se abre el navegador en la sesión de AnyDesk; autoriza con tu cuenta de Google) → confirmar.

Verificación:

```bat
C:\grupo_chemie\rclone\rclone.exe lsd gdrive: --config C:\grupo_chemie\config\rclone.conf
C:\grupo_chemie\rclone\rclone.exe copy C:\grupo_chemie\publicar gdrive:GrupoChemie/publicar --config C:\grupo_chemie\config\rclone.conf -v
```

Tras esto, en tu Drive aparece `GrupoChemie/publicar/informe_semanal.html`: ábrelo desde el móvil cuando quieras, sin AnyDesk. El orquestador ya lanza esta copia al final de cada ciclo (paso "drive", no crítico). El token se refresca solo dentro de `rclone.conf`; ese fichero está en el `.gitignore` de la Parte A — no sale del PC.

---

## FASE 8 — BACKUPS EN PRODUCCIÓN

Los comandos y la doctrina completa (gbak/nbackup) están en el **Anexo A de la Parte A**. En producción quedan así: el orquestador lanza `gbak -b -g -v` de las 3 bases cada lunes automáticamente (Fase 6.1); tu único ritual manual es la **prueba de restauración mensual** (`gbak -c` a `backups\_test_restore\`, verificar que abre y un COUNT cuadra, borrar). Apúntalo como recurrente el primer lunes de mes.

---

## FASE 9 — VALIDACIÓN FINAL (punto 15 del encargo)

### 9.0 Lo primero: las cifras de control viven en DOS universos distintos

Demostración aritmética con tus propias cifras:

- 143.222,31 / **778.715,80** = **18,39 %** ✓ (coincide exactamente con el % del CSV de clientes)
- 143.222,31 / 614.619,45 = 23,30 % ✗
- 265.456,28 / **614.619,45** = **43,19 %** ✓ (coincide exactamente con el % de margen documentado)

Conclusión ineludible: **el dato de top-cliente (MABE 143.222,31 € = 18,39 %) se calculó sobre el universo COMERCIAL (778.715,80 €), mientras que el par facturación/margen (614.619,45 € / 265.456,28 €) es del universo CONTABLE.** Validar cada cifra contra su universo; mezclar universos garantiza "no cuadra" sin que nada esté mal.

### 9.1 Validaciones sobre el universo comercial (v_ventas_linea)

```sql
-- V1: facturacion comercial Chemie 2025 -> esperado ~778.715,80 € (tolerancia inicial ±0,5 %)
SELECT ROUND(SUM(importe), 2) AS ventas_2025
FROM v_ventas_linea
WHERE empresa = 'CHEMIE' AND fecha BETWEEN DATE '2025-01-01' AND DATE '2025-12-31';

-- V2: top cliente 2025 -> esperado S.A.T. HORTOFRUTICOLA MABE, 143.222,31 € y 18,39 %
SELECT cliente, ROUND(SUM(importe), 2) AS ventas,
       ROUND(100.0 * SUM(importe) / SUM(SUM(importe)) OVER (), 2) AS pct
FROM v_ventas_linea
WHERE empresa = 'CHEMIE' AND fecha BETWEEN DATE '2025-01-01' AND DATE '2025-12-31'
GROUP BY 1 ORDER BY ventas DESC LIMIT 5;
```

### 9.2 Validación sobre el universo contable (MOVIMIENTOSDIARIO)

`MOVIMIENTOSDIARIO` es tabla real confirmada; inclúyela en `tablas_objetivo`. La cifra contable sale del grupo 70 del plan:

```sql
-- V3: ventas contables Chemie 2025 -> esperado ~614.619,45 €
-- (nombres de columna del diario segun esquema_CHEMIE.csv: cuenta, fecha, debe, haber)
SELECT ROUND(SUM(haber) - SUM(debe), 2) AS ventas_contables_2025
FROM stg_diario   -- mapeo adicional sobre raw_chemie_movimientosdiario
WHERE cuenta LIKE '70%' AND fecha BETWEEN DATE '2025-01-01' AND DATE '2025-12-31';
```

El delta entre universos, **778.715,80 − 614.619,45 = 164.096,35 €**, es un entregable propio de conciliación, no un fallo del pipeline: hipótesis a cerrar con datos (intragrupo, abonos/rectificativas, series no contabilizadas, albaranes sin facturar, IVA). Es, con ventaja, tu mejor primera pregunta técnica para Javier en septiembre: llegas con el descuadre cuantificado y las hipótesis listadas, no con una sospecha vaga.

### 9.3 Validación fresca — cierre de mayo 2026 (de tu propio repo)

```sql
-- V4: mayo 2026 Chemie -> esperado: 35.129,10 € ventas s/IVA; 33 facturas; 21 clientes;
--     margen 48,40 %; compras 21.251,04 €
SELECT ROUND(SUM(importe),2) AS ventas,
       COUNT(DISTINCT factura) AS facturas,
       COUNT(DISTINCT cliente_id) AS clientes,
       ROUND(100.0*SUM(margen_calc)/NULLIF(SUM(importe),0),2) AS margen_pct
FROM v_ventas_linea
WHERE empresa='CHEMIE' AND fecha BETWEEN DATE '2026-05-01' AND DATE '2026-05-31';

SELECT ROUND(SUM(importe),2) AS compras
FROM v_compras_linea
WHERE empresa='CHEMIE' AND fecha BETWEEN DATE '2026-05-01' AND DATE '2026-05-31';
```

Esta es la validación más valiosa de las cuatro: es reciente, la produjiste tú con el método antiguo, y si cuadra confirma a la vez extracción, mapeo y tipado.

### 9.4 Tolerancias y criterio de aceptación

- Primera pasada: **±0,5 %** por cifra, cada una contra su universo. Suficiente para dar el pipeline por bueno.
- Segunda pasada (sin prisa, en agosto): reconciliar **a céntimo** V1 y V4; documentar cada exclusión encontrada (serie, tipo de documento, estado) como filtro explícito y comentado en el mapeo.

### 9.5 Árbol de diagnóstico si NO cuadra (en orden de probabilidad)

1. **Universo equivocado** — estás comparando comercial contra contable. Revisa 9.0 antes que nada.
2. **Fan-out del join cabecera×líneas** — el join duplica líneas. Test: `SELECT factura, COUNT(*) FROM v_ventas_linea GROUP BY 1 ORDER BY 2 DESC LIMIT 5` y compara contra las líneas reales de esas facturas en el ERP. Si hay duplicación, la clave del join está incompleta (falta serie o ejercicio en la condición).
3. **Abonos/rectificativas** — ¿entran con signo negativo o los estás excluyendo? Deben entrar con su signo.
4. **Filtro de serie o tipo de documento** — el listado del ERP que generó la cifra de control quizá excluía series (proformas, presupuestos). Mira qué series existen: `SELECT DISTINCT serie... ` y prueba a excluir/incluir.
5. **Campo de fecha equivocado** — fecha de factura vs fecha de registro vs fecha de vencimiento. En el esquema habrá varias FECHA*; la buena es la de emisión del documento.
6. **IVA incluido** — si tu suma sale ~21 % alta, estás sumando total con IVA en vez de base.
7. **Base de empresa equivocada** — ruta .fdb cruzada en config.json (lo delataría también el manifest: recuentos absurdos).
8. **Año fiscal vs natural** — poco probable aquí, pero gratis de descartar.

**Regla dura:** si V1/V2/V4 no cuadran en ±0,5 %, **no se construye ni un KPI más** hasta encontrar la causa en este árbol. Cuadrar primero, ampliar después.

---

## CALENDARIO JULIO → 15 SEPTIEMBRE

| Cuándo | Qué | Criterio de hecho |
|---|---|---|
| Julio, sem. 1–2 | Parte A entera (Fases 0–2) + subirme los `esquema_*.csv` | `test_conexion.py` en verde con LECTOR; tildes OK; te devuelvo los 4 mapeos rellenos |
| Julio, sem. 3–4 | Parte B: primera extracción real + build + prueba de humo | V1, V2 y V4 dentro de ±0,5 %; EJIDOMAR visible en A2 |
| Agosto, sem. 1–2 | Fases 5+7: informe semanal en Drive; ciclo manual semanal (pipeline.bat) | Informe legible en el móvil sin AnyDesk |
| Agosto, sem. 3–4 | Fase 9 fina: conciliación de universos (V3, delta 164 k€ despiezado); fijar umbral € del tramo >60d; runbook en el repo | Documento de conciliación con hipótesis cuantificadas |
| 1–15 sept | Fase 6.3: tareas SYSTEM creadas; ciclo desatendido completo | Un día entero sin tocar nada: extracto + informe + Drive solos; `PIPELINE COMPLETO OK` en scheduler.log |
| Post 15-sept | Limpieza maestro ACI con Javier; histórico 2024 re-extraído para alertas interanuales; Power BI exploratorio; ampliar tablas (stock, lotes) | — |

Recordatorio de la capa política (del documento de diseño, sigue vigente): el sistema se presenta como tu herramienta personal de aprendizaje de la operativa, no como fiscalización de Javier ni de tu padre. El descuadre de 164 k€ se lleva como pregunta, no como acusación.

---

## CIERRE DEL MANUAL — checklist de sistema en producción

1. ☐ Partes A y B completas (sus checklists de cierre en verde).
2. ☐ `report.py` + `informe.html.j2` generando informe con todas las secciones mapeadas.
3. ☐ `run_pipeline.py` + `pipeline.bat` ejecutando el ciclo completo a mano sin errores.
4. ☐ rclone configurado con scope `drive.file`; informe visible en Drive desde el móvil.
5. ☐ Validaciones V1, V2 y V4 dentro de ±0,5 % (y V3 lanzada, aunque la conciliación fina siga abierta).
6. ☐ Tareas `GrupoChemie_ONSTART` y `GrupoChemie_DIARIA` creadas como SYSTEM y probadas con `schtasks /Run`.
7. ☐ gbak automático de lunes verificado y primera prueba de restauración mensual hecha.
8. ☐ Retención comprobada tras 13+ extractos (la carpeta más antigua desaparece sola).
9. ☐ Repo actualizado: scripts en `sql/03_scripts/`, este manual en `sql/01_guias_claude/`, decisión de arquitectura en `sql/02_decisiones/`, y `.gitignore` protegiendo config/datos.

Con el punto 9 marcado, el sistema cumple el criterio de éxito original: **ciclo completo desatendido en el PC de la empresa, sin infraestructura personal, con cifras validadas contra controles conocidos y alertas activas sobre los riesgos reales del grupo (contaminación de maestro, EJIDOMAR, concentración, cartera vencida).**
