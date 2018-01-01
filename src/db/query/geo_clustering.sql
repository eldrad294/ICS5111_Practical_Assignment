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
#
#
#
01 Done!
3 Done!
75 Done!
ABE Done!
AL Done!
AZ Done!
BW Done!
BY Done!
C Done!
CA Done!
DE Done!
EDH Done!
ELN Done!
ESX Done!
FAL Done!
FIF Done!
FL Done!
FLN Done!
GLG Done!
HH Done!
HLD Done!
IL Done!
KHL Done!
MLN Done!
NC Done!
NE Done!
NI Done!
NLK Done!
NTH Done!
NV Done!
NY Done!
NYK Done!
OH Done!
ON Done!
PA Done!
PKN Done!
QC Done!
RCC Done!
SC Done!
SCB Done!
SL Done!
ST Done!
STG Done!
TAM Done!
VT Done!
WA Done!
WHT Done!
WI Done!
WLN Done!
XGL Done!
ZET Done!