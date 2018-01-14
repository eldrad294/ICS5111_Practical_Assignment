#Nodes
#
(select concat(
	   '{"name": "',b.name,'" ,',
	   '"id": "',b.id,'" ,',
       '"rvCnt": ',b.review_count,' ,',
       '"type": "','green','"}'
       )
from yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
join yelp_db.user u
on r.user_id = u.id
join yelp_db.category c
on b.id = c.business_id
join yelp_db.enhanced_category ec
on ec.primary_category = c.category
or ec.secondary_category = c.category
or ec.tertiary_category = c.category
where 1=1
and b.city = 'Woodmere'
and r.useful > 0
and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%Food%'
group by b.id)
union
(select concat(
	   '{"name": "',u.name,'" ,',
	   '"id": "',u.id,'" ,',
       '"rvCnt": ',u.review_count,' ,',
       '"type": "','grey','"}'
       )
from yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
join yelp_db.user u
on r.user_id = u.id
join yelp_db.category c
on b.id = c.business_id
join yelp_db.enhanced_category ec
on ec.primary_category = c.category
or ec.secondary_category = c.category
or ec.tertiary_category = c.category
where 1=1
and b.city = 'Woodmere'
and r.useful > 0
and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%Food%'
group by u.id);
#
# Links
select b.id as business_id,
	   u.id as user_id,
       r.text as review_text
from yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
join yelp_db.user u
on r.user_id = u.id
join yelp_db.category c
on b.id = c.business_id
join yelp_db.enhanced_category ec
on ec.primary_category = c.category
or ec.secondary_category = c.category
or ec.tertiary_category = c.category
where 1=1
and b.city = 'Woodmere'
and r.useful > 0
and concat(ec.primary_category, ec.secondary_category, ec.tertiary_category) like '%Food%'
group by b.id, u.id;