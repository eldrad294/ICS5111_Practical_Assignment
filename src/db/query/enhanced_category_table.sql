CREATE TABLE `enhanced_category` (
  `primary_category` varchar(22) NOT NULL,
  `secondary_category` varchar(22) NOT NULL,
  `tertiary_category` varchar(22)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
LOAD DATA LOCAL INFILE 'D:/Projects/ICS5111_Practical_Assignment/data/yelp-business-categories-list.csv'
INTO TABLE enhanced_category
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
commit;