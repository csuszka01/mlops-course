### 4. 
- A f1 kalkulációnál használt threshold mellett a rf jobban teljesített mint a logreg
- viszont más threshold-nál a logreg volt jobb az ROC szerint

- Azért választom a rf-n_estimators=300 -at, mivel kevesebb False Negative döntést hozott, ami a feladatban
    azt jelenti hogy kevesebb tényleges beteg pácienst osztályozott egészségesnek.

- választott run_id: 4fdfe927faa04847b7acea7067d19a90


### 6.1.

- Alias - model version - run - evidence (params, metrics, artifacts, tags) - tag - commit - source code

### 6.2.

- Akkor valódi a commit hash ha a run közben a working tree tiszta volt. Ha nem akkor más kód futott és nem a tagben lévő commit

### 6.3.

- Utasítsd el — ennek ára: run-ok akadnak el a promóción pusztán azért, mert a tree piszkos volt, nem azért, mert a modell rossz
 

### 6.4

- Egy alias átmozgatható egy másik verzióra anélkül, hogy magát a verziót érintené (azonnali rollback, újralogolás nélkül), egy fix Staging stage egyetlen globális címke, modellenként egyetlen verzióhoz kötve, ilyen rugalmasság nincs

### 6.5

- mivel nincs verziózva a data set, csendben megváltozhatott vagy  a futtatás óta. Adatverziózásra van szükség pl. tagként naplózva.


### 7.1

- változott:        az aliasok (champion, staging más verzióra mutatnak)
- nem változot:     a verziók ugyanúgy megvannak mint előtte

### 7.2

- version tag-ek, a make trace kimenetéből kiderül, hogy ki és mikor promótála champion-re

### 7.3

 - nem sikerült elsőre, version 5 -> 4 rollback után a trace dirty állapotot mutatott a commit alapján.