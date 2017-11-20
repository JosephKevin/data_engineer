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

		And output the coordinates of the nearest stars. You do not need to output the distance.
		You also do not need to implement this with full production level error checking on filesystem,
		program arguments etc. This is just an exercise, assume a non-adversarial user.
	2. How might your solution change if we wanted to create a findstars service​ that can
		respond quickly to requests for distance from an arbitrary point with no memory
		restrictions, and we want to query it to return the nearest K stars from arbitrary point
		X=(x,y,z) ?
		Describe how you would design your solution. You don’t need implement it, unless the
		temptation is too great.