DELIMITER $$
DROP FUNCTION IF EXISTS haversine$$
/*
HAVERSINE FORMULA:

Returns the distance in degrees on the Earth 
between two known points of latitude and longitude'
*/
CREATE FUNCTION haversine(
        lat1 FLOAT, lon1 FLOAT,
        lat2 FLOAT, lon2 FLOAT
     ) RETURNS FLOAT
    NO SQL DETERMINISTIC
    COMMENT 'Returns the distance in degrees on the Earth
             between two known points of latitude and longitude'
BEGIN
    RETURN DEGREES(ACOS(
              COS(RADIANS(lat1)) *
              COS(RADIANS(lat2)) *
              COS(RADIANS(lon2) - RADIANS(lon1)) +
              SIN(RADIANS(lat1)) * SIN(RADIANS(lat2))
            )) * 111.45; #We multiply by 111.45 to convert degrees to kilometres.
END$$
 
DELIMITER ;