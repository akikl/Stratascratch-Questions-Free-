### Title: 
Churro Activity Date
### Question:
Find the activity date and the pe_description of facilities with the name 'STREET CHURROS' and with a score of less than 95 points.

SELECT activity_date,pe_description FROM los_angeles_restaurant_health_inspections WHERE facility_name LIKE 'STREET CHURROS' AND score<95;

# Import your libraries import pandas as pd  # Start writing code los_angeles_restaurant_health_inspections[(los_angeles_restaurant_health_inspections['facility_name']=='STREET CHURROS')&(los_angeles_restaurant_health_inspections['score']<95)][['activity_date','pe_description']]
