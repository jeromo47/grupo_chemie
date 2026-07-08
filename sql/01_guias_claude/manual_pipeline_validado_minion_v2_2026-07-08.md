# MANUAL VALIDADO Y ATERRIZADO — PIPELINE GRUPO CHEMIE

**Estado:** revisado contra entorno real de oficina el 2026-07-08  
**Base técnica:** manual Claude v1 + validación práctica en máquina real  
**Objetivo:** dejar una versión fiable, corta y accionable para validar antes de construir el pipeline completo.

---

## 1. Conclusiones cerradas tras validación real

### 1.1 Lo que Claude acertó

La arquitectura general propuesta por Claude es válida:

- Firebird 2.5 como origen
- extracción externa al ERP
- Python para extracción tipada
- Parquet como capa intermedia
- DuckDB como base analítica
- informe HTML
- sincronización a Drive
- cron/tarea programada más adelante, no el primer día

También acertó en el enfoque prudente:

- primero reconocimiento real del entorno
- no tocar producción a ciegas
- usar solo lectura
- validar con cifras conocidas antes de ampliar el sistema

### 1.2 Lo que hubo que corregir

Claude partía de un supuesto que en este entorno no era literal:

- no hay una `CHEMIE.FDB` visible por empresa en el árbol normal
- la base real de cada empresa está en un archivo **`MASTERSQL.TEC`**

Por tanto, el manual original debe adaptarse así:

- donde decía buscar `.FDB` por empresa, en este entorno hay que usar `MASTERSQL.TEC`
- donde presumía `masterkey`, aquí la credencial válida encontrada es otra

### 1.3 Hallazgos reales ya validados

#### Servidor Firebird

- instalación: `C:\Program Files (x86)\Firebird\Firebird_2_5`
- versión: `WI-V2.5.2.26540 Firebird 2.5`
- servicio activo en Windows
- puerto: `3050`
- sistema operativo: Windows 64 bits

#### Bases reales por empresa

- Chemie: `C:\MasterSQL\GRUPO CHEMIE LA JUAIDA S.L\MASTERSQL.TEC`
- ACI: `C:\MasterSQL\Almeriense Complementos Industriales\MASTERSQL.TEC`
- Ecoclean: `C:\MasterSQL\ECOCLEAN ALMERIA C.B\MASTERSQL.TEC`

También existen backups por empresa:

- `MasterSql.gbk`

#### Credencial válida confirmada

- usuario: `SYSDBA`
- contraseña: `00000000`

#### Forma de conexión válida confirmada

```powershell
isql.exe -user SYSDBA -password 00000000 "localhost:C:\MasterSQL\GRUPO CHEMIE LA JUAIDA S.L\MASTERSQL.TEC"
```

Esto ya quedó probado en vivo.

---

## 2. Pruebas reales ya superadas

### 2.1 Conexión directa a Chemie

La conexión a `MASTERSQL.TEC` funciona por `isql` usando `SYSDBA / 00000000`.

### 2.2 Tablas visibles confirmadas

Se ejecutó `SHOW TABLES;` con éxito y aparecieron, entre muchas otras:

- `CLIENTES`
- `VTOSCLIENTES`
- `MOVIMIENTOSDIARIO`
- `PLANCONTABLE`
- `GENERALFACTUC`
- `LINEASFACTUC`
- `GENERALFACTUP`
- `LINEASFACTUP`
- `VTOSPROVEEDORES`
- `ARTICULOS`
- `FAMILIAS`
- `PROVEEDORES`

### 2.3 Recuentos reales confirmados en Chemie

- `CLIENTES` → `575`
- `VTOSCLIENTES` → `12.195`
- `MOVIMIENTOSDIARIO` → `133.403`

### 2.4 Muestras reales ya vistas

#### CLIENTES

Consulta útil validada:

```sql
SELECT FIRST 10 CODIGO, RAZONSOCIAL, NIFCIF, POBLACION FROM CLIENTES;
```

Conclusión:

- tabla usable
- `CODIGO` es clave operativa razonable
- `RAZONSOCIAL`, `NIFCIF`, `POBLACION` salen bien

#### VTOSCLIENTES

Consulta útil validada:

```sql
SELECT FIRST 10 FACTURA, EFECTO, CODIGOCLIENTE, RAZONSOCIAL, FECHAVTO, IMPORTEVTO, IMPORTECOBRO, ESTADO, IMPORTEPENDIENTE FROM VTOSCLIENTES;
```

Conclusión:

- la tabla sirve para cartera de cobros
- `FACTURA` puede venir `NULL`
- `EFECTO` puede venir relleno cuando `FACTURA` no
- `ESTADO` trae valores legibles como `Cobrado`
- `IMPORTEPENDIENTE` puede venir `NULL` cuando está cobrado, así que luego habrá que normalizar con `COALESCE`

#### MOVIMIENTOSDIARIO

Consulta útil validada:

```sql
SELECT FIRST 10 FECHA, EJERCICIO, ASIENTO, MOVIMIENTO, CUENTA, CONCEPTO, IMPORTE FROM MOVIMIENTOSDIARIO;
```

Conclusión:

- tabla usable para capa contable
- varias líneas por asiento
- `MOVIMIENTO` ordena líneas dentro del asiento
- `CUENTA`, `CONCEPTO` e `IMPORTE` salen limpios

### 2.5 Charset práctico

Aunque no se cerró aún con consulta formal a metadatos, las muestras de texto ya indican que el comportamiento visible es compatible con **WIN1252**, que además aparece repetidamente en la estructura de tablas ya inspeccionada.

---

## 3. Qué cambia esto en el plan

### 3.1 Lo que ya no hace falta discutir

Ya no estamos en fase de “a ver si se puede”.

Ya está demostrado que:

- sí se puede abrir la base real
- sí se puede consultar por Firebird directo
- sí hay tablas clave explotables
- sí hay vía real para construir el pipeline

### 3.2 Lo que no conviene hacer todavía

Todavía no conviene:

- lanzar automatización completa
- montar tareas programadas
- tocar usuarios/grants si no hace falta
- meterse aún con backup/restores de producción
- construir el pipeline completo de Claude de golpe

### 3.3 Lo que sí conviene hacer ahora

Conviene hacer una fase intermedia corta:

1. fijar un **manual validado** con estos hallazgos
2. repetir pruebas mínimas en **ACI** y **Ecoclean**
3. crear un pequeño bloque SQL reutilizable
4. confirmar columnas y tablas objetivo mínimas
5. solo entonces pasar a Python

---

## 4. Paso a paso recomendado a partir de aquí

## Fase A — cerrar validación de las 3 empresas

### Paso A1. Repetir conexión en ACI

```powershell
& "C:\Program Files (x86)\Firebird\Firebird_2_5\bin\isql.exe" -user SYSDBA -password 00000000 "localhost:C:\MasterSQL\Almeriense Complementos Industriales\MASTERSQL.TEC"
```

Dentro:

```sql
SELECT COUNT(*) FROM CLIENTES;
SELECT COUNT(*) FROM VTOSCLIENTES;
SELECT COUNT(*) FROM MOVIMIENTOSDIARIO;
QUIT;
```

### Paso A2. Repetir conexión en Ecoclean

```powershell
& "C:\Program Files (x86)\Firebird\Firebird_2_5\bin\isql.exe" -user SYSDBA -password 00000000 "localhost:C:\MasterSQL\ECOCLEAN ALMERIA C.B\MASTERSQL.TEC"
```

Dentro:

```sql
SELECT COUNT(*) FROM CLIENTES;
SELECT COUNT(*) FROM VTOSCLIENTES;
SELECT COUNT(*) FROM MOVIMIENTOSDIARIO;
QUIT;
```

### Criterio de salida de Fase A

- las 3 empresas abren
- las 3 responden a las 3 tablas clave
- ya queda cerrada la credencial y ruta real del proyecto

---

## Fase B — dejar consultas reutilizables y dejar de ir manualmente

### Paso B1. Crear un fichero SQL mínimo para Chemie

Propuesta: `C:\Users\Jero\Desktop\chemie_test.sql`

```sql
SELECT COUNT(*) AS N_CLIENTES FROM CLIENTES;
SELECT COUNT(*) AS N_VTOSCLIENTES FROM VTOSCLIENTES;
SELECT COUNT(*) AS N_MOVIMIENTOSDIARIO FROM MOVIMIENTOSDIARIO;

SELECT FIRST 10 CODIGO, RAZONSOCIAL, NIFCIF, POBLACION FROM CLIENTES;

SELECT FIRST 10 FACTURA, EFECTO, CODIGOCLIENTE, RAZONSOCIAL, FECHAVTO, IMPORTEVTO, IMPORTECOBRO, ESTADO, IMPORTEPENDIENTE FROM VTOSCLIENTES;

SELECT FIRST 10 FECHA, EJERCICIO, ASIENTO, MOVIMIENTO, CUENTA, CONCEPTO, IMPORTE FROM MOVIMIENTOSDIARIO;

QUIT;
```

### Paso B2. Ejecutarlo

```powershell
& "C:\Program Files (x86)\Firebird\Firebird_2_5\bin\isql.exe" -user SYSDBA -password 00000000 "localhost:C:\MasterSQL\GRUPO CHEMIE LA JUAIDA S.L\MASTERSQL.TEC" -i "C:\Users\Jero\Desktop\chemie_test.sql"
```

### Paso B3. Duplicar para ACI y Ecoclean

Misma idea, cambiando solo la ruta de base.

### Criterio de salida de Fase B

- pruebas repetibles
- menos errores manuales
- misma batería de chequeo en las 3 empresas

---

## Fase C — elegir las tablas mínimas del pipeline v1

No hace falta intentar 15 tablas el primer día.

### Recomendación prudente

#### Bloque mínimo v1

- `CLIENTES`
- `VTOSCLIENTES`
- `MOVIMIENTOSDIARIO`

#### Bloque siguiente v1.1

- `PROVEEDORES`
- `VTOSPROVEEDORES`
- `PLANCONTABLE`

#### Bloque v2 comercial

- `GENERALFACTUC`
- `LINEASFACTUC`
- `ARTICULOS`
- `FAMILIAS`

### Motivo

Con eso se cubre por fases:

1. maestro de clientes
2. cartera de cobros
3. universo contable
4. cartera de pagos
5. ventas y margen después

---

## Fase D — antes de Python, validar negocio útil con SQL simple

Estas consultas sí tienen sentido antes de construir nada grande.

### D1. Cartera pendiente real

```sql
SELECT FIRST 20
  CODIGOCLIENTE,
  RAZONSOCIAL,
  FECHAVTO,
  IMPORTEVTO,
  IMPORTECOBRO,
  IMPORTEPENDIENTE,
  ESTADO
FROM VTOSCLIENTES
WHERE COALESCE(IMPORTEPENDIENTE, 0) > 0
ORDER BY FECHAVTO;
```

### D2. Top cuentas contables por volumen

```sql
SELECT FIRST 20
  CUENTA,
  COUNT(*) AS N,
  SUM(IMPORTE) AS TOTAL
FROM MOVIMIENTOSDIARIO
GROUP BY CUENTA
ORDER BY TOTAL DESC;
```

### D3. Primeras cuentas grupo 70 o 43 para orientación

```sql
SELECT FIRST 20 CUENTA, CONCEPTO, IMPORTE
FROM MOVIMIENTOSDIARIO
WHERE CUENTA STARTING WITH '70' OR CUENTA STARTING WITH '43';
```

### Criterio de salida de Fase D

- ver cartera real
- ver patrón contable real
- empezar a distinguir universo comercial vs universo contable

---

## Fase E — pasar a Python solo cuando lo anterior esté cerrado

Una vez cerradas A, B, C y D:

### entonces sí

- montar `config.json`
- usar `MASTERSQL.TEC` como ruta de base en vez de `.FDB`
- usar `SYSDBA / 00000000`
- empezar con extracción de 3 tablas, no de 15

### Config adaptado al entorno real

Ejemplo conceptual:

```json
{
  "host": "localhost",
  "puerto": 3050,
  "usuario": "SYSDBA",
  "password": "00000000",
  "charset_conexion": "WIN1252",
  "empresas": {
    "CHEMIE": {
      "fdb": "C:\\MasterSQL\\GRUPO CHEMIE LA JUAIDA S.L\\MASTERSQL.TEC"
    },
    "ACI": {
      "fdb": "C:\\MasterSQL\\Almeriense Complementos Industriales\\MASTERSQL.TEC"
    },
    "ECOCLEAN": {
      "fdb": "C:\\MasterSQL\\ECOCLEAN ALMERIA C.B\\MASTERSQL.TEC"
    }
  },
  "tablas_objetivo": [
    "CLIENTES",
    "VTOSCLIENTES",
    "MOVIMIENTOSDIARIO"
  ],
  "tablas_criticas": [
    "VTOSCLIENTES",
    "MOVIMIENTOSDIARIO"
  ]
}
```

---

## 5. Qué partes del manual de Claude deben reescribirse

### Parte A

Cambios obligatorios:

- sustituir búsqueda de `.FDB` por identificación de `MASTERSQL.TEC`
- sustituir credencial provisional por `SYSDBA / 00000000`
- incluir la validación real ya hecha
- simplificar la fase de descubrimiento, porque ya sabemos mucho más que al inicio

### Parte B

Cambios obligatorios:

- `config.json` debe apuntar a `.TEC`
- el primer extractor debe empezar por 3 tablas, no por todo el universo
- el mapeo de `VTOSCLIENTES` debe contemplar `FACTURA` nula y `EFECTO` relleno

### Parte C

No hay que tocar mucho todavía.

Se mantiene en espera hasta que:

- haya extracción real estable
- haya build real en DuckDB
- se haya validado primero manualmente con más seguridad

---

## 6. Recomendación final para validar con Claude

### Texto corto para pedir validación

> Hemos validado en máquina real que las bases de empresa no son `.FDB` visibles sino `MASTERSQL.TEC`, que se abren por Firebird 2.5 con `SYSDBA / 00000000` y ruta `localhost:C:\MasterSQL\...\MASTERSQL.TEC`. Ya hemos confirmado lectura real sobre `CLIENTES`, `VTOSCLIENTES` y `MOVIMIENTOSDIARIO` en Chemie. Revisa si el enfoque correcto ahora es adaptar tu manual para arrancar con esas tres tablas y posponer el pipeline completo hasta confirmar también ACI y Ecoclean. Valida además si ves prudente mantener `WIN1252` como charset inicial y usar `VTOSCLIENTES` + `MOVIMIENTOSDIARIO` como núcleo del v1.

---

## 7. Estado actual resumido

### Cerrado

- entorno Firebird identificado
- ruta real de bases identificada
- credencial válida identificada
- conexión real validada
- muestras reales validadas en Chemie
- tablas clave mínimas confirmadas

### Pendiente inmediato

- repetir counts en ACI
- repetir counts en Ecoclean
- crear fichero SQL reutilizable
- validar cartera pendiente real
- validar primeras agregaciones del diario

### No hacer todavía

- automatización completa
- tareas programadas
- pipeline DuckDB completo
- construcción de KPIs avanzados
- tocar usuarios/grants si no es necesario

---

## 8. Juicio final

La guía de Claude era buena como arquitectura, pero necesitaba aterrizaje real.

Ese aterrizaje ya existe.

### La versión correcta a partir de hoy es esta:

- **sí** Firebird directo
- **sí** pipeline externo
- **sí** Python después
- **sí** DuckDB después
- pero **primero** validación controlada con `MASTERSQL.TEC`, `SYSDBA / 00000000` y tablas mínimas reales.
