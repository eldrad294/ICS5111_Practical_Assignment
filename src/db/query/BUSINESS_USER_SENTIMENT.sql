DROP TABLE IF EXISTS business_user_sentiment;
/*
Creates a business table replica, and adds a 
new vector column to represent user sentiment, 
defaulting to 0. 

Sentiment of values are considered as follows:
1) ∞ < x < -10    : Neg
2) -10 <= x <= 10 : Neu
3) 10 < x < ∞	  : Pos
*/
CREATE TABLE `business_user_sentiment` (
  `id` varchar(22) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `neighborhood` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `postal_code` varchar(255) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `stars` float DEFAULT NULL,
  `review_count` int(11) DEFAULT NULL,
  `is_open` tinyint(4) DEFAULT NULL,
  `user_sentiment` int(11) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
