# Matriz de productos químicos y marco regulatorio v1

## Objetivo
Construir una base útil para que Jero pueda distinguir, con el tiempo y cada vez con más precisión:
- qué tipo de producto es cada uno
- en qué contexto se usa
- qué legislación o marco regulatorio le aplica
- qué riesgos de uso o comercialización tiene
- y por qué se utiliza un producto u otro en cada caso

Este archivo no pretende cerrar toda la clasificación técnica en una sola pasada.
Pretende dejar una **estructura estable y gobernable** para ir identificando productos y separándolos con criterio.

---

## 1. Principio importante
No conviene mezclar bajo la etiqueta genérica de “productos químicos” cosas muy distintas.

A la vista del material ya analizado en Chemie, al menos hay que distinguir estas capas:
1. **detergentes / limpiadores / desengrasantes**
2. **desinfectantes / biocidas**
3. **productos de uso en industria alimentaria / postcosecha / lavado de frutas**
4. **tratamiento de aguas**
5. **coadyuvantes tecnológicos**
6. **productos auxiliares industriales**
7. **pinturas / disolventes / aerosoles**
8. **productos con posible impacto REACH/CLP/FDS sin ser necesariamente biocidas**

---

## 2. Marcos regulatorios que ya salen del proyecto
## A. REACH / CLP / FDS
Este marco parece transversal para gran parte de la actividad de Chemie como:
- distribuidor mayorista
- envasador
- comercializador de productos químicos

### Implicaciones prácticas
- fichas de datos de seguridad
- actualización documental
- trazabilidad hacia clientes y trabajadores
- clasificación y etiquetado

---

## B. ROESBA / biocidas
Aplica cuando el producto entra de verdad en perímetro biocida.

### Lo ya apoyado en el proyecto
Chemie aparece sobre todo en:
- almacenamiento
- comercialización / distribución de biocidas

Y no tanto, por ahora, como empresa centrada en prestación principal de tratamientos biocidas.

### Implicaciones prácticas
- no todo desinfectante comercial o producto agresivo debe darse automáticamente por biocida sin revisar su encaje real
- hay que distinguir muy bien entre:
  - biocida verdadero
  - detergente/desengrasante
  - coadyuvante
  - tratamiento de aguas

---

## C. Registro sanitario / industria alimentaria
Aparece para productos y líneas ligadas a:
- lavado de frutas
- tratamiento de aguas
- desinfección / limpieza en entornos alimentarios

### Advertencia
El proyecto ya sugiere que este encaje sanitario histórico no siempre fue el definitivo ni el más limpio, porque parte del catálogo parece haberse reordenado luego entre:
- biocidas
- coadyuvantes
- otros marcos específicos

---

## D. CAAE / producción ecológica
Aparece con fuerza en OXISAN y en el mundo de:
- insumo compatible con producción ecológica
- coadyuvante tecnológico
- tratamiento de aguas de lavado / postcosecha

### Implicación práctica
No todo producto “para agro” o “para alimentación” entra por el mismo marco.
Hay productos que no deberían clasificarse mentalmente igual que un biocida clásico.

---

## 3. Estructura recomendada para identificar bien cada producto
Para cada producto relevante conviene acabar teniendo esta ficha mínima:

### 1. Identificación básica
- referencia interna
- nombre comercial
- familia
- empresa
- si está activo o en desuso

### 2. Tipo funcional
Elegir una categoría principal, por ejemplo:
- detergente
- desengrasante
- desinfectante
- biocida
- tratamiento de aguas
- coadyuvante tecnológico
- producto auxiliar industrial
- pintura/disolvente
- aerosol
- otro

### 3. Ámbito de uso
- industria alimentaria
- cooperativas agrícolas
- limpieza general
- postcosecha
- lavado de frutas
- taller / automoción
- nave / almacén
- uso técnico industrial

### 4. Marco regulatorio principal
- REACH/CLP/FDS
- ROESBA / biocidas
- registro sanitario histórico / industria alimentaria
- CAAE / ecológico
- tratamiento de aguas
- varios / por determinar

### 5. Riesgos de clasificación
- ¿puede confundirse con biocida sin serlo?
- ¿puede confundirse con producto alimentario cuando en realidad es auxiliar?
- ¿necesita validación documental extra?

### 6. Criterio de uso
- para qué se usa realmente
- en qué caso conviene usarlo
- por qué se elige frente a otro
- qué limitaciones o cautelas tiene

---

## 4. Primeras familias que parecen prioritarias
A la vista del trabajo ya hecho, las familias más interesantes para empezar son:
- **01 DESENGRASANTES Y LIMPIADORES GENERALES**
- **03 PROD. ESPECIALES INDUST. ALIMENTARIA**
- **09 PROD. Y ACCESORIOS PARA LIMPIEZA**
- **06 PINTURAS Y DISOLVENTES**
- **07 AEROSOLES**
- productos o líneas conectadas con **biocidas**
- productos o líneas conectadas con **OXISAN / tratamiento aguas / postcosecha**

Estas familias no agotan todo el negocio, pero sí parecen de alto valor para aprender el bloque químico con criterio.

---

## 5. Qué conviene no hacer
- no asumir que toda la familia “química” tiene el mismo marco legal
- no confundir “desinfectante” con “biocida” automáticamente
- no leer solo por nombre comercial sin soporte documental técnico
- no intentar memorizar normativa sin separar antes tipos reales de producto

---

## 6. Siguiente paso práctico recomendado
### Paso 1
Usar el maestro de artículos base de Chemie para sacar una **preclasificación inicial por familias y nombres**.

Archivo soporte creado:
- `13J34_maestro_productos_chemie_base.csv`

### Paso 2
Construir una tabla viva derivada con columnas como:
- referencia
- descripcion
- familia
- tipo_funcional_provisional
- ambito_uso_provisional
- marco_regulatorio_principal_provisional
- nivel_confianza
- dudas

### Paso 3
Cruzar esa tabla con:
- documentación de biocidas
- registro sanitario
- CAAE / OXISAN
- y preguntas a tu tío

---

## 7. Juicio de valor
Este bloque puede darte muchísimo valor a medio plazo.

No solo por aprender normativa,
sino porque te obligará a hacer algo mucho más importante:

> distinguir producto, uso, riesgo y marco legal,
> en vez de tratar “lo químico” como un bloque difuso que solo entiende tu tío.

Y eso es precisamente lo que necesitas si quieres dejar de depender ciegamente de conocimiento oral en el área más sensible del negocio.
