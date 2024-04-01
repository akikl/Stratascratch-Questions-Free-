### Title: 
MacBookPro users
### Question:
Count the number of user events performed by MacBookPro users. Output the result along with the event name. Sort the result based on the event count in the descending order.

SELECT event_name,COUNT(*) AS event_count FROM playbook_events WHERE device='macbook pro' GROUP BY event_name ORDER BY event_count DESC;

# Import your libraries import pandas as pd  # Start writing code df=playbook_events[playbook_events['device']=='macbook pro'] df['event_count']=df.groupby('event_name')['user_id'].count()
