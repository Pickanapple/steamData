# Steam data

## Spill på Steam

![Antall spill uten 2025 med trendlinje](visualiseringer/antallSpillUten2025.png)

Her ser vi hvordan antall spill på Steam har utbredt seg siden det begynte. Jeg har fjernet 2025 siden det har nettopp begynt og endrer trenden (generert med numpy). Her er grafen med 2025 inkludert:

![Antall spill med 2025](visualiseringer/antallSpill.png)

Vi kan også se på hvor mange spill ble gitt ut hvert år:

![Hvert år med 2025](visualiseringer/spillHvertÅr.png)
![Hvert år uten 2025](visualiseringer/spillHvertÅrUten2025.png)

## Sjanger og kategori

Det kan også være nyttig å se på hvor hvor mange spill av hver sjanger har blitt kjøpt/gitt ut.

![Sektordiagram sjanger](visualiseringer/sjangereSolgt.png)
![Sjanger solgt](visualiseringer/mestSolgtSjanger.png)
![Sjanger gitt ut](visualiseringer/antallSjanger.png)

![kategorier solgt](visualiseringer/mestSolgtKategori.png)
![kategorier gitt ut](visualiseringer/antallKategorier.png)

## Største spill

Når vi snakker om spill må vi nevne mest kjøpt spill og spillene med høyest spilletall i samme øyeblikk. Her ser vi mange spill som har samme størelse som kommer fra at dataen hadde bare en estimering, og jeg måtte ta en middelverdi. Dette git mindre nøyaktig data, men jeg kan fremdeles vise frem neon resultater.

![mest solgte spill](visualiseringer/mestSolgteSpill.png)

![CCU](visualiseringer/toppCCU.png)
