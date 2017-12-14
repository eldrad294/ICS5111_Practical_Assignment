#
# Graph SQLs
sql_BUSINESS_DISTRIBUTION_OVER_STATES = 'select count(state) as cnt, state from yelp_db.business group by state order by cnt desc limit 15;'
sql_BUSINESS_DISTRIBUTION_OVER_STATES_2 = 'select count(state), state from yelp_db.business group by state;'
sql_REVIEW_COUNT_METRICS = 'select review_count from yelp_db.business where is_open = 1 and review_count < 50 order by review_count;'
sql_BUSINESS_RATING_VS_REVIEW_COUNT = 'SELECT stars, review_count from yelp_db.business where is_open = 1;'
sql_PHOTO_CATEGORIZED_BY_LABEL = 'SELECT count(label) as cnt, label FROM yelp_db.photo group by label;'
sql_REVIEWS = 'SELECT text FROM yelp_db.review'
sql_YELP_ELITE_OVER_TIME = 'SELECT count(e.user_id), e.year from yelp_db.elite_years e group by e.year;'
#
# Other SQLs
sql_REVIEW_BUSINESS_AND_TEXT = 'select business_id, text from yelp_db.review limit 1010;'
sql_UPDATE_BUSINESS =  lambda sentiment_vector, id : 'update yelp_db.business_user_sentiment set user_sentiment = ' + str(sentiment_vector) + ' where id = \'' + str(id) + '\';'