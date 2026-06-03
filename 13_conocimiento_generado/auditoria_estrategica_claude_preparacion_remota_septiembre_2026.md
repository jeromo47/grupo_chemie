# Auditoría estratégica Claude - preparación remota hasta septiembre 2026

## Contexto
Esta nota resume y conserva el giro metodológico propuesto tras la auditoría de Claude, una vez aclarado que Jero **no estará físicamente dentro de la empresa hasta septiembre de 2026**.

La idea central es esta:
> de aquí a septiembre el trabajo no debe simular operación presencial, sino maximizar la **preparación remota útil**.

Por tanto, el proyecto debe trabajar solo con tres fuentes reales:
1. **DuckDB / base analítica** ya cargada
2. **conocimiento parcial y preguntas dirigidas** hacia tío y padre a distancia
3. **documentación histórica ya existente**, que a estas alturas tiene retorno marginal mucho menor

---

## Juicio principal
La rama histórica/documental del proyecto ha dado mucho valor y no debe tirarse.
Pero, a efectos de incorporación de Jero en septiembre, la prioridad cambia.

### Nuevo principio de trabajo
- **DuckDB** = fuente remota principal de alto retorno
- **tío y padre** = fuente perecedera de criterio y know-how que debe prepararse con preguntas buenas
- **histórico documental** = consulta y contexto, no frente principal de desarrollo

---

## Cambio de rol recomendado para Minion
Hasta ahora Minion ha trabajado sobre todo como:
- historiador del grupo
- arqueólogo documental
- sintetizador de pasado y estructura

De aquí a septiembre debe pivotar hacia:
- **analista de datos comerciales y de dependencias reales extraíbles en remoto**
- **preparador de entrada de Jero en septiembre**
- **generador de preguntas dirigidas para transferencia de know-how**

---

## Líneas de trabajo priorizadas hasta septiembre
## Línea A - Explotación sistemática de DuckDB
Debe absorber la mayor parte del esfuerzo remoto.

### Frentes concretos sugeridos
1. **Concentración real de clientes por empresa**
   - top clientes
   - porcentaje del total
   - lectura de dependencia real
2. **Dependencia por comercial**
   - peso de cartera por comercial
   - papel real del comercial veterano
   - punto de partida de Laura
3. **Margen real por familia de producto**
   - de dónde sale el dinero de verdad
   - qué familias sostienen negocio y cuáles no
4. **Aclaración de la alerta ACI**
   - margen negativo fuerte
   - stock contaminado / distorsionado
   - separación entre ruido de dato y problema real
5. **Mapa de proveedores y concentración de abastecimiento**
   - dependencia real por proveedor
   - riesgo de suministro o negociación

### Regla de salida
Cada análisis de BD debe terminar en dos piezas:
- un archivo de conocimiento generado
- una o varias preguntas nuevas para tío/padre

---

## Línea B - Preparación de la transferencia del tío y del padre
No se trata todavía de documentar procesos vistos in situ, sino de construir un **banco de preguntas de alta calidad**.

### Principio útil
La BD y los análisis comerciales deben generar preguntas concretas.
No interesa llegar a septiembre con charlas genéricas, sino con preguntas como:
- por qué este cliente pesa tanto
- qué pasa con este proveedor crítico
- qué explica esta anomalía
- qué criterio se usa en esta excepción

### Entregable principal
- `banco_preguntas_transferencia_tio_padre.md`

---

## Línea C - Diseño del cuadro de mando
No conviene construir aún el dashboard final.
Sí conviene congelar:
- qué KPIs importan
- cómo se definen
- de qué tabla/capa salen
- qué periodicidad tendrán

### Meta
Llegar a septiembre con una definición estable del cuadro de mando, aunque no esté todavía plenamente desplegado.

---

## Implicaciones para la estructura del proyecto
### Lo que debe declararse casi cerrado
- rama histórica de Chemie pre-2024 como frente principal de desarrollo
- nuevas mini-auditorías históricas de bajo retorno
- refinamientos documentales con poco impacto operativo inmediato

### Lo que debe pasar a primer plano
- preparación remota para septiembre
- explotación comercial y de dependencia en DuckDB
- transferencia de know-how
- cuadro de mando mínimo

---

## Propuesta de secuencia remota
### Junio
- concentración de clientes
- dependencia por comercial
- primeras entradas en banco de preguntas

### Julio
- margen por familia/producto
- aclaración de ACI
- primeras conversaciones dirigidas con tío si es posible

### Agosto
- mapa de proveedores y concentración
- definición congelada del cuadro de mando
- banco de preguntas listo para septiembre

### Septiembre
- ya dentro: ejecutar el plan presencial de absorción
- completar procesos in situ
- usar el banco de preguntas como guía de transferencia real

---

## Conclusión operativa
El mayor riesgo ya no es no saber más del pasado de Chemie.
El mayor riesgo es llegar a septiembre sin haber usado la BD para formar criterio comercial y sin haber preparado la extracción del conocimiento que hoy vive en el tío y en el padre.

Por tanto, el proyecto entra desde ahora en una nueva fase:
> **preparación remota para la incorporación de septiembre**

con foco en:
- análisis comercial y de dependencias desde DuckDB
- banco de preguntas de transferencia
- definición del cuadro de mando
