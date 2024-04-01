### Title: 
Average Salaries
### Question:
Compare each employee's salary with the average salary of the corresponding department. Output the department, first name, and salary of employees along with the average salary of that department.

SELECT department,first_name, salary,AVG(salary)OVER(Partition BY department)AS Avg_salary FROM employee

# Import your libraries import pandas as pd  # Start writing code employee['avg_salary']=employee.groupby('department')['salary'].transform('mean') employee[['department','first_name','salary','avg_salary']]
