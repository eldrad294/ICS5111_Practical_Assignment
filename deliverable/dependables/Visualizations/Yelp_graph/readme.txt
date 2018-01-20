HTML:

Graph.html

Graph2.html


JSON:

graph.json file contains two arrays consisting of nodes and links:
Nodes: businesses are type green, Users are type grey
Links: reviews are type red, yellow or blue depending on sentiment, comment text


Python code developed by Gabriel L. Sammut
Selects nodes and links for specific locations (by city / category (to check exactly with Gabriel) )

Force directed Graph (D3js) used to show
Businesses (in green) and Users (in grey) as nodes
Reviews as coloured edge

AIM of Visualisation:

1) Graph.html

To show the number of reviews for a particular business and whether the same user has reviewed other business in the same area or whether it constitutes an isolated review.

? Disconnected business with no links would not have any reviews.


2) Graph2.html

This displays the comments text by users in an html window. It is used to browse along businesses and users to read comments.








