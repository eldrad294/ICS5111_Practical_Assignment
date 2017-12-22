/*
The query requires the following inputs:

1) Current Time: (Sunday|10:00)
2) User Location in latitude and longitude: (43.8409, -79.399)
3) Business Category: (Food)
4) Top N retrievals for limit stopkey (100)

The query returns top N results for closest businesses to the user,
based on the suggested business category
*/
select concat(
		   '{"id": "',b.id,'", ',
		   '"name": "',b.name,'", ',
		   '"distance": ',b.haversine_distance,', ',
		   '"latitude": ',b.latitude,', ',
		   '"longitude": ',b.longitude,', ',
		   '"address": "',b.address,'", ',
		   '"neighborhood": "',b.neighborhood,'", ',
		   '"stars": ',b.stars,', ',
		   '"reviewcount": ',b.review_count,', ',
           '"user_sentiment": ',b.user_sentiment,', ',
		   '"status": "',
           case
			 when substring(h.hours,1,POSITION('|' IN h.hours)-1) = 'Sunday'
			   and '11:00' between substring(h.hours,POSITION('|' IN h.hours) + 2, 4)
			   and substring(h.hours,POSITION('|' IN h.hours) + 7)
			 then 'Open'
			 else 'Closed'
		   end,'"} '
           )
	from
	(
		select haversine(latitude,longitude,43.8409, -79.3996) as haversine_distance,
			   id,
			   name,
			   latitude,
			   longitude,
			   address,
			   neighborhood,
			   stars,
			   review_count,
               user_sentiment
		from yelp_db.business_user_sentiment
		where 1=1
		and latitude is not null
		and longitude is not null
		and user_sentiment >= 1
	) as b
	join yelp_db.category c
	on b.id = c.business_id
	join yelp_db.enhanced_category ec
	on ec.primary_category = c.category
	or ec.secondary_category = c.category
	or ec.tertiary_category = c.category
	join yelp_db.hours h
	on b.id = h.business_id
	where 1=1
	and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%Food%'
	and substring(h.hours,1,POSITION('|' IN h.hours)-1) = 'Sunday'
	group by b.id
	order by b.haversine_distance
	limit 100;
