# Roadmap de control del proyecto CHEMIE

## Rol de este roadmap
No sustituye el análisis principal.
Sirve para ordenar la memoria documental, el versionado y los siguientes artefactos que deben quedar guardados.

## Fase 1 — Consolidación de control documental
- [x] Crear carpeta de control del proyecto CHEMIE
- [x] Crear README de rol y reglas
- [x] Crear mapa maestro de archivos
- [x] Crear resúmenes de archivos
- [x] Crear registro de incidencias
- [x] Crear preguntas para septiembre
- [x] Crear roadmap de control

## Fase 2 — Reabsorber el descubrimiento Firebird ya hecho
- [ ] Crear un documento limpio con tablas Firebird ya validadas para CHEMIE
- [ ] Separar tablas confirmadas, candidatas y descartadas
- [ ] Registrar muestras útiles confirmadas (`VTOSCLIENTES`, `CLIENTES`, etc.)
- [ ] Dejar trazado qué faltó ejecutar o consolidar

## Fase 3 — Preparar ingesta ordenada de nuevos outputs de ChatGPT
- [ ] Cuando ChatGPT produzca nuevas queries, guardar el SQL bajo ruta clara con versión
- [ ] Cuando produzca exportes, registrarlos en el mapa
- [ ] Cuando produzca conclusiones, resumirlas sin darles rango de hecho si no están validadas
- [ ] Mantener separación explícita entre hecho, hipótesis y pendiente

## Fase 4 — Preparación para almacenamiento/indexación en SSD
- [ ] Definir naming estable para nuevos artefactos
- [ ] Separar fuente / derivado / control / SQL
- [ ] Preparar lote de documentos que sí merece ingesta posterior en BD local

## Regla de paso de fase
No cerrar una fase por sensación.
Cerrar solo cuando exista:
- archivo guardado
- ruta conocida
- resumen mínimo
- y estatus claro (fuente / derivado / control / SQL)


## Fase 2bis — Integración de la entrega estructurada 2026-05-27
- [x] Descomprimir e inventariar `CHEMIE_AGENT_INPUT`
- [x] Confirmar presencia efectiva de `05_incidencias_grupo.txt`, `06_productos_costes_y_anomalias_grupo.txt` y `00_schema_tablas_clave_grupo.txt`
- [x] Confirmar que la entrega ya incluye PSV estructurados 07A-10I y una base local DuckDB
- [ ] Registrar, cuando convenga, qué artefactos de la entrega pasan a ser referencia activa en el sistema principal
- [ ] Decidir si `chemie_grupo.duckdb` se replica o se rehace dentro de la arquitectura local definitiva del SSD
