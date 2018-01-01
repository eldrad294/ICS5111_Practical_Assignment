LOAD DATA LOCAL INFILE 'D:/Projects/ICS5111_Practical_Assignment/data/business_user_sentiment.csv'
INTO TABLE business_user_sentiment
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
commit;

/*
insert into yelp_db.business_user_sentiment
SELECT *,0 FROM yelp_db.business;
commit;
*/
