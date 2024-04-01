### Title: 
Most profitable company
### Question:
Find the most profitable company from the financial sector. Output the result along with the continent.

select company,continent  from forbes_global_2010_2014 WHERE forbes_global_2010_2014.rank=1 ;

# Import your libraries import pandas as pd  # Start writing code forbes_global_2010_2014[(forbes_global_2010_2014['sector']=='Financials') &(forbes_global_2010_2014['rank']==1)][['company','continent']]
