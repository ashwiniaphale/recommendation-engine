import pandas as pd 

userInput = input("Please enter a movie and its year to see the reccomendations! ")

rating_df = pd.read_csv("ratings_copy1.csv")
#print(rating_df.head(50))

movie_df = pd.read_csv("movies_copy1.csv")
#print(movie_df.head(50))

joined_df = rating_df.merge(movie_df, on = "movieId", how="left")
#print(joined_df.head(20))

avg_rating  = pd.DataFrame(joined_df.groupby('title')['rating'].mean())
#print(avg_rating.head(20))

avg_rating['total ratings'] = pd.DataFrame(joined_df.groupby('title')['rating'].count())
#print(avg_rating.head(10))

movieTable = joined_df.pivot_table(index='userId', columns='title', values='rating')
#print(movieTable.head(30))

correlations = movieTable.corrwith(movieTable[userInput])
#print(correlations.head(10))

rec  = pd.DataFrame(correlations, columns=["Correlation"])
rec.dropna(inplace=True)
rec = rec.join(avg_rating['total ratings'])
#print(rec.head(5))

r = rec[rec['total ratings']> 100].sort_values('Correlation', ascending = False).reset_index()
print(r.head(6))

