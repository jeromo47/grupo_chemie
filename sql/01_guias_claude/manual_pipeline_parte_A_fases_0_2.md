# MANUAL EJECUTABLE — PARTE A (Fases 0–2 + Backups Firebird)

**Pipeline Grupo Chemie: Firebird 2.5 → Python → Parquet → DuckDB → Informe → Drive**
**Versión 1.0 — 2026-07-05. Parte A de 3. Cubre los puntos 1–7 del encargo.**

- **Parte A (este archivo):** decisiones verificadas, reconocimiento del entorno, instalación base, descubrimiento del esquema, usuario de solo lectura, backups gbak/nbackup.
- **Parte B:** scripts de extracción a Parquet, reconstrucción DuckDB, vistas canónicas y alertas (puntos 8–10).
- **Parte C:** informe semanal, tarea programada, sincronización Drive, retención y validación final (puntos 11–15).

**Ubicación en tu repo (según tu convención de `sql/README.md`):** este manual → `sql/01_guias_claude/`; los scripts → `sql/03_scripts/`; las decisiones cerradas → `sql/02_decisiones/`.

---

## 0. DECISIONES VERIFICADAS (puntos 1 y 2 del encargo)

Verificaciones ejecutadas en vivo el 2026-07-05 (PyPI JSON API, instalación real bajo Python 3.12.3, inspección de tu repo GitHub):

| Componente | Decisión | Versión exacta | Cómo se verificó |
|---|---|---|---|
| Driver Python Firebird | **`fdb`** | **2.0.4** | PyPI en vivo: última release subida **2025-07-22**, descripción oficial: *"Legacy Python driver for Firebird 2.5"*. Instalado e importado bajo Python 3.12.3: OK. Wheel universal `py2.py3-none-any` (puro ctypes, sin compilación, sin problemas con versiones nuevas de Python). |
| Alternativa descartada | `firebird-driver` | 2.0.3 | Su propia descripción en PyPI declara **"Requires: Firebird 3+"**. Incompatible con servidor 2.5. Descartado con fuente, no por opinión. |
| Python | **3.12.x de 64 bits, obligatorio** | última 3.12.x de python.org | Todo el código de este manual se ejecutó bajo 3.12.3. El motivo del x64 está en la fila siguiente. |
| pyarrow | escritura Parquet tipado | **24.0.0** | PyPI en vivo: **NO existe wheel win32**, solo `win_amd64`. Un Python de 32 bits no puede instalar pyarrow. |
| duckdb | base analítica | **1.5.4** | PyPI en vivo: **NO existe wheel win32**, solo `win_amd64`/`win_arm64`. Mismo motivo. |
| jinja2 | plantilla del informe | **3.1.6** | Instalado; render con formato es-ES probado. |
| Cliente Firebird | **fbclient.dll 2.5.9 de 64 bits** (kit oficial x64), aparte de la del ERP | 2.5.9 | Consecuencia en cadena: Python x64 solo carga DLL x64 vía ctypes; la DLL del ERP será x86 casi seguro (se comprueba en 0.4). Un cliente 2.5 x64 habla sin problema con un servidor 2.5 x86 por TCP: el protocolo de red no depende de la bitness. |

**Resolución del punto 1 del encargo, en una frase:** `fdb==2.0.4` sobre Python 3.12 x64, cargando una `fbclient.dll` 2.5.9 x64 propia, conectando por TCP a `localhost` contra el servidor que ya corre. `firebird-driver` queda descartado para siempre en este proyecto mientras el servidor sea 2.5.

### Correcciones al diseño previo, descubiertas inspeccionando tu repo GitHub

El repo `jeromo47/grupo_chemie` sí era accesible y lo revisé entero. Cinco hallazgos que cambian cosas:

1. **La cartera de cobros/pagos SÍ existe en el ERP y ya la extrajiste una vez.** Tu DuckDB previo contiene `t_07b_clientes_pendientes_grupo_2025` (87 filas: FACTURA, EFECTO, FECHA_VTO, IMPORTE_PENDIENTE, DIAS_VENCIDO, TRAMO_ANTIGUEDAD, flags) y `t_07c_proveedores_pendientes_grupo_2025` (42 filas). El "gap crítico de tesorería" se reformula: **el dato existe; lo que no existe es un flujo recurrente y tipado.** Eso es exactamente lo que monta este manual.
2. **Tablas Firebird reales ya confirmadas por tu propio descubrimiento previo:** `VTOSCLIENTES`, `CLIENTES`, `MOVIMIENTOSDIARIO`, `PLANCONTABLE` (constan en `14_control_proyecto_chemie/`). Convención de MasterSQL: español, mayúsculas, plural, sin prefijos. La Fase 2 parte de ahí, no de cero.
3. **Tu DuckDB previo tiene las 51 tablas enteras en VARCHAR** (todo texto, según `12B_diccionario_columnas.md`). Este pipeline lo sustituye por tipos reales (DECIMAL/DATE), que es lo que permite validar a céntimo.
4. **Tu método actual de extracción es volcado de texto tipo isql** ("he limpiado cabeceras repetidas y espacios de salida de Firebird", en `20B_VALIDACION_CIERRE_MAYO_2026.md`). Ese paso de limpieza manual desaparece con `fdb`: los datos llegan ya tipados.
5. **Cifra de control fresca disponible para la validación final (Parte C):** cierre mayo 2026 Chemie = 35.129,10 € ventas s/IVA, 33 facturas, 21 clientes, margen 48,40 %, compras 21.251,04 € (de tu propio repo).

---

## FASE 0 — RECONOCIMIENTO (solo lectura, 1 sesión AnyDesk, ~45 min)

Todo en PowerShell **como administrador**. Nada de esta fase escribe en la base de datos.

### 0.1 Localizar el servicio Firebird, su ruta y su puerto

```powershell
Get-CimInstance Win32_Service | Where-Object {$_.Name -like "*Firebird*" -or $_.DisplayName -like "*Firebird*"} | Select-Object Name, State, StartMode, PathName
```

Apunta `PathName` → esa es la carpeta de instalación del servidor (p. ej. `C:\Program Files (x86)\Firebird\Firebird_2_5\bin\fbserver.exe`). A esa carpeta base la llamaremos `%FBDIR%` en el resto del manual (la raíz, sin `\bin`).

Puerto (por defecto 3050):

```powershell
Get-NetTCPConnection -State Listen | Where-Object {$_.LocalPort -eq 3050} | Select-Object LocalAddress, LocalPort, OwningProcess
# Si no aparece nada en 3050, mira el puerto configurado:
Select-String -Path "%FBDIR%\firebird.conf" -Pattern "RemoteServicePort"
```

**Bifurcación crítica:** si NO existe servicio Firebird, el ERP estaría usando Firebird **embedded** (`fbembed.dll` en la carpeta de MasterSQL), que en 2.5/Windows abre el archivo en exclusiva. Con varios puestos de la oficina usando MasterSQL contra este PC, es casi imposible que sea embedded — pero compruébalo. Si fuera embedded: **párate aquí y me lo dices**; cambia el plan de conexión y no tiene sentido seguir con esta parte tal cual.

### 0.2 Versión exacta del motor

```powershell
& "%FBDIR%\bin\isql.exe" -z -q
```

Muestra algo tipo `ISQL Version: WI-V2.5.x.xxxxx`. Sal con `QUIT;`. (Alternativa una vez conectados en 1.6: `SELECT rdb$get_context('SYSTEM','ENGINE_VERSION') FROM rdb$database;`)

### 0.3 Localizar los tres .fdb (Chemie, ACI, Ecoclean)

```powershell
Get-Content "%FBDIR%\aliases.conf"   # alias = ruta, si MasterSQL usa alias
# Si no hay alias útiles, búsqueda directa:
Get-ChildItem -Path C:\,D:\ -Recurse -Include *.fdb,*.gdb -ErrorAction SilentlyContinue | Select-Object FullName, Length, LastWriteTime
```

Apunta las tres rutas completas. Verifica cuál es cuál por nombre, tamaño y fecha de última escritura (la que se modifica cada día laborable es la activa).

### 0.4 Bitness de la fbclient.dll existente (punto 2 del encargo)

Comprobación no destructiva leyendo la cabecera PE del fichero (no ejecuta ni carga la DLL, solo lee bytes):

```powershell
function Get-DllBitness($path) {
  $b = [System.IO.File]::ReadAllBytes($path)
  $pe = [BitConverter]::ToInt32($b, 0x3C)
  $m  = [BitConverter]::ToUInt16($b, $pe + 4)
  if ($m -eq 0x8664) { "x64" } elseif ($m -eq 0x14C) { "x86 (32-bit)" } else { "otro: 0x{0:X4}" -f $m }
}
# Candidatas típicas:
Get-DllBitness "%FBDIR%\bin\fbclient.dll"
if (Test-Path "C:\Windows\System32\fbclient.dll") { Get-DllBitness "C:\Windows\System32\fbclient.dll" }   # si existe aquí, es x64
if (Test-Path "C:\Windows\SysWOW64\fbclient.dll") { Get-DllBitness "C:\Windows\SysWOW64\fbclient.dll" }   # si existe aquí, es x86
# Y la que use MasterSQL (fbclient.dll o su alias legado gds32.dll en la carpeta del ERP):
Get-ChildItem "C:\" -Recurse -Include fbclient.dll,gds32.dll -ErrorAction SilentlyContinue | Select-Object FullName
```

Regla de decisión (se ejecuta en Fase 1.4):
- Si `C:\Windows\System32\fbclient.dll` existe y es x64 → **se usará esa, sin descargar nada**.
- Si solo hay fbclient x86 (lo esperable) → en Fase 1.4 descargarás el kit ZIP x64 de Firebird 2.5.9.
- La DLL del ERP **no se toca, no se mueve y no se sustituye jamás**. Nuestra x64 vive en carpeta propia.

Confirma también la arquitectura de Windows (será x64, pero confírmalo):

```powershell
systeminfo | findstr /i "System Type"
```

### 0.5 Cómo te has estado conectando hasta ahora (comprobación de seguridad)

Has dicho que "haces consultas query al archivo de la bbdd". Verifica en tu herramienta actual (FlameRobin, IBExpert, DBeaver, lo que uses) el campo de conexión:

- Si conecta como `localhost:C:\ruta\BASE.FDB` (o `localhost/3050:...`) → **correcto**, vas a través del servidor. Sigue así.
- Si conecta con la **ruta a secas** (`C:\ruta\BASE.FDB` sin host) y la herramienta lleva motor embedded propio → **has estado jugando con fuego**: dos motores abriendo el mismo archivo es el escenario clásico de corrupción en Firebird 2.5. Desde hoy, siempre con `localhost:` delante de la ruta.

### 0.6 Credenciales (sin tocar SYSDBA)

Prueba primero la contraseña por defecto (instalaciones de este perfil la dejan puesta muy a menudo):

```powershell
& "%FBDIR%\bin\isql.exe" -user SYSDBA -password masterkey "localhost:C:\RUTA_COMPLETA\CHEMIE.FDB"
```

Si entra, dentro de isql:

```sql
SELECT COUNT(*) FROM CLIENTES;
QUIT;
```

- Si `masterkey` no funciona: busca la contraseña en los archivos de configuración de MasterSQL (`.ini`, `.cfg`, o registro de Windows bajo claves de Tecnimática/MasterSQL). Los ERP Delphi de esta generación suelen guardarla en texto plano u ofuscación trivial.
- Si tu herramienta actual ya conecta, esa credencial vale: apúntala tal cual.
- **PROHIBIDO cambiar la contraseña de SYSDBA** (nada de `gsec -mo SYSDBA`): vive en `security2.fdb` a nivel de servidor, y si MasterSQL la lleva hardcodeada, romperías el ERP de toda la oficina. En Fase 2.6 creamos un usuario nuevo en vez de tocar el existente.

### 0.7 Exclusión de antivirus (causa clásica de corrupción de .fdb)

```powershell
Add-MpPreference -ExclusionExtension ".fdb"
Add-MpPreference -ExclusionPath "CARPETA_DONDE_ESTAN_LOS_FDB"
Get-MpPreference | Select-Object ExclusionExtension, ExclusionPath
```

(Si hay antivirus de terceros en vez de Windows Defender, la exclusión se hace en su consola; el concepto es idéntico: el AV no debe escanear ni bloquear los `.fdb` en caliente.)

### 0.8 Checklist de salida de Fase 0 — apunta esto y guárdalo

| Dato | Valor |
|---|---|
| %FBDIR% (carpeta raíz del servidor Firebird) | |
| Versión del motor (WI-V2.5.__) | |
| Puerto (3050 u otro) | |
| Ruta .fdb CHEMIE | |
| Ruta .fdb ACI | |
| Ruta .fdb ECOCLEAN | |
| Bitness fbclient del ERP | |
| ¿Existe fbclient x64 en System32? (sí/no) | |
| Usuario/contraseña que funcionan | |
| ¿Herramienta actual conecta vía localhost:? (sí/no) | |

---

## FASE 1 — INSTALACIÓN BASE (~30 min)

### 1.1 Python 3.12 x64, instalación silenciosa

Descarga desde python.org el instalador **Windows installer (64-bit)** de la última 3.12.x y ejecútalo así:

```bat
python-3.12.10-amd64.exe /passive InstallAllUsers=1 PrependPath=1 Include_launcher=1
```

Verificación obligatoria de que es de 64 bits:

```bat
py -3.12 -c "import struct; print(struct.calcsize('P')*8)"
```

Debe imprimir **64**. Si imprime 32, has instalado el instalador equivocado: desinstala y repite.

### 1.2 Estructura de carpetas (exacta)

```bat
mkdir C:\grupo_chemie
cd C:\grupo_chemie
mkdir config scripts sql sql\mapping sql\vistas sql\alertas extracts data informes publicar logs backups backups\_test_restore fbclient_x64
```

### 1.3 Entorno virtual y dependencias pineadas

```bat
cd C:\grupo_chemie
py -3.12 -m venv venv
venv\Scripts\python.exe -m pip install --upgrade pip
```

Crea `C:\grupo_chemie\requirements.txt` con exactamente esto:

```text
fdb==2.0.4
duckdb==1.5.4
pyarrow==24.0.0
jinja2==3.1.6
```

```bat
venv\Scripts\pip.exe install -r requirements.txt
```

### 1.4 Cliente Firebird x64 (resolución del punto 2 del encargo)

Según lo que salió en Fase 0.4:

- **Caso A — ya existe fbclient x64 en `C:\Windows\System32`:** en `config.json` (paso 1.5) pon `"fbclient_dll": "C:\\Windows\\System32\\fbclient.dll"` y no descargues nada.
- **Caso B (esperable) — solo hay fbclient x86:** descarga de firebirdsql.org, sección de descargas de Firebird 2.5, el **ZIP kit x64** de la versión 2.5.9 (fichero tipo `Firebird-2.5.9.27139-0_x64.zip`, la variante zip sin instalador). Extrae el ZIP y copia a `C:\grupo_chemie\fbclient_x64\` estos ficheros desde su `\bin` y raíz: `fbclient.dll`, `icudt30.dll`, `icuin30.dll`, `icuuc30.dll`, y los runtime `msvcp80.dll` / `msvcr80.dll` si vienen en el kit. **No instales nada**: son ficheros sueltos en una carpeta propia; el servicio Firebird existente ni se entera.

El código carga la DLL de forma explícita (ya incluido en los scripts):

```python
os.add_dll_directory(r"C:\grupo_chemie\fbclient_x64")
fdb.load_api(r"C:\grupo_chemie\fbclient_x64\fbclient.dll")
```

El `add_dll_directory` es necesario en Python 3.8+ para que Windows resuelva las DLL dependientes (ICU, runtime) desde la carpeta de la fbclient. Un cliente 2.5.9 x64 contra un servidor 2.5.x x86 en `localhost` es plenamente compatible: mismo protocolo de red.

### 1.5 Configuración y perímetro de credenciales

Crea `C:\grupo_chemie\config\config.json` (rellena con los valores de la checklist 0.8):

```json
{
  "fbclient_dll": "C:\\grupo_chemie\\fbclient_x64\\fbclient.dll",
  "host": "localhost",
  "puerto": 3050,
  "usuario": "SYSDBA",
  "password": "PON_AQUI_LA_REAL",
  "charset_conexion": "PENDIENTE_FASE_2_1",
  "empresas": {
    "CHEMIE":   {"fdb": "C:\\ruta\\real\\CHEMIE.FDB"},
    "ACI":      {"fdb": "C:\\ruta\\real\\ACI.FDB"},
    "ECOCLEAN": {"fdb": "C:\\ruta\\real\\ECOCLEAN.FDB"}
  },
  "tablas_objetivo": ["SE_RELLENA_EN_FASE_2"],
  "tablas_criticas": ["VTOSCLIENTES"],
  "retencion_semanas_extracts": 12,
  "retencion_semanas_fbk": 8,
  "gbak_exe": "C:\\Program Files (x86)\\Firebird\\Firebird_2_5\\bin\\gbak.exe",
  "dia_gbak": 0
}
```

(`dia_gbak: 0` = lunes; la Parte C usa estos campos de retención y backup.)

Crea `C:\grupo_chemie\.gitignore` (si versionas esta carpeta en tu repo):

```text
config/config.json
config/rclone.conf
extracts/
data/
logs/
backups/
publicar/
venv/
fbclient_x64/
```

**Regla de perímetro:** en GitHub solo van scripts, SQL y este manual. Credenciales, datos, backups y binarios, jamás.

### 1.6 Test de conexión mínimo (punto 5 del encargo: transacción de solo lectura)

**Sintaxis exacta y justificación del TPB:** usamos transacción **READ ONLY + CONCURRENCY (snapshot) + WAIT**. Efectos: vista consistente de todas las tablas durante toda la extracción (todas las SELECT ven el mismo instante), cero bloqueo a los escritores del ERP (los lectores no bloquean en la arquitectura MVCC de Firebird), e impacto en el garbage collection despreciable para una transacción que vive minutos. Nota verificada en fdb 2.0.4 por introspección real: los atributos `TPB.access_mode / isolation_level / lock_resolution` existen, y también la constante `fdb.ISOLATION_LEVEL_READ_COMMITED_RO` (ojo: con una sola T en COMMITED, es la grafía oficial del paquete). No usamos esa constante porque es read-committed; queremos snapshot para que las tablas extraídas sean coherentes entre sí.

Crea `C:\grupo_chemie\scripts\test_conexion.py`:

```python
import os, json, sys
from pathlib import Path
import fdb

BASE = Path(__file__).resolve().parent.parent
cfg = json.loads((BASE / "config" / "config.json").read_text(encoding="utf-8"))

dll = Path(cfg["fbclient_dll"])
os.add_dll_directory(str(dll.parent))
fdb.load_api(str(dll))

def tpb_solo_lectura():
    tpb = fdb.TPB()
    tpb.access_mode = fdb.isc_tpb_read            # READ ONLY
    tpb.isolation_level = fdb.isc_tpb_concurrency # SNAPSHOT consistente
    tpb.lock_resolution = fdb.isc_tpb_wait
    return tpb

cs = cfg["charset_conexion"]
for emp, e in cfg["empresas"].items():
    dsn = f"{cfg['host']}/{cfg['puerto']}:{e['fdb']}"
    try:
        con = fdb.connect(dsn=dsn, user=cfg["usuario"], password=cfg["password"],
                          charset=None if cs.startswith("PENDIENTE") else cs)
        tr = con.trans(default_tpb=tpb_solo_lectura())
        cur = tr.cursor()
        cur.execute("SELECT rdb$get_context('SYSTEM','ENGINE_VERSION'), current_timestamp FROM rdb$database")
        print(emp, "OK ->", cur.fetchone())
        tr.commit(); con.close()
    except Exception as ex:
        print(emp, "FALLO ->", ex); sys.exit(1)
print("CONEXION VERIFICADA EN LAS 3 BASES")
```

Ejecuta:

```bat
C:\grupo_chemie\venv\Scripts\python.exe C:\grupo_chemie\scripts\test_conexion.py
```

Salida esperada: tres líneas `OK -> ('2.5.x', datetime(...))` y el mensaje final. Si falla:
- `unable to complete network request` → servicio parado o puerto equivocado (Fase 0.1).
- `Your user name and password are not defined` → credencial equivocada (Fase 0.6).
- `Unable to load fbclient` o error de DLL → bitness equivocada o faltan las ICU/runtime en la carpeta (Fase 1.4).

---

## FASE 2 — DESCUBRIMIENTO DEL ESQUEMA (semana 1 de julio)

### 2.1 Charset real (punto 3 del encargo)

Charset por defecto de cada base:

```sql
SELECT TRIM(cs.RDB$CHARACTER_SET_NAME) AS charset_por_defecto
FROM RDB$DATABASE d
JOIN RDB$CHARACTER_SETS cs ON cs.RDB$CHARACTER_SET_ID = d.RDB$CHARACTER_SET_ID;
```

Y a nivel de columna (por si hay mezcla, frecuente en ERP veteranos):

```sql
SELECT TRIM(cs.RDB$CHARACTER_SET_NAME) AS charset, COUNT(*) AS n_columnas
FROM RDB$RELATION_FIELDS rf
JOIN RDB$FIELDS f ON f.RDB$FIELD_NAME = rf.RDB$FIELD_SOURCE
LEFT JOIN RDB$CHARACTER_SETS cs ON cs.RDB$CHARACTER_SET_ID = f.RDB$CHARACTER_SET_ID
JOIN RDB$RELATIONS r ON r.RDB$RELATION_NAME = rf.RDB$RELATION_NAME
WHERE COALESCE(r.RDB$SYSTEM_FLAG,0)=0 AND f.RDB$FIELD_TYPE IN (14,37)
GROUP BY 1 ORDER BY 2 DESC;
```

**Tabla de decisión** — rellena `charset_conexion` en `config.json` según el resultado:

| Resultado dominante | Valor en config | Efecto en fdb |
|---|---|---|
| WIN1252 | `"WIN1252"` | fdb devuelve `str` ya bien decodificado |
| ISO8859_1 | `"ISO8859_1"` | ídem |
| NONE | `"NONE"` | fdb devuelve `bytes`; el extractor de la Parte B ya los decodifica como `cp1252` (es lo que escriben los clientes Windows españoles sobre bases NONE) |

**Test obligatorio de tildes/ñ** (CLIENTES es tabla real confirmada):

```sql
SELECT FIRST 15 * FROM CLIENTES;
```

Los nombres tipo "MUÑOZ", "GARCÍA" deben verse correctos. Si salen `MUÃ‘OZ` o `MU?OZ`, el charset elegido es incorrecto: cambia según la tabla de decisión y repite el test. No sigas a la Fase 3 con tildes rotas: contaminarías todos los Parquet.

### 2.2 Inventario de tablas (punto 4 del encargo)

```sql
SELECT TRIM(RDB$RELATION_NAME) AS tabla
FROM RDB$RELATIONS
WHERE COALESCE(RDB$SYSTEM_FLAG,0)=0 AND RDB$VIEW_BLR IS NULL
ORDER BY 1;
```

(`RDB$SYSTEM_FLAG=0` excluye tablas de sistema; `RDB$VIEW_BLR IS NULL` excluye vistas.) Firebird 2.5 no tiene recuento rápido de filas en metadatos; con este tamaño de base, `SELECT COUNT(*)` por tabla es viable — el script `descubre.py` (2.7) lo hace por ti y vuelca todo a CSV.

### 2.3 Columnas y tipos por tabla

```sql
SELECT TRIM(rf.RDB$FIELD_NAME) AS columna,
       f.RDB$FIELD_TYPE AS tipo, f.RDB$FIELD_SUB_TYPE AS subtipo,
       f.RDB$FIELD_LENGTH AS longitud, f.RDB$FIELD_PRECISION AS precision_,
       f.RDB$FIELD_SCALE AS escala,
       TRIM(cs.RDB$CHARACTER_SET_NAME) AS charset,
       rf.RDB$NULL_FLAG AS not_null
FROM RDB$RELATION_FIELDS rf
JOIN RDB$FIELDS f ON f.RDB$FIELD_NAME = rf.RDB$FIELD_SOURCE
LEFT JOIN RDB$CHARACTER_SETS cs ON cs.RDB$CHARACTER_SET_ID = f.RDB$CHARACTER_SET_ID
WHERE rf.RDB$RELATION_NAME = 'VTOSCLIENTES'   -- cambia por cada tabla que estudies
ORDER BY rf.RDB$FIELD_POSITION;
```

**Mapa de códigos RDB$FIELD_TYPE en Firebird 2.5** (imprímetelo):

| Código | Tipo |
|---|---|
| 7 | SMALLINT |
| 8 | INTEGER |
| 10 | FLOAT |
| 12 | DATE |
| 13 | TIME |
| 14 | CHAR |
| 16 | BIGINT (con escala < 0 → NUMERIC/DECIMAL(18, \|escala\|)) |
| 27 | DOUBLE PRECISION |
| 35 | TIMESTAMP |
| 37 | VARCHAR |
| 261 | BLOB (subtipo 1 = texto) |

Regla clave: **escala negativa en tipos 7/8/16 significa NUMERIC/DECIMAL con esa escala** — así guarda MasterSQL los importes casi con total seguridad. El extractor de la Parte B los recibe como `decimal.Decimal` y los escribe como DECIMAL(18,4) en Parquet: exactitud a céntimo garantizada.

### 2.4 Claves e índices

```sql
-- PK/FK/UNIQUE con sus columnas
SELECT TRIM(rc.RDB$RELATION_NAME) AS tabla, TRIM(rc.RDB$CONSTRAINT_TYPE) AS tipo,
       TRIM(s.RDB$FIELD_NAME) AS columna, s.RDB$FIELD_POSITION AS pos
FROM RDB$RELATION_CONSTRAINTS rc
JOIN RDB$INDEX_SEGMENTS s ON s.RDB$INDEX_NAME = rc.RDB$INDEX_NAME
ORDER BY 1, 2, 4;

-- A qué tabla padre apunta cada FK (para reconstruir el modelo cabecera→líneas→maestros)
SELECT TRIM(rc.RDB$RELATION_NAME) AS tabla_hija, TRIM(rc2.RDB$RELATION_NAME) AS tabla_padre
FROM RDB$RELATION_CONSTRAINTS rc
JOIN RDB$REF_CONSTRAINTS ref ON ref.RDB$CONSTRAINT_NAME = rc.RDB$CONSTRAINT_NAME
JOIN RDB$RELATION_CONSTRAINTS rc2 ON rc2.RDB$CONSTRAINT_NAME = ref.RDB$CONST_NAME_UQ
WHERE rc.RDB$CONSTRAINT_TYPE = 'FOREIGN KEY';
```

### 2.5 Búsqueda dirigida de las tablas objetivo (con lo que ya sabes)

Confirmadas por tu descubrimiento previo: `VTOSCLIENTES`, `CLIENTES`, `MOVIMIENTOSDIARIO`, `PLANCONTABLE`. Por la convención de nombres de MasterSQL, lanza esto y marca candidatas:

```sql
SELECT TRIM(RDB$RELATION_NAME) FROM RDB$RELATIONS
WHERE COALESCE(RDB$SYSTEM_FLAG,0)=0 AND RDB$VIEW_BLR IS NULL
  AND (RDB$RELATION_NAME LIKE 'VTOS%' OR RDB$RELATION_NAME LIKE 'CLIENTE%'
    OR RDB$RELATION_NAME LIKE 'PROVEEDOR%' OR RDB$RELATION_NAME LIKE 'ARTICULO%'
    OR RDB$RELATION_NAME LIKE 'FAMILIA%' OR RDB$RELATION_NAME LIKE 'FACTURA%'
    OR RDB$RELATION_NAME LIKE 'LINEA%' OR RDB$RELATION_NAME LIKE 'ALBARAN%'
    OR RDB$RELATION_NAME LIKE 'PEDIDO%' OR RDB$RELATION_NAME LIKE 'MOVIMIENTO%'
    OR RDB$RELATION_NAME LIKE 'ALMACEN%' OR RDB$RELATION_NAME LIKE 'STOCK%'
    OR RDB$RELATION_NAME LIKE 'LOTE%' OR RDB$RELATION_NAME LIKE 'SERIE%'
    OR RDB$RELATION_NAME LIKE 'BANCO%' OR RDB$RELATION_NAME LIKE 'REMESA%'
    OR RDB$RELATION_NAME LIKE 'EFECTO%' OR RDB$RELATION_NAME LIKE 'COBRO%'
    OR RDB$RELATION_NAME LIKE 'PAGO%' OR RDB$RELATION_NAME LIKE 'TARIFA%'
    OR RDB$RELATION_NAME LIKE 'DESCUENTO%' OR RDB$RELATION_NAME LIKE 'COMERCIAL%'
    OR RDB$RELATION_NAME LIKE 'ZONA%' OR RDB$RELATION_NAME LIKE 'PLANCON%')
ORDER BY 1;
```

**Objetivo de salida:** rellenar en `config.json` la lista `tablas_objetivo` con ~10–15 nombres reales: ventas cabecera + líneas, `VTOSCLIENTES`, vencimientos de proveedor (busca `VTOSPROVEEDORES`), `CLIENTES`, `PROVEEDORES`, `ARTICULOS`, `FAMILIAS`, compras cabecera + líneas, stock, y `MOVIMIENTOSDIARIO` (imprescindible para el universo contable de la validación final de la Parte C).

### 2.6 Usuario Firebird de solo lectura (punto 6 del encargo)

En FB 2.5 los usuarios viven en `security2.fdb` (a nivel de servidor, comunes a las 3 bases); los GRANT son por base de datos. **Aviso de legado:** en 2.5 solo cuentan los **8 primeros caracteres** de la contraseña — elige una de exactamente 8 para no autoengañarte.

Conectado a cualquiera de las bases como SYSDBA (isql):

```sql
CREATE USER LECTOR PASSWORD 'Lect2026';
```

No existe `GRANT SELECT ON ALL TABLES` en 2.5. Genera los GRANT con la propia base — ejecuta esta consulta en **cada una** de las 3 bases y guarda la salida:

```sql
SELECT 'GRANT SELECT ON ' || TRIM(RDB$RELATION_NAME) || ' TO LECTOR;'
FROM RDB$RELATIONS
WHERE COALESCE(RDB$SYSTEM_FLAG,0)=0 AND RDB$VIEW_BLR IS NULL;
```

Guarda la salida como `C:\grupo_chemie\sql\grants_lector_CHEMIE.sql` (y equivalentes ACI/ECOCLEAN) y ejecútala:

```bat
"%FBDIR%\bin\isql.exe" -user SYSDBA -password LA_REAL "localhost:C:\ruta\CHEMIE.FDB" -i C:\grupo_chemie\sql\grants_lector_CHEMIE.sql
```

Después, en `config.json`: `"usuario": "LECTOR"`, `"password": "Lect2026"`. Vuelve a pasar `test_conexion.py` para confirmar.

Si por lo que sea no puedes crear usuarios (permisos, política del proveedor), seguir con las credenciales del ERP es aceptable: la transacción READ ONLY del TPB ya es tu protección de escritura. El usuario LECTOR es defensa en profundidad, no la única defensa.

### 2.7 Script de descubrimiento completo — `descubre.py`

Vuelca el inventario entero (tabla, filas, columnas, tipos) a un CSV por empresa, para trabajarlo en frío sin AnyDesk. Crea `C:\grupo_chemie\scripts\descubre.py`:

```python
import os, json, csv
from pathlib import Path
import fdb

BASE = Path(__file__).resolve().parent.parent
cfg = json.loads((BASE/"config"/"config.json").read_text(encoding="utf-8"))
os.add_dll_directory(str(Path(cfg["fbclient_dll"]).parent))
fdb.load_api(cfg["fbclient_dll"])

Q_TABLAS = """SELECT TRIM(RDB$RELATION_NAME) FROM RDB$RELATIONS
WHERE COALESCE(RDB$SYSTEM_FLAG,0)=0 AND RDB$VIEW_BLR IS NULL ORDER BY 1"""
Q_COLS = """SELECT TRIM(rf.RDB$FIELD_NAME), f.RDB$FIELD_TYPE, f.RDB$FIELD_SUB_TYPE,
f.RDB$FIELD_LENGTH, f.RDB$FIELD_SCALE FROM RDB$RELATION_FIELDS rf
JOIN RDB$FIELDS f ON f.RDB$FIELD_NAME=rf.RDB$FIELD_SOURCE
WHERE rf.RDB$RELATION_NAME=? ORDER BY rf.RDB$FIELD_POSITION"""

def tpb_ro():
    t = fdb.TPB(); t.access_mode = fdb.isc_tpb_read
    t.isolation_level = fdb.isc_tpb_concurrency; t.lock_resolution = fdb.isc_tpb_wait
    return t

out = BASE/"extracts"/"_esquema"; out.mkdir(parents=True, exist_ok=True)
cs = cfg["charset_conexion"]
for emp, e in cfg["empresas"].items():
    con = fdb.connect(dsn=f"{cfg['host']}/{cfg['puerto']}:{e['fdb']}",
                      user=cfg["usuario"], password=cfg["password"],
                      charset=None if cs.startswith("PENDIENTE") else cs)
    tr = con.trans(default_tpb=tpb_ro()); cur = tr.cursor()
    cur.execute(Q_TABLAS); tablas = [r[0] for r in cur.fetchall()]
    with open(out/f"esquema_{emp}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["tabla", "filas", "columna", "tipo", "subtipo", "longitud", "escala"])
        for t in tablas:
            try:
                cur.execute(f"SELECT COUNT(*) FROM {t}"); n = cur.fetchone()[0]
            except Exception:
                n = -1
            cur.execute(Q_COLS, (t,))
            for c in cur.fetchall():
                fila = [x.decode("cp1252", "replace") if isinstance(x, bytes) else x for x in c]
                w.writerow([t, n] + fila)
    tr.commit(); con.close()
    print(emp, len(tablas), "tablas ->", out/f"esquema_{emp}.csv")
```

```bat
C:\grupo_chemie\venv\Scripts\python.exe C:\grupo_chemie\scripts\descubre.py
```

Nota exacta: los nombres de tabla van **sin comillas** en las consultas (MasterSQL crea identificadores sin comillas → Firebird los guarda en mayúsculas y el SQL sin comillas los resuelve solo). Ejecuta esto fuera de horario pico (a las 09:10 o tras las 18:00): los COUNT(*) recorren tablas enteras.

### 2.8 Salida de Fase 2 (requisito para pasar a la Parte B)

- `config.json` completo: charset real + `tablas_objetivo` con 10–15 nombres reales + usuario LECTOR.
- Los tres `esquema_*.csv` guardados (súbelos a nuestro chat: con ellos te escribo la capa de mapeo de la Parte B con los nombres de columna reales, sin placeholders).
- Test de tildes/ñ pasado.
- `test_conexion.py` en verde con LECTOR.

---

## ANEXO A — BACKUPS FIREBIRD 2.5 EN WINDOWS (punto 7 del encargo)

### gbak — backup lógico (el que usarás)

Es el único backup que valida la estructura, compacta y es restaurable en cualquier máquina. **Es seguro con la base en uso**: abre su propia transacción snapshot y produce una copia consistente.

Backup semanal (la Parte C lo integra en el pipeline los lunes):

```bat
"C:\Program Files (x86)\Firebird\Firebird_2_5\bin\gbak.exe" -b -g -v -user SYSDBA -password LA_REAL localhost:C:\ruta\CHEMIE.FDB C:\grupo_chemie\backups\CHEMIE_2026-07-06.fbk -y C:\grupo_chemie\logs\gbak_chemie.log
```

Flags: `-b` backup, `-g` sin garbage collection (más rápido y no carga al servidor), `-v` verbose, `-y fichero` log de la operación. Ajusta la ruta de gbak.exe a tu `%FBDIR%` real de la Fase 0.1.

**Prueba de restauración mensual** (un backup no probado no es un backup):

```bat
"%FBDIR%\bin\gbak.exe" -c -v -user SYSDBA -password LA_REAL C:\grupo_chemie\backups\CHEMIE_2026-07-06.fbk C:\grupo_chemie\backups\_test_restore\CHEMIE_TEST.FDB
```

`-c` crea la base y **falla si el destino existe** — es tu seguro. **Jamás uses `-rep`** (replace) contra la ruta de producción: sobrescribe sin piedad. Tras verificar que la restaurada abre y un COUNT cuadra, borra `CHEMIE_TEST.FDB`.

### nbackup — backup físico (documentado, NO lo uses en v1)

```bat
:: Nivel 0 (copia física completa, base en uso):
"%FBDIR%\bin\nbackup.exe" -B 0 C:\ruta\CHEMIE.FDB C:\grupo_chemie\backups\CHEMIE_L0.nbk -user SYSDBA -password LA_REAL
:: Nivel 1 (incremental sobre el nivel 0):
"%FBDIR%\bin\nbackup.exe" -B 1 C:\ruta\CHEMIE.FDB C:\grupo_chemie\backups\CHEMIE_L1.nbk -user SYSDBA -password LA_REAL
```

Y el modo lock/unlock, que es **la única forma lícita de copiar el archivo .fdb físico**:

```bat
"%FBDIR%\bin\nbackup.exe" -L C:\ruta\CHEMIE.FDB    :: congela: los cambios van a un delta
copy C:\ruta\CHEMIE.FDB X:\destino\                 :: ahora sí puedes copiar el archivo
"%FBDIR%\bin\nbackup.exe" -N C:\ruta\CHEMIE.FDB    :: descongela y fusiona el delta
```

**Cuándo usar cada uno, sin ambigüedad:** para este grupo (bases pequeñas), gbak semanal + prueba de restore mensual cubre el 100 % de la necesidad; nbackup incremental solo aportaría con bases de decenas de GB. El bloque `-L`/`-N` queda documentado por una sola razón: si algún día alguien necesita copiar el archivo físico, ese es el único procedimiento — **copiar un .fdb en caliente sin `-L` es la receta de corrupción número uno**, y si haces `-L`, el `-N` posterior no es opcional.

---

## CIERRE DE LA PARTE A — checklist antes de pasar a la Parte B

1. ☐ Checklist 0.8 completa (rutas, puerto, versión, credenciales, bitness).
2. ☐ Python 3.12 x64 + venv + las 4 dependencias pineadas instaladas.
3. ☐ fbclient x64 operativa (Caso A o B) y `test_conexion.py` con tres OK.
4. ☐ Charset decidido en config.json y test de tildes/ñ pasado.
5. ☐ `descubre.py` ejecutado: tres `esquema_*.csv` generados.
6. ☐ `tablas_objetivo` rellenada con 10–15 nombres reales (VTOSCLIENTES y MOVIMIENTOSDIARIO incluidas).
7. ☐ Usuario LECTOR creado y con GRANTs en las 3 bases (o fallback justificado).
8. ☐ Primer gbak manual de las 3 bases lanzado y con log limpio.

Con los `esquema_*.csv` en mano, la Parte B (extract.py, build_duckdb.py, vistas y alertas) se escribe con nombres de columna reales en la capa de mapeo — cero placeholders.
