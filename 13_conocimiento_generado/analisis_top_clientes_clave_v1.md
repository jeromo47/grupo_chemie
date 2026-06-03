# Análisis de top clientes clave v1

## Objetivo
Poner nombres concretos encima de la concentración comercial detectada, especialmente en ALMERIENSE, para preparar mejor las preguntas a padre y tío antes de septiembre.

Fuentes soporte:
- `13J18_top_clientes_detalle_cartera.csv`
- `13J19_top_clientes_maestro_enriquecido.csv`

---

## 1. ALMERIENSE - dato confirmado
## 2024
### Top 5 clientes
1. **EJIDOMAR, Sdad.Coop.And.** -> **48.036,39 €** -> **33,05 %**
2. **AGROPONIENTE NATURAL PRODUCE, S.L.** -> **34.441,03 €** -> **23,69 %**
3. **BOOKING (ARRENDAMIENTO MACENAS)** -> **21.602,89 €** -> **14,86 %**
4. **ALMAGRO NATURE, S.L.** -> **12.964,50 €** -> **8,92 %**
5. **GRUPO CHEMIE LA JUAIDA, S.L.** -> **7.200,00 €** -> **4,95 %**

### Lectura prudente
Ya aquí se ve que ALMERIENSE no solo está concentrada en pocos clientes, sino que además mezcla:
- cliente agrícola/cooperativo real
- ingreso ligado a arrendamiento / booking
- operación intragrupo con Chemie

Eso exige separar muy bien qué parte de ALMERIENSE es:
- comercial ordinario
- patrimonial / alquiler
- intragrupo

---

## 2025
### Top 4 clientes
1. **EJIDOMAR, Sdad.Coop.And.** -> **65.138,48 €** -> **44,53 %**
2. **AGROPONIENTE NATURAL PRODUCE, S.L.** -> **34.275,10 €** -> **23,43 %**
3. **BOOKING (ARRENDAMIENTO MACENAS)** -> **20.373,95 €** -> **13,93 %**
4. **GRUPO CHEMIE LA JUAIDA, S.L.** -> **7.200,00 €** -> **4,92 %**

### Conclusión confirmada
Solo estos cuatro ya explican una parte enorme de ALMERIENSE.
Además:
- **EJIDOMAR** gana todavía más peso en 2025.
- **Chemie** sigue apareciendo como cliente por el alquiler interno de **7.200 €**.
- **BOOKING (ARRENDAMIENTO MACENAS)** pesa mucho como línea singular y no debería mezclarse sin más con actividad comercial ordinaria.

---

## 2. Señales de calidad del dato en ALMERIENSE
### EJIDOMAR 2025
- ventas: **65.138,48 €**
- coste estimado: **164.078,94 €**
- margen estimado: **-98.940,46 €**
- líneas: **194**
- referencias: **83**
- familias: **13**
- líneas con margen negativo: **37**
- líneas con referencia genérica: **42**

### Interpretación prudente
Esto no debe leerse todavía como pérdida real cerrada del cliente sin más.
Sí parece una señal muy fuerte de que:
- la alerta de ALMERIENSE no es menor
- hay contaminación de coste/maestro muy probable
- y conviene separar con cuidado qué es ruido y qué es negocio real

### AGROPONIENTE NATURAL PRODUCE 2025
- ventas: **34.275,10 €**
- margen estimado: **4.458,65 €**
- líneas: **136**
- referencias: **50**
- familias: **13**

### BOOKING (ARRENDAMIENTO MACENAS)
- aparece como cliente top tanto en 2024 como en 2025
- no tiene familias ni referencias reales de producto en este corte
- por aclaración directa de Jero, corresponde al **alquiler de Macenas** gestionado a través de la plataforma **Booking**, que cobra comisión de reservas y gestiona las facturas
- por tanto, no debe leerse como cliente comercial ordinario de producto, sino como **línea de ingreso de alquiler / explotación patrimonial canalizada por plataforma**

### GRUPO CHEMIE LA JUAIDA, S.L.
- aparece como cliente top por el flujo ya conocido de **7.200 €/año**
- esto confirma otra vez que parte del volumen de ALMERIENSE está sostenido por relaciones estructurales internas, no solo por mercado puro

---

## 3. Qué preguntas genera esto
### Para padre
- ¿EJIDOMAR es hoy el cliente comercial más sensible de ALMERIENSE?
- ¿Qué relación real hay con AGROPONIENTE NATURAL PRODUCE?
- ¿Qué parte del “negocio” de ALMERIENSE consideras verdaderamente comercial y qué parte ves más patrimonial o estructural?

### Para tío
- ¿Por qué EJIDOMAR sale con margen tan negativo en 2025? ¿dato sucio, coste mal arrastrado, familia contaminada o problema real?
- ¿Qué parte del peso de ALMERIENSE depende de clientes reales de mercado y qué parte de flujos internos o rentas?
- ¿Qué cliente de ALMERIENSE te preocupa más de verdad por dependencia o por calidad del margen?

---

## 4. Conclusión operativa
Este corte deja una idea muy clara:

> **ALMERIENSE no debe analizarse todavía como si fuera una cartera comercial limpia y homogénea.**

Parece mezclar al menos tres capas:
1. clientes agrícolas/comerciales reales
2. ingresos patrimoniales o especiales
3. relaciones intragrupo

Eso refuerza la prioridad de:
- aclarar ACI / ALMERIENSE
- separar actividad comercial ordinaria de ingresos estructurales
- no sobreinterpretar márgenes brutos sin depurar el dato

---

## 5. Próximo paso natural
El siguiente análisis con más retorno es:
- **margen por familia / producto**

porque ayudará a responder:
- de dónde sale el dinero de verdad
- qué familias sostienen negocio
- y qué parte del ruido de ALMERIENSE y CHEMIE puede venir de familias o referencias concretas
