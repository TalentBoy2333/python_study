import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Series
data = pd.Series(np.random.randn(1000, ), index=np.arange(1000))
data = data.cumsum()

# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('abcd'))
data = data.cumsum()
print(data.head())

''' plot
''' 
# data.plot()
# plt.show()

''' scatter
'''
ax = data.plot.scatter(x='a', y='b', color='DarkBlue', label='Class 1')
data.plot.scatter(x='a', y='c', color='DarkGreen', label='Class 2', ax=ax)
plt.show()