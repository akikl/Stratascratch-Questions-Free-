### Title: 
Salaries Differences
### Question:
Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the absolute difference in salaries.

with eng as ( SELECT max(salary)as engineering from db_employee e inner join db_dept d on e.department_id = d.id  where department='engineering') ,mark as ( SELECT max(salary)as marketing from db_employee e inner join db_dept d on e.department_id = d.id  where department='marketing') select marketing-engineering as salary_difference from eng e join mark m

# Import your libraries import pandas as pd  # Start writing code df=pd.merge(db_employee,db_dept,left_on='department_id',right_on='id') df[df['department']=='marketing']['salary'].max()-df[df['department']=='engineering']['salary'].max()
