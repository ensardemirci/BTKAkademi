import pandas as pd

df = pd.read_csv('20 - Pandas/Datasets/youtube-ing.csv')

# 1
# result = df.head(10)

# 2
# result = df[5:].head()

# 3
# result = df.info()
# result = df.columns

# 4
# result = df.drop(['thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed','description'],axis=1)
# result = df.columns

# 5
# result = [df['likes'].mean(),df['dislikes'].mean()]

# 6
# result = df[['likes','dislikes']].head(50)

# 7
# result = df[['title','views']].sort_values('views', ascending=False).head(1)


# 8
# result = df[['title','views']].sort_values('views', ascending=False).tail(1)

# 9
# result = df[['title','views']].sort_values('views', ascending=False).head(10)

# 10
# result = df.groupby('category_id').mean().sort_values('likes')['likes']

# 11
# result = df.groupby('category_id')[['category_id','comment_count']].sum().sort_values('comment_count', ascending=False)

# 12
# result = df.groupby('category_id').count()['video_id'] #Alternatif
# result = df['category_id'].value_counts()


# 13
# df['Yeni'] = df['title'].str.len()
# result = df[['title','Yeni']]


# 14
# df['TagSayi'] = df['tags'].str.split('|').apply(len) #alternetif
# df['TagSayi'] = df['tags'].apply(lambda x: len(x.split('|')))
# result = df[['tags','TagSayi']]

# 15
def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])