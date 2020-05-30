import pandas as pd

df = pd.read_csv('20 - Pandas/Datasets/nba.csv')


# 1
result = df.head(10)

# 2
result = len(df.index)

# 3
result = df['Salary'].mean()

# 4
result = df['Salary'].max()

# 5
result = df[['Name','Salary']].sort_values('Salary', ascending=False).head(1)

# 6
result = df.query('20 <= Age < 25 ')[['Name','Team','Age']].sort_values('Age', ascending=False)

# 7
result = df.query('Name == "John Holland" ')['Team']

# 8
result = df.pivot_table(columns='Team', values='Salary').mean() # alternatif
result = df.groupby('Team').mean()['Salary']

# 9
result = df['Team'].nunique()

# 10
result = df.groupby('Team')['Name'].nunique() # Alternatif
result = df['Team'].value_counts()

# 11
df.dropna(inplace= True)
result = df['Name'].str.contains('and')
result = df[result]

def str_find(name): #Altrenatif

    if 'and' in name.lower():
        return True
    return False

print(df[df['Name'].apply(str_find)])