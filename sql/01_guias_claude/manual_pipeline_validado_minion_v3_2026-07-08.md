# MANUAL VALIDADO Y CORREGIDO — PIPELINE GRUPO CHEMIE

**Estado:** revisado contra entorno real de oficina y corregido tras revisión crítica externa el 2026-07-08  
**Base técnica:** manual Claude v1 + validación práctica en máquina real + objeciones de seguridad y método ya integradas  
**Objetivo:** dejar una versión fiable, prudente y accionable antes de construir el pipeline completo.

---

## 1. Conclusiones cerradas tras validación real

### 1.1 Lo que queda confirmado

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

#### Conexión real validada

Se ha probado con `isql` que `MASTERSQL.TEC` responde como base Firebird válida.

#### Tablas reales confirmadas por lectura

- `CLIENTES`
- `VTOSCLIENTES`
- `MOVIMIENTOSDIARIO`
- además, `SHOW TABLES;` confirmó la presencia de muchas más, incluidas:
  - `GENERALFACTUC`
  - `LINEASFACTUC`
  - `GENERALFACTUP`
  - `LINEASFACTUP`
  - `PLANCONTABLE`
  - `VTOSPROVEEDORES`
  - `ARTICULOS`
  - `FAMILIAS`
  - `PROVEEDORES`

#### Recuentos reales confirmados en Chemie

- `CLIENTES` → `575`
- `VTOSCLIENTES` → `12.195`
- `MOVIMIENTOSDIARIO` → `133.403`

---

## 2. Correcciones críticas al documento anterior

### 2.1 Seguridad

La credencial real no debe quedar escrita en documentos versionados del repo.

Por tanto, a partir de esta versión:

- **no se vuelve a escribir la contraseña real en Markdown versionado**
- en toda documentación pública o repo: usar `SYSDBA / [REDACTED]`
- la contraseña real debe vivir solo en:
  - ejecución manual puntual
  - `config.json` local fuera de Git
  - o un almacén local no versionado

### 2.2 Deuda de seguridad

Aunque la credencial real funciona, si es débil no debe tocarse ahora sin coordinación con el proveedor o Javier.

Se documenta como deuda para septiembre:

- revisar credencial Firebird real
- revisar si está hardcodeada en MasterSQL o utilidades auxiliares
- endurecerla solo con validación completa del ecosistema

### 2.3 Error metodológico corregido

Las consultas tipo:

```sql
SELECT FIRST 10 ...
```

**no prueban el esquema completo** de la tabla. Solo prueban las columnas elegidas para esa muestra.

Por tanto:

- las muestras manuales sirven para validar acceso y legibilidad
- **no sirven para cerrar el mapping definitivo**
- el cierre real del esquema debe hacerse con metadatos sobre `RDB$RELATION_FIELDS`
- eso es precisamente lo que debe resolver `descubre.py`

### 2.4 Charset no cerrado todavía

Aunque `WIN1252` es una hipótesis razonable por estructura observada, todavía no debe darse por cerrado hasta hacer:

1. consulta de metadatos de charset real
2. prueba real con nombres que contengan tildes o Ñ

Por tanto, en esta versión:

- `WIN1252` queda como **hipótesis de trabajo**, no como hecho final

### 2.5 Diario contable aún no cerrado del todo

La muestra manual de `MOVIMIENTOSDIARIO` enseñó `IMPORTE`, pero no prueba todavía si el modelo operativo final debe leerse como:

- importe único con signo
- o importe único más otra columna adicional no inspeccionada aún
- o un patrón que solo se aclarará con el esquema completo

Por tanto:

- la validación V3 contable de Claude **no debe fijarse aún**
- primero hay que correr `descubre.py`
- y luego validar el signo/magnitud con consultas sobre cuentas 70, 43, etc.

### 2.6 `VTOSCLIENTES` requiere mapping más prudente

Hallazgos ya confirmados en muestra:

- `FACTURA` puede ser `NULL`
- `EFECTO` puede venir relleno cuando `FACTURA` es `NULL`
- `IMPORTEPENDIENTE` ya existe en ERP

Por tanto, el mapping correcto debe:

- no asumir `FACTURA` siempre rellena
- preservar `IMPORTEPENDIENTE` del ERP
- además calcular pendiente derivada para cruce
- marcar discrepancias entre ambas

---

## 3. Qué sí queda validado del enfoque Claude

La arquitectura general sigue siendo correcta:

- Firebird 2.5 como origen
- extracción externa al ERP
- Python para extracción tipada
- Parquet como capa intermedia
- DuckDB como base analítica
- informe HTML
- sincronización a Drive
- automatización solo cuando la base técnica esté cerrada

También sigue siendo correcto el enfoque prudente:

- no tocar producción a lo loco
- usar solo lectura
- validar contra cifras conocidas antes de ampliar el sistema

---

## 4. Nueva secuencia correcta a partir de hoy

La secuencia manual tabla por tabla ya ha cumplido su función.

Ya no compensa seguir haciendo consultas sueltas como vía principal.

### Siguiente acción recomendada

**Pasar ya a la Fase 1 + Fase 2 del manual Claude, adaptadas al entorno real, y correr `test_conexion.py` + `descubre.py`.**

Esto es mejor que seguir con Fases B–D manuales por tres motivos:

1. ya tenemos rutas reales
2. ya tenemos conexión validada
3. ya tenemos suficiente certeza como para automatizar el descubrimiento sin seguir perdiendo tiempo manualmente

---

## 5. Paso a paso actualizado

## Fase A — adaptar el manual Claude al entorno real

### A1. Rutas reales en vez de `.FDB`

En toda configuración local, sustituir el supuesto genérico `.FDB` por:

- `C:\MasterSQL\GRUPO CHEMIE LA JUAIDA S.L\MASTERSQL.TEC`
- `C:\MasterSQL\Almeriense Complementos Industriales\MASTERSQL.TEC`
- `C:\MasterSQL\ECOCLEAN ALMERIA C.B\MASTERSQL.TEC`

### A2. Credencial

En documentación versionada:

- usar `SYSDBA / [REDACTED]`

En configuración local no versionada:

- la credencial real funcional

### A3. Charset

No fijar aún `WIN1252` como definitivo hasta correr validación formal.

---

## Fase B — instalar Python y dependencias

Esto ya sí compensa hacerlo.

### B1. Instalar Python 3.12 x64

Seguir la Parte A original de Claude.

### B2. Crear entorno virtual

Seguir la Parte A original de Claude.

### B3. Instalar dependencias

Mínimo:

```text
fdb==2.0.4
duckdb==1.5.4
pyarrow==24.0.0
jinja2==3.1.6
```

---

## Fase C — configuración local mínima

Crear `config.json` local, no versionado, apuntando a `.TEC`.

Ejemplo conceptual:

```json
{
  "host": "localhost",
  "puerto": 3050,
  "usuario": "SYSDBA",
  "password": "RELLENAR_LOCAL",
  "charset_conexion": "PENDIENTE_VALIDAR",
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

Nota:

- `charset_conexion` queda pendiente
- no debe subirse a Git

---

## Fase D — ejecutar `test_conexion.py`

Objetivo:

- comprobar que Python + fdb abren las 3 bases reales
- no solo Chemie manualmente por `isql`

### Criterio de salida de Fase D

- 3 bases en verde
- confirmación de que la conexión manual se traduce bien a Python

---

## Fase E — ejecutar `descubre.py`

Este es ahora el paso más rentable.

### Objetivo de `descubre.py`

Sacar, de un tirón y sobre las 3 empresas:

- todas las tablas
- todas las columnas
- tipos
- conteos por tabla

### Entregables esperados

- `esquema_CHEMIE.csv`
- `esquema_ACI.csv`
- `esquema_ECOCLEAN.csv`

### Qué resuelve esto

1. cierra esquema completo real
2. evita seguir con muestras parciales manuales
3. valida si ACI y Ecoclean tienen columnas exactamente iguales o no
4. permite cerrar:
   - `stg_ventas_linea`
   - `stg_compras_linea`
   - `stg_cartera_cobros`
   - `stg_cartera_pagos`
5. permite verificar el patrón real de `MOVIMIENTOSDIARIO`

---

## Fase F — validaciones concretas que deben salir de `descubre.py`

### F1. Charset real

Hacer la consulta de metadatos propuesta por Claude y una prueba con tildes/Ñ.

### F2. Columnas reales de ACI y Ecoclean

No asumir que replican Chemie solo por nombre de tabla.

### F3. `VTOSPROVEEDORES`

Verificar que exista con columnas realmente útiles y comprobar si trae `IMPORTEPENDIENTE` o equivalente.

### F4. `MOVIMIENTOSDIARIO`

Cerrar definitivamente:

- si trabaja solo con `IMPORTE`
- si existe otra columna relevante para signo
- cómo mapear la validación contable V3 sin suposiciones falsas

### F5. `VTOSCLIENTES`

Validar el conjunto real de valores de `ESTADO`:

```sql
SELECT ESTADO, COUNT(*) FROM VTOSCLIENTES GROUP BY ESTADO;
```

Esto sigue siendo consulta útil incluso antes o después de `descubre.py`.

---

## 6. Mapping corregido de cartera de cobros

La propuesta de Claude para `stg_cartera_cobros` es razonable y mejora el documento anterior.

### Propuesta de trabajo

```sql
CREATE OR REPLACE VIEW stg_cartera_cobros AS
SELECT 'CHEMIE' AS empresa,
 CODIGOCLIENTE AS cliente_id,
 RAZONSOCIAL AS cliente,
 COALESCE(FACTURA, 'EFECTO-' || CAST(EFECTO AS VARCHAR)) AS factura,
 EFECTO AS efecto,
 FECHAVTO AS fecha_vto,
 IMPORTEVTO AS importe_vto,
 COALESCE(IMPORTECOBRO, 0) AS cobrado,
 ESTADO AS estado,
 IMPORTEPENDIENTE AS pendiente_erp
FROM raw_chemie_vtosclientes
UNION ALL
SELECT 'ACI', CODIGOCLIENTE, RAZONSOCIAL,
 COALESCE(FACTURA, 'EFECTO-' || CAST(EFECTO AS VARCHAR)), EFECTO, FECHAVTO,
 IMPORTEVTO, COALESCE(IMPORTECOBRO,0), ESTADO, IMPORTEPENDIENTE
FROM raw_aci_vtosclientes
UNION ALL
SELECT 'ECOCLEAN', CODIGOCLIENTE, RAZONSOCIAL,
 COALESCE(FACTURA, 'EFECTO-' || CAST(EFECTO AS VARCHAR)), EFECTO, FECHAVTO,
 IMPORTEVTO, COALESCE(IMPORTECOBRO,0), ESTADO, IMPORTEPENDIENTE
FROM raw_ecoclean_vtosclientes;
```

### Vista canónica mejorada

```sql
CREATE OR REPLACE VIEW v_cartera_cobros AS
SELECT *,
 COALESCE(pendiente_erp, importe_vto - cobrado) AS pendiente,
 ABS(COALESCE(pendiente_erp,0) - (importe_vto - cobrado)) > 0.01 AS flag_pendiente_discrepante,
 datediff('day', fecha_vto, current_date) AS dias_vencido,
 CASE WHEN datediff('day', fecha_vto, current_date) <= 0 THEN '0_no_vencido'
 WHEN datediff('day', fecha_vto, current_date) <= 30 THEN '1_vencido_0_30'
 WHEN datediff('day', fecha_vto, current_date) <= 60 THEN '2_vencido_31_60'
 ELSE '3_vencido_mas_60' END AS tramo
FROM stg_cartera_cobros
WHERE COALESCE(pendiente_erp, importe_vto - cobrado) > 0.005;
```

Esto añade un detector muy útil:

- `flag_pendiente_discrepante`

que conviene incorporar luego al sistema de alertas.

---

## 7. Usuario LECTOR

Corrección importante frente al documento anterior:

- para validación manual con `isql`, seguir provisionalmente con `SYSDBA` es aceptable
- **para Python y pipeline, sí conviene crear `LECTOR` cuanto antes**

Motivo:

- evita dejar `SYSDBA` como credencial de operación habitual del pipeline
- reduce superficie de riesgo desde el primer script

### Recomendación

Crear `LECTOR` inmediatamente después de validar `test_conexion.py` y antes de consolidar el uso de Python para extracción.

---

## 8. Qué no hacer todavía

- no automatizar tareas programadas aún
- no construir alertas finales aún
- no fijar validación contable V3 aún
- no asumir que las columnas de ACI y Ecoclean son idénticas sin `descubre.py`
- no cerrar charset sin validación formal

---

## 9. Siguiente acción concreta recomendada

### Acción siguiente única

**Instalar Python 3.12 x64, crear venv, instalar `fdb`, y correr `test_conexion.py` seguido de `descubre.py`.**

Esa es ahora la acción correcta porque:

- ya tenemos rutas
- ya tenemos acceso
- ya tenemos pruebas manuales suficientes
- y `descubre.py` resuelve en una ejecución lo que manualmente sería lento, parcial y propenso a error

### Qué espero al acabar

- 3 conexiones OK por Python
- 3 `esquema_*.csv`
- base objetiva para cerrar mappings de ventas, compras, cobros y pagos
- base objetiva para corregir la parte contable del manual

---

## 10. Juicio final

La arquitectura Claude sigue siendo válida, pero el orden bueno ya no es seguir a mano con consultas sueltas.  
El punto de madurez actual del proyecto pide pasar a descubrimiento automatizado controlado.

### Versión correcta a partir de hoy

- **sí** Firebird directo
- **sí** `MASTERSQL.TEC`
- **sí** Python
- **sí** `descubre.py` ya
- **sí** crear `LECTOR` antes de consolidar pipeline
- **no todavía** automatización final ni validación contable cerrada
