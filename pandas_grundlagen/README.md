
# Einstieg in pandas

![Kurzübersicht zu `pandas`: die meisten Daten in diesem Kurs sind als Tabellen vom Typ pd.DataFrame abgelegt. DataFrames bestehen aus einem Index und mehreren Spalten. Jede Spalte hat den Typ pd.Series](pandas_uebersicht.png)

## Die Arbeitsumgebung zur interaktiven Datenanalyse

### Aufgabe 1

starte die IPython Konsole über Anaconda

### Aufgabe 2

Importiere pandas:

    import pandas as pd

### Aufgabe 3

Lade Daten zur Weltbevölkerung:

    df = pd.read_csv('grosse_laender_2015.csv', index_col=0)

### Aufgabe 4

Probiere die 20 Pandas-Befehle von den Karten aus.

### Aufgabe 5

Gruppiert die Befehle gemeinsam so, wie Ihr es für sinnvoll haltet.
 

## Extras

* Jupyter Notebooks
* Neuerungen in Python 3


### Quelle

Daten zur Verfügung gestellt von [www.gapminder.org](http://www.gapminder.org)