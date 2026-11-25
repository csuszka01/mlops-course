## Feladatok

1. - Sima age helyett bin-eket használnék, amiből ugyanúgy lehet eloszlást csinálni, és nem lesz ~100 cardinalitás

2. - p95 értékek átlaga nem ugyanaz mint az összes mért érték p95-je

    histogram_quantile(
        0.95,
        sum by (le) (rate(http_request_duration_seconds_bucket{job="diabetes-api"}[5m]))
    )

    - először bucketekbe kell szervezni, majd onnan leolvasni. Így lesz leolvasható a helyes p95 latency

3. - Nem fogadnám el, 99.9% availability mellett 43 perc kiesés tartozik havonta 99%-nál ez 7h12m. Egy egy órás leállás elvinné az egész havi büdzsét.