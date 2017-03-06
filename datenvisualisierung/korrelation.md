
# Eine Korrelation plotten

In dieser Aufgabe werden wir den Zusammenhang von Lebenserwartung und Fruchtbarkeit untersuchen. Dazu werden wir einen Scatterplot für das Jahr 2015 anfertigen.

### Schritt 1

Lade die Datei `gapminder_fertility.csv` in pandas.

    import pandas as pd

    lifeexp = pd.read_csv('gapminder_total_fertility.csv', index_col=0)

### Schritt 2

Verfahre genauso mit der Datei `gapminder_lifeexpectancy.xlsx`. Speichere es in einem `DataFrame` mit dem Namen `fertility`.

**Du benötigst dazu die Funktion `pd.read_excel`.**

### Schritt 3

Prüfe ob beide Tabellen die gleiche Größe haben

    print(lifeexp.shape)

**Wenn sie nicht die gleiche Größe haben, ist das nicht schlimm.**

### Schritt 4

Verbinde beide Tabellen mit der Funktion `merge`. Durch die Einstellung `left_index=True, right_index=True` werden Zeilen mit gleichem Index zusammengeführt.

    df = lifeexp.merge(fertility, left_index=True, right_index=True)

### Schritt 5

Zeige die Tabelle an. Finde heraus, wie die Spalten für das Jahr 2015 heißen:

    print(df.columns)

Wähle beide Spalten für ein Jahr aus (**Achtung! Eventuell unterscheiden sie sich im Datentyp**) und schreibe sie in ein neues `DataFrame`.

    df = df[['spalte1', 'spalte2']]

### Schritt 6

Eliminiere Leerzeilen aus der Tabelle mit:

    df = df.dropna()

### Schritt 7

Plotte die beiden Spalten gegeneinander:

    import pylab as plt
    df.plot.scatter('spalte1', 'spalte2', style='ro')
    plt.savefig('korrelation.png')

### Schritt 8

Benenne die Spalten um, so daß das Diagramm sinnvoller beschriftet ist:

    df['Lebenserwartung'] = df['spalte1']
