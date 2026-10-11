## 2.1

 - Domain expert mondja meg hogy mi legyn a free text sorsa. Ha tartalmaz sok esetben értékes információt akkor külön oszlop legyen, free text-ként ne rakjuk bele az adatok közé, nem lehet validálni,

## 2.2
- OSZLOP                     CHECK                   HIBÁS ÉRTÉK

- nincs ilyen oszlop a schema-ban
    —  RawMeasurements    column_in_schema                 notes
- rossz adattípus, szám helyett szöveg
   3  glucose            coerce_dtype('float64')          unknown
- out of range adatok
     23  bmi                less_than_or_equal_to(100.0)     280.0
- nem tudja számként kezelni a szöveget
      —  glucose            greater_than_or_equal_to(0)      TypeError("'>=' not supp

- glucose két hibát is okozott, float helyett string értéke volt egy sorban, aztán emiatt a range check sem futott le rajta


## 4.1

- gate nélkül bekerült a hibás sor a train, test dataset-be
- a modell használná a training során a hibás adatot

## 4.2

- ha nem talál sikeres validate-et akkor megáll
- _require_validated(settings)


## 4.3 

- prepare skipped

- validate futott mert schemas.py megváltozott
- train, eval is futott ugyanez a file változása miatt

- nem kell ujratanítani a modellt, mert a MAX_AGE validációja változott, az adat nem