# Steam data

[Lenke til datasettet](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset)

## Om prosjektet

Dette prosjektet var en mulighet å øve på **databehandling** i **Python** og **Jupyter**. Den ga meg muligheter å øve med forskjellige virkemiddler som **Pandas**, **Polars** og å skrive det **manuelt**. Jeg fikk også øving i å skrive **markdown** filer som denne.

## Mappestruktur

- **_games.csv_**: datasettet. Denne bruker [**Github LFS**](https://git-lfs.com/)
- _**pandas.ipynb**_: [**Jupyter Notebook**](https://jupyter.org/) der jeg har brukt **Pandas** til å utforske datasettet. Her finner man også forklaringer til metodene/hvorfor jeg gjorde de forskjellige tingene.
- _**polars.ipynb**_: Det samme, men jeg bruker **Polars**.
- **_manuell.py_**: Her bruker jeg [VScode sin Notebook funksjon](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). I denne filen er det flere _# %%_ kommentarer som er brukt for å dele filen inn i celler. Dette er noe jeg kommer til å bruke mer enn **ipynb** filer i fremtiden siden det er bedre debug muligheter og lettere å dele filene.
- _**polarsVsPandasTime.py**_ er en kort fil som viser tidsforskjellen mellom **Polars** og **Pandas**
- **visualiseringer/** er der jeg har lagret grafene som jeg genererte.
- **resultater.md** Det jeg har funnet ut.

## Metoder i bruk

Jeg brukte 3 forskjellige metoder for å lese dataen: [**Pandas**](https://pandas.pydata.org/), [**Polars**](https://pola.rs/) og **Manuell**. Jeg brukte _**csv**_ formaten for å lese inn dataen siden jeg foretrekker å bruke det. Noen ganger ville jeg bruke _**JSON**_, som for eksempel når jeg skal lagre data (for eksempel i trafikkhusoppgaven i forige prøve), men jeg liker som oftest å leseinn datasettet.

## Hvorfor brukte jeg Polars?  

Pandas er veldig ofte brukt i industrien for å håndtere store datasett, men er ofte kritisert for å være innefektiv. Polars er en mye mer effektiv bibliotek enn Pandas (jeg har lagt til en fil som heter **polarsVsPandasTime.py** for å vise forskjellen):

    Pandas tid: 5.316129446029663
    Polars tid: 0.30678844451904297

    Polars var fortest

### Hvorfor er Polars forterre enn Pandas?

1. Polars er skrevet i [Rust &#x1F980;](https://www.rust-lang.org/) istedetfor i [Python &#x1F40D;](https://www.python.org/). Dette gir den nesten [C++](https://en.wikipedia.org/wiki/C%2B%2B) hastighet mens den kjører i Python.
2. Den bruker en blanding av [lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation) og [eager evaluation](https://www.dremio.com/wiki/eager-evaluation/). Dette betyr at programmet trenger bare håndtere det den trenger istedetfor alt i en gang. Siden jeg ikke har satt meg veldig inn i det ennå kan Polars effektiviseres, og kan dermed bli ennå fortere enn det jeg har skrevet nå.
