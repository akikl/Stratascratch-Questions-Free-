### Title: 
Finding Updated Records
### Question:
We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.

SELECT id,first_name,last_name,department_id ,max(salary) FROM  ms_employee_salary GROUP BY id,first_name,last_name,department_id ORDER BY id 

# Import your libraries import pandas as pd  # Start writing code ms_employee_salary['salary']=ms_employee_salary.groupby('id')['salary'].transform('max') ms_employee_salary.drop_duplicates()
