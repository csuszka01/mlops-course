## 1

1. - promote:  max_p95_ms and max_error_rate held for 24 hours
   - rollback: max_p95_ms or max_error_rate is exceeded

   a modell késleltetése és a hibaarány tudja triggereli, promote esetben 24 óra után, rollback pedig amint a határértéket túllépi a canary

   a true label, vagyis, hogy mi a valós diagnózis, csak később derül ki, valós orvosi vizsgálat után, ez az infó nem áll rendelkezésre.

2. - 60 paciens kerül a canary-ra, azt láthatjuk rajta, hogy drasztikusan eltérően viselkedik-e.

3. - min_probability_spread = 0.1. V3 esetén 0.2 már nem menne át

    pass  behaviour.not_a_constant           p_pos=0.4751, p_neg=0.2773, min spread 0.1
                                            |---------------------------|
                                                    kb. 0.18 eltérés
## 2

