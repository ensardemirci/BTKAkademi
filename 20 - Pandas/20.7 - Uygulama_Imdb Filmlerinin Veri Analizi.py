import pandas as pd

df = pd.read_csv('20 - Pandas/Datasets/imdb.csv')
# 2
result = df.head()
# 3
result = df.head(10)
# 4
result = df.tail()
# 5
result = df.tail(10)
# 6
result = df['Movie_Title']
# 7
result = df['Movie_Title'].head()
# 8
result = df[['Movie_Title','Rating']].head()
# 9
result = df[['Movie_Title','Rating']].tail(7)
# 10
result = df[['Movie_Title','Rating']][5:].head(5)
# 11
result = df[['Movie_Title','Rating']].query('Rating > 8').head(50)
# 12
result = df[['Movie_Title','YR_Released']].query('2014 <= YR_Released <= 2015')
# 13
result = df[['Movie_Title','Rating','Num_Reviews']].query('Num_Reviews > 100000 | 8 <= Rating <= 9 ')

print(result)

