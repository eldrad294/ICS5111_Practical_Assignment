/*
Estimating the latitude / longitude of where a user lives,
based on the assumption that the highest trending state
with respect to review count is the place of habitat for
a particular user. Taking all businesses for the top
chosen state visited by the user, the longitude and
latitude coordinates are calculated as an estimate of the
user's place of habitat +/- distance error.
*/
select u.id,
	   u.name,
	   avg(latitude) as latitude,
	   avg(longitude) as longitude,
       case
           when avg(b.stars) > 4.5 then "Upper Class"
           when avg(b.stars) > 3.5 then "Medium Class"
           else "Lower Class"
		end
       financial_status,
       max(city) as city,
       case
           when u.useful > u.funny and u.useful > u.cool then "Useful"
           when u.funny > u.useful and u.funny > u.cool then "Funny"
           else "Cool"
	   end personality_trait_dubbed_by_reviewers,
       u.fans,
       u.review_count,
       u.average_stars as review_rating,
       case
	       when compliment_hot > compliment_more
             and compliment_hot > compliment_profile
             and compliment_hot > compliment_cute
             and compliment_hot > compliment_list
             and compliment_hot > compliment_note
             and compliment_hot > compliment_plain
             and compliment_hot > compliment_cool
             and compliment_hot > compliment_funny
             and compliment_hot > compliment_writer
             and compliment_hot > compliment_photos then 'Hot comments'
		   when compliment_more > compliment_hot
             and compliment_more > compliment_profile
             and compliment_more > compliment_cute
             and compliment_more > compliment_list
             and compliment_more > compliment_note
             and compliment_more > compliment_plain
             and compliment_more > compliment_cool
             and compliment_more > compliment_funny
             and compliment_more > compliment_writer
             and compliment_more > compliment_photos then 'More comments'
		   when compliment_profile > compliment_hot
             and compliment_profile > compliment_more
             and compliment_profile > compliment_cute
             and compliment_profile > compliment_list
             and compliment_profile > compliment_note
             and compliment_profile > compliment_plain
             and compliment_profile > compliment_cool
             and compliment_profile > compliment_funny
             and compliment_profile > compliment_writer
             and compliment_profile > compliment_photos then 'Profile related comments'
		   when compliment_cute > compliment_hot
             and compliment_cute > compliment_more
             and compliment_cute > compliment_profile
             and compliment_cute > compliment_list
             and compliment_cute > compliment_note
             and compliment_cute > compliment_plain
             and compliment_cute > compliment_cool
             and compliment_cute > compliment_funny
             and compliment_cute > compliment_writer
             and compliment_cute > compliment_photos then 'Cute comments'
		   when compliment_list > compliment_hot
             and compliment_list > compliment_more
             and compliment_list > compliment_profile
             and compliment_list > compliment_cute
             and compliment_list > compliment_note
             and compliment_list > compliment_plain
             and compliment_list > compliment_cool
             and compliment_list > compliment_funny
             and compliment_list > compliment_writer
             and compliment_list > compliment_photos then 'List comments'
		   when compliment_note > compliment_hot
             and compliment_note > compliment_more
             and compliment_note > compliment_profile
             and compliment_note > compliment_cute
             and compliment_note > compliment_list
             and compliment_note > compliment_plain
             and compliment_note > compliment_cool
             and compliment_note > compliment_funny
             and compliment_note > compliment_writer
             and compliment_note > compliment_photos then 'Notice comments'
		   when compliment_plain > compliment_hot
             and compliment_plain > compliment_more
             and compliment_plain > compliment_profile
             and compliment_plain > compliment_cute
             and compliment_plain > compliment_list
             and compliment_plain > compliment_note
             and compliment_plain > compliment_cool
             and compliment_plain > compliment_funny
             and compliment_plain > compliment_writer
             and compliment_plain > compliment_photos then 'Plain / Straight to the point comments'
		   when compliment_cool > compliment_hot
             and compliment_cool > compliment_more
             and compliment_cool > compliment_profile
             and compliment_cool > compliment_cute
             and compliment_cool > compliment_list
             and compliment_cool > compliment_note
             and compliment_cool > compliment_plain
             and compliment_cool > compliment_funny
             and compliment_cool > compliment_writer
             and compliment_cool > compliment_photos then 'Cool comments'
		   when compliment_funny > compliment_hot
             and compliment_funny > compliment_more
             and compliment_funny > compliment_profile
             and compliment_funny > compliment_cute
             and compliment_funny > compliment_list
             and compliment_funny > compliment_note
             and compliment_funny > compliment_plain
             and compliment_funny > compliment_cool
             and compliment_funny > compliment_writer
             and compliment_funny > compliment_photos then 'Funny comments'
		   when compliment_writer > compliment_hot
             and compliment_writer > compliment_more
             and compliment_writer > compliment_profile
             and compliment_writer > compliment_cute
             and compliment_writer > compliment_list
             and compliment_writer > compliment_note
             and compliment_writer > compliment_plain
             and compliment_writer > compliment_cool
             and compliment_writer > compliment_funny
             and compliment_writer > compliment_photos then 'Well written comments'
           else 'Photos'
		end trending_compliments
from yelp_db.review r
join yelp_db.business b
on r.business_id = b.id
join
(select id,
	   name,
	   useful,
	   funny,
       cool,
       fans,
       review_count,
       average_stars,
       compliment_hot,
       compliment_more,
       compliment_profile,
       compliment_cute,
       compliment_list,
       compliment_note,
       compliment_plain,
       compliment_cool,
       compliment_funny,
       compliment_writer,
       compliment_photos
from yelp_db.user u
where u.id = '8RcEwGrFIgkt9WQ35E6SnQ'
) u
on r.user_id = u.id
where 1=1
and r.user_id = '8RcEwGrFIgkt9WQ35E6SnQ'
and b.state = (
	SELECT  b.state
	FROM yelp_db.review r
	join yelp_db.business b
	on r.business_id = b.id
	where 1=1
	and r.user_id = '8RcEwGrFIgkt9WQ35E6SnQ'
	group by b.state
	order by count(r.text) desc
	limit 1
);
#
/*
Retrieve a history of where a user has been,
through reviews and tips left by the user at
different business locations.
*/
select un.user_id,
	   b.state,
	   b.city,
       b.neighborhood,
       b.latitude,
       b.longitude,
       b.address,
       b.name,
       un.date
from (
	(SELECT t.user_id as user_id,
			t.business_id as business_id,
			t.text as text,
			t.date as date
	FROM yelp_db.tip t
	where user_id = '8RcEwGrFIgkt9WQ35E6SnQ')
	union
	(select r.user_id as user_id,
			r.business_id as business_id,
			r.text as text,
			r.date as date
	from yelp_db.review r
	where user_id = '8RcEwGrFIgkt9WQ35E6SnQ')) un
join yelp_db.business b
on b.id = un.business_id
order by date desc;
#
/*
Retrieves top 500 users based on highest amount
of reviews and/or tips
*/
select uni.user_id
from (
	(select count(*) as rev_count,
		   r.user_id as user_id
	from yelp_db.review r
    group by user_id)
	union
	(select count(*) as rev_count,
		   t.user_id as user_id
	from yelp_db.tip t
    group by user_id)
) uni
group by uni.user_id
order by sum(uni.rev_count) desc
limit 500;
