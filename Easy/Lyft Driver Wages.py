### Title: 
Lyft Driver Wages
### Question:
Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD. Output all details related to retrieved records.

SELECT * FROM lyft_drivers WHERE yearly_salary <=30000 OR yearly_salary >=70000

# Import your libraries import pandas as pd  # Start writing code lyft_drivers[(lyft_drivers['yearly_salary']<=30000)|(lyft_drivers['yearly_salary']>=70000)]
