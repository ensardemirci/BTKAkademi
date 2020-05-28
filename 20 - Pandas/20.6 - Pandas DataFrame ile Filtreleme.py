import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns= ['Column1','Column2','Column3','Column4','Column5'])

result = df
result = df.columns
result = df.head() # İlk 5 adet kayıt
result = df.head(10)
result = df.tail() # Son 5 veri
result = df.tail(10)
result = df['Column1'].head()
result = df.Column1.head()
result = df[['Column1','Column3']].head()
result = df[5:15][['Column1','Column3']].head()

result = df > 50
result = df[df > 50]
result = df['Column1'] > 50
result = df[df['Column1'] > 50][['Column1','Column2']]
result = df[(df['Column1'] > 50) & (df['Column2'] <= 70)] # Çok kriterli Filtreleme & ( And )
result = df[(df['Column1'] > 50) | (df['Column2'] > 70)] # Çok kriterli Filtreleme | ( Or )
result = df.query('Column1 >= 50 & Column1 %2 == 0')


print(result)
