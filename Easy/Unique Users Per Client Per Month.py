### Title: 
Unique Users Per Client Per Month
### Question:
Write a query that returns the number of unique users per client per month

SELECT client_id,Month(time_id) AS month,COUNT(DISTINCT(user_id)) As users_num from fact_events GROUP BY client_id,Month(time_id);

# Import your libraries import pandas as pd  # Start writing code fact_events['month']=fact_events['time_id'].dt.month df=fact_events.groupby(['client_id','month'])['user_id'].nunique()
