### Title: 
Order Details
### Question:
Find order details made by Jill and Eva. Consider the Jill and Eva as first names of customers. Output the order date, details and cost along with the first name. Order records based on the customer id in ascending order.

SELECT first_name,order_date,order_details,total_order_cost FROM customers c INNER JOIN  orders o ON c.id=o.cust_id WHERE first_name IN ('Jill','Eva')  ORDER BY o.cust_id;

# Import your libraries import pandas as pd  # Start writing code df=pd.merge(customers,orders,left_on='id',right_on='cust_id',how='inner') df[(df['first_name']=='Jill')|(df['first_name']=='Eva')][['first_name','order_date','order_details','total_order_cost']]
