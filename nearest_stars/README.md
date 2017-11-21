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

##Solution to question1
1. Stream through the data from stdin (time complexity O(n))
2. As we stream through the data keep a k sized max heap
3. If a new point distance is less than or equal to the max element of the max heap, push the new data distance and pop the maximum element from the max heap (time complexity 2 x O(logk))
4. The max heap contains the k closest points to the sun (space complexity O(k))
5. We keep a has map with {distance, [list of stars at that distance]} for a convenient print method
	***Total Time Complexity: O(nlogk)
	Total Space Complexity: O(k)***
6. Run Instructions: Input parameters: k: the number of nearest neighbors to be found
	1. clone the git repo
	2. CD to the directory ```.../data_engineer/nearest_star/```  
	3. Run the command ```gunzip -c hygdata_v3.csv.gz | python k_nearest_stars.py 10``` to get 10 nearest neighbors.
   Check the q1.png image for runtime metrics.

## Question 2
1. k nearest neighbors is a topic of research, especially for higher dimensions, but since we have only 3 dimensions we have a few options each with its pros and cons.

	***Option 1:*** Follow solution 1 approach and loop through the list keeping a k sized max heap.
	* pros: Guaranteed correct result
	* cons: time complexity O(nlogk), for large number of start(n) performance may suffer

	***Option 2:*** Use a kd-tree structure to map the coordinates into 3d space.
	* pros: time complexity of O(log n)
	* cons: 
		* give approximate nearest neighbors, may miss some neighbors
		* requires pre processing the data
	* reference: 
		* ```https://en.wikipedia.org/wiki/K-d_tree#Nearest_neighbour_search``` 
		* ```https://www.youtube.com/watch?v=TLxWtXEbtFE``` 
		* ```http://andrewd.ces.clemson.edu/courses/cpsc805/references/nearest_search.pdf```

	***Option 3:*** scikit learn knn
	* pros: stable library
	* cons: does not scale well to large datasets approximate algorithm training required
	* reference:
		* ```http://scikit-learn.org/stable/modules/neighbors.html```

	***Option 4:*** Open source library ```annoy``` is used to find nearest neighbors in high dimensions, uses kd-tree along with priority queue approach. If we start a micro service and keep the service running with the index or data in memory we can do lookups in O(log(n)+k) time which is much faster than the approach in question 1.
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
	* Run Instructions: Implemented Option 4's algorithm
		1. Input Parameters: k : the number of nearest neighbors to be found
						  point_star: the name of the star whose neighbors are to be found.    
			A service to get k closest stars to a given star has been implemented using the library annoy. 
		2. clone the git repo and from the folder ```.../data_engineer/nearest_star/``` run the command ```pip install annoy```
		3. preprocess the data using the command ```gunzip -c hygdata_v3.csv.gz | python k_nearest_stars_pre_process.py``` 
		4. Run the query ```python3 knn_query.py 10 Sol```. Check the q4_option4.png for runtime metrics.
