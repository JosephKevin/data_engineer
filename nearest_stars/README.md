# README


## Nearest Stars
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

## Assumptions:
1. The x, y, z coordinates are always decimal numbers and not empty
2. The x, y, z coordinates are always on the 17, 18, 19 indexes of the input file and star name field in at index 6
3. The suns name is 'Sol' reference: ```http://earthsky.org/space/what-is-the-suns-name```
4. The input file always has field names in the first line
5. The second line in the file is always the sun's entry
6. We know that the coordinates of the sun are ```(0.000005, 0.0, 0.0)```
7. Distance is measured by euclidean distance
8. No adversial user, all the parameters to the program are in order and of the correct type
9. Argument k is an integer
10. k must be less than or equal to number of stars.

## Solution to question1
1. Stream through the data from stdin (time complexity O(n))
2. As we stream through the data keep a k sized max heap
3. If a new point distance is less than or equal to the max element of the max heap, push the new data distance and pop the maximum element from the max heap (time complexity 2 x O(logk))
4. The max heap contains the k closest points to the sun (space complexity O(k))
5. We keep a has map with {distance, [list of stars at that distance]} for a convenient print method
	***Total Time Complexity: O(nlogk)
	Total Space Complexity: O(k)***

### Run Instructions: 
***Input parameters:*** 
	* k: the number of nearest neighbors to be found
1. clone the git repo
2. CD to the directory ```.../data_engineer/nearest_star/```  
3. Run the command ```gunzip -c hygdata_v3.csv.gz | python k_nearest_stars.py 10``` to get 10 nearest neighbors.
   Check the q1.png image for runtime metrics.

## Solution to question2
To create a findstars service with quick response time. We must  do the pre processing of data before hand and only run a quick lookup against the preprocessed data for a query. A suitable data structure to store spatial data for small dimensions(dimensions< 20) for quick lookup is kd-tree. 
1. Construct a kd tree from the stars data. ***Time complexity: O(nlogn)***
2. Store the processed data in the disk.
3. Start a micro service to serve query request and keep the processed in memory for quick access. ***Space complexity: O(n)***
4. Respond to a query for k nearest neighbors quickly. ***Time complexity: O(logn)***

### Run Instructions:
Steps 1 and 2 can be skipped if already performed question1
***Input parameters:*** 
	* k: the number of nearest neighbors to be found
	* x: the x coordinate of the query point
	* y: the y coordinate of the query point
	* z: the z coordinate of the query point
1. clone the git repo
2. CD to the directory ```.../data_engineer/nearest_star/``` 
3. Preprocess the data using the command ```gunzip -c hygdata_v3.c│   74a699d..fb52136  master -> master
sv.gz| python pre_process.py```
4. Query for 10 nearest points with x = 0.000005, y = 0.0, z = 0.0 using the command ```python find_stars.py 10 0.000005 0.0 0.0```

### References:
1. ```http://andrewd.ces.clemson.edu/courses/cpsc805/references/nearest_search.pdf```
2. ```https://en.wikipedia.org/wiki/K-d_tree#Nearest_neighbour_search``` 
3. ```https://www.youtube.com/watch?v=TLxWtXEbtFE``` 

### Other option for question2:
1. Since our dimensions are small kd-tree will be sufficient, but for higher dimensions we can consider another advanced options. ***annoy*** is used to find nearest neighbors in high dimensions, uses kd-tree along with priority queue approach. If we start a micro service and keep the service running with the data in memory we can do quick approximate lookups.
	* pros: 
		* easy to use and widely addopted
		* Uses static file (small size) as indexes
		* reasonably accurate (Was tested on the HYG-database and produced correct results)
	* cons: 
		* Not an exact matching algorithm
		* requires preprocessing the data
	* reference:
		* ```https://github.com/spotify/annoy``` 
		* ```https://www.youtube.com/watch?v=QkCCyLW0ehU&t=2447s```
