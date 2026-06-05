# Validación paquete 20B - Cierre mensual mayo 2026

## Estado

Paquete recibido y leído correctamente. Los 10 CSV están presentes. He limpiado cabeceras repetidas y espacios de salida de Firebird.

## Resumen ejecutivo del mes

|Empresa|Fact. venta|Clientes|Ventas s/IVA|Coste est.|Margen est.|Margen %|Fact. compra|Proveedores|Compras s/IVA|
|---|---|---|---|---|---|---|---|---|---|
|CHEMIE|33|21|35.129,10 €|18.125,75 €|17.003,35 €|48,40%|30|25|21.251,04 €|
|ALMERIENSE|6|4|5.642,40 €|3.442,13 €|2.200,27 €|39,00%|26|20|6.044,87 €|
|ECOCLEAN|49|36|9.740,05 €|4.974,36 €|4.765,69 €|48,93%|8|7|2.738,08 €|


Ventas grupo mayo 2026: **50.511,55 €**. Compras grupo mayo 2026: **30.033,99 €**.

## Principal cliente y proveedor por empresa

|Empresa|Top cliente|Ventas|% ventas|Top proveedor|Compras|% compras|
|---|---|---|---|---|---|---|
|CHEMIE|INDASOL, S.A.T. Nº9404|8.072,50 €|22,98%|DICOCEL, S.A.|5.504,67 €|25,90%|
|ALMERIENSE|EJIDOMAR, Sdad.Coop.And.|1.985,30 €|35,19%|EDY ORLANDO PARRAGA CONTRERAS|1.499,85 €|24,81%|
|ECOCLEAN|GASTROALMERIA, S.L|1.160,80 €|11,92%|DICOCEL, S.A.|961,99 €|35,13%|

## Pendientes y bancos/deuda

|Empresa|Top clientes pendientes|Top proveedores pendientes|Bancos 572|Deuda LP 170|Deuda CP 520|
|---|---|---|---|---|---|
|CHEMIE|241.383,28 €|123.442,19 €|94.151,95 €|19.178,92 €|0,00 €|
|ALMERIENSE|174.834,45 €|89.550,73 €|73.941,10 €|55.889,41 €|0,00 €|
|ECOCLEAN|21.793,69 €|5.789,80 €|41.692,26 €|0,00 €|0,00 €|

## Validación / advertencias

- **Ventas de cabecera vs ventas por líneas cuadran** en las tres empresas: los importes de ventas de `20B1` y `20B3` coinciden.

- **Márgenes son estimados** porque usan coste medio/precio medio de compra. No equivale a margen contable cerrado.

- **Clientes/proveedores pendientes son estimación a cierre 31/05/2026**. Hay saldos muy antiguos desde 2007-2008; no deben leerse como cobrables/pagables reales sin depuración.

- **Bancos/deuda** se calcula desde diario acumulado hasta 31/05/2026. Incluye cuentas históricas con saldo cero y cuentas de deuda antiguas; sirve como primer corte, no como certificado bancario.

- La clasificación simple en Almeriense en mayo 2026 sale como `MERCADO_OPERATIVO`; no detecta patrimonial en este mes concreto. No extrapolar al año.


## Archivos limpios generados

Se ha generado `20B_PAQUETE_CIERRE_MAYO_2026_CSV_LIMPIO.zip` con los 10 CSV sin cabeceras repetidas y con importes redondeados.
