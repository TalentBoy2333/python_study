import pandas as pd 
import numpy as np  

dates = pd.date_range('20210101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['a', 'b', 'c', 'd'])
df.iloc[0, 1] = np.nan 
df.iloc[1, 2] = np.nan 
print(df)
print()

'''
how = 'any' or 'all'
'''
print(df.dropna(axis=0, how='any')) # 丢弃含有 nan 的 axis
print()

print(df.fillna(value=0)) # 填值
print()

print(df.isnull()) # 判断是否有 nan, 返回一个二值表格