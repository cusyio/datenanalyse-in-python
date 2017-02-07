
import pandas as pd

laender = pd.read_csv('grosse_laender_2015.csv', index_col=0)

# ---- Info für Karten ----

laender.values

# siehe (p.125)
laender.index

df = laender.transpose()

ger = pd.Series([80000000, 1.4], index=['population', 'fertility'])

def anfangsbuchstabe(s): return s[0]
laender['initial'] = laender['continent'].apply(anfangsbuchstabe)

laender.index

laender['continent']

laender['population'] > 200000000

laender[laender['population'] > 200000000]

'Russia' in df

laender['fertility'] * 1.5

laender['population'] + 1000000

laender[['population', 'continent']]

laender.ix[3:7]

# p.143/144
laender.describe()

laender['population'].mean()

laender['population'].sum()

laender.cumsum()

laender.head(3)

laender.tail(3)

laender.shape()

import pylab as plt
laender.plot('population', 'fertility', style='ro')
plt.savefig('pop.png')

laender['continent'].value_counts()

laender.groupby('continent')['population'].sum()

laender.stack()

laender.sort(['continent', 'fertility'])

laender['continent'].unique()

del laender['fertility']
