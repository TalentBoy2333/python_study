import pandas as pd 
import numpy as np  

''' part 1
'''

left = pd.DataFrame(
    {
        'key': ['k0', 'k1', 'k2', 'k3', ], 
        'a': ['a0', 'a1', 'a2', 'a3', ], 
        'b': ['b0', 'b1', 'b2', 'b3', ], 
    }
)

right = pd.DataFrame(
    {
        'key': ['k0', 'k1', 'k2', 'k3', ], 
        'c': ['c0', 'c1', 'c2', 'c3', ], 
        'd': ['d0', 'd1', 'd2', 'd3', ], 
    }
)
print(left)
print(right)

res = pd.merge(left, right, on='key')
print(res)

''' part 2
'''

left = pd.DataFrame(
    {
        'key1': ['k0', 'k0', 'k1', 'k2', ], 
        'key2': ['k0', 'k1', 'k0', 'k1', ], 
        'a': ['a0', 'a1', 'a2', 'a3', ], 
        'b': ['b0', 'b1', 'b2', 'b3', ], 
    }
)

right = pd.DataFrame(
    {
        'key1': ['k0', 'k1', 'k1', 'k2', ], 
        'key2': ['k0', 'k0', 'k0', 'k0', ], 
        'c': ['c0', 'c1', 'c2', 'c3', ], 
        'd': ['d0', 'd1', 'd2', 'd3', ], 
    }
)
print(left)
print(right)

'''
how, ['left', 'right', 'inner', 'outer', ], 默认 inner
'''
res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)

''' part 3
'''
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
print(df2)
print()

# res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
res = pd.merge(df1, df2, on='col1', how='outer', indicator='merge_method')
print(res)

''' part 4 
'''
df1 = pd.DataFrame(
    {
        'a': ['a0', 'a1', 'a2'], 
        'b': ['b0', 'b1', 'b2'], 
    }, 
    index = ['k0', 'k1', 'k2']
)
df2 = pd.DataFrame(
    {
        'c': ['c0', 'c1', 'c2'], 
        'd': ['d0', 'd1', 'd2'], 
    }, 
    index = ['k0', 'k2', 'k3']
)
print(df1)
print(df2)
print()

res = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
print(res)

''' part 5
'''
boys = pd.DataFrame(
    {
        'k': ['k0', 'k1', 'k2'], 
        'age': [1, 2, 3], 
    }
)
girls = pd.DataFrame(
    {
        'k': ['k0', 'k0', 'k3'], 
        'age': [4, 5, 6], 
    }
)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
