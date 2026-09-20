### 1. 

Minio tartalmazza a modell file-okat, artifact-eket

Postgres a metaadatokat, amik jellemzik a run-okat

Model fájlok nagy méretűek, Postgres-ben csak row, column alapú metaadatokat tárolunk.
A Minio tárolja a nagyméretű modelleket

### 2.

Bárki a csapatból meg tudja nézni, hogy milyen paraméterek mellett született az eredmény, össze lehet hasonlítani a többi run-nal
bármikor a jövőben. Terminal-ban nem lehetett ezt megtenni.