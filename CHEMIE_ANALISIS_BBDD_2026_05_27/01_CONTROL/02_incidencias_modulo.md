# Incidencias del módulo CHEMIE_ANALISIS_BBDD_2026_05_27

## INC-001 — Acceso local a DuckDB habilitado, incidencia técnica cerrada
- **Tipo**: técnica
- **Dato confirmado**: la base `chemie_grupo.duckdb` existe en `00_INPUT/CHEMIE_AGENT_INPUT/11_BASE_LOCAL/` y ya puede abrirse en este entorno.
- **Resolución**: se ha habilitado soporte local para DuckDB y se ha extraído el schema inicial real.
- **Estado**: cerrada.

## INC-002 — Los TXT fuente quedan como respaldo y contraste, no como fuente principal sustitutiva
- **Tipo**: metodológica
- **Dato confirmado**: existe un paquete amplio bajo `01_TXT_FUENTE` y un índice técnico de archivos válidos.
- **Incidencia**: no deben usarse para sustituir automáticamente la fuente principal, según regla del módulo.
- **Estado**: abierta controlada.
