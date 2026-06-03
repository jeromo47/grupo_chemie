# Banco de preguntas para transferencia de tío y padre

## Objetivo
Acumular preguntas concretas y de alto valor para usar en conversaciones con:
- tío
- padre

Este archivo no busca conversación genérica.
Busca capturar preguntas accionables nacidas de:
- análisis de DuckDB
- dudas estratégicas de incorporación
- dependencias operativas
- alertas económicas o comerciales

---

## Regla de uso
Cada nuevo análisis relevante debe producir, si procede:
1. un hallazgo documentado
2. una o más preguntas concretas para este banco

---

## 1. Bloque oficina / administración / contabilidad práctica
### Tío
- ¿Cuál es el orden real de prioridades cuando no se puede pagar todo a la vez?
- ¿Qué proveedores no se pueden tensar nunca y por qué?
- ¿Qué parte del cierre mensual revisas tú sí o sí porque no te fías de que salga sola?
- ¿Qué errores del contable son recurrentes y cómo los detectas rápido?
- ¿Qué informes del ERP miras de verdad cada semana o cada mes?
- ¿Qué cuentas o movimientos te sirven como alarma temprana de que algo va mal?
- ¿Qué tareas haces tú personalmente porque nadie más las resuelve bien hoy?

### Padre
- ¿Qué decisiones económicas importantes prefieres revisar personalmente antes de ejecutarlas?
- ¿Dónde crees que más se puede equivocar la oficina sin que se note a tiempo?

---

## 2. Bloque comercial / clientes
### Padre
- ¿Qué clientes sostienen de verdad el negocio, aunque en papel parezca que hay muchos?
- ¿Qué clientes pesan no solo por volumen, sino por prestigio, estabilidad o arrastre comercial?
- ¿Qué clientes son delicados por trato personal y no por precio?
- ¿Qué promesas comerciales no deben hacerse nunca aunque el cliente presione?
- ¿Qué cliente parece bueno en facturación pero en realidad complica mucho margen, cobro o servicio?

### Tío
- ¿Qué clientes generan más incidencias administrativas, cobros raros o desorden?
- ¿Qué clientes parecen importantes pero en realidad no aportan tanto margen o calidad?

---

## 3. Bloque compras / proveedores
### Tío
- ¿Qué proveedores son realmente estratégicos y por qué?
- ¿Dónde hay dependencia personal o histórica más que dependencia objetiva?
- ¿Qué proveedor tiene más capacidad de apretar precio, plazo o suministro?
- ¿Qué familias de producto te preocupan más por suministro o por regulación?

---

## 4. Bloque normativa / técnica
### Tío
- ¿Qué parte de la normativa química aplicada a cooperativas agrícolas es más crítica dominar al principio?
- ¿Qué errores regulatorios son los más peligrosos aunque comercialmente parezcan pequeños?
- ¿Qué productos, usos o líneas requieren más criterio técnico y menos improvisación?
- ¿Qué temas técnicos debería aprender Jero primero para no depender ciegamente de terceros?

---

## 5. Bloque personas / dependencias
### Tío
- Si tú faltaras dos semanas, ¿qué tres cosas se bloquearían antes?
- Si faltara el contable, ¿qué tareas podrías reasignar fácil y cuáles no?
- ¿Qué dependencia del equipo te parece real y cuál exagerada por costumbre?

### Padre
- ¿Quién te preocupa más como punto de fallo humano en la empresa y por qué?
- ¿Qué puesto crees que parece sustituible pero en realidad no lo es tanto?
- ¿Dónde ves más riesgo de conflicto, desgaste o salida en los próximos años?

---

## 6. Preguntas alimentadas ya desde DuckDB
### Concentración de clientes / dependencia por comercial
#### Para tío
- ¿Qué significa exactamente el comercial `0` en el maestro? ¿es sin asignar, cartera histórica, administración o mezcla?
- ¿Quiénes son en la práctica los códigos comerciales `3`, `32`, `36` y `38`?
- ¿Qué clientes grandes de ALMERIENSE y CHEMIE están realmente sostenidos por una sola persona?
- ¿Qué parte del maestro comercial está limpia y qué parte arrastra asignaciones históricas o poco fiables?

#### Para padre
- ¿Qué clientes del top 10 de ALMERIENSE son estratégicos de verdad y cuáles son más sustituibles?
- ¿El cliente que pesa tanto bajo el código `3` es una relación crítica personal, una excepción o un cliente ya consolidado por la empresa más que por una persona?
- ¿Qué clientes importantes generan mucho volumen pero poca tranquilidad comercial o poco margen?
- ¿EJIDOMAR es hoy el cliente comercial más sensible de ALMERIENSE?
- ¿Qué relación real pesa más: EJIDOMAR, AGROPONIENTE NATURAL PRODUCE o la línea especial de BOOKING?

#### Para tío
- ¿Por qué EJIDOMAR sale con margen tan negativo en 2025? ¿dato sucio, coste mal arrastrado o problema real?
- ¿Qué parte del peso de ALMERIENSE depende de mercado puro y qué parte de ingresos especiales o intragrupo?

## 7. Preguntas alimentadas ya desde DuckDB - margen por familia/producto
### Para tío
- ¿Qué familias de CHEMIE consideras de verdad el núcleo comercial y de margen del negocio?
- ¿Qué parte del margen de limpieza, celulosa y especiales industria alimentaria es estable y qué parte depende de pocos clientes?
- En ALMERIENSE, ¿cómo separarías margen comercial ordinario de alquileres, booking y líneas especiales?
- ¿Qué familias o referencias sabes ya que salen sucias por maestro, coste medio o referencias genéricas?

### Para padre
- ¿Qué familias consideras más estratégicas comercialmente en CHEMIE?
- ¿Dónde ves más futuro real: limpieza, celulosa, especiales industria alimentaria u otras?
- ¿Qué línea de ALMERIENSE consideras negocio real y cuál simple complemento o arrastre patrimonial?

## 8. Preguntas alimentadas ya desde DuckDB - proveedores y abastecimiento
### Para tío
- ¿Qué proveedores de CHEMIE consideras verdaderamente estratégicos y difíciles de sustituir?
- ¿Dónde hay dependencia por calidad, por precio, por regulación o por relación histórica?
- ¿Hay proveedores grandes de CHEMIE que realmente serían sustituibles sin trauma?
- En ECOCLEAN, ¿qué proveedores son estructurales y cuáles más oportunistas?
- En ALMERIENSE, ¿las compras están bastante diversificadas o hay dependencia oculta que aquí no se ve?

### Para padre
- ¿Qué proveedor te preocupa más si mañana falla?
- ¿Dónde ves más dependencia personal o histórica en compras?
- ¿Qué proveedor consideras parte del corazón del negocio de CHEMIE?

## 9. Preguntas alimentadas ya desde DuckDB - alerta ACI / ALMERIENSE
### Para tío
- ¿Qué originó el monstruo de stock en referencias como `999999`, `000000` y similares?
- ¿Qué parte del margen negativo de ALMERIENSE 2025 atribuyes a stock/coste contaminado y qué parte a negocio real?
- ¿Qué productos o familias sabes ya que no deben usarse para leer rentabilidad sin depuración previa?
- ¿Cómo separarías de forma práctica la actividad comercial ordinaria de ALMERIENSE frente a Booking/Macenas y alquiler nave a Chemie?

### Para padre
- ¿Qué parte de ALMERIENSE ves realmente como negocio vivo comercial y qué parte como estructura de apoyo o patrimonial?
- ¿Qué cliente o línea de ALMERIENSE te preocupa más como negocio real, dejando fuera alquileres y flujos internos?

## 10. Preguntas alimentadas ya desde DuckDB - dependencias críticas concretas
### Para tío
- ¿Qué cliente perdería más daño real mañana: EJIDOMAR, MABE, INDASOL u otro?
- ¿Qué proveedor de CHEMIE sería más difícil sustituir en la práctica?
- ¿Qué dependencia te preocupa más hoy, la comercial o la de abastecimiento?
- ¿Qué códigos comerciales del maestro corresponden a personas reales y cuáles a cajones históricos?

### Para padre
- ¿Qué relación comercial consideras más delicada personalmente?
- Si mañana tuvieras que proteger solo 5 relaciones del negocio, cuáles serían?
- ¿Qué dependencia te preocupa más por persona y no por cifra?

## 11. Preguntas pendientes de seguir alimentando desde DuckDB
Este bloque debe seguir creciendo con hallazgos concretos futuros o con nuevas necesidades de septiembre.
