### 1.

- Minden push után futtatja az összes lab összes tesztjét, amit a starter folderben talál a lab/-/starter alatt

### 5.

1. - CI-ra a fejlesztő vár, a CT a háttérben fut le. A CI a kód review után van jóváhagyva, a CT-t a gate ellenőrzi.

2. - A modell kiadása végső soron emberi döntés, attól még, hogy átment a gate-en, lehet, hogy nem akarjuk azonnal kiadni. Biztos megfelel-e, megéri-e kiadni, mennyivel lett jobb, mint a staging vagy a champion.

3. - Ha túl van terhelve a github akkor kihagyhatja az action-t, vagy az késve fut le.