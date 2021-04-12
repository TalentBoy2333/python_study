import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44])
print(s)
print()

dates = pd.date_range('20210101', periods=6)
print(dates)
print()

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
print()

d = {
    'A': 1,
    'B': pd.Timestamp('20130102'), 
    'C': pd.Series(1, index=list(range(4)), dtype='float32'), 
    'D': np.array([1,2,3,4], dtype='int32'), 
    'E': pd.Categorical(['test', 'train', 'test', 'train']), 
    'F': 'foo'
}
df = pd.DataFrame(d)
print(df)
print()
print(df.dtypes)
print()
print(df.index)
print(df.columns)
print(df.values)
print()
print(df.describe())
print()
print(df.T)
print()
print(df.sort_index(axis=1, ascending=False))
print()
print(df.sort_values(by='E'))
