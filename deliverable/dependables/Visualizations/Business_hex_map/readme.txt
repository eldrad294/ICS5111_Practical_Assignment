HTML:

hexmap.html

JSON:

geo.json

(python code by Stephen Abela)


geo.json contains an array of hexbins with centre co-ordinates denoted by lng / lat and a count of businesses contained in each hexbin)

{"0":{"cnt":1.0,"lng":-142.4670002576,"lat":89.9993},"1":{"cnt":1.0,"lng":-122.4350224397,"lat":37.9568717208}


Each hexbin is drawn as a Polygon layer over a google map.

Hexbins are colour coded to represented business density (logarithmic scale) as follows:
White 1 - 9
Lightblue 10 - 99
Blue 100 - 999
Darkblue 1000 +


Python code:



