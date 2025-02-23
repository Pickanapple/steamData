# %%
import csv
import matplotlib.pyplot as plt
import numpy as np
import re

csv.field_size_limit(2_147_483_647)

# %%

data = []

with open("games.csv", encoding="utf-8") as f: 
    dataReader = csv.reader(f, delimiter=",")
    
    headers = next(dataReader)

    for i in dataReader:
        dataTemp = {} 
        for j in range(len(i)):
            try: 
                i = float(i)
            except TypeError:
                pass

            dataTemp[headers[j]] = i[j]

        data.append(dataTemp)
# %%
dataWithoutUnplayedGames = [i for i in data if int(i["Peak CCU"]) > 0]

# %%
def estimate_middle_value(numbers):
    if type(numbers) == int:
        return numbers

    numbers = numbers.replace(" - ", " ")
    lower, upper = map(int, numbers.split())
    return (upper + lower) / 2

for i in dataWithoutUnplayedGames: 
    i["Estimated owners middle value"] = estimate_middle_value(i["Estimated owners"])

# %%
dataWithoutUnplayedGames[0]

# %%
genres = {}
genreSales = {}
categories = {}
categorySales = {}

for i in dataWithoutUnplayedGames:
    genresUsed = str(i["Genres"]).strip().split(",")
    categoriesUsed = str(i["Categories"]).strip().split(",")

    for j in genresUsed:
        if j == "nan":
            j = "None"
            
        if j not in genreSales.keys():
            genreSales[j] = i["Estimated owners middle value"]  
        else: 
            genreSales[j] += i["Estimated owners middle value"]

    for j in categoriesUsed:
        if j == "nan":
            j = "None"

        if j not in categorySales.keys():
            categorySales[j] = i["Estimated owners middle value"]  
        else: 
            categorySales[j] += i["Estimated owners middle value"]

for i in data:
    genresUsed = str(i["Genres"]).strip().split(",")
    categoriesUsed = str(i["Categories"]).strip().split(",")

    for j in genresUsed:
        if j == "nan":
            j = "None"

        if j not in genres.keys():
            genres[j] = 1
        else: 
            genres[j] += 1

    for j in categoriesUsed:
        if j == "nan":
            j = "None"

        if j not in categories.keys():
            categories[j] = 1
        else: 
            categories[j] += 1

genres = dict(sorted(genres.items(), key=lambda item: item[1]))
genreSales = dict(sorted(genreSales.items(), key=lambda item: item[1]))
categories = dict(sorted(categories.items(), key=lambda item: item[1]))
categorySales = dict(sorted(categorySales.items(), key=lambda item: item[1]))

print(genres)
print(genreSales)

# %%
plt.barh(genres.keys(), genres.values())
plt.gcf().set_size_inches(15, 8)
plt.title("Antall spill i hver sjanger")
plt.grid()

plt.savefig("visualiseringer/antallSjanger.png")

plt.show()

# %%
plt.barh(genreSales.keys(), genreSales.values())
plt.gcf().set_size_inches(15, 8)
plt.title("Most solgte sjangere")
plt.grid()

plt.savefig("visualiseringer/mestSolgtSjanger.png")

plt.show()

# %%
plt.barh(categories.keys(), categories.values())
plt.gcf().set_size_inches(15, 8)
plt.title("Antall spill i hver kategori")
plt.grid()

plt.savefig("visualiseringer/antallKategorier.png")

plt.show()

# %%
plt.barh(categorySales.keys(), categorySales.values())
plt.gcf().set_size_inches(15, 8)
plt.title("Mest solgte kategorier")
plt.grid()

plt.savefig("visualiseringer/mestSolgtKategori.png")

plt.show()

# %%
plt.title("Sjangerne på Steam fordelt basert på salg")

plt.pie(genreSales.values(), labels=genreSales.keys(), autopct='%1.1f%%')
plt.savefig("visualiseringer/sjangereSolgt")

# %%
top50Spill = sorted(dataWithoutUnplayedGames, key=lambda x: x["Estimated owners middle value"], reverse=True)[:50]

# %%
plt.barh([i["Name"] for i in top50Spill], [i["Estimated owners middle value"] for i in top50Spill])
plt.gcf().set_size_inches(15, 15)
plt.title("Top 50 mest solgte spill")
plt.grid()

plt.savefig("visualiseringer/mestSolgteSpill.png")

plt.show()

# %%
top50StørstCCU = sorted(dataWithoutUnplayedGames, key=lambda x: x["Peak CCU"], reverse=True)[:50]

# %%
plt.barh([i["Name"] for i in top50StørstCCU], [i["Peak CCU"] for i in top50StørstCCU])
plt.gcf().set_size_inches(15, 15)
plt.title("Top 50 høyest CCU")
plt.grid()

plt.savefig("visualiseringer/toppCCU.png")

plt.show()

# %%
steamGamesOverTime = {}

for i in data:
    try: 
        year = int(re.findall("\d{4}", i["Release date"])[0])
    except: 
        continue
    
    if year in steamGamesOverTime.keys(): 
        steamGamesOverTime[year] += 1
    else: 
        steamGamesOverTime[year] = 1
    
steamGamesOverTime = dict(sorted(steamGamesOverTime.items()))
print(steamGamesOverTime)

# %%
plt.plot(steamGamesOverTime.keys(), steamGamesOverTime.values())
plt.title("Antall Steam spill git ut i hvert år")
plt.ylim(bottom=0)

plt.grid()

plt.savefig("visualiseringer/spillHvertÅr.png")

plt.show()

# %%
without2025 = steamGamesOverTime.copy()
without2025.pop(2025)

# %%
plt.plot(without2025.keys(), without2025.values())
plt.title("Antall Steam spill git ut i hvert år uten 2025")

z = np.polyfit(list(without2025.keys()), list(without2025.values()), 1)
p = np.poly1d(z)

plt.plot(without2025.keys(), p(list(without2025.keys())), "r--")
plt.ylim(bottom=0)

plt.grid()

plt.savefig("visualiseringer/spillHvertÅrUten2025.png")

plt.show()

# %%
cumultativeSteamGames = {k: v for k, v in zip(range(list(steamGamesOverTime.keys())[0], list(steamGamesOverTime.keys())[-1] + 1), np.cumsum(list(steamGamesOverTime.values())))}
cumultativeSteamGames

# %%
plt.plot(cumultativeSteamGames.keys(), cumultativeSteamGames.values())
plt.grid()
plt.ylim(bottom = 0)
plt.title("Antall spill på Steam")

plt.savefig("visualiseringer/antallSpill.png")

plt.show()

# %%
without2025CumSum = cumultativeSteamGames.copy()
without2025CumSum.pop(2025)

# %%
plt.plot(without2025CumSum.keys(), without2025CumSum.values())
plt.title("Antall spill på Steam totalt uten 2025")

z = np.polyfit(list(without2025CumSum.keys()), list(without2025CumSum.values()), 1)
p = np.poly1d(z)

plt.plot(without2025CumSum.keys(), p(list(without2025CumSum.keys())), "r--")
plt.ylim(bottom=0)

plt.grid()

plt.savefig("visualiseringer/antallSpillUten2025.png")
# %%
