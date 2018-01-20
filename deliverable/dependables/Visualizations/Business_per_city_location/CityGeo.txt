HTML

citygeo.html


JSON

city_geo.json

JSON file format as follows

{0{business_cnt1, lat36.09960174560547, lng-115.30699920654297, city 110 Las Vegas, avg_stars5, min_stars5, max_stars5, review_cnt47} ,

Python code as developed by Gabriel L. Sammut

Each record shows a unique city name, its location, the total business counts in that particular city, and the average star rating, min_stars and max_starts and the total number of reviews available for the businesses in the city)

AIM OF VISUALISATION

This representation uses a bubble chart over google maps to show the business density in all cities in the yelp dataset. 
Size of bubble represents business counts for the city

Info window provides details for the particular city
- geolocation (latlong)
- avg_stars
- min_stars
- max_stars
- total number of reviews

Notes
It is to be noted that smaller bubbles may indicate redundant city names  spelling mistakes 
