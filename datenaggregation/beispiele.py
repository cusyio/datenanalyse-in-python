import pandas as pd
import numpy as np

df = pd.read_csv('grosse_laender_2015.csv', index_col=0)

df['population'] = df['population'] / 1000000)
df['population'] = df['population'].apply(round)

# 1. nach einer Spalte
g1 = df.groupby('continent')

# 2. nach einem Array gleicher Länge
industrialized = np.array([False, True, True, True, False, True, True, False, False, False, True, True])
g2 = df.groupby(industrialized)

# 3. nach einem Dictionary mit Schlüsseln auf den Index
language = {'Bangladesh':'HD', 'Brazil':'PT', 'China':'CN', 'India':'HD', 'Indonesia':'ID', 'Japan':'JP', 'Mexico':'ES', 'Nigeria':'NG', 'Pakistan':'AR', 'Philippines':'PP', 'Russia':'RU', 'United States':'EN'}
g3 = df.groupby(language)

# 4. mit einer Funktion
g4 = df.groupby(len)

# 5. mit einer Liste der obigen
g5 = df.groupby(['continent', language, len])

# 6. entlang der X-Achse gruppieren
g6 = df[['population', 'fertility']].transpose().groupby(len, axis=1)

#---------------------------------------

# Aggregation mit Standardfunktionen
g1.mean()
g1.max()
g1.min()
g1.sum()
g1.count()
g1.std()
g1.median()
g1.quantile(0.9)
g1.describe()

# Aggregation mit Spaltenauswahl
g1['population'].describe()

# Aggregation mit Liste von Funktionen
g1.agg(['count', 'mean', 'std'])
g1.agg([('Summe', 'sum')])

# Eigene Aggregatfunktion definieren
def summe_groesser200(array):
    return sum([x for x in array if x>200])

g1.agg(summe_groesser200)

# Eigene Aggregatfunktion mit Parameter
def summe_groesser(array, threshold):
    return sum([x for x in array if x>threshold])

g1.agg(summe_groesser, threshold=200)

# Iterieren über Gruppen
for name, group in g1:
    print(name)
    print(group)

# Gruppen als Dictionary
dict(list(g1))

# Transformation mit Funktionsname
g1.transform('mean')

# Transformation mit Funktion
g1.transform(len)

# Transformation mit eigener Funktion
def normalisieren(array):
    return array - array.mean()

g1.transform(normalisieren)

# Beliebige Funktion anwenden
def dummy(df):
    return pd.DataFrame([[1,2,3], [4,5,6]])

g1.apply(dummy)
