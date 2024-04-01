### Title: 
Police Captains
### Question:
Find the base pay for Police Captains. Output the employee name along with the corresponding base pay.

SELECT employeename,basepay FROM sf_public_salaries WHERE jobtitle LIKE'%Captain%';

# Import your libraries import pandas as pd  # Start writing code sf_public_salaries[sf_public_salaries['jobtitle'].str.contains('CAPTAIN')][['employeename','basepay']]
