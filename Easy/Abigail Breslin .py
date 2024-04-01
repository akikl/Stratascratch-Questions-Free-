### Title: 
Abigail Breslin 
### Question:
Count the number of movies that Abigail Breslin nominated for oscar

SELECT COUNT(movie) AS n_movies_by_abi FROM oscar_nominees WHERE nominee LIKE 'Abigail Breslin'

# Import your libraries import pandas as pd  # Start writing code len(oscar_nominees[oscar_nominees['nominee']=='Abigail Breslin'])
