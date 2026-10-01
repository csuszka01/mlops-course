## 2. Feladat

- 97 byte pointer file a teljes dataset helyett, pont ez az object store lényege, hogy a nagyméretű fájlokat oda rakjuk, git pedig csak a referenciákat tárolja.
- Ha ugyanaz az adat, ugyanazt a hash-t eredményezi. Ha megváltozik valamelyik csv, akkor nem fogja ugyanazt a .dvc-t kapni.
- dvc pull, a remote-nak elérhetőnek kell lennie, a remote-ban kell lennie a dvc által mutatott állománynak, 

## 4. Feladat

- git a .dvc-t változtatta meg, a dvc pedig a .dvc alapján lehúzta a remote-ból a megfelelő adatszetet

- remote-ból kerül betöltésre, aztán a local cache-ben is benne lesz

## 5. Feladat

-     - src/week_04_dvc_introduction/pipeline.py  --> run futott, teszt elhasalt mikor nem volt
      - src/week_04_dvc_introduction/model.py
      - models/model.pkl
      - models/mlflow_run_id.json
      - data/processed/test.csv

-     Más modell paraméterek mellett futott, C, max_iter, de randostate is okozhatja a változást

Feedback:
    Keep the small JSON files in Git (`cache: false`); metrics/metrics.json goes under `metrics:`.

    Ezen nagyon sokáig gondolkodtam a dokumentáció olvasásával is, hogy mégis melyik menjen az outs-ba, melyik a metrics-be. A hibás yaml indentációk miatt csomószor nem futott a teszt

## 6. Feladat



## 7. Feladat

