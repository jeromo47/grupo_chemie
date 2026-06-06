# Pieza operativa de limpieza de ALMERIENSE v1

## Objetivo
Traducir el hallazgo del módulo `23B` a un plan práctico de limpieza y control para que ALMERIENSE deje de gobernarse con una mezcla tóxica de:
- referencias genéricas
- costes sospechosos
- stock contaminado
- intragrupo
- patrimonial / no core

La idea no es cerrar aquí la contabilidad oficial.
La idea es dejar claro:
- qué revisar primero
- qué no usar todavía como KPI
- y qué habría que validar con administración/asesoría o con la oficina real

---

## 1. Punto de partida
El módulo `23B` deja una conclusión bastante fuerte:

> **el gran agujero bruto de margen 2025 de ALMERIENSE parece venir mucho más de contaminación técnica del dato y mezcla de capas no core que de una pérdida operativa limpia del negocio aparentemente sano.**

Eso significa que la prioridad no es “interpretar mejor el -71k”.
La prioridad es:

> **limpiar qué parte del dato no debería mandar en el KPI.**

---

## 2. Qué NO usar todavía como KPI de gestión
Hasta que no se limpie esta zona, yo no usaría de forma dura en ALMERIENSE:

### No usar como KPI principal
- margen bruto total 2025 de ALMERIENSE
- margen % total 2025 de ALMERIENSE
- lectura de rentabilidad por referencia si aparece `999999`, `000000` o descripciones basura
- lectura de stock/coste de familias claramente contaminadas

### Sí usar con mucha prudencia
- ventas por empresa
- clientes reales
- intragrupo visible
- patrimonial/no core separado

---

## 3. Prioridad 1 - referencias genéricas
Esta es la gran bolsa de veneno.

### Qué revisar
- referencia `999999`
- referencia `000000`
- referencias vacías
- líneas con descripción textual sin estructura real de artículo
- líneas cajón desastre de material heterogéneo

### Por qué
Porque el módulo demuestra que esta zona concentra una parte enorme del agujero de margen estimado.

### Qué haría en práctica
#### A. Sacar listado maestro de referencias tóxicas
Con al menos:
- referencia
- descripción
- familia
- ventas 2025
- coste estimado 2025
- margen estimado 2025
- número de líneas
- número de clientes

#### B. Clasificarlas una a una en bloques
- referencia genérica a eliminar
- referencia genérica a partir en varias reales
- referencia correcta pero mal costada
- referencia de abono/devolución/caso especial
- referencia patrimonial/no core

#### C. Pregunta práctica para oficina/administración
- ¿por qué se usa esta referencia?
- ¿qué productos reales se meten aquí dentro?
- ¿se usa por comodidad, por falta de maestro o por incidencia histórica?

---

## 4. Prioridad 2 - costes sospechosos
### Qué revisar
- líneas con coste desproporcionado frente a venta
- líneas con margen extremadamente negativo
- líneas donde `CANTIDAD * PRECIOMEDIOCOMPRA` claramente destruye la lógica económica visible

### Por qué
Porque muchas líneas negativas no parecen negocio malo sino coste mal arrastrado o estructura maestra rota.

### Qué haría en práctica
#### A. Sacar top 20-30 líneas más absurdas
Con:
- referencia
- descripción
- cliente
- venta
- coste
- margen
- familia

#### B. Separarlas en tres grupos
- error claro de dato
- caso dudoso
- posible pérdida real

#### C. Regla buena
No intentar arreglar todo de golpe.
Empezar por lo que más pesa en importe y distorsión.

---

## 5. Prioridad 3 - patrimonial / no core
### Qué revisar
- alquiler vacacional Casa Macenas
- alquiler de nave a Grupo Chemie
- cualquier otra línea no comercial pura

### Por qué
Porque esta capa no debe mezclarse con margen de mercado si lo que quieres es entender negocio operativo.

### Qué haría en práctica
- marcar esas líneas/clientes como **no core** de forma consistente
- revisar si en el futuro deben salir en bloque aparte del dashboard
- y evitar que contaminen comparativas con Chemie o con una comercial pura

---

## 6. Prioridad 4 - intragrupo
### Qué revisar
- ventas a Chemie
- ventas a vinculadas/personas relacionadas
- alquileres o cesiones internas

### Por qué
Porque parte de esta capa puede ser perfectamente real, pero no debe leerse igual que mercado puro.

### Qué haría en práctica
- crear etiqueta simple de **intragrupo** visible
- revisarla separada en cualquier cierre de ALMERIENSE
- no mezclarla con cartera comercial ordinaria

---

## 7. Qué familias me dan más sospecha
Con lo visible hoy, pondría especial atención en:
- **COMPLEMENTOS VARIOS**
- bloques donde aparecen muchas `999999`
- parte de **MAQUINARIA/HERRAMIENTAS/ACCESORIOS** con `000000`
- y cualquier familia donde el margen dependa de referencias cajón desastre

### Traducción
No es que la familia esté mal por definición.
Es que hoy puede estar soportando mezcla de artículos que hacen inútil el KPI tal como sale.

---

## 8. Qué preguntaría a administración / asesoría / oficina
### Bloque 1 - referencias
- ¿quién creó o usa `999999` y `000000`?
- ¿qué uso real tienen hoy?
- ¿se pueden cerrar o partir?

### Bloque 2 - coste
- ¿de dónde sale exactamente el `PRECIOMEDIOCOMPRA` en estas líneas?
- ¿hay arrastres raros de stock o abonos?
- ¿hay referencias que heredan coste viejo imposible?

### Bloque 3 - estructura
- ¿qué parte de ALMERIENSE debería leerse aparte como patrimonial?
- ¿qué parte debería tratarse como intragrupo puro?
- ¿qué parte es mercado sano que sí conviene seguir como KPI?

---

## 9. Cómo cambiaría el dashboard mientras tanto
Hasta limpiar ALMERIENSE, yo haría esto:

### Sí mostrar
- ventas
- compras
- clientes
- intragrupo visible
- patrimonial visible
- nota de fiabilidad

### Mostrar con bandera roja o amarilla
- margen total ALMERIENSE
- margen % ALMERIENSE

### No usar como lectura simple
- compararla visualmente igual que Chemie o Ecoclean

---

## 10. Resultado buscado
No hace falta que ALMERIENSE quede perfecta mañana.
El objetivo razonable sería este:

> **pasar de una sociedad analíticamente tóxica a una sociedad dividida en bloques entendibles, donde al menos el negocio limpio no quede enterrado por referencias basura y coste absurdo.**

---

## Conclusión ejecutiva
La prioridad buena ahora no es seguir diciendo que ALMERIENSE está contaminada.
Eso ya lo sabemos.

La prioridad buena es esta:

> **limpiar primero referencias genéricas, costes absurdos, patrimonial/no core e intragrupo para que el KPI de ALMERIENSE deje de mentir.**

Ese es el siguiente paso con más retorno real.
