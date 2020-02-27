
# pandas Einführungsübungen

#### 1. bla (★☆☆)

```python
df.values
```

#### 1. bla (★☆☆)

```python
df = df.transpose()
```

#### 1. bla (★☆☆)

```python
ger = pd.Series([80000000, 1.4], index=['population', 'fertility'])
```

#### 1. bla (★☆☆)

```python
def anfangsbuchstabe(s): return s[0]
df['initial'] = df['continent'].apply(anfangsbuchstabe)
```

#### 1. bla (★☆☆)

```python
df.index
```

#### 1. bla (★☆☆)

```python
df['continent']```

#### 1. bla (★☆☆)

```python
df['population'] > 200000000
```

#### 1. bla (★☆☆)

```python
df[df['population'] > 200000000]
```

#### 1. bla (★☆☆)

```python
'Russia' in df
```

#### 1. bla (★☆☆)

```python
df['population'] / 1000000
```

#### 1. bla (★☆☆)

```python
df['population'] + 1000000
```

#### 1. bla (★☆☆)

```python
df[['population', 'continent']]
```

#### 1. bla (★☆☆)

```python
df.loc[3:7]
```

#### 1. bla (★☆☆)

```python
# p.143/144
df.describe()
```

#### 1. bla (★☆☆)

```python
df['population'].mean()
```

#### 1. bla (★☆☆)

```python
df['population'].sum()
```

#### 1. bla (★☆☆)

```python
df.cumsum()
```

#### 1. bla (★☆☆)

```python
df.head(3)
```

#### 1. bla (★☆☆)

```python
df.tail(3)
```

#### 1. bla (★☆☆)

```python
df.shape
```

#### 1. bla (★☆☆)

```python
import pylab as plt
df.plot('population', 'fertility', style='ro')
plt.savefig('pop.png')
```

#### 1. bla (★☆☆)

```python
df['continent'].value_counts()
```

#### 1. bla (★☆☆)

```python
df.groupby('continent')['population'].sum()
```

#### 1. bla (★☆☆)

```python
df.stack()
```

#### 1. bla (★☆☆)

```python
df.sort_values(['continent', 'fertility'])
```

#### 1. bla (★☆☆)

```python
df['continent'].unique()
```

#### 1. bla (★☆☆)

```python
del df['fertility']
