# Informe ALMERIENSE 2025 - despiece del agujero de margen v1

## Alcance y criterio
Este módulo analiza **solo ALMERIENSE 2025**.

Fuente principal usada:
- CSV limpios del paquete `23B`

Fuente secundaria de contexto/advertencias:
- `01_VALIDACION/23B_VALIDACION_ALMERIENSE_2025_DESPIECE_MARGEN.md`

Criterio central de esta pieza:
- no interpretar el margen bruto estimado de ALMERIENSE 2025 como pérdida real cerrada sin separar antes capas y contaminación del dato

---

## 1. Resumen ejecutivo
Este módulo cambia de forma importante la lectura de ALMERIENSE 2025.

### La idea central
> **El agujero bruto de margen 2025 de ALMERIENSE no parece venir principalmente del negocio operativo aparentemente limpio, sino de una mezcla de ruido técnico fuerte y capas no core/intragrupo.**

### Foto bruta del problema
- **Ventas 2025:** **146.266,63 €**
- **Coste estimado:** **217.750,59 €**
- **Margen estimado:** **-71.483,96 €**
- **Margen % estimado:** **-48,87 %**

### Pero al separar capas prioritarias
queda un **resto limpio aproximado** de:
- **Ventas:** **94.907,18 €**
- **Coste estimado:** **44.490,12 €**
- **Margen estimado:** **50.417,06 €**
- **Margen % estimado:** **53,12 %**

### Conclusión rápida
Esto no demuestra que ALMERIENSE sea un negocio magnífico.
Pero sí demuestra algo muy importante:

> **no es correcto leer el -71,5k como pérdida operativa real del negocio limpio sin depuración previa.**

---

## 2. Qué se ha separado
La extracción usa una clasificación prioritaria por línea:

1. `INTRAGRUPO`
2. `PATRIMONIAL_NO_CORE`
3. `REFERENCIA_GENERICA`
4. `COSTE_CERO`
5. `COSTE_STOCK_SOSPECHOSO`
6. `MARGEN_NEGATIVO`
7. `RESTO_LIMPIO_APROX`

Esto no pretende ser contabilidad oficial.
Pretende separar el problema en bloques útiles para gestión.

---

## 3. Resultado por capas prioritarias

| Capa | Líneas | Ventas s/IVA | Coste estimado | Margen estimado | Lectura |
|---|---:|---:|---:|---:|---|
| REFERENCIA_GENERICA | 122 | 15.194,90 € | 163.111,64 € | -147.916,74 € | principal foco de distorsión |
| COSTE_STOCK_SOSPECHOSO | 4 | 736,05 € | 7.808,32 € | -7.072,27 € | distorsión técnica fuerte |
| MARGEN_NEGATIVO | 4 | 627,90 € | 909,01 € | -281,11 € | bloque residual pequeño |
| COSTE_CERO | 8 | 2.015,40 € | 0,00 € | 2.015,40 € | también contamina lectura |
| INTRAGRUPO | 17 | 8.565,80 € | 1.431,50 € | 7.134,30 € | no debe mezclarse con mercado puro |
| PATRIMONIAL_NO_CORE | 26 | 24.219,40 € | 0,00 € | 24.219,40 € | capa no comercial pura |
| RESTO_LIMPIO_APROX | 294 | 94.907,18 € | 44.490,12 € | 50.417,06 € | bloque más interpretable |

### Lectura
El gran hallazgo no está en intragrupo ni en patrimonial por sí solos.
Está en que la **distorsión masiva** viene de:
- referencias genéricas
- costes sospechosos
- y solapes entre margen negativo y codificación mala

---

## 4. Dónde está de verdad la contaminación

## 4.1 Referencias genéricas
Es la capa más destructiva.

### Magnitud
- **156 líneas marcadas** en flags
- **46.614,30 €** ventas afectadas en solape
- **-116.497,34 €** margen estimado en líneas flaggeadas

### Ejemplos visibles
- múltiples líneas `999999`
- varias `000000`
- descripciones cajón desastre
- artículos con coste absolutamente desproporcionado respecto a la venta

### Lectura
Aquí no parece haber “mal negocio normal”.
Aquí parece haber sobre todo:
- mala codificación
- coste mal arrastrado
- artículos cajón desastre
- y mezcla de productos distintos bajo referencias inútiles

---

## 4.2 Coste sospechoso / stock sospechoso
### Magnitud
- `FLAG_COSTE_SOSPECHOSO`:
  - **45 líneas**
  - margen agregado **-161.091,44 €**
- `FLAG_MARGEN_NEGATIVO`:
  - **59 líneas**
  - margen agregado **-162.793,02 €**

### Lectura
El dato más importante aquí no es solo el importe.
Es el **solape** entre:
- referencia genérica
- coste sospechoso
- margen negativo

Eso indica que el agujero no está repartido sanamente por el negocio.
Está muy concentrado en una zona técnica claramente tóxica del maestro/coste.

---

## 4.3 Patrimonial / no core
### Magnitud
- **Ventas:** aprox. **31.419,40 €** en flags
- **Margen:** aprox. **31.419,40 €**

### Lectura
Aquí pesa sobre todo:
- alquiler vacacional Casa Macenas
- alquiler nave a Grupo Chemie

Esto refuerza otra vez la idea ya conocida:
- ALMERIENSE no es solo comercial
- mezcla claramente ingresos no core/patrimoniales

---

## 4.4 Intragrupo
### Magnitud
- **Ventas:** **8.565,80 €**
- **Margen:** **7.134,30 €**

### Lectura
La capa intragrupo existe y no debe mezclarse con lectura de mercado puro.
Parte de este bloque puede rozar también lo patrimonial, pero la clasificación prioritaria la deja aquí primero.

---

## 5. Qué cambia en la interpretación de ALMERIENSE

## Lectura mala
“ALMERIENSE pierde 71 mil euros reales en 2025 y el negocio está roto.”

## Lectura mejor
“ALMERIENSE 2025 muestra un margen bruto estimado fuertemente negativo, pero el agujero parece estar dominado por referencias genéricas, costes/stock sospechosos y mezcla de capas no core/intragrupo; el resto más limpio aproximado sale con margen positivo.”

## Implicación fuerte
Esto no absuelve a ALMERIENSE.
Pero sí cambia mucho el tipo de problema:

> **más que un negocio claramente hundido, parece una sociedad mal gobernable analíticamente mientras no se limpie el dato.**

Y eso tiene consecuencias muy distintas de gestión.

---

## 6. Qué haría yo con esto en la práctica

## 6.1 Lo que NO haría
- no usaría el margen 2025 bruto de ALMERIENSE como KPI de decisión duro
- no la compararía visualmente en dashboard igual que Chemie o Ecoclean sin bandera roja
- no sacaría conclusiones definitivas sobre rentabilidad real de la sociedad

## 6.2 Lo que sí haría
### A. Crear una lista de limpieza técnica mínima
Prioridad alta sobre:
- referencias `999999`
- referencias `000000`
- familias afectadas como `COMPLEMENTOS VARIOS`
- líneas con coste desproporcionado
- líneas con coste cero

### B. Separar gobernanza de ALMERIENSE por capas
- **mercado operativo**
- **patrimonial/no core**
- **intragrupo**
- **ruido técnico**

### C. Cambiar la forma de leerla en dashboard
ALMERIENSE necesita, como mínimo:
- etiqueta de fiabilidad baja/media
- lectura separada
- y nota visible de no comparabilidad limpia con Chemie

---

## 7. Qué conclusión me parece más sólida
La mejor frase para resumir este módulo sería esta:

> **El gran agujero de ALMERIENSE 2025 parece explicarse mucho más por contaminación técnica del dato y mezcla de capas no core que por una pérdida operativa limpia del negocio aparentemente sano.**

Y la segunda sería:

> **antes de decidir sobre ALMERIENSE como negocio, hay que depurar referencias, coste y clasificación; si no, se gobierna una sombra y no la empresa real.**

---

## 8. Siguiente paso recomendado
Después de este módulo, el siguiente paso con más retorno ya no es otro informe narrativo general.
Sería uno de estos dos:

1. **pieza operativa de limpieza de ALMERIENSE**
   - qué referencias/familias revisar
   - qué no usar como KPI
   - qué validar con administración/asesoría

2. **depuración de pendientes reales**
   - ahora que ya hemos limpiado mucho la lectura de margen

### Mi recomendación real
Iría primero a por la **pieza operativa de limpieza de ALMERIENSE**.
Porque este módulo ya ha identificado bastante bien dónde está el veneno.
