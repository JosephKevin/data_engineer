import sys
import fileinput
from collections import defaultdict
from heapq import heapify, heappush, heappushpop
from star import star
import utils

def find_k_nearest(k, point_star):
	"""
	Function to loop through each line in the stdin and keep track of the k
	closest points

	Args:
		k: the number of closest neighbors to find
		point_star: the star for which to find the k closest neighbors

	Returns:
		max_heap: a heap containing the k closest distances to the point_star
		star_dist: a key value pari of {dist-d1: [list of stars at dist-d1 to point_star]}
	"""
	max_heap = []
	star_dist = defaultdict(list)
	# skip header and sun column
	utils.skip_line(2)
	for line in sys.stdin:
		star_name, x, y, z = utils.parse_line(line=line)
		dist = utils.euclidean_dist(x=(x, y, z), y=point_star)
		new_star = star(x=x, y=y, z=z, star_name=star_name)
		if len(max_heap) < k:
			heappush(max_heap, -1 * dist)
			star_dist[dist].append(new_star)
		elif dist <= -1 * max_heap[0]:
			heappushpop(max_heap, -1 * dist)
			star_dist[dist].append(new_star)
	return max_heap, star_dist

def print_elements(max_heap, star_dist, k):
	"""
	Function to print the k neighbors which are closest to the point_star

	Args:
		max_heap: a heap containing the k closest distances to the point_star
		star_dist: a key value pari of {dist-d1: [list of stars at dist-d1 to point_star]}
		k: the number of closest neighbors to find

	Returns:
		Prints the list of k closest stars to point_star
	"""
	counter = 0
	heapify(max_heap)
	max_heap = list(set(max_heap))
	max_heap.sort(reverse=True)
	print('-------------------------{0} Closest points-------------------------'.format(k))
	for i in range(0, len(max_heap)):
		for star in star_dist[-1*max_heap[i]]:
			if counter >= k:
				return 
			star.print()
			counter += 1
	print('--------------------------------------------------------------------')

def driver(k, point_star):
	"""
	Function to drive the process

	Args:
		k: the number of closest neighbors to find
		point_star: the star for which to find the k closest neighbors

	Returns:
		No Return
	"""
	max_heap, star_dist = find_k_nearest(k = k, point_star = sun)
	print_elements(max_heap, star_dist, k = k)

if __name__ == '__main__':
	k = int(sys.argv[1])
	sun = (0.000005, 0.0, 0.0)
	driver(k=k, point_star=sun)




