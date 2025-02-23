import pandas as pd
import polars as pl
import time

startPandas = time.time()
pd.read_csv("games.csv")
endPandas = time.time()

startPolars = time.time()
pl.scan_csv("games.csv").collect()
endPolars = time.time()

pandasTime = endPandas - startPandas
polarsTime = endPolars - startPolars

print(f"Pandas tid: {pandasTime}\nPolars tid: {endPolars - startPolars}\n\n{"Pandas" if polarsTime > pandasTime else "Polars" if pandasTime > polarsTime else "Ingen"} var fortest")