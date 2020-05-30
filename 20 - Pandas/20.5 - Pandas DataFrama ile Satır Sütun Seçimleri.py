import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index=['A','B','C'], columns= ['Column1', 'Column2', 'Column3'])
print(df)

result = df['Column1']
result = df[['Column1', 'Column2']]

# loc['row','column'] ==> loc['row'] > loc[':','column']
result = df.loc['A']
print(result)
result = df.loc[:,'Column1']
result = df.loc[:,'Column1':'Column3']
result = df.loc[:,:'Column3']
result = df.loc['A':'C','Column1':'Column3']
result = df.iloc[2]
result = df.loc['A','Column2']
result = df.loc[['A','B'],'Column2']

df['Column4'] = pd.Series(randn(3), ['A','B','C'])
df['Column5'] = df['Column1'] + df['Column3']

result = df.drop('Column5', axis=1)


print(result)
print(df)
