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
sql_REVIEW_BUSINESS_AND_TEXT = lambda state : 'select business_id, text from yelp_db.review r join yelp_db.business b on b.id = r.business_id where 1=1 and r.useful > 0 and b.state = \'' + str(state) + '\';'
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
                                                                                           "'\"user_sentiment\": ',b.user_sentiment,', '," \
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
                                                                                           "		   review_count, " \
                                                                                           "           user_sentiment " \
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
sql_BUSINESS_CLUSTERING_NEIGHBORHOOD = "select concat( "\
                                                "'{\"business_cnt\":',count(*),', ', "\
                                                "'\"lat\":',avg(latitude), ', ', "\
                                                "'\"lng\":',avg(longitude), ', ' , "\
                                                "'\"neighborhood\": \"',neighborhood, '\", ', "\
                                                "'\"avg_stars\":',avg(stars), ', ' , "\
                                                "'\"min_stars\":',min(stars),', ' , "\
                                                "'\"max_stars\":',max(stars),', ' , "\
                                                "'\"review_cnt\":',sum(review_count), '} ' "\
                                        ")  "\
                                       "from yelp_db.business "\
                                       "where 1=1 "\
                                       "and neighborhood is not null "\
                                       "and neighborhood <> '' "\
                                       "group by neighborhood; "
sql_BUSINESS_CLUSTERING_CITY =  "select concat( " \
                                    "'{\"business_cnt\":',count(*),', ',  " \
                                    "'\"lat\":',avg(latitude), ', ', " \
                                    "'\"lng\":',avg(longitude), ', ' , " \
                                    "'\"city\": \"',city, '\", ', " \
                                    "'\"avg_stars\":',avg(stars), ', ' , " \
                                    "'\"min_stars\":',min(stars),', ' , " \
                                    "'\"max_stars\":',max(stars),', ' , " \
                                    "'\"review_cnt\":',sum(review_count), '} ' " \
                                    ") " \
                                "from yelp_db.business " \
                                "where 1=1 " \
                                "and city is not null " \
                                "and city <> '' " \
                                "group by city;"
sql_BUSINESS_CLUSTERING_STATE = "select concat( " \
                                        "'{\"business_cnt\":',count(*),', ',  " \
                                        "'\"lat\":',avg(latitude), ', ', " \
                                        "'\"lng\":',avg(longitude), ', ' , " \
                                        "'\"state\": \"',state, '\", ', " \
                                        "'\"avg_stars\":',avg(stars), ', ' , " \
                                        "'\"min_stars\":',min(stars),', ' , " \
                                        "'\"max_stars\":',max(stars),', ' , " \
                                        "'\"review_cnt\":',sum(review_count), '} ' " \
                                        ") " \
                                "from yelp_db.business " \
                                "where 1=1 " \
                                "and state is not null " \
                                "and state <> '' " \
                                "group by state;"
sql_BUSINESS_USER_NODES = lambda state, category : "(select concat( " \
                                                    "	   '{\"name\": \"',b.name,'\" ,',  " \
                                                    "	   '\"id\": \"',b.id,'\" ,', " \
                                                    "      '\"rvCnt\": ',b.review_count,' ,', " \
                                                    "      '\"type\": \"','green','\"}' " \
                                                    "      ) " \
                                                    "from yelp_db.review r " \
                                                    "join yelp_db.business b " \
                                                    "on r.business_id = b.id " \
                                                    "join yelp_db.user u " \
                                                    "on r.user_id = u.id " \
                                                    "join yelp_db.category c " \
                                                    "on b.id = c.business_id " \
                                                    "join yelp_db.enhanced_category ec " \
                                                    "on ec.primary_category = c.category " \
                                                    "or ec.secondary_category = c.category " \
                                                    "or ec.tertiary_category = c.category " \
                                                    "where 1=1 " \
                                                    "and b.city = '" + str(state) + "' " \
                                                    "and r.useful > 0 " \
                                                    "and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%" + str(category) + "%' " \
                                                    "group by b.id) " \
                                                    "union " \
                                                    "(select concat( " \
                                                    "	   '{\"name\": \"',u.name,'\" ,', " \
                                                    "	   '\"id\": \"',u.id,'\" ,', " \
                                                    "      '\"rvCnt\": ',u.review_count,' ,', " \
                                                    "      '\"type\": \"','grey','\"}' " \
                                                    "      ) " \
                                                    "from yelp_db.review r " \
                                                    "join yelp_db.business b " \
                                                    "on r.business_id = b.id " \
                                                    "join yelp_db.user u " \
                                                    "on r.user_id = u.id " \
                                                    "join yelp_db.category c " \
                                                    "on b.id = c.business_id " \
                                                    "join yelp_db.enhanced_category ec " \
                                                    "on ec.primary_category = c.category " \
                                                    "or ec.secondary_category = c.category " \
                                                    "or ec.tertiary_category = c.category " \
                                                    "where 1=1 " \
                                                    "and b.city = '" + str(state) + "' " \
                                                    "and r.useful > 0 " \
                                                    "and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%" + str(category) + "%' " \
                                                    "group by u.id); "
sql_BUSINESS_USER_LINKS = lambda state, category : "select b.id as business_id, " \
                                                    "	   u.id as user_id, " \
                                                    "      r.text as review_text " \
                                                    "from yelp_db.review r " \
                                                    "join yelp_db.business b " \
                                                    "on r.business_id = b.id " \
                                                    "join yelp_db.user u " \
                                                    "on r.user_id = u.id " \
                                                    "join yelp_db.category c " \
                                                    "on b.id = c.business_id " \
                                                    "join yelp_db.enhanced_category ec " \
                                                    "on ec.primary_category = c.category " \
                                                    "or ec.secondary_category = c.category " \
                                                    "or ec.tertiary_category = c.category " \
                                                    "where 1=1 " \
                                                    "and b.city = '" + str(state) + "' " \
                                                    "and r.useful > 0 " \
                                                    "and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%" + str(category) + "%' " \
                                                    "group by b.id, u.id; "
sql_REVIEW_TEXT_PER_USER = lambda user_id : "(select text " \
                                            "from yelp_db.review r " \
                                            "where 1=1 " \
                                            "and user_id = '" + str(user_id) + "') " \
                                            "union " \
                                            "(select text " \
                                            "from yelp_db.tip " \
                                            "where 1=1 " \
                                            "and user_id = '" + str(user_id) + "'); "
sql_USER_DATA_MINE = lambda user_id : "select u.id, " \
                                        "	   u.name, " \
                                        "	   avg(latitude) as latitude, " \
                                        "	   avg(longitude) as longitude, " \
                                        "      case " \
                                        "          when avg(b.stars) > 4.0 then \"Upper Class\" " \
                                        "          when avg(b.stars) > 3.0 then \"Medium Class\" " \
                                        "          else \"Lower Class\" " \
                                        "		end " \
                                        "      financial_status, " \
                                        "      max(city) as city, " \
                                        "      case " \
                                        "          when u.useful > u.funny and u.useful > u.cool then \"Useful\" " \
                                        "          when u.funny > u.useful and u.funny > u.cool then \"Funny\" " \
                                         "          else \"Cool\" " \
                                        "	   end personality_trait_dubbed_by_reviewers, " \
                                        "      u.fans, " \
                                        "      u.review_count, " \
                                        "      u.average_stars as review_rating, " \
                                        "      case " \
                                        "	       when compliment_hot > compliment_more " \
                                        "            and compliment_hot > compliment_profile " \
                                        "            and compliment_hot > compliment_cute " \
                                        "            and compliment_hot > compliment_list " \
                                        "            and compliment_hot > compliment_note " \
                                        "            and compliment_hot > compliment_plain " \
                                        "            and compliment_hot > compliment_cool " \
                                        "            and compliment_hot > compliment_funny " \
                                        "             and compliment_hot > compliment_writer " \
                                        "            and compliment_hot > compliment_photos then 'Hot comments' " \
                                        "		   when compliment_more > compliment_hot " \
                                        "            and compliment_more > compliment_profile " \
                                        "            and compliment_more > compliment_cute " \
                                        "            and compliment_more > compliment_list " \
                                        "            and compliment_more > compliment_note " \
                                        "            and compliment_more > compliment_plain " \
                                        "            and compliment_more > compliment_cool " \
                                        "            and compliment_more > compliment_funny " \
                                        "            and compliment_more > compliment_writer " \
                                        "            and compliment_more > compliment_photos then 'More comments' " \
                                        "		   when compliment_profile > compliment_hot " \
                                        "            and compliment_profile > compliment_more " \
                                        "            and compliment_profile > compliment_cute " \
                                        "            and compliment_profile > compliment_list " \
                                        "            and compliment_profile > compliment_note " \
                                        "            and compliment_profile > compliment_plain " \
                                        "            and compliment_profile > compliment_cool " \
                                        "            and compliment_profile > compliment_funny " \
                                        "            and compliment_profile > compliment_writer " \
                                        "            and compliment_profile > compliment_photos then 'Profile related comments' " \
                                        "		   when compliment_cute > compliment_hot " \
                                        "            and compliment_cute > compliment_more " \
                                        "            and compliment_cute > compliment_profile " \
                                        "            and compliment_cute > compliment_list " \
                                        "            and compliment_cute > compliment_note " \
                                        "            and compliment_cute > compliment_plain " \
                                        "            and compliment_cute > compliment_cool " \
                                        "            and compliment_cute > compliment_funny " \
                                        "            and compliment_cute > compliment_writer " \
                                        "            and compliment_cute > compliment_photos then 'Cute comments' " \
                                        "		   when compliment_list > compliment_hot " \
                                        "            and compliment_list > compliment_more " \
                                        "            and compliment_list > compliment_profile " \
                                        "            and compliment_list > compliment_cute " \
                                        "            and compliment_list > compliment_note " \
                                        "            and compliment_list > compliment_plain " \
                                        "            and compliment_list > compliment_cool " \
                                        "            and compliment_list > compliment_funny " \
                                        "            and compliment_list > compliment_writer " \
                                        "            and compliment_list > compliment_photos then 'List comments' " \
                                        "		   when compliment_note > compliment_hot " \
                                        "            and compliment_note > compliment_more " \
                                        "            and compliment_note > compliment_profile " \
                                        "            and compliment_note > compliment_cute " \
                                        "            and compliment_note > compliment_list " \
                                        "            and compliment_note > compliment_plain " \
                                        "            and compliment_note > compliment_cool " \
                                        "            and compliment_note > compliment_funny " \
                                        "            and compliment_note > compliment_writer " \
                                        "            and compliment_note > compliment_photos then 'Notice comments' " \
                                        "		   when compliment_plain > compliment_hot " \
                                        "            and compliment_plain > compliment_more " \
                                        "            and compliment_plain > compliment_profile " \
                                        "            and compliment_plain > compliment_cute " \
                                        "            and compliment_plain > compliment_list " \
                                        "            and compliment_plain > compliment_note " \
                                        "            and compliment_plain > compliment_cool " \
                                        "            and compliment_plain > compliment_funny " \
                                        "            and compliment_plain > compliment_writer " \
                                        "            and compliment_plain > compliment_photos then 'Plain / Straight to the point comments' " \
                                        "		   when compliment_cool > compliment_hot " \
                                        "            and compliment_cool > compliment_more " \
                                        "            and compliment_cool > compliment_profile " \
                                        "            and compliment_cool > compliment_cute " \
                                        "            and compliment_cool > compliment_list " \
                                        "            and compliment_cool > compliment_note " \
                                        "            and compliment_cool > compliment_plain " \
                                        "            and compliment_cool > compliment_funny " \
                                        "            and compliment_cool > compliment_writer " \
                                        "            and compliment_cool > compliment_photos then 'Cool comments' " \
                                        "		   when compliment_funny > compliment_hot " \
                                        "            and compliment_funny > compliment_more " \
                                        "            and compliment_funny > compliment_profile " \
                                        "            and compliment_funny > compliment_cute " \
                                        "            and compliment_funny > compliment_list " \
                                        "            and compliment_funny > compliment_note " \
                                        "            and compliment_funny > compliment_plain " \
                                        "            and compliment_funny > compliment_cool " \
                                        "            and compliment_funny > compliment_writer " \
                                        "            and compliment_funny > compliment_photos then 'Funny comments' " \
                                        "		   when compliment_writer > compliment_hot " \
                                        "            and compliment_writer > compliment_more " \
                                        "            and compliment_writer > compliment_profile " \
                                        "            and compliment_writer > compliment_cute " \
                                        "            and compliment_writer > compliment_list " \
                                        "            and compliment_writer > compliment_note " \
                                        "            and compliment_writer > compliment_plain " \
                                        "            and compliment_writer > compliment_cool " \
                                        "            and compliment_writer > compliment_funny " \
                                        "            and compliment_writer > compliment_photos then 'Well written comments' " \
                                        "          else 'Photos' " \
                                        "		end trending_compliments " \
                                        "from yelp_db.review r " \
                                        "join yelp_db.business b " \
                                        "on r.business_id = b.id " \
                                        "join " \
                                        "(select id, " \
                                        "	   name, " \
                                        "	   useful, " \
                                        "	   funny, " \
                                        "      cool, " \
                                        "      fans, " \
                                        "      review_count, " \
                                        "      average_stars, " \
                                        "      compliment_hot, " \
                                        "      compliment_more, " \
                                        "      compliment_profile, " \
                                        "      compliment_cute, " \
                                        "      compliment_list, " \
                                        "      compliment_note, " \
                                        "      compliment_plain, " \
                                        "      compliment_cool, " \
                                        "      compliment_funny, " \
                                        "      compliment_writer, " \
                                        "      compliment_photos " \
                                        "from yelp_db.user u " \
                                        "where u.id = '" + str(user_id) + "' " \
                                        ") u " \
                                        "on r.user_id = u.id " \
                                        "where 1=1 " \
                                        "and r.user_id = '" + str(user_id) + "' " \
                                        "and b.state = ( " \
                                        "	SELECT  b.state " \
                                        "	FROM yelp_db.review r " \
                                        "	join yelp_db.business b " \
                                        "	on r.business_id = b.id " \
                                        "	where 1=1 " \
                                        "	and r.user_id = '" + str(user_id) + "' " \
                                        "	group by b.state " \
                                        "	order by count(r.text) desc " \
                                        "	limit 1 " \
                                        ");"
sql_USER_HISTORY = lambda user_id : "select un.user_id, " \
                                    "	   b.state, " \
                                    "	   b.city, " \
                                    "       b.neighborhood, " \
                                    "       b.latitude, " \
                                    "       b.longitude, " \
                                    "       b.address, " \
                                    "       b.name, " \
                                    "       un.date " \
                                    "from ( " \
                                    "	(SELECT t.user_id as user_id, " \
                                    "			t.business_id as business_id, " \
                                    "			t.text as text, " \
                                    "			t.date as date " \
                                    "	FROM yelp_db.tip t " \
                                    "	where user_id = '" + str(user_id) + "') " \
                                    "	union " \
                                    "	(select r.user_id as user_id, " \
                                    "			r.business_id as business_id, " \
                                    "			r.text as text, " \
                                    "			r.date as date " \
                                    "	from yelp_db.review r " \
                                    "	where user_id = '" + str(user_id) + "')) un " \
                                    "join yelp_db.business b " \
                                    "on b.id = un.business_id " \
                                    "order by date desc;"
sql_RETRIEVE_TOP_N_USERS = lambda N : "select uni.user_id " \
                                        "from ( " \
                                        "	(select count(*) as rev_count, " \
                                        "		   r.user_id as user_id " \
                                        "	from yelp_db.review r " \
                                        "   group by user_id) " \
                                        "	union " \
                                        "	(select count(*) as rev_count, " \
                                        "		   t.user_id as user_id " \
                                        "	from yelp_db.tip t " \
                                        "   group by user_id) " \
                                        ") uni " \
                                        "group by uni.user_id " \
                                        "order by sum(uni.rev_count) desc " \
                                        "limit " + str(N) + ";"