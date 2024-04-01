### Title: 
Number Of Bathrooms And Bedrooms
### Question:
Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.

SELECT city,property_type, AVG(bathrooms) ,AVG(bedrooms) FROM airbnb_search_details GROUP BY city,property_type;

# Import your libraries import pandas as pd  # Start writing code airbnb_search_details.groupby(['city','property_type'])[['bedrooms','bathrooms']].mean().reset_index()
