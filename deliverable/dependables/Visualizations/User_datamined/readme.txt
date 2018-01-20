HTML:

user_datamined.html


JSON:

user_datamined_top_500.json


JSON file contains an array in the following format:

{"users": [{"user_id":"CxDOIDnH8gp9KXzpBHJYXw","name":"Jennifer", "latitude":43.77303699833903,"longitude":-79.37240392133796,"financial_status":"Medium Class", "city":"York Regional Municipality", "personality_trait_dubbed_by_reviewers":"Funny","fans":575,"review_count":5778,"review_rating":3.29,"trending_compliments":"Plain / Straight to the point comments","top_20_words":"really,good,like,food,little,even,nice,quite,lunch,would,back,place,great,love,time,order,want,restaurant,though,area,"}, .....   }

Python code as developed by Gabriel L. Sammut

The json file returns:
Top 500 users based on their total number of reviews
An average location (lat/long/city) based on the business locations of their submitted reviews
User details: personality traits, fans, review_count, review_rating, compliments, top_20_words

*** current file has an error "\uuu" in top word - to remove the backslash please


AIM OF VISUALISATION:

Bubble chart over google maps where:
Size of bubble represents number of reviews
Colour shows the financial status of users (Lower=white, Medium=cyan or Higher Class=blue)

Info Window to show specific details for each user:
Name
Averaged lat / long, peak city location
Personality trait
Review counts
Review rating


To modify:

Add legend for color scale (Lower=white, Medium=cyan or Higher Class=blue)
Include part of top_20_words in Info window





