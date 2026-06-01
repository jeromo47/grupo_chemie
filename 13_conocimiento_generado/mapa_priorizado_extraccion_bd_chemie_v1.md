# Mapa priorizado de extracción desde base de datos - Chemie v1

## Objetivo
Convertir las necesidades de mejora de Chemie en una **hoja de ruta operativa de extracción**, para que cuando tengamos mejor acceso a base de datos, exportes más finos o informes regenerables, sepamos exactamente:
- qué pedir primero
- para qué sirve cada extracción
- y qué retorno analítico da cada bloque

La idea no es extraer por extraer, sino **extraer con finalidad analítica clara**.

---

## 1. Criterio de priorización
Ordeno las extracciones por esta lógica:
1. **alto retorno analítico inmediato**
2. **capacidad de limpiar dudas ya abiertas**
3. **impacto en la lectura global de Chemie**
4. **facilidad razonable de pedir o regenerar desde el sistema**

---

## 2. Prioridad 1 - Clientes pendientes reales
### Qué habría que extraer
Un detalle de cartera de clientes mucho más fino que el resumen actual, idealmente con:
- cliente
- documento / factura / efecto
- fecha factura
- fecha vencimiento
- importe original
- importe pendiente actual
- estado real (`pendiente`, `cobrado parcial`, `devuelto`, `renovado`, `anulado`, `incobrable`, etc.)
- fecha último movimiento
- comercial o familia si existe
- observaciones internas si el sistema las guarda

### Para qué sirve
- separar definitivamente **riesgo vivo** de **residuo histórico**
- limpiar la lectura de Mercedes, Agrupa Adra y resto
- saber qué saldos siguen realmente abiertos y cuáles son ruido contable

### Retorno
**Altísimo**.
Es probablemente la extracción con mejor relación esfuerzo/valor ahora mismo.

### Preguntas que ayudaría a cerrar
- cuánto del `Pendiente` es realmente cobrable/exigible
- qué casos son viejos pero aún vivos
- qué parte es simplemente basura histórica no depurada

---

## 3. Prioridad 2 - Deuda / financiación 2024-2025
### Qué habría que extraer
Un detalle por operación financiera con:
- entidad
- póliza / préstamo / leasing / renting / confirming / descuento si aplica
- saldo inicial 2024
- movimientos 2024
- saldo cierre 2024
- movimientos 2025
- saldo cierre 2025
- intereses asociados
- amortización / cancelación / novación si se ve
- cuenta contable asociada

### Para qué sirve
- explicar con precisión por qué baja la deuda en 2025
- saber si hubo cancelación real, refinanciación, venta de activo o simple reclasificación
- dejar cerrada la mejora financiera con más solidez

### Retorno
**Muy alto**.
Es la segunda gran pieza para pasar de lectura buena a lectura muy sólida.

### Preguntas que ayudaría a cerrar
- de dónde sale exactamente el desapalancamiento
- qué deuda desaparece y por qué
- qué parte del alivio de intereses responde a menos saldo real

---

## 4. Prioridad 3 - Operaciones vinculadas
### Qué habría que extraer
Un libro o listado de operaciones con vinculadas y personas relacionadas, idealmente con:
- contraparte
- sociedad / persona
- fecha
- documento
- concepto
- cuenta
- debe / haber
- saldo abierto / cerrado
- naturaleza estimada (`comercial`, `alquiler`, `patrimonial`, `vehículo`, `préstamo`, `anticipo`, etc.)

### Foco especial
- **ACI / Almeriense**
- **Jerónimo Molina Caparrós**
- **Jerónimo Molina Cantón** si aparece
- **Ecoclean**
- cualquier otra relacionada recurrente

### Para qué sirve
- separar mejor lo ordinario de lo interno/patrimonial
- evitar mezclar alquiler, compra normal, venta interna y activo transmitido
- dejar muy limpia la lectura del núcleo

### Retorno
**Muy alto**, aunque algo más dependiente de cómo exporte el programa.

### Preguntas que ayudaría a cerrar
- qué parte de las vinculadas es negocio ordinario
- qué parte es soporte estructural
- qué parte responde a operaciones patrimoniales o familiares

---

## 5. Prioridad 4 - Extraordinarios y no recurrentes
### Qué habría que extraer
Un detalle de apuntes no ordinarios, al menos por cuentas sensibles:
- `67x`
- `77x`
- bajas de inmovilizado
- regularizaciones
- anulaciones
- ingresos/gastos extraordinarios o asimilables

Con campos como:
- fecha
- asiento
- documento
- concepto
- cuenta
- importe
- contraparte si existe

### Para qué sirve
- limpiar la lectura del beneficio ordinario
- saber cuánto ruido meten Ducati, activos, anulaciones o ajustes
- distinguir negocio base de movimientos especiales

### Retorno
**Alto**.
Muy útil para convertir la mejora 2025 en una lectura más robusta.

---

## 6. Prioridad 5 - Margen / mix comercial
### Qué habría que extraer
Si la base lo permite:
- ventas por cliente
- ventas por familia / producto / línea
- coste asociado por familia o línea
- margen por cliente o familia
- comparativa 2024 vs 2025

### Para qué sirve
- entender de dónde sale realmente la mejora del margen
- ver si depende de:
  - mejores precios
  - mejor mix
  - menos coste en ciertas familias
  - mejores clientes
  - o líneas concretas como OXISAN u otras

### Retorno
**Alto**, pero menos urgente que cartera, deuda y vinculadas.

---

## 7. Prioridad 6 - Vehículos / inmovilizado operativo
### Qué habría que extraer
Un detalle de inmovilizado móvil / vehículos con:
- código activo
- descripción
- fecha alta
- coste
- amortización acumulada
- fecha baja o venta
- contraparte
- asiento asociado
- saldo pendiente si existió

### Foco especial
- **Ducati**
- **Mini**
- **BMW X3**
- cualquier otro vehículo relevante que aparezca en Chemie

### Para qué sirve
- cerrar bien la historia Mini / Ducati
- separar operaciones personales/patrimoniales del negocio ordinario
- dejar más limpia la lectura de activos y extraordinarios

### Retorno
**Medio-alto**.
No es lo primero, pero sí una pieza buena de cierre fino.

---

## 8. Extracciones complementarias útiles
### 8.1 Concentración real de clientes
Para medir dependencia comercial real del top 5 / top 10.

### 8.2 Concentración real de proveedores
Para medir dependencia de abastecimiento y sensibilidad del margen.

### 8.3 Antigüedad de saldos
Un aged balance real por tramos:
- 0-30
- 31-60
- 61-90
- 91-180
- 181-365
- >365

Esto sería especialmente valioso para clientes y, si compensa, también para proveedores.

---

## 9. Orden recomendado de ejecución real
### Si solo pudiéramos pedir 3 cosas
#### 1.
**Detalle fino de clientes pendientes reales**

#### 2.
**Detalle de deuda / financiación 2024-2025**

#### 3.
**Detalle de operaciones vinculadas**

### Si pudiéramos pedir 5
Añadiría después:
#### 4.
**Detalle de extraordinarios / inmovilizado / bajas**

#### 5.
**Ventas-costes-margen por cliente/familia**

---

## 10. Qué se gana con esto
Si estas extracciones salen razonablemente bien, Chemie pasaría de:
- **empresa bien entendida en términos generales**

a:
- **empresa entendida con nivel casi de control de gestión / auditoría interna ligera**

Y eso tendría mucho valor para todo el proyecto, porque Chemie ya es la pieza tractora del núcleo.

---

## 11. Conclusión ejecutiva
Si tuviera que resumir este mapa en una frase:

> **Lo primero que conviene extraer mejor de Chemie no es “todo”, sino cartera real de clientes, deuda/financiación y vinculadas; ahí está el mayor salto de calidad analítica inmediato.**

Ese debería ser el orden base mientras no aparezca una nueva necesidad más urgente.
