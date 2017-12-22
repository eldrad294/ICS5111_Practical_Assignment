#Nodes
select b.name,
       b.type
from(
  select
         name,
         "green" as type
  from yelp_db.business
) b
union
select u.name,
       u.type
from(
  select
		name,
        "color" as type
  from yelp_db.user
) u;
# Links
SELECT b.name,
       u.name
FROM yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
join yelp_db.user u
on r.user_id = u.id;