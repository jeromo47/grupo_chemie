# Informe ALMERIENSE 2025 - despiece del agujero de margen v2 compacto

## 1. Resumen ejecutivo
Este módulo aclara bastante bien el principal punto negro del grupo en 2025.

### Idea central
- El margen bruto estimado total de **ALMERIENSE 2025** sale en **-71.483,96 €**.
- Pero el agujero **no parece venir principalmente del negocio operativo limpio**.
- La mayor parte del problema se concentra en:
  - referencias genéricas
  - costes/stock sospechosos
  - y mezcla con capas intragrupo y patrimoniales/no core

### Hallazgo clave
Al apartar esas capas, queda un **resto limpio aproximado** de:
- **Ventas:** **94.907,18 €**
- **Coste estimado:** **44.490,12 €**
- **Margen estimado:** **50.417,06 €**
- **Margen % estimado:** **53,12 %**

### Conclusión rápida
No es correcto leer el -71,5k como pérdida operativa real cerrada del negocio limpio.

---

## 2. Dónde está el problema

## Referencia genérica
Es la mayor distorsión del módulo.

### Capa prioritaria
- **122 líneas**
- **15.194,90 €** ventas
- **163.111,64 €** coste
- **-147.916,74 €** margen

### Flags con solape
- **156 líneas**
- **46.614,30 €** ventas afectadas
- **-116.497,34 €** margen flaggeado

### Lectura
Aquí el problema parece mucho más técnico que comercial:
- referencias `999999`
- referencias `000000`
- artículos cajón desastre
- costes absurdos frente a ventas pequeñas

---

## Coste/stock sospechoso
- `FLAG_COSTE_SOSPECHOSO`: **45 líneas** -> **-161.091,44 €** margen
- `FLAG_MARGEN_NEGATIVO`: **59 líneas** -> **-162.793,02 €** margen

### Lectura
El veneno está muy concentrado en pocas zonas técnicas del dato, no repartido por todo el negocio limpio.

---

## Intragrupo
- **8.565,80 €** ventas
- **7.134,30 €** margen

## Patrimonial / no core
- aprox. **31.419,40 €** ventas
- aprox. **31.419,40 €** margen

### Lectura
ALMERIENSE mezcla claramente:
- mercado
- patrimonial/no core
- intragrupo

Eso confirma que no puede gobernarse con lectura plana de ventas/margen.

---

## 3. Qué cambia en la interpretación

## Lectura incorrecta
“ALMERIENSE pierde 71 mil euros reales y el negocio está roto.”

## Lectura correcta
“ALMERIENSE 2025 muestra un margen bruto estimado muy negativo, pero el agujero está dominado por contaminación técnica del dato y capas no core/intragrupo; el bloque más limpio sale con margen positivo estimado.”

### Traducción
El problema principal no parece ser solo de negocio.
Parece ser de:
- maestro
- coste
- codificación
- clasificación
- y mezcla de naturaleza económica distinta

---

## 4. Qué haría con esto
### No haría
- no usar el margen bruto 2025 de ALMERIENSE como KPI de decisión duro
- no compararla visualmente igual que Chemie o Ecoclean sin bandera roja

### Sí haría
1. revisar referencias `999999` y `000000`
2. revisar familias contaminadas, especialmente `COMPLEMENTOS VARIOS`
3. separar mercado / patrimonial / intragrupo
4. marcar ALMERIENSE con **fiabilidad baja/media** en el dashboard

---

## 5. Conclusión ejecutiva
Si hubiera que resumir este módulo en una frase:

> **El gran agujero de ALMERIENSE 2025 parece venir mucho más de contaminación técnica del dato y mezcla de capas no core que de una pérdida operativa limpia del negocio aparentemente sano.**

## 6. Siguiente paso natural
El siguiente paso bueno ya no sería más teoría general de ALMERIENSE.
Sería una:
- **pieza operativa de limpieza de ALMERIENSE**

con:
- qué referencias revisar
- qué no usar como KPI
- y qué validar con administración/asesoría.
