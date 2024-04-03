### Title: 
Popularity of Hack
### Question:
Meta/Facebook has developed a new programing language called Hack.To measure the popularity of Hack they ran a survey with their employees. The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored. Based on the above, find the average popularity of the Hack per office location. Output the location along with the average popularity.

select e.location,avg(s.popularity) from facebook_employees e JOIN facebook_hack_survey s  ON e.id=s.employee_id GROUP BY e.location ;

# Import your libraries import pandas as pd  # Start writing code df=pd.merge(facebook_employees,facebook_hack_survey,left_on='id',right_on='employee_id',how='inner')  df.groupby('location')['popularity'].mean()
