# Emergency Dispatch & Traffic Physics Dataset

**Forrás:** https://www.kaggle.com/datasets/razanihababdellatif/emergency-dispatch-and-traffic-physics-dataset?resource=download

**Licensz:** Attribution 4.0 International, szabadon használható

**Sorok:** 24 693 | **Oszlopok:** 29

Szintetikus, 200 000 soros benchmark-adatkészlet, amely városi, elővárosi és vidéki forgalmat, baleseti és mentési statisztikákat tartalmaz.

Baleset-előrejelzésre, súlyosság-osztályozásra, valamint a mentési idők és útlezárások elemzésére használható.

A felhaznált minták között,  **8231** baleset és **16 462** balesetmentes rekord található (az eredeti **191 769** balesetmentes rekordból mintavételezve), azaz kb. **33%** a balesetek aránya. **1461** különböző dátumot fed le (**4 év**).

**Feladattípus:** Binary Classification, `Accident_Occurred` feature predikció

**Méret és elérhetőség** 4,4 MB, 60 másodperc alatt tanítható, github kommittálható, szabadon elérhető csv file.

**Data type:** Tabular


## Oszlopok leírása

### ID és idő
| Oszlop | Leírás |
|---|---|
| `Record_ID` | Rekordazonosító (`REC_xxxxxxx`). 24 669 egyedi érték, tehát kb. 24 duplikált ID. |
| `Timestamp` | Az esemény teljes időbélyege. |
| `Date` | A rekord dátuma. |
| `Hour` | Napszak órája (0–23). |
| `Month` | Hónap (1–12). |
| `Day_of_Week` | A hét napja (7 kategória: a hét napjai angol nevekkel, pl. `Friday`). |
| `Time_of_Day` | Napszak-kategória (4 érték: `Evening Peak`, `Morning Peak`, `Night`, `Midday`). |
| `Is_Holiday` | 1 = ünnepnap, 0 = nem. |
 
### Helyszín és út
| Oszlop | Leírás |
|---|---|
| `Area_Type` | Terület típusa (3 érték: `Urban`, `Suburban`, `Rural`). |
| `Road_Type` | Úttípus (4 érték: `Interstate`, `Arterial`, `Collector`, `Local`). |
| `Intersection_Type` | Csomópont típusa (3 érték: `4-Way`, `T-Junction`, `Roundabout`; + NaN). |
| `Speed_Limit_kmh` | Megengedett sebesség (km/h). |
| `Road_Condition` | Útfelszín állapota (5 érték: `Dry`, `Wet`, `Snowy`, `Icy`, `Standing Water`). |
 
### Környezet és forgalom
| Oszlop | Leírás |
|---|---|
| `Weather` | Időjárás. Valójában 4 kategória: `Clear`, `Rain`, `Snow`, `Fog`. A nyers adatban 7 érték szerepel, mert az eső inkonzisztensen van írva: `Rain`, `rain`, `Rain ` (szóközzel), ` RAIN` – tisztítás szükséges. |
| `Visibility_m` | Látótávolság méterben. ~685 hiányzó érték. |
| `Congestion_Index` | Forgalmi torlódási index (magasabb = nagyobb torlódás). |
 
### Vezető és jármű
| Oszlop | Leírás |
|---|---|
| `Vehicle_Type` | Járműkategória (5 érték: `Sedan`, `SUV`, `Truck`, `Motorcycle`, `Bus`). |
| `Driver_Age` | A vezető életkora (év). |
| `Driver_Experience_yrs` | Vezetési tapasztalat években. ~479 hiányzó érték. |
| `Vehicle_Age_yrs` | A jármű kora években. |
| `Recorded_Speed_kmh` | Mért sebesség (km/h). A maximum 999 – valószínűleg placeholder/kiugró érték. |
 
### Baleset kimenetele
| Oszlop | Leírás |
|---|---|
| `Accident_Occurred` | **Célváltozó.** 1 = baleset történt, 0 = nem. |
| `Collision_Type` | Ütközés típusa (4 érték: `Rear-End`, `Side-Impact`, `Head-On`, `Single-Vehicle`; + NaN). Csak balesetnél kitöltött. |
| `Vehicles_Involved` | Érintett járművek száma; balesetmentes rekordnál 0. |
| `Accident_Severity` | Baleset súlyossága (5 érték: `No Accident`, `Minor`, `Moderate`, `Severe`, `Fatal`). |
| `Dispatch_Priority` | Kiérkezési prioritás (3 érték: `Standard`, `Medium`, `High`; + NaN). Csak balesetnél kitöltött. |
 
### Reagálás és hatás
| Oszlop | Leírás |
|---|---|
| `Baseline_Expected_Response_Time_min` | Várt kiérkezési idő percben; minden sorban ki van töltve. |
| `Actual_Response_Time_min` | Tényleges kiérkezési idő percben; balesetmentes rekordnál 0. |
| `Road_Closure_Duration_min` | Útlezárás időtartama percben; balesetmentes rekordnál 0. Erősen jobbra ferde eloszlás. |


## Megjegyzések
- A `Collision_Type`, `Vehicles_Involved`, `Accident_Severity`, `Dispatch_Priority`, `Actual_Response_Time_min` és `Road_Closure_Duration_min` mezők értéke csak baleset után ismert, így csak a `Accident_Occurred == 1` értékű rekordoknál nem NaN
- Több feature esetén is hiányzó NaN értékek
- String típusú feature több esetben nem konzisztensen kis- vagy nagybetűs
- Adattisztítás szükséges, Numerikus feature kiugró értékek szerepelnek (pl. `Recorded_Speed_kmh` **999 km/h**)

## Numerikus oszlopok statisztikái

| Oszlop | Min | Max | Átlag |
|---|---:|---:|---:|
| `Hour` | 0 | 23 | 12,28 |
| `Month` | 1 | 12 | 6,53 |
| `Is_Holiday` | 0 | 1 | 0,03 |
| `Speed_Limit_kmh` | 30 | 120 | 60,89 |
| `Visibility_m` | 66,4 | 15 000 | 6 211,79 |
| `Congestion_Index` | 2,2 | 100 | 61,02 |
| `Driver_Age` | 16 | 85 | 38,04 |
| `Driver_Experience_yrs` | 0 | 49 | 10,47 |
| `Vehicle_Age_yrs` | 0 | 30 | 6,96 |
| `Recorded_Speed_kmh` | 0 | 999 | 51,09 |
| `Baseline_Expected_Response_Time_min` | 3 | 28,5 | 12,27 |
| `Accident_Occurred` | 0 | 1 | 0,33 |
| `Vehicles_Involved` | 0 | 5 | 0,70 |
| `Actual_Response_Time_min` | 0 | 56,6 | 7,32 |
| `Road_Closure_Duration_min` | 0 | 1 772,5 | 62,02 |
