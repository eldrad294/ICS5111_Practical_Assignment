#
# Graph SQLs
sql_BUSINESS_DISTRIBUTION_OVER_STATES = 'select count(state) as cnt, state from yelp_db.business group by state order by cnt desc limit 15;'
sql_BUSINESS_DISTRIBUTION_OVER_STATES_2 = 'select count(state), state from yelp_db.business group by state;'
sql_REVIEW_COUNT_METRICS = 'select review_count from yelp_db.business where is_open = 1 and review_count < 50 order by review_count;'
sql_BUSINESS_RATING_VS_REVIEW_COUNT = 'SELECT stars, review_count from yelp_db.business where is_open = 1;'
sql_PHOTO_CATEGORIZED_BY_LABEL = 'SELECT count(label) as cnt, label FROM yelp_db.photo group by label;'
sql_REVIEWS = lambda year : 'SELECT text FROM yelp_db.review where date like \'' + str(year) + '%\' and stars = 5 LIMIT 100;'
sql_YELP_ELITE_OVER_TIME = 'SELECT count(e.user_id), e.year from yelp_db.elite_years e group by e.year;'
#
# Other SQLs
sql_REVIEW_BUSINESS_AND_TEXT = 'select business_id, text from yelp_db.review where useful > 0;'
sql_UPDATE_BUSINESS =  lambda sentiment_vector, id : 'update yelp_db.business_user_sentiment set user_sentiment = ' + str(sentiment_vector) + ' where id = \'' + str(id) + '\';'
sql_BUSINESS_USER_SENTIMENT = lambda category, coordinates, sentiment_threshold, time, N : "select concat(" \
                                                                                           "'{\"id\": \"',b.id,'\", '," \
                                                                                           "'\"name\": \"',b.name,'\", '," \
                                                                                           "'\"distance\": ',b.haversine_distance,', ',"  \
                                                                                           "'\"latitude\": ',b.latitude,', ',"  \
                                                                                           "'\"longitude\": ',b.longitude,', '," \
                                                                                           "'\"address\": \"',b.address,'\", '," \
                                                                                           "'\"neighborhood\": \"',b.neighborhood,'\", '," \
                                                                                           "'\"stars\": ',b.stars,', '," \
                                                                                           "'\"reviewcount\": ',b.review_count,', '," \
                                                                                           "'\"status\": \"'," \
                                                                                           "         case when substring(h.hours,1,POSITION('|' IN h.hours)-1) = '" + str(time[0]) + "' " \
                                                                                           "           and '" + str(time[1]) + "' between substring(h.hours,POSITION('|' IN h.hours) + 2, 4) " \
                                                                                           "           and substring(h.hours,POSITION('|' IN h.hours) + 7) " \
                                                                                           "         then 'Open' " \
                                                                                           "         else 'Closed' " \
                                                                                           "       end ,'\"} ')" \
                                                                                           "from ( " \
                                                                                           "    select haversine(latitude,longitude," + str(coordinates[0]) + ", " + str(coordinates[1]) + ") as haversine_distance, " \
                                                                                           "		   id, " \
                                                                                           "		   name, " \
                                                                                           "		   latitude, " \
                                                                                           "		   longitude, " \
                                                                                           "		   address, " \
                                                                                           "		   neighborhood, " \
                                                                                           "		   stars, " \
                                                                                           "		   review_count " \
                                                                                           "	from yelp_db.business_user_sentiment " \
                                                                                           "	where 1=1 " \
                                                                                           "	and latitude is not null " \
                                                                                           "	and longitude is not null " \
                                                                                           "	and user_sentiment >= " + str(sentiment_threshold)  + " "\
                                                                                           ") as b " \
                                                                                           "join yelp_db.category c " \
                                                                                           "on b.id = c.business_id " \
                                                                                           "join yelp_db.enhanced_category ec " \
                                                                                           "on ec.primary_category = c.category " \
                                                                                           "or ec.secondary_category = c.category " \
                                                                                           "or ec.tertiary_category = c.category " \
                                                                                           "join yelp_db.hours h " \
                                                                                           "on b.id = h.business_id " \
                                                                                           "where 1=1 " \
                                                                                           "and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%" + str(category) + "%' " \
                                                                                           "and substring(h.hours,1,POSITION('|' IN h.hours)-1) = '" + str(time[0]) + "' " \
                                                                                           "group by b.id " \
                                                                                           "order by b.haversine_distance " \
                                                                                           "limit " + str(N) + "; "