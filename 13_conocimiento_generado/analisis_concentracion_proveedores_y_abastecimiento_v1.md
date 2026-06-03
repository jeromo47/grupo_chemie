# Análisis de concentración de proveedores y abastecimiento v1

## Objetivo
Completar la foto comercial remota no solo por el lado de clientes, sino también por el lado de compras y dependencia de abastecimiento.

Fuentes soporte creadas:
- `13J23_top10_proveedores_concentracion_por_empresa_anio.csv`
- `13J24_resumen_concentracion_proveedores.csv`
- `13J25_top_proveedores_maestro_enriquecido.csv`
- `13J26_compras_por_proveedor_y_familia.csv`

---

## 1. Dato confirmado - concentración de proveedores
### ALMERIENSE
#### 2024
- proveedores con compras: **78**
- top 1: **16,01 %**
- top 3: **28,65 %**
- top 5: **37,88 %**
- top 10: **53,65 %**

#### 2025
- proveedores con compras: **81**
- top 1: **18,48 %**
- top 3: **29,17 %**
- top 5: **37,18 %**
- top 10: **52,46 %**

### Lectura prudente
ALMERIENSE no parece extremadamente dependiente de uno o dos proveedores. Tiene concentración moderada, bastante más repartida que su cartera de clientes.

---

### CHEMIE
#### 2024
- proveedores con compras: **66**
- top 1: **21,55 %**
- top 3: **40,50 %**
- top 5: **52,24 %**
- top 10: **75,18 %**

#### 2025
- proveedores con compras: **77**
- top 1: **18,52 %**
- top 3: **38,41 %**
- top 5: **50,52 %**
- top 10: **71,86 %**

### Lectura prudente
CHEMIE sí muestra una dependencia clara de un bloque relativamente pequeño de proveedores. No parece crítica de un único proveedor, pero sí de un top 5/top 10 bastante fuerte.

---

### ECOCLEAN
#### 2024
- proveedores con compras: **12**
- top 1: **31,07 %**
- top 3: **59,61 %**
- top 5: **79,77 %**
- top 10: **99,23 %**

#### 2025
- proveedores con compras: **12**
- top 1: **30,40 %**
- top 3: **60,64 %**
- top 5: **81,75 %**
- top 10: **98,88 %**

### Lectura prudente
ECOCLEAN tiene una base de proveedores pequeña y bastante concentrada. Esto es coherente con su escala menor y su papel complementario, pero conviene no ignorarlo: si se cae uno de los principales proveedores, la fragilidad relativa es mayor.

---

## 2. CHEMIE - principales proveedores
### 2025
1. **DICOCEL, S.A.** -> **80.261,72 €**
2. **INDUSTRIA PAPELERA DE MURO, S.L.** -> **53.170,81 €**
3. **DETERVAL CHEMICAL, S.L.** -> **33.058,69 €**
4. **JABIPACK, S.L.** -> **27.133,56 €**
5. **LUIS CONTRERAS S.L.** -> **25.331,71 €**
6. **MANGIR UTILITIES, S.L.** -> **23.122,32 €**
7. **ALMACENES ALMERIENSES DEL COLOR, S.L.** -> **19.115,21 €**
8. **HILADOS BIETE, S.L.** -> **18.953,08 €**

### Lectura prudente
La foto de CHEMIE es bastante coherente con lo ya visto en familias de producto:
- papel / celulosa
- química / detergencia
- envase / packaging
- suministros relacionados con líneas reales del negocio

Eso refuerza que CHEMIE sí tiene una estructura de abastecimiento con lógica comercial bastante reconocible.

---

## 3. ECOCLEAN - principales proveedores
### 2025
1. **PLA ALBERT, S.L.** -> **8.488,29 €**
2. **ALCAUQUÍMICA, S.L.** -> **4.834,33 €**
3. **EXCLUSIVAS TRIANA, S.L.U.** -> **3.610,00 €**
4. **JUAN JOSE HERNANDEZ ANTEQUERA** -> **3.031,93 €**
5. **DETERVAL CHEMICAL, S.L.** -> **2.589,04 €**
6. **MANGIR UTILITIES, S.L.** -> **2.491,28 €**
7. **GRUPO CHEMIE LA JUAIDA, S.L.** -> **868,00 €**

### Lectura prudente
ECOCLEAN muestra:
- dependencia de pocos proveedores
- algo de relación de compra con Chemie
- y una base pequeña, lo que cuadra con su escala menor

Esto no parece anómalo por sí mismo, pero sí confirma que su robustez de abastecimiento probablemente es más estrecha.

---

## 4. ALMERIENSE - principales proveedores
### 2025
1. **APARISI CEPILLOS, S.L.** -> **15.440,24 €**
2. **ELECTROMAIN ELECTRONICA IND., S.L.** -> **4.793,45 €**
3. **INDUSTRIAS CARMAR, S.L.** -> **4.129,75 €**
4. **SCOA MAYORISTAS DE FERRETERIA, S.L.** -> **3.504,60 €**

### Lectura prudente
ALMERIENSE parece menos dependiente de muy pocos proveedores que de muy pocos clientes. Esto es interesante:
- el gran cuello de botella no parece estar en compras
- parece estar bastante más en **concentración de ingresos** y en la mezcla de líneas de negocio

---

## 5. Qué parece decir este bloque
### Confirmado
- **CHEMIE** depende de un top de proveedores importante, pero dentro de una lógica bastante coherente con sus líneas de negocio.
- **ECOCLEAN** tiene base pequeña y concentrada, coherente con su escala.
- **ALMERIENSE** no parece sufrir tanta concentración en compras como en ventas.

### Interpretación prudente
Esto ayuda a priorizar mejor los riesgos:
- en **ALMERIENSE**, el mayor problema no parece ser abastecimiento sino lectura de modelo de negocio, calidad del dato y concentración de clientes
- en **CHEMIE**, sí conviene entender bien los proveedores clave porque sostienen gran parte del núcleo del negocio
- en **ECOCLEAN**, la pequeña escala hace que cualquier proveedor importante pese relativamente más

---

## 6. Preguntas que genera
### Para tío
- ¿Qué proveedores de CHEMIE consideras verdaderamente estratégicos y difíciles de sustituir?
- ¿Dónde hay dependencia por calidad, por precio, por regulación o por relación histórica?
- ¿Hay proveedores en CHEMIE que parezcan grandes por compra pero que realmente sean fácilmente sustituibles?
- En ECOCLEAN, ¿qué proveedores son estructurales y cuáles oportunistas?
- En ALMERIENSE, ¿las compras están razonablemente diversificadas o hay dependencia oculta no visible en este corte?

### Para padre
- ¿Qué proveedor te preocupa más si mañana falla?
- ¿Dónde ves más dependencia personal o histórica en compras?
- ¿Qué proveedor consideras parte del corazón del negocio de CHEMIE?

---

## 7. Conclusión operativa
Este bloque completa bastante bien la foto remota:
- ya sabemos mejor **quién compra** el grupo
- ya sabemos mejor **de quién compra**
- y empieza a verse por dónde están los riesgos reales de concentración

### Balance provisional
- **ALMERIENSE** = riesgo comercial y de mezcla de modelo, más que de compras
- **CHEMIE** = negocio más coherente, pero con proveedores troncales que sí merecen mapa fino
- **ECOCLEAN** = base menor y más concentrada, coherente con su escala

### Siguiente paso natural
El siguiente frente de más retorno parece ser:
- **acotar la alerta ACI / ALMERIENSE**

porque ya tenemos suficiente contexto comercial para volver sobre esa pieza con más criterio.
