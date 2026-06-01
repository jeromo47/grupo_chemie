# Mini auditoría - Relación económica Chemie / ACI v1

## Objetivo
Analizar la relación económica entre:
- **GRUPO CHEMIE LA JUAIDA, S.L.**
- **ALMERIENSE DE COMPLEMENTOS INDUSTRIALES, S.L. / S.L.U.**

para entender si estamos ante:
- una relación puntual
- una relación recurrente
- una dependencia relevante
- o simplemente un cruce menor entre sociedades del núcleo

---

## Fuente principal
Paquete económico guardado en:
- `/home/jero/cloud/02_proyectos/grupo_familiar/00_inbox/2026-05-22_paquete_informe_consultoria_grupo_chemie_2024_2025/`

Especialmente:
- `02_margen_clientes_proveedores_grupo.txt`
- `03_cobros_bancos_deuda_grupo.txt`
- `04_pyg_patrimonio_grupo.txt`

---

## 1. Conclusión principal
Sí existe **relación económica real y recurrente** entre Chemie y ACI.

Pero, con lo visible hasta ahora, **no parece una relación de gran volumen dominante**, sino más bien:
- recurrente
- operativa
- relativamente contenida en importe
- y aparentemente bien liquidada al cierre

La impresión es la de una relación interna funcional de soporte o suministro, no la de una gran dependencia económica opaca.

---

## 2. Evidencia básica de cruce real
### En proveedores / compras del grupo aparecen referencias a ACI
En `02_margen_clientes_proveedores_grupo.txt` se ve:
- **TOP_PROVEEDORES_2025** -> `ALMERIENSE DE COMPL. INDUSTRIALES, S.L.` con **4 facturas** y **1.826,40 €**
- `COMPRAS_GRUPO 2024` -> `ALMERIENSE DE COMPL. INDUSTRIALES, S.L.` con **1** movimiento y **476,00 €**
- `COMPRAS_GRUPO 2025` -> `ALMERIENSE DE COMPL. INDUSTRIALES, S.L.` con **4** movimientos y **1.826,40 €**

Además aparece también la variante contable/nominativa:
- `ALMERIENSE COMPTOS. INDUSTRIALES, S.L.` con **4 movimientos** y **7.200,00 €** en 2024
- y otros **4 movimientos** por **7.200,00 €** en 2025

### Qué sugiere
No estamos ante una única factura anecdótica.
Parece una relación repetida y sostenida en el tiempo.

---

## 3. Evidencia contable de movimientos vinculados
En `04_pyg_patrimonio_grupo.txt` aparecen bloques explícitos de:
- **`MOVIMIENTOS_VINCULADOS_POR_CONCEPTO`**

con entradas como:
- `Pago Fra. 2-230158, ALMERIENSE DE COMPL...` -> **1.490,42 €**
- `Fra. nº 2-240162, ALMERIENSE DE COMPL...` -> **340,74 €**
- posterior pago de esa misma factura -> **340,74 €**
- `Fra. nº 2-250126, ALMERIENSE DE COMPL...` -> **239,78 €**
- posterior pago de esa misma factura -> **239,78 €**

### Qué sugiere
Aquí se ve un patrón bastante limpio:
- ACI factura a Chemie
- Chemie registra la compra/gasto
- luego paga
- y la cuenta queda regularizada

---

## 4. Estado de saldos al cierre
En `03_cobros_bancos_deuda_grupo.txt` y `04_pyg_patrimonio_grupo.txt` aparece:
- cuenta `4000000049 ALMERIENSE DE COMPL. INDUSTRIALES, S.L.` -> **0,00** tanto en 2024 como en 2025

### Lectura
Esto es muy importante.
Significa que, al menos en la foto de cierre que estamos viendo:
- no parece existir un gran saldo abierto entre Chemie y ACI
- la relación no aparece enquistada en cuentas a pagar/cobrar relevantes al cierre

### Implicación
La relación parece más de **operativa corriente y liquidada**, no de financiación cruzada grande pendiente en balance, al menos por esta cuenta.

---

## 5. Interpretación funcional más probable
### Mi mejor lectura ahora mismo
ACI parece actuar respecto de Chemie como una combinación de:
- proveedor próximo
- soporte comercial/logístico
- o suministrador interno/relacionado para ciertos conceptos concretos

### Lo que NO parece
No parece, con lo visible:
- el gran financiador oculto de Chemie
- una cuenta puente enorme sin depurar
- ni una relación opaca de gran volumen sistémico

### Lo que SÍ parece
Una relación:
- natural dentro del ecosistema del grupo
- recurrente
- compatible con la hipótesis de ACI como sociedad bisagra de soporte

---

## 6. Los 7.200 € recurrentes llaman la atención
### Dato
Aparece la variante `ALMERIENSE COMPTOS. INDUSTRIALES, S.L.` con:
- **2024** -> 4 movimientos -> **7.200,00 €**
- **2025** -> 4 movimientos -> **7.200,00 €**

### Por qué importa
Ese patrón tan redondo y repetido suena menos a compra irregular de mercancía y más a:
- servicio recurrente
- cuota interna
- alquiler/uso
- soporte estructural
- o facturación periódica de naturaleza bastante estable

### Lectura prudente
No lo cierro aún, pero es una de las mejores pistas para entender **qué papel funcional concreto desempeña ACI respecto de Chemie**.

---

## 7. Qué me parece más probable sobre esta relación
### Hipótesis fuerte
La relación Chemie-ACI parece tener dos capas:

#### capa 1 - operativa menor y corriente
- pequeñas facturas
- compras puntuales
- pagos y regularización normal

#### capa 2 - flujo recurrente más estructural
- patrón 7.200 €/año
- posible servicio o soporte estable
- probablemente no aleatorio

### Esto encaja con el modelo general
- Chemie = motor operativo principal
- ACI = sociedad soporte, mixta, con papel logístico/patrimonial/comercial

---

## 8. Riesgo o alerta
### Lo que NO veo
No veo por ahora una alarma fuerte de:
- saldo intersocietario descontrolado
- financiación encubierta masiva
- o gran agujero cruzado entre Chemie y ACI

### Lo que sí merece revisión
- identificar la naturaleza exacta del flujo recurrente de **7.200 €**
- ver si corresponde a:
  - alquiler
  - servicios
  - cesión de medios
  - administración
  - soporte comercial o logístico

### Tipo de alerta
No roja.
Más bien una **alerta amarilla de interpretación**: importante para entender el grupo, no necesariamente por riesgo contable grave.

---

## 9. Qué se puede afirmar ya
- Chemie y ACI sí tienen **relación económica real**
- la relación es **recurrente**
- la escala visible es **moderada**, no dominante
- los saldos visibles aparecen **regularizados al cierre**
- existe un subpatrón muy interesante de **7.200 € anuales** que merece ser explicado

---

## 10. Conclusión ejecutiva
Si tuviera que resumir esta mini auditoría en una frase:

> **ACI sí parece formar parte de la fontanería económica real de Chemie, pero más como sociedad de soporte recurrente y contenida que como gran contrapeso financiero u operativo del núcleo.**

Eso me parece una pieza importante, porque da más solidez a la idea de ACI como **sociedad bisagra** dentro del sistema.

---

## 11. Siguiente paso recomendado
Veo dos caminos buenos:

1. revisar el patrón de **7.200 €** para entender su naturaleza
2. o pasar a una **síntesis integrada económica + vinculadas + patrimonio** del núcleo

### Mi recomendación real
Haría la **síntesis integrada**.
Creo que ya tenemos material suficiente para una nota bastante potente de conjunto.
