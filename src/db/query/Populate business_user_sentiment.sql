insert into yelp_db.business_user_sentiment
SELECT *,0 FROM yelp_db.business;
commit;