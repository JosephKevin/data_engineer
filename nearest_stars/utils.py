import sys
import math

def euclidean_dist(x, y):
	"""
	Function to calculate euclidean distance

	Args:
		x: n dimension point
		y: n dimension point

	Returns:
		Euclidean distance between x and y
	"""
	return round(math.sqrt(sum([(float(a) - float(b)) ** 2 for a, b in zip(x, y)])), 4)

def parse_line(line, x=17, y=18, z=19, name_idx=6):
	"""
	Function to parse the HYG-datase line and get out x,y,z and start name

	Args:
		x: index of x coordinate in the file
		y: index of y coordinate in the file
		z: index of z coordinate in the file
	    name_idx: index of name in the file

	Returns:
		name, x, y, z
	"""
	line_lst = line.strip().split(',')
	return line_lst[name_idx], float(line_lst[x]), float(line_lst[y]), float(line_lst[z]) 

def skip_line(num_line = 1):
	"""
	Function to skip lines when reading from stdin

	Args:
		num_line: number of lines to skip
	"""
	for i in range(0, num_line):
		next(sys.stdin)