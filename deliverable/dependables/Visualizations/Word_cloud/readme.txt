HTML

word_cloud.html

requires: d3cloud.js (// Word cloud layout by Jason Davies, http://www.jasondavies.com/word-cloud/)

data.csv file containing a list of words, sentiment and count (normalised to range 10 - 100) 
format as follows:

password,category,size
also,neu,80
always,neu,40
asked,neu,10
available,neu,10
back,neu,100
best,pos,50
better,pos,40
chinese,neu,20
come,neu,50

The csv file returns the top ____ words after counting all of the first 2 words in all reviews (to confirm ask Gabriel)
Each word is categorised according to its associated sentiment.

AIM OF VISUALISATION

The word cloud will provide a visual impression of the commonest positive words featured in the yelp reviews.

NB. while providing a great visual effect, word clouds are not considered very scientific.








