select concat(
	    '{"business_cnt":',count(*),', ',
		'"lat":',avg(latitude), ', ',
        '"lng":',avg(longitude), ', ' ,
        '"neighborhood": "',neighborhood, '", ',
        '"avg_stars":',avg(stars), ', ' ,
        '"min_stars":',min(stars),', ' ,
        '"max_stars":',max(stars),', ' ,
        '"review_cnt":',sum(review_count), '} '
        )
from yelp_db.business
where 1=1
and neighborhood is not null
and neighborhood <> ''
group by neighborhood;
#
select concat(
	    '{"business_cnt":',count(*),', ',
		'"lat":',avg(latitude), ', ',
        '"lng":',avg(longitude), ', ' ,
        '"city": "',city, '", ',
        '"avg_stars":',avg(stars), ', ' ,
        '"min_stars":',min(stars),', ' ,
        '"max_stars":',max(stars),', ' ,
        '"review_cnt":',sum(review_count), '} '
        )
from yelp_db.business
where 1=1
and city is not null
and city <> ''
group by city;
#
select concat(
	    '{"business_cnt":',count(*),', ',
		'"lat":',avg(latitude), ', ',
        '"lng":',avg(longitude), ', ' ,
        '"state": "',state, '", ',
        '"avg_stars":',avg(stars), ', ' ,
        '"min_stars":',min(stars),', ' ,
        '"max_stars":',max(stars),', ' ,
        '"review_cnt":',sum(review_count), '} '
        )
from yelp_db.business
where 1=1
and state is not null
and state <> ''
group by state;