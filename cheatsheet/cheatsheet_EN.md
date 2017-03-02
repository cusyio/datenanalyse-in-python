
# pandas Cheat Sheet

## Getting Started

### import pandas

```python
import pandas as pd
```

### create a Series

```python
s = pd.Series([1, 2, 3], index=['A', 'B', 'C'], name='col1')
```

### create a DataFrame

```python
data = [[1, 4], [2, 5], [3, 6]]
index = ['A', 'B', 'C']
df = pd.DataFrame(data, index=index, columns=['col1', 'col2'])
```

### load a DataFrame

```python
df = pd.read_csv('filename.csv', 
     sep=',', 
     names=['col1', 'col2'], 
     index_col=0, 
     encoding='utf-8',
     nrows=3)
```

## Selecting Rows and Columns

### select single Column

```python
df['col1']
```

### select multiple columns

```python
df[['col1', 'col2']]
```

### show first n rows

```python
df.head(2)
```

### show last n rows

```python
df.tail(2)
```

### select rows by index values

```python
df.ix['A']
df.ix[['A', 'B']]
```

### select rows by position

```python
df.ix[1]
df.ix[1:]
```

## Data Wrangling

### filter by value

```python
df[df['col1'] > 1]
```

### sort by columns

```python
df.sort(['col2', 'col2'], ascending=[False, True])
```

### identify duplicate rows

```python
df.duplicated()
```

### identify unique rows

```python
df['col1'].unique()
```

### swap rows and columns

```python
df = df.transpose()
```

### remove a column

```python
del df['col2']
```

### clone a DataFrame

```python
clone = df.copy()
```

### connect multiple DataFrames vertically

```python
df2 = df + 10
pd.concat([df, df2])
```

## Merge multiple DataFrames horizontally

```python
df3 = pd.DataFrame([[1, 7], [8, 9]], 
	      index=['B', 'D'], 
	      columns=['col1', 'col3'])
```

### only merge complete rows (INNER JOIN)

```python
df.merge(df3)
```

### left column stays complete (LEFT OUTER JOIN)

```python
df.merge(df3, how='left')
```

### right column stays complete (RIGHT OUTER JOIN)

```python
df.merge(df3, how='right')
```
    
### preserve all values (OUTER JOIN)

```python
df.merge(df3, how='outer')
```

### merge rows by index

```python
df.merge(df3, left_index=True, right_index=True
```

### fill NaN values

```python
df.fillna(0.0)
```

### apply your own function

```python
def func(x): return 2**x
df.apply(func)
```

## Arithmetics and Statistics

### add to all values

```python
df + 10
```

### sum over columns

```python
df.sum()
```

### cumulative sum over columns

```python
df.cumsum()
```

### mean over columns

```python
df.mean()
```

### standard devieation over columns

```python
df.std()
```

### count all values that occurr

```python
df['col1'].value_counts()
```

### summarize descriptive statistics

```python
df.describe()
```

## Hierarchical Indexing

### create hierarchical index

```python
df.stack()
```

### dissolve hierarchical index

```python
df.unstack()
```

## Aggregation

### create group object

```python
g = df.groupby('col1')
```

### iterate over groups

```python
for i, group in g:
    print(i, group)
```

### aggregate groups

```python
g.sum()
g.prod()
g.mean()
g.std()
g.describe()
```

### select columns from groups

```python
g['col2'].sum()
g[['col2', 'col3']].sum()
```

### transform values

```python
import math
g.transform(math.log)
```

### apply a list function on each group

```python
def strsum(group):
    return ''.join([str(x) for x in group.values])
g['col2'].apply(strsum)
```

## Data Export

### data as NumPy-Array

```python
df.values
```

### save data as CSV file

```python
df.to_csv('output.csv', sep=",")
```

### format DataFrame as tabular string

```python
df.to_string()
```

### convert DataFrame to a dictionary

```python
df.to_dict()
```

### save DataFrame as Excel-table

```python
df.to_excel('output.xlsx')
```

(requires package `xlwt`)

## Visualization

### import matplotlib

```python
import pylab as plt
```

### start a new diagram

```python
plt.figure()
```

### scatterplot

```python
df.plot.scatter('col1', 'col2', style='ro')
```

### bar plot

```python
df.plot.bar(x='col1', y='col2', width=0.7)
```

### area plot

```python
df.plot.area(stacked=True, alpha=1.0)
```

### box-and-whisker-plot

```python
df.plot.box()
```

### histogram over one column

```python
df['col1'].plot.hist(bins=3)
```

### histogram over all columns

```python
df.plot.hist(bins=3, alpha=0.5)
```

### set tick marks

```python
labels = ['A', 'B', 'C', 'D']
positions = [1.0, 2.0, 3.0, 4.0]
plt.xticks(positions, labels)
plt.yticks(positions, labels)
```

### select area to plot

```python
plt.axis([0.0, 2.5, 0.0, 10.0])
# [from x, to x, from y, to y]
```

### Label diagram and axes

```python
plt.title('Correlation')
plt.xlabel('Nunstück')
plt.ylabel('Slotermeyer')
```

### save most recent diagram

```python
plt.savefig('plot.png')
plt.savefig('plot.png', dpi=300)
plt.savefig('plot.svg')
```
