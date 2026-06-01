# Estado inicial del módulo CHEMIE_ANALISIS_BBDD_2026_05_27

## Rol
Agente técnico-documental.

## Fuente principal declarada
- `00_INPUT/CHEMIE_AGENT_INPUT/11_BASE_LOCAL/chemie_grupo.duckdb`

## Documentos de control declarados
- `00_INPUT/CHEMIE_AGENT_INPUT/00_CONTROL/10J_INDICE_TECNICO_EXTRACCIONES.md`
- `00_INPUT/CHEMIE_AGENT_INPUT/00_CONTROL/10J_ARCHIVOS_VALIDOS_ENTREGA_AGENTE.txt`

## Reglas activas en este módulo
1. No inventar datos, tablas, columnas ni conclusiones.
2. No modificar archivos originales ni memoria anterior.
3. Usar DuckDB como fuente principal.
4. Usar `01_TXT_FUENTE` solo como respaldo.
5. Si una consulta falla, revisar el schema real.
6. Diferenciar dato confirmado, hipótesis e incidencia pendiente.

## Estado técnico actual
### Dato confirmado
- La carpeta independiente `CHEMIE_ANALISIS_BBDD_2026_05_27` existe y contiene el ZIP descomprimido en `00_INPUT`.
- La base `chemie_grupo.duckdb` está presente en la ruta esperada.
- Los documentos de control `10J_INDICE_TECNICO_EXTRACCIONES.md` y `10J_ARCHIVOS_VALIDOS_ENTREGA_AGENTE.txt` están presentes y han sido leídos.
- El acceso técnico a DuckDB ya ha quedado habilitado en este entorno.
- Se ha inspeccionado el schema real inicial de la base y se ha guardado en `01_CONTROL/00_schema_duckdb_inicial.md`.

### Incidencia pendiente
- Ninguna bloqueante para lectura de la fuente principal en este momento.

### Consecuencia
- El módulo queda operativo para consultas directas sobre la fuente principal DuckDB.

## Uso del respaldo
Los archivos bajo `00_INPUT/CHEMIE_AGENT_INPUT/01_TXT_FUENTE` deben tratarse como respaldo documental y contraste, no como sustitución automática de la base principal mientras DuckDB siga disponible.
