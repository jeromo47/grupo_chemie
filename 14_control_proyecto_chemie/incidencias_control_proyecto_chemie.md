# Incidencias de control del proyecto CHEMIE

## Regla
Registrar aquí incidencias de:
- trazabilidad
- versionado
- mezcla de archivos
- ambigüedad de rutas
- errores de extracción
- validaciones no cerradas

---

## Incidencias abiertas

### INC-001 — Descubrimiento Firebird interrumpido / no consolidado documentalmente
- **Hecho**: hubo una sesión de descubrimiento paso a paso sobre Chemie con tablas como `VTOSCLIENTES`, `CLIENTES`, `MOVIMIENTOSDIARIO`, `PLANCONTABLE`, etc.
- **Problema**: la conversación operativa se cruzó varias veces con pegados erróneos del bloc de notas, y no quedó consolidado en un artefacto limpio único.
- **Impacto**: riesgo de perder parte del trabajo técnico ya validado si no se recompone en un documento ordenado.
- **Estado**: abierta.
- **Acción sugerida**: cuando se retome, crear un resumen técnico limpio del descubrimiento Firebird Chemie con tablas validadas, tablas descartadas y muestras realmente útiles.

### INC-002 — Archivos fuente mencionados pero no confirmados en ruta efectiva
- **Hecho**: se han mencionado `05_incidencias_grupo.txt`, `06_productos_costes_y_anomalias_grupo.txt` y `00_schema_tablas_clave_grupo.txt` como principales.
- **Problema**: su ubicación efectiva no ha quedado validada aquí.
- **Impacto**: el mapa documental queda incompleto.
- **Estado**: abierta.
- **Acción sugerida**: confirmar rutas exactas y registrar en el mapa maestro.

### INC-003 — Riesgo de mezcla entre archivos provisionales y definitivos
- **Hecho**: existen fuentes, SQL, exportes y derivados analíticos en varias capas.
- **Problema**: si no se etiqueta bien qué es fuente, qué es derivado y qué es control, se puede mezclar una pasada provisional con una conclusión consolidada.
- **Impacto**: pérdida de trazabilidad.
- **Estado**: abierta estructuralmente.
- **Acción sugerida**: mantener esta carpeta de control como referencia y etiquetar cada nuevo archivo.


### INC-004 — La entrega 2026-05-27 introduce una capa derivada más avanzada que debe etiquetarse con cuidado
- **Hecho**: el paquete `CHEMIE_AGENT_INPUT` trae no solo fuentes, sino también resúmenes, índices técnicos, roadmap y base local DuckDB.
- **Problema**: si no se distingue bien, puede mezclarse una fuente primaria con una interpretación técnica o estratégica derivada.
- **Impacto**: riesgo de dar rango de hecho a documentos que en realidad son guías, resúmenes o conclusiones operativas.
- **Estado**: abierta estructuralmente.
- **Acción sugerida**: mantener la separación fuente / derivado / control / base local y citar siempre el tipo de artefacto.

### INC-005 — La entrega incluye `__MACOSX` y residuos de empaquetado
- **Hecho**: el ZIP trae estructura `__MACOSX` y ficheros `._*`.
- **Problema**: son basura técnica que puede contaminar inventarios automáticos.
- **Impacto**: ruido documental.
- **Estado**: abierta menor.
- **Acción sugerida**: ignorar explícitamente esa rama en cualquier ingesta posterior.
