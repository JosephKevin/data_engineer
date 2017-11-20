README

Nearest Stars
Version 3 of the HYG star database contains almost 120,000 stars. You can download it and
find field descriptions here:
https://github.com/astronexus/HYG-Database
1. Write a program called findstars​ to find the set of nearest K stars from the Sun without
	loading the entire dataset into memory. The program should output the Cartesian
	coordinates of the K nearest stars. The coordinates in the database above have an
	origin (0,0,0) at the Earth. Please ignore the distance field in the original database and
	calculate what you need from the coordinates.
	Provide the source code of your program. It can be in any language you want. It should
	be runnable from the command line as:

	```gunzip -c hygdata_v3.csv.gz | <launch your code> k```

   
2. How might your solution change if we wanted to create a findstars service​ that can
	respond quickly to requests for distance from an arbitrary point with no memory
	restrictions, and we want to query it to return the nearest K stars from arbitrary point
	X=(x,y,z) ?
	Describe how you would design your solution. You don’t need implement it, unless the
	temptation is too great.

Assumptions:
	1. The x, y, z coordinates are always decimal numbers and not empty
	2. The x, y, z coordinates are always on the 17, 18, 19 indexes of the input file and star name field in at index 6
	3. The suns name is 'Sol' reference: ```http://earthsky.org/space/what-is-the-suns-name```
	4. The input file always has field names in the first line
	5. The second line in the file is always the sun's entry
	6. We know that the coordinates of the sun are ```(0.000005, 0.0, 0.0)```