### Title: 
Customer Details
### Question:
Find the details of each customer regardless of whether the customer made an order. Output the customer's first name, last name, and the city along with the order details. You may have duplicate rows in your results due to a customer ordering several of the same items. Sort records based on the customer's first name and the order details in ascending order.

SELECT c.first_name,c.last_name, c.city,o.order_details  FROM customers c LEFT JOIN orders o  ON c.id=o.cust_id ORDER BY c.first_name, o.order_details;

# Import your libraries import pandas as pd  # Start writing code df=pd.merge(orders,customers,left_on='cust_id',right_on='id',how='right') df[['first_name','last_name','city','order_details']].sort_values(     ['first_name','order_details'])
