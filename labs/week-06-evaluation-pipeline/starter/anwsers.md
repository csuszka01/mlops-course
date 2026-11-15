## 2. Feladat

 1. Missing BMI group volt a legrosszabb, accuracy különbség az aggregálthoz képest 0.2656. Mivel csak 2 minta alapján dolgozott az eval, ezért ez az eredmény nem megbízható.

 2. Nem vonható le konklúzió belőle, mielőtt több sorból számított eredmény nem lesz elérhető.

 3. Minden pozitív nagyobb valószínűségű mint minden negatív (ROC AUC = 1), de egyet sem jelez előre pozitívnak (Recall = 0). Azt lehet levonni, hogy 0.5-ös küszöb rossz hozzá, mert a valószínűségek mind alatta vannak. Az AUC csak a sorrendet nézi, az F1 viszont a küszöbre épül, ezért lehet egyszerre az egyik tökéletes, a másik nulla.

## 4. Feladat

1. A gate nem lehet más stage függősége. Helyette a register és a promote GO verdikt nélkül nem fog lefutni.

2. A NOGO modellek is regisztrálva lennének. Akkor derülhet ki ha valaki futtatja a repro-t és látja, hogy NOGO gate mellett regisztrálva lett a modell.

3. A modell felhasználása dönti el, hogy melyik metrika a fontosabb, nincs univerzálisan jó. Azacceptance.regression.primary_metric pont ehhez köti a pipeline-t, miután kiértékeltük melyik metrika tükrözi legjobban meg a modellünk teljesítményét, itt adjuk meg.

## 5. Feladat

1. A selection rate azt méri, hányat jelzünk pozitívnak, nem azt, hogy helyesen. Az életkorral nő a valódi gyakoriság (40-49: 17/31 pozitív, 21-29: 21/94), így a magasabb jelzési arány részben jogos. A TPR azt nézi, megtaláljuk-e a valódi betegeket egyformán, ezért az a kapu.

2. Az age_band-ben kevés a pozitív, ezért a TPR zajos. Az insulin_missing csoportok nagyobbak, ott megbízhatóbb a gap. Szigorítanám, ha több adat lenne elérhető.

3. Etnikai származás. Az adatgyűjtéskor kellett volna rögzíteni, utólag nem pótolható.