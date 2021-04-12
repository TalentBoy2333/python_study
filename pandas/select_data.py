import pandas as pd 
import numpy as np  

dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
print()

# print(df['a'])
# print(df.a)
# print(df[0:3])
# print(df['2021-01-02': '2021-01-05'])
# print()

# print(df.loc['20210103'])
# print(df.loc['20210103', ['a', 'b']])
# print()

# print(df.iloc[3:5, 1:3])
# print() 

print(df[df.a > 8])