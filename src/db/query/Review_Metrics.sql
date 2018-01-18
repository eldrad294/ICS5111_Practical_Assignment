--
-- N on reviews distribution per business states
select count(*),
	   b.state
from yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
group by b.state;
--
-- N on tips distribution per state
select count(*),
	   b.state
from yelp_db.tip t
join yelp_db.business b
on t.business_id = b.id
group by b.state;
--
-- N on photo caption distribution per state
select count(*),
	   b.state
from yelp_db.photo p
join yelp_db.business b
on p.business_id = b.id
group by b.state;
--
---------------------------------------------------------------------
--
-- N of primary_category
SELECT count(*),
	   primary_category
FROM yelp_db.enhanced_category
group by primary_category;
--
-- N of secondary_category
SELECT count(*),
	   secondary_category
FROM yelp_db.enhanced_category
group by secondary_category;
--
---------------------------------------------------------------------
--
-- Retrieve review distribution by category
select count(r.id) as review_counts,
	   c.category
from yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
join yelp_db.category c
on b.id = c.business_id
where 1=1
group by c.category;
--
-- Retrieve tip distribution by category
select count(*) as tip_counts,
	   c.category
from yelp_db.tip t
join yelp_db.business b
on t.business_id = b.id
join yelp_db.category c
on b.id = c.business_id
where 1=1
group by c.category;
--
-- Retrieve photo caption distribution by category
select count(*) as category_counts,
	   c.category
from yelp_db.photo p
join yelp_db.business b
on p.business_id = b.id
join yelp_db.category c
on b.id = c.business_id
where 1=1
group by c.category;
--
---------------------------------------------------------------------
--
-- Review metrics types
select sum(useful) as total_useful,
	   max(useful) as max_useful,
       min(useful) as min_useful,
	   sum(funny) as total_funny,
       max(funny) as max_funny,
       min(funny) as min_funny,
       sum(cool) as total_cool,
       max(cool) as max_cool,
       min(cool) as min_cool,
       avg(stars) as avg_stars,
       max(stars) as max_stars,
       min(stars) as min_stars,
       avg(length(text)) as avg_text,
       max(length(text)) as max_text,
       min(length(text)) as min_text
from yelp_db.review;
--
---------------------------------------------------------------------
--
-- Review counts distribution per day over time
select count(*) as rev_count,
	   date
from yelp_db.review
group by date
order by date;
--
-- User tips per day
select count(*) as tips,
	   date
from yelp_db.tip
group by date
order by date;
--
-- User yelping_since signups per day
select count(*) as user_signup,
	   yelping_since
from yelp_db.user
group by yelping_since
order by yelping_since;
--
---------------------------------------------------------------------
--
-- Average review length per star rating
SELECT avg(length(text)),
	   stars
FROM yelp_db.review
group by stars;
--
---------------------------------------------------------------------
--
-- star ratings vs date
SELECT stars,
	   date,
       case
         when useful >= funny and useful >= cool then "useful"
         when funny >= useful and funny >= cool then "funny"
         else "cool"
	   end
from yelp_db.review;