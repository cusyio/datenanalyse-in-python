
# pandas Cheat Sheet

## Getting Started

### import pandas

    import pandas as pd

### create a Series

    s = pd.Series([1, 2, 3], index=['A', 'B', 'C'], name='col1')

### create a DataFrame

    data = [[1, 4], [2, 5], [3, 6]]
    index = ['A', 'B', 'C']
    df = pd.DataFrame(data, index=index, columns=['col1', 'col2'])

### load a DataFrame

    df = pd.read_csv('filename.csv', 
         sep=',', 
         names=['col1', 'col2'], 
         index_col=0, 
         encoding='utf-8',
         nrows=3)


## Selecting Rows and Columns

### select single Column

    df['col1']

### select multiple columns

    df[['col1', 'col2']]
 
### show first n rows

    df.head(2)

### show last n rows

    df.tail(2)

### select rows by index values

    df.ix['A']
    df.ix[['A', 'B']]

### select rows by position

    df.ix[1]
    df.ix[1:]



## Data Wrangling

### filter by value

    df[df['col1'] > 1]

### sort by columns

    df.sort(['col2', 'col2'], ascending=[False, True])


### identify duplicate rows

    df.duplicated()

### identify unique rows

    df['col1'].unique()

### swap rows and columns

    df = df.transpose()

### remove a column

    del df['col2']

### clone a DataFrame

    clone = df.copy()

### connect multiple DataFrames vertically

    df2 = df + 10
    pd.concat([df, df2])
    

## Merge multiple DataFrames horizontally

    df3 = pd.DataFrame([[1, 7], [8, 9]], 
    	      index=['B', 'D'], 
    	      columns=['col1', 'col3'])

### only merge complete rows (INNER JOIN)

    df.merge(df3)

### left column stays complete (LEFT OUTER JOIN)

    df.merge(df3, how='left')

### right column stays complete (RIGHT OUTER JOIN)

    df.merge(df3, how='right')
    
### preserve all values (OUTER JOIN)

    df.merge(df3, how='outer')

### merge rows by index

    df.merge(df3, left_index=True, right_index=True

### fill NaN values

    df.fillna(0.0)

### apply your own function

    def func(x): return 2**x
    df.apply(func)


## Arithmetics and Statistics

### add to all values

    df + 10

### sum over columns

    df.sum()

### cumulative sum over columns

    df.cumsum()

### mean over columns

    df.mean()

### standard devieation over columns

    df.std()

### count all values that occurr

    df['col1'].value_counts()

### summarize descriptive statistics

    df.describe()


## Hierarchical Indexing

### create hierarchical index

    df.stack()

### dissolve hierarchical index

    df.unstack()



## Aggregation

### create group object

    g = df.groupby('col1')

### iterate over groups

    for i, group in g:
        print(i, group)

### aggregate groups

    g.sum()
    g.prod()
    g.mean()
    g.std()
    g.describe()

### select columns from groups

    g['col2'].sum()
    g[['col2', 'col3']].sum()

### transform values

    import math
    g.transform(math.log)

### apply a list function on each group

    def strsum(group):
        return ''.join([str(x) for x in group.values])
    g['col2'].apply(strsum)


## Data Export

### data as NumPy-Array

    df.values

### save data as CSV file

    df.to_csv('output.csv', sep=",")

### format DataFrame as tabular string

    df.to_string()

### convert DataFrame to a dictionary

    df.to_dict()

### save DataFrame as Excel-table

    df.to_excel('output.xlsx')

(requires package `xlwt`)

## Visualization

### import matplotlib

    import pylab as plt

### start a new diagram

    plt.figure()

### scatterplot

    df.plot.scatter('col1', 'col2', style='ro')

### bar plot

    df.plot.bar(x='col1', y='col2', width=0.7)

### area plot

    df.plot.area(stacked=True, alpha=1.0)

### box-and-whisker-plot

    df.plot.box()

### histogram over one column

    df['col1'].plot.hist(bins=3)

### histogram over all columns

    df.plot.hist(bins=3, alpha=0.5)

### set tick marks

    labels = ['A', 'B', 'C', 'D']
    positions = [1.0, 2.0, 3.0, 4.0]
    plt.xticks(positions, labels)
    plt.yticks(positions, labels)

### select area to plot
    
    plt.axis([0.0, 2.5, 0.0, 10.0])
    # [from x, to x, from y, to y]

### Label diagram and axes

    plt.title('Correlation')
    plt.xlabel('Nunstück')
    plt.ylabel('Slotermeyer')

### save most recent diagram

    plt.savefig('plot.png')
    plt.savefig('plot.png', dpi=300)
    plt.savefig('plot.svg')

