import pandas as pd 

data = pd.read_csv('student.csv')
print(data)

pd.to_pickle(data, 'save.pkl')
data = pd.read_pickle('save.pkl')
print(data)