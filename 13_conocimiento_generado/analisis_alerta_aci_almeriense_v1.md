# Análisis de alerta ACI / ALMERIENSE v1

## Objetivo
Acotar mejor la alerta abierta sobre ACI / ALMERIENSE, especialmente en torno a:
- margen muy negativo en 2025
- stock absurdo o contaminado
- mezcla entre comercial, patrimonial e intragrupo

Fuentes soporte creadas:
- `13J27_aci_almeriense_desglose_clientes_especiales.csv`
- `13J28_aci_almeriense_resumen_por_tipo_lectura.csv`
- `13J29_aci_almeriense_stock_anomalias_detalle.csv`
- `13J30_aci_almeriense_productos_ruido_top.csv`

---

## 1. Lo que ya puede sostenerse con bastante fuerza
### ACI / ALMERIENSE no debe leerse como una empresa comercial homogénea
A estas alturas, la lectura más razonable es que mezcla al menos tres capas:
1. **cliente de mercado**
2. **línea patrimonial / alquiler**
3. **intragrupo con Chemie**

Eso ya no es una intuición abstracta. Sale bastante claro en los cortes de clientes y productos.

---

## 2. Desglose por tipo de lectura
## 2024
### CLIENTE_MERCADO
- ventas: **115.642,35 €**
- coste: **74.351,15 €**
- margen: **41.291,20 €**
- líneas: **645**
- líneas sin coste: **65**
- líneas con margen negativo: **105**
- líneas con referencia genérica: **78**

### PATRIMONIAL_BOOKING
- ventas: **21.602,89 €**
- coste: **0,00 €**
- margen: **21.602,89 €**
- líneas: **18**
- líneas sin coste: **18**

### INTRAGRUPO_CHEMIE
- ventas: **8.116,60 €**
- coste: **832,26 €**
- margen: **7.284,34 €**
- líneas: **16**

### Lectura prudente
En 2024, la parte de mercado todavía sale globalmente con margen positivo razonable. La parte patrimonial y la intragrupo añaden margen limpio, pero no parecen esconder un desastre global por sí solas.

---

## 2025
### CLIENTE_MERCADO
- ventas: **117.306,88 €**
- coste: **216.521,50 €**
- margen: **-99.214,62 €**
- líneas: **440**
- líneas sin coste: **39**
- líneas con margen negativo: **59**
- líneas con referencia genérica: **71**

### PATRIMONIAL_BOOKING
- ventas: **20.373,95 €**
- coste: **0,00 €**
- margen: **20.373,95 €**
- líneas: **22**
- líneas sin coste: **22**

### INTRAGRUPO_CHEMIE
- ventas: **8.585,80 €**
- coste: **1.229,09 €**
- margen: **7.356,71 €**
- líneas: **13**

### Conclusión provisional fuerte
La patrimonial y la intragrupo ayudan, pero **no explican el agujero**.
El problema grande está dentro de la capa etiquetada aquí como **CLIENTE_MERCADO 2025**.

---

## 3. Qué parece estar contaminando la lectura
## Stock
La distorsión del stock de ALMERIENSE parece enormemente concentrada en referencias sospechosas.

### Caso más extremo
- `999999` / `VARIOS`
- familia: **COMPLEMENTOS VARIOS**
- stock actual: **-298.294,98**
- valor stock coste medio: **-16.579.234,99 €**
- marcado como referencia genérica

### Otros casos fuertes
- `999992` ELECTRODOMESTICOS Y HIFI -> **-187.828,47 €**
- `01133445` ACEITE COMPRESORES -> **-63.333,00 €**
- `000000` HERRAMIENTAS VARIAS -> **-53.934,93 €**
- múltiples referencias negativas muy fuertes en hornos, cadenas, cepillos y complementos varios

### Lectura prudente
Aquí ya puede afirmarse con bastante confianza que el stock de ALMERIENSE está **muy contaminado** y que esa contaminación no es un detalle menor, sino una de las causas probables principales del absurdo económico detectado en el margen.

---

## 4. Ruido de producto y referencias genéricas
El top de productos “ruidosos” de ALMERIENSE vuelve a reforzar el patrón:
- referencias `999999`
- referencias `000000`
- referencias vacías
- líneas patrimoniales sin familia real
- pares de abono/venta que parecen dejar huella rara en margen

### Ejemplos visibles
- `ARANDELA ZINCADA Ø10 DIN 125` -> margen **-5.410,00 €**
- `ARANDELA SEGURIDAD DIN 6799-04` -> **-2.373,75 €**
- múltiples `CHAVETA DIN...` con margen muy negativo
- líneas de alquiler de nave o alquiler vacacional con **coste cero** y sin familia productiva

### Interpretación prudente
No parece razonable leer este bloque como si reflejara puro rendimiento comercial por referencia. Hay una mezcla grande de:
- referencias genéricas
- problemas de maestro
- coste mal arrastrado
- líneas no comerciales puras
- patrimonial / alquiler
- intragrupo

---

## 5. Qué sí puede sostenerse ya
### Confirmado
1. **La alerta de ALMERIENSE es real como alerta de calidad de dato y de mezcla de modelo.**
2. **El stock está muy contaminado**, y no en un nivel anecdótico.
3. **La capa patrimonial y la intragrupo existen y pesan**, pero no son el origen principal del margen negativo de 2025.
4. **El agujero aparente de 2025 está en la capa de mercado**, aunque muy probablemente mezclado con un coste/stock/maestro poco fiable.

### Interpretación prudente
A día de hoy, la mejor lectura no es:
> “ALMERIENSE pierde 99 mil euros reales de mercado y punto”

Tampoco es:
> “todo es falso y no pasa nada”

La lectura más seria parece ser:
> **hay una distorsión grave del dato comercial/stock/coste en ALMERIENSE y, mientras no se depure, no puede leerse su margen 2025 como verdad económica limpia**.

---

## 6. Qué preguntas genera
### Para tío
- ¿Qué originó el monstruo de stock en referencias como `999999`, `000000` y similares?
- ¿Qué parte del margen negativo de ALMERIENSE 2025 atribuyes a stock/coste contaminado y qué parte a negocio real?
- ¿Qué productos o familias sabes ya que no deben usarse para leer rentabilidad sin depuración previa?
- ¿Cómo separarías de forma práctica la actividad comercial ordinaria de ALMERIENSE frente a Booking/Macenas y alquiler nave a Chemie?

### Para padre
- ¿Qué parte de ALMERIENSE ves realmente como negocio vivo comercial y qué parte como estructura de apoyo/patrimonial?
- ¿Qué cliente o línea de ALMERIENSE te preocupa más como negocio real, dejando fuera alquileres y flujos internos?

---

## 7. Conclusión operativa
Este bloque recorta bastante bien la alerta ACI / ALMERIENSE.

### Lo que parece ya bastante claro
- **no es una simple comercial pequeña normal**
- **no es una cuenta limpia de ventas/compras/margen**
- **sí mezcla capas distintas de negocio**
- **sí tiene un problema fuerte de calidad de dato en stock y referencias**

### Utilidad para septiembre
Esto permite llegar con una hipótesis mucho mejor:
- en ALMERIENSE hay que entrar separando primero:
  1. actividad comercial ordinaria
  2. actividad patrimonial / alquiler
  3. intragrupo
  4. ruido de stock / coste / maestro

Y no intentar leerla como una sola cosa.
