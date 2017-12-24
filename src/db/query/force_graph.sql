#Nodes
#
select concat(
	   '{"name": "',b.name,'" ,',
	   '"id": "',b.id,'" ,',
       '"rvCnt": ',b.review_count,' ,',
       '"type": "','green','"}'
       )
from yelp_db.business b
join yelp_db.category c
on b.id = c.business_id
join yelp_db.enhanced_category ec
on ec.primary_category = c.category
or ec.secondary_category = c.category
or ec.tertiary_category = c.category
where 1=1
and b.state = 'OH'
and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%Food%'
union
select concat(
	   '{"name": "',u.name,'" ,',
	   '"id": "',u.id,'" ,',
       '"rvCnt": ',u.review_count,' ,',
       '"type": "','grey','"}'
       )
from yelp_db.user u;
#
# Links
SELECT b.id,
       u.id,
       r.text
FROM yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
join yelp_db.category c
on b.id = c.business_id
join yelp_db.enhanced_category ec
on ec.primary_category = c.category
or ec.secondary_category = c.category
or ec.tertiary_category = c.category
join yelp_db.user u
on r.user_id = u.id
where 1=1
and b.state = 'OH'
and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%Food%';