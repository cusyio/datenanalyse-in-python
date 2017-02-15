
import pandas as pd
import pylab as plt

pop = pd.read_excel('gapminder_population.xlsx', index_col=0)

cc = pd.read_csv('country_codes.csv', index_col=0)
cc = cc[['region', 'sub-region']]

pop = pd.merge(pop, cc, left_index=True, right_index=True, how='left')


continent = pop.groupby('region').sum()

ctrans = continent.transpose()
ctrans = ctrans / 1000000

ctrans.plot.area()
plt.xlabel('Jahr')
plt.ylabel('Bevölkerung [Mio.]')
plt.savefig('hist.png')
plt.savefig('hist.svg')

cdiff = ctrans.diff()
# cdiff.ix[cdiff.index[:16]] = cdiff.ix[cdiff.index[:16]] / 10
# cdiff.plot.area(stacked=False)

cdiff.ix[cdiff.index[16:]].plot.area(stacked=False)
plt.ylabel('Bevölkerungswachstum [Mio/Jahr]')
plt.xlabel('Jahr')
plt.savefig('diff.png')
plt.savefig('diff.svg')

'''
Sources:

Data from www.gapminder.org/data

Country codes from https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes
'''
