import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=['a','c','e','f','h'], columns=['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,50,np.nan,30,np.nan,10]
df['column4'] = newColumn
result = df
result = df.drop('column1', axis=1)
result = df.drop('a', axis=0)

result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df['column1'].isnull().sum()
result = df[df['column1'].isnull()]['column1']
result = df[df['column1'].notnull()]['column1']

result = df.dropna() # axis = 0 ( Satır )
result = df.dropna(axis=1) # axis = 1 ( Sütun )
result = df.dropna(how= 'any') # 1 adetr bile olsa silinir
result = df.dropna(how= 'all') # komple nan olanlar silinir
result = df.dropna(subset=['column1','column2'], how = 'all') # sütun seçme
result = df.dropna(subset=['column1','column2'], how = 'any')
result = df.dropna(thresh=2) # en az 2 adet veri varsa silme
result = df.dropna(thresh=4) # en az 4 adet veri varsa silme

result = df.fillna( value='Not input')



print(result)
