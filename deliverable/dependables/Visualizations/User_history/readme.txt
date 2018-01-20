HTML:

user_hist.html


JSON:

user_hist_top_10.json


JSON file contains an array in the following format:

{"user_history": [{"user_id":"CxDOIDnH8gp9KXzpBHJYXw","state":"ON","city":"Whitby","neighborhood":"","latitude":43.8756,"longitude":-78.9596,"address":"939 Dundas Street W","name":"Butchies","date":"2017-07-25 00:00:00"},   }

Python code as developed by Gabriel L. Sammut

The json file returns:
Review history of the top 5 users (based on their total number of reviews)
The business name and location (lat/long/address/city/state) based on the business locations of their submitted reviews
The user details: id and name
Date of review

? selected by some other criteria (to ask Gabriel)

AIM OF VISUALISATION:

Bubble chart over google maps where:

Colour shows unique users

Arrowed lines to show history trail of a particular user


Info Window to show specific details for each user:
Name of user
Name of business / lat / long
Date reviewed


