# Tabla deuda padre y sociedades v1

## Objetivo
Guardar una tabla viva y manual de préstamos/deudas/hipotecas relevantes comunicados por Jero, para poder consultarlos después de forma rápida.

## Regla de uso
- Esta tabla no se actualiza automáticamente.
- La referencia válida será siempre la **última fecha de actualización comunicada** para cada préstamo.
- Si hay amortización extraordinaria, cambio de cuota, cancelación o corrección, Jero lo comunicará y se actualizará la tabla.
- Si un dato no consta, se deja explícitamente como **no consta**.

---

## 1. Préstamos a nombre de Jerónimo Molina Cantón

| Titular | Préstamo | Banco | Activo / nota | Capital total | Capital pendiente | Cuota | Fecha última actualización | Fecha fin | Observaciones |
|---|---|---|---|---:|---:|---:|---|---|---|
| Jerónimo Molina Cantón | Hidama Toyo | Cajamar | Vivienda principal en El Toyo, valorada aprox. en 1 M€ | 45.000 € | 32.110 € | 309 € | 04/05/2026 | 21/11/2037 | dato comunicado por Jero |
| Jerónimo Molina Cantón | Final Toyo | Cajamar | Vivienda principal en El Toyo | 19.000 € | 1.032 € | 264 € | 10/04/2026 | no consta | dato comunicado por Jero |
| Jerónimo Molina Cantón | Vivienda Toyo | Cajamar | Vivienda principal en El Toyo | 207.000 € | 134.294 € | 1.164 € | 16/04/2026 | 16/01/2038 | dato comunicado por Jero |
| Jerónimo Molina Cantón | Piso Niñas | Cajamar | Vivienda alquilada a un tercero; el alquiler paga el importe de la hipoteca. Valor estimado comunicado: 225.000 € | 115.000 € | 68.943 € | 688 € | 24/04/2026 | 24/03/2037 | fecha fin teórica corregida por Jero |

### Total parcial Jerónimo Molina Cantón
- **Capital inicial conjunto:** **386.000 €**
- **Capital pendiente conjunto conocido:** **236.379 €**
- **Cuota mensual conjunta conocida:** **2.425 €**

---

## 2. Préstamos a nombre de ACI / Almeriense Complementos Industriales

| Titular | Préstamo | Banco | Activo / nota | Capital total | Capital pendiente | Cuota | Fecha última actualización | Fecha fin | Observaciones |
|---|---|---|---|---:|---:|---:|---|---|---|
| ACI / Almeriense Complementos Industriales | Casa Mojácar | Caixa | Casa con alquiler turístico vacacional; cubre mantenimiento y comunidad y deja algo de excedente. Valor estimado comunicado: 280.000 € | 100.000 € | 42.031 € | 632 € | 01/01/2026 | 20/10/2031 | dato comunicado por Jero |

### Total parcial ACI
- **Capital inicial conjunto:** **100.000 €**
- **Capital pendiente conjunto conocido:** **42.031 €**
- **Cuota mensual conjunta conocida:** **632 €**

---

## 3. Préstamos a nombre de CHEMIE

| Titular | Préstamo | Banco | Activo / nota | Capital total | Capital pendiente | Cuota | Fecha última actualización | Fecha fin | Observaciones |
|---|---|---|---|---:|---:|---:|---|---|---|
| CHEMIE | Macan | no consta | Vehículo de uso privado del padre | 35.000 € | 16.245 € | 669 € | 08/04/2026 | 08/06/2028 | dato comunicado por Jero |
| CHEMIE | BMW XR | no consta | Moto de uso privado del padre | 20.518 € | 19.141 € | 312 € | 24/02/2026 | 24/07/2028 | dato comunicado por Jero |

### Total parcial CHEMIE
- **Capital inicial conjunto:** **55.518 €**
- **Capital pendiente conjunto conocido:** **35.386 €**
- **Cuota mensual conjunta conocida:** **981 €**

---

## 4. Total conjunto actualmente cargado

### Capital inicial total conocido
- **541.518 €**

### Capital pendiente total conocido
- **313.796 €**

### Cuota mensual total conocida
- **4.038 €**

---

## 5. Planes de pensiones / PPA / ahorro relacionado

| Nº | Entidad | Producto | Importe usado | ¿Plan/PPA? | Pre-2007 documentado | Decisión / lectura |
|---:|---|---|---:|---|---:|---|
| 1 | Cajamar | Cajamar Mixto I / Fondocajamar 190152422 | 48.652,44 € aprox. a 01/01/2026 | Sí | 29.456,25 € | Producto clave. Aplicar reducción 40 %. |
| 2 | Allianz | Allianz Pensiones Consolidado PPA 035210135 | 28.911,46 € | Sí, PPA | 17.865,99 € | Producto clave. Confirmar prestación mixta. |
| 3 | Cajamar | Cajamar Previsión PPA 190037963 | 11.715,00 € aprox. a 01/01/2026 | Sí, PPA | No documentado | Pedir certificado pre/post-2007. |
| 4 | Unicaja | Fondocajamar traspasado 190044331 | 23.673,41 € | Sí | No documentado | Muy importante. Puede arrastrar pre-2007 por traspaso. |
| 5 | CaixaBank | Plan Inversión Vinculado OP 14525 | 3.063,00 € | Sí | No documentado | Importe pequeño. Pedir certificado. |
| 6 | Allianz | Plan Pensión 48760061 | 971,24 € | Sí | No documentado | Importe pequeño. Pedir certificado. |
| 7 | Mapfre | Mapfre Crecimiento 4260750000 | 0 € / pendiente | A confirmar | No documentado | No incluir hasta certificado. |
| 8 | Allianz | FondoVida Plus 48991977 | 810,31 € | No tratar como plan/PPA | No aplica | Seguro/ahorro separado. |

### Totales orientativos actualmente cargados
- **Bloque plan/PPA principal identificado (1-6):** **116.986,55 €**
- **Pre-2007 documentado ya visible:** **47.322,24 €**
- **Seguro/ahorro separado no tratar como plan/PPA:** **810,31 €**

---

## 6. Límites actuales
- No constan todavía tipos de interés.
- No constan todavía entidades bancarias para `Macan` y `BMW XR`; sí constan ya `Cajamar` para los cuatro préstamos personales del Toyo/Piso Niñas y `Caixa` para `Casa Mojácar`.
- No consta cuadro de amortización completo.
- No constan comisiones, seguros vinculados o garantías adicionales.
- No consta todavía si existen más préstamos personales, avales o pólizas no mencionadas.
- No consta todavía un inventario completo de valoraciones y rentas asociadas para todos los activos financiados; por ahora solo queda comunicado de forma útil que `Piso Niñas` se autofinancia con alquiler a tercero y que `Casa Mojácar` genera alquiler vacacional que cubre mantenimiento/comunidad y deja algo de remanente.
- En planes de pensiones/PPA todavía faltan certificados finos pre/post-2007 en varios productos y confirmación de la naturaleza exacta de algunos instrumentos.

---

## 7. Criterio de consulta futura
Cuando Jero pida esta información, se devolverá preferentemente:
- préstamo
- titular
- capital pendiente
- cuota
- fecha última actualización
- fecha fin
- y, cuando toque, activo subyacente, renta asociada y lógica económica del préstamo

En el bloque de planes/PPA, se devolverá preferentemente:
- entidad
- producto
- importe usado
- si es plan/PPA real o no
- pre-2007 documentado
- y siguiente acción recomendable

Y se advertirá que la cifra válida es la **última comunicada manualmente** por Jero.
