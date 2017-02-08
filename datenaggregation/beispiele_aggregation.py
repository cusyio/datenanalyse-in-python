
from beispiele_gruppen import g1

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
