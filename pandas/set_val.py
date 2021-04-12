import pandas as pd 
import numpy as np  

dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
print()

df.iloc[2, 2] = 111
print(df)
print()

df['f'] = np.nan
print(df)
print()

df['e'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20210101', periods=6))
print(df)
print()

df['g'] = np.arange(1, 7)
print(df)

