# 17B_auditoria_ecoclean_894

## Objeto
- Verificar el dato `ECOCLEAN = 894` procedente de `13J13_movimientos_sensibles_551_752_758.csv`.

## Dato confirmado
- Total de registros en `13J13` por empresa:
  - ALMERIENSE: 89
  - CHEMIE: 49
  - ECOCLEAN: 894

- ECOCLEAN suma **894** registros en este CSV.
- El conteo corresponde a **apuntes/lineas contables** del extracto sensible, no necesariamente a operaciones económicas únicas.

## Desglose ECOCLEAN
- Años afectados:
  - 2024: 457 apuntes
  - 2025: 437 apuntes

- Clasificación sensible detectada en ECOCLEAN:
  - 758: 890
  - 551: 4

- Cuentas que más explican el volumen (top 10 por número de apuntes):
  - 7580000000 | INGRESOS_758: 890 apuntes, debe 38.143,58 €, haber 38.262,64 €, saldo neto -119,06 €
    - conceptos más repetidos: Fra. Nº 2-35,FRESH PREMIUM, S.L. (2), Fra. Nº 2-280,GARRI AGRICOLA, S.L. (2), Fra. Nº 2-301,SUMINISTRO AGRICOLA ACIEN (2)
  - 5510000000 | SOCIOS_GRUPO_551: 4 apuntes, debe 7.600,00 €, haber 7.600,00 €, saldo neto 0,00 €
    - conceptos más repetidos: Asiento de Apertura (2), Asiento de Cierre (2)

## Interpretación prudente
- El `894` parece ser un recuento de **apuntes contables sensibles** o **registros contables a revisar**, no de operaciones únicas cerradas.
- Si varias operaciones generan múltiples apuntes contables, el volumen puede verse inflado respecto a una lectura de “operaciones”.
- Por precisión documental, `movimientos sensibles` puede inducir a pensar en movimientos únicos; la etiqueta más prudente es **apuntes contables sensibles**.

## Recomendación de redacción
- En el informe final, la formulación más precisa sería: **"apuntes contables sensibles detectados"**.
- Alternativa válida: **"registros contables a revisar"**.
- Menos recomendable para este caso: **"operaciones sensibles"**, porque puede sobreinterpretar el dato.

## Conclusión breve
- A falta de depuración adicional, el `894` no parece un error aritmético del CSV, pero sí un **conteo potencialmente inflado por apuntes contables repetidos o fragmentados**.
- La recomendación no es cambiar la cifra sin más, sino **cambiar la redacción** para dejar claro que se trata de apuntes/registros contables sensibles, no de operaciones únicas.