### Title: 
Spotify ranking list
### Question:
Find how many times each artist appeared on the Spotify ranking list Output the artist name along with the corresponding number of occurrences. Order records by the number of occurrences in descending order.

SELECT artist,COUNT(*) AS n_apperances FROM spotify_worldwide_daily_song_ranking GROUP BY artist ORDER BY n_apperances DESC;

# Import your libraries import pandas as pd  # Start writing code spotify_worldwide_daily_song_ranking['n_occurences']=spotify_worldwide_daily_song_ranking['artist'].value_counts().reset_index()
