# Análisis de margen por familia y producto v1

## Objetivo
Entender mejor de dónde sale el dinero real del grupo y qué parte del ruido de margen puede venir de familias o productos concretos.

Fuentes soporte creadas:
- `13J20_margen_por_familia_empresa_anio.csv`
- `13J21_top_familias_ventas_y_margen.csv`
- `13J22_productos_top_margen_y_peor_margen.csv`

---

## 1. CHEMIE - familias que sostienen negocio
## 2025
### Top familias por ventas y margen
1. **08 CELULOSA-LINEA BLANCA**
   - ventas: **194.711,45 €**
   - margen: **81.217,35 €**
2. **09 PROD. Y ACCESORIOS PARA LIMPIEZA**
   - ventas: **126.589,05 €**
   - margen: **50.004,38 €**
3. **03 PROD. ESPECIALES INDUST. ALIMENTARIA**
   - ventas: **101.262,90 €**
   - margen: **63.474,43 €**
4. **01 DESENGRASANTES Y LIMPIADORES GENERALES**
   - ventas: **74.493,40 €**
   - margen: **50.115,10 €**
5. **06 PINTURAS Y DISOLVENTES**
   - ventas: **73.488,30 €**
   - margen: **28.281,08 €**

### Lectura prudente
CHEMIE parece tener un núcleo comercial bastante reconocible. El dinero no sale de una dispersión total, sino sobre todo de:
- celulosa / línea blanca
- limpieza
- especiales de industria alimentaria
- desengrasantes / limpiadores
- pinturas / disolventes

Eso es bastante útil de cara a septiembre, porque ya sugiere qué familias merece entender primero en producto, cliente y margen.

---

## 2024
La estructura es muy parecida:
1. **08 CELULOSA-LINEA BLANCA** -> **228.898,40 €** / **100.733,47 €**
2. **09 PROD. Y ACCESORIOS PARA LIMPIEZA** -> **119.234,15 €** / **44.351,17 €**
3. **03 PROD. ESPECIALES INDUST. ALIMENTARIA** -> **83.766,55 €** / **53.675,09 €**
4. **06 PINTURAS Y DISOLVENTES** -> **64.002,22 €** / **27.754,20 €**
5. **01 DESENGRASANTES Y LIMPIADORES GENERALES** -> **62.856,60 €** / **42.440,55 €**

### Conclusión confirmada
CHEMIE muestra continuidad razonable en sus familias troncales entre 2024 y 2025. Eso refuerza la idea de negocio reconocible y no de mezcla caótica.

---

## 2. ECOCLEAN - familias que sostienen negocio
## 2025
1. **09 PROD. Y ACCESORIOS PARA LIMPIEZA**
   - ventas: **30.901,25 €**
   - margen: **11.605,15 €**
2. **08 CELULOSA-LINEA BLANCA**
   - ventas: **25.638,10 €**
   - margen: **10.187,82 €**
3. **01 DESENGRASANTES Y LIMPIADORES GENERALES**
   - ventas: **16.240,70 €**
   - margen: **10.786,62 €**
4. **03 PROD. ESPECIALES INDUST. ALIMENTARIA**
   - ventas: **8.484,60 €**
   - margen: **5.052,12 €**

### Lectura prudente
ECOCLEAN parece más simple y más limpia en su estructura de familias. Su negocio parece descansar sobre limpieza, celulosa y desengrasantes, en línea con su papel ya leído como estructura ligera y complementaria.

---

## 2024
La foto es muy parecida:
- limpieza
- celulosa
- desengrasantes
- especiales industria alimentaria

### Conclusión confirmada
ECOCLEAN también muestra continuidad razonable. No parece una estructura sin patrón comercial reconocible.

---

## 3. ALMERIENSE - lectura mucho más delicada
Aquí la lectura es más sucia y exige prudencia.

## 2024
### Familias / bloques relevantes
- aparece una familia vacía con:
  - ventas: **31.412,15 €**
  - margen: **30.026,37 €**
  - **73 líneas sin coste**
- **COMPLEMENTOS VARIOS**
  - ventas: **33.513,17 €**
  - margen: **3.135,66 €**
  - **57 líneas con margen negativo**
  - **73 líneas con referencia genérica**
- **MAQUINARIA/HERRAMIENTAS/ACCESORIOS** aparece como peor margen agregado

## 2025
Ya se vio además que **EJIDOMAR** arrastra un margen extremadamente negativo en el corte por cliente.

### Lectura prudente
ALMERIENSE no parece lista todavía para una lectura limpia por familias sin depuración previa. Se mezclan probablemente:
- negocio comercial ordinario
- líneas de alquiler / patrimoniales
- referencias genéricas
- costes sucios o mal arrastrados
- familias vacías

### Juicio práctico
La prioridad aquí no es “sacar conclusiones finas de margen por familia”, sino **separar ruido de dato y capas de negocio**.

---

## 4. Señales fuertes a nivel de producto
### ALMERIENSE
Los peores márgenes aparecen mucho en referencias tipo:
- `999999`
- `000000`
- referencias vacías

Ejemplos:
- **ARANDELA ZINCADA Ø10 DIN 125** -> margen **-5.410,00 €**
- **ARANDELA SEGURIDAD DIN 6799-04** -> **-2.373,75 €**
- múltiples líneas `000000` con márgenes negativos fuertes

### Interpretación prudente
Esto apunta bastante a:
- referencias genéricas
- contaminación de maestro
- imputaciones de coste poco fiables
- y necesidad de no tratar estos peores productos como verdad comercial cerrada sin depurar antes el dato

### Pero también aparece una señal útil
Los top márgenes de ALMERIENSE incluyen ya con claridad:
- **alquiler vacacional casa Macenas**
- **alquiler nave industrial**

Esto, unido a la aclaración directa de Jero sobre Booking/Macenas, refuerza que ALMERIENSE mezcla capas patrimoniales o especiales con lo comercial.

---

## 5. Qué parece sostener el dinero real del grupo
### Confirmado a esta altura
#### CHEMIE
Lo sostienen sobre todo:
- celulosa / línea blanca
- limpieza
- especiales industria alimentaria
- desengrasantes
- pinturas / disolventes

#### ECOCLEAN
Lo sostienen sobre todo:
- limpieza
- celulosa
- desengrasantes
- especiales industria alimentaria

#### ALMERIENSE
No puede leerse todavía igual de limpio. Parece mezclar:
- comercial industrial
- referencias genéricas / coste sucio
- arrendamientos
- intragrupo

---

## 6. Preguntas que genera
### Para tío
- ¿Qué familias de CHEMIE consideras de verdad el núcleo comercial y de margen del negocio?
- ¿Qué parte del margen de limpieza/celulosa/especiales es estable y qué parte depende de pocos clientes?
- En ALMERIENSE, ¿cómo separarías negocio comercial, alquileres y líneas especiales para leer bien el margen?
- ¿Qué familias o referencias sabes ya que salen sucias por maestro o por coste medio?

### Para padre
- ¿Qué familias consideras más estratégicas comercialmente en CHEMIE?
- ¿Dónde ves más futuro real: limpieza, celulosa, especiales alimentarios u otras?
- ¿Qué línea de ALMERIENSE consideras negocio real y cuál simple complemento o arrastre patrimonial?

---

## 7. Conclusión operativa
Este bloque deja una lectura bastante útil:

1. **CHEMIE sí parece tener un núcleo de familias reconocible y razonablemente sano**.
2. **ECOCLEAN también tiene una estructura comercial simple y bastante coherente**.
3. **ALMERIENSE sigue siendo la pieza más contaminada y mezclada**, y por tanto exige depuración específica antes de tomar su margen como verdad cerrada.

### Siguiente paso natural
El siguiente bloque con más retorno sería:
- **proveedores y concentración de abastecimiento**

porque completaría la foto comercial por el otro lado del negocio.
