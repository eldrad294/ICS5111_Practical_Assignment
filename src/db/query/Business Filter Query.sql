/*
Filter closest businesses,
based on suggested business
categories.
*/
select b.id,
	   b.name, 
       b.haversine_distance
from 
(
	select haversine(latitude,longitude,43.8409, -79.3996) as haversine_distance, 
		   id, 
           name
	from yelp_db.business_user_sentiment
    where 1=1 
    and latitude is not null
    and longitude is not null
    and user_sentiment > 10
) as b
join yelp_db.category c
on b.id = c.business_id
where 1=1
and c.category = 'Food'
order by b.haversine_distance
limit 10;