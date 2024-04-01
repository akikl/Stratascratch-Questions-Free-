# Bike Last Used Question

## Question:
Find the last time each bike was in use. Output both the bike number and the date-timestamp of the bike's last use (i.e., the date-time the bike was returned). Order the results by bikes that were most recently used.

[Question Link](https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=3)

## MySQL Solution:
```sql
SELECT 
    bike_number,
    MAX(end_time) AS last_used
FROM
    dc_bikeshare_q1_2012
GROUP BY bike_number
ORDER BY last_used DESC;


# Import your libraries
import pandas as pd

# Start writing code
res = dc_bikeshare_q1_2012.groupby('bike_number')['end_time'].max().reset_index()
res.sort_values(by='end_time', ascending=False)
