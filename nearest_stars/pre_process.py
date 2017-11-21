import sys
from scipy import spatial
import numpy as np
from star import star
import utils

def pre_process(leaf_size=40, processed_data=r'./proc_data.tree', lookup=r'./id_star.lkp'):
	"""
	Function to pre process the stars data into a kd tree and save the data

	Args:
		leaf_size: The number of points at which the algorithm switches over to brute-force. Has to be positive
		processed_data: The location where the processed data is to be stored as a pickle file
		lookup: The location where the data id to object lookup is stored

	Returns:
		No return
	"""
	utils.skip_line(1)
	stars = []
	idx = 0
	id_star_dct = {}
	for line in sys.stdin:
		star_name, x, y, z = utils.parse_line(line)
		stars.append([x, y, z])
		id_star_dct[idx] = star(x, y, z, star_name)
		idx += 1
	# construct a kd-tree
	tree = spatial.KDTree(stars, leafsize=leaf_size)
	utils.save_as_pickle(data=tree, pickle_file=processed_data)
	utils.save_as_pickle(data=id_star_dct, pickle_file=lookup)
	

if __name__ == '__main__':
	pre_process()