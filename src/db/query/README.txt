To Execute In Following Order:

------------------------------------------

1) Connect to yelp_db schema as mysql root 
2) Execute script 'BUSINESS_USER_SENTIMENT.sql'
3) Execute script 'Populate business_user_sentiment.sql'. Do not run the commented sql. CSV file can be found under ../data/business_user_sentiment.csv 
4) Execute script 'enhanced_category_table.sql'. CSV file can be found under ../data/yelp-business-categories-list.csv
5) Execute script 'Haversine MySQL Function.sql'.
6) Refresh connection by disconnecting and re-connecting. Verify that the new schema objects have been created/populated.

------------------------------------------