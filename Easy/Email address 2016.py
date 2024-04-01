### Title: 
Email address 2016
### Question:
Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email. Output the library code.

SELECT DISTINCT home_library_code FROM library_usage WHERE circulation_active_year=2016 AND provided_email_address= 'FALSE' AND notice_preference_definition='email' ;

# Import your libraries import pandas as pd  # Start writing code library_usage[(library_usage['circulation_active_year']==2016)&(library_usage['provided_email_address']==False)&(library_usage['notice_preference_definition']=='email')][['home_library_code']].drop_duplicates()
