### Title: 
Reviews of Hotel Arena
### Question:
Find the number of rows for each review score earned by 'Hotel Arena'. Output the hotel name (which should be 'Hotel Arena'), review score along with the corresponding number of rows with that score for the specified hotel.

SELECT hotel_name,reviewer_score, COUNT(*) FROM hotel_reviews WHERE hotel_name LIKE 'Hotel Arena' GROUP BY  hotel_name,reviewer_score

# Import your libraries import pandas as pd  # Start writing code df=hotel_reviews[hotel_reviews['hotel_name']=='Hotel Arena']  df.groupby(['reviewer_score','hotel_name']).agg(n_reviews=pd.NamedAgg(column='reviewer_score',aggfunc='count')).reset_index()
