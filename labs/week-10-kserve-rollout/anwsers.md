## Kérdések

1. - promote:  max_p95_ms and max_error_rate held for 24 hours
   - rollback: max_p95_ms or max_error_rate is exceeded

   a modell késleltetése és a hibaarány tudja triggereli, promote esetben 24 óra után, rollback pedig amint a határértéket túllépi a canary

   a true label, vagyis, hogy mi a valós diagnózis, csak később derül ki, valós orvosi vizsgálat után, ez az infó nem áll rendelkezésre.

2. - 60 paciens kerül a canary-ra, azt láthatjuk rajta, hogy drasztikusan eltérően viselkedik-e.

3. - min_probability_spread = 0.1. V3 esetén 0.2 már nem menne át

    pass  behaviour.not_a_constant           p_pos=0.4751, p_neg=0.2773, min spread 0.1
                                            |---------------------------|
                                                    kb. 0.18 eltérés

4. - Annyi kérés kell ami mellett az expected sampling spread 1% alá esik, és még azután is előfordulhat szerencsétlen esetben, mivel minden kérés gyakorlatilag egy bias-os coin flip.

5. - A model gate FAIL-elt, ezt tartanám meg ha csak egy check maradhatna, mert modell kiértékelésnél sok aspektust vizsgál (pl. fairness) és ez alapján egy GO sokat elárul a modell megbízhatóságáról, persze nem tökéletes, mivel későbbi adatokon elbukhat.

6. - A canary.percent visszaállt 0-ra, így a v1 kapja ismét a teljes forgalmat.

7. - A canary.percent visszaállítani 0-ra (? nem igazán értem, az előadásban ez van említve)

8. - concurrency  16:   168.2 rps, p95   237.29 ms, errors 0.00%  OVER
   - 4 és 16 közötti concurreny-nél lépi át a tűrhető késleltetést a rendszer.