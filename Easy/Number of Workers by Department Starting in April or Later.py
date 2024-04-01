### Title: 
Number of Workers by Department Starting in April or Later
### Question:
Find the number of workers by department who joined in or after April.  Output the department name along with the corresponding number of workers.  Sort records based on the number of workers in descending order.

SELECT department,COUNT(*)  FROM worker WHERE MONTH(joining_date)>=4 GROUP BY department;

# Import your libraries import pandas as pd  # Start writing code df=worker[worker['joining_date'].dt.month>=4] df.groupby('department')['worker_id'].count().reset_index().sort_values(     'worker_id',ascending=False)
