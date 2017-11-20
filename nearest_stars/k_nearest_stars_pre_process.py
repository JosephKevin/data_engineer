import sys
from annoy import AnnoyIndex
import fileinput
import pickle
from star import star
import utils

def pre_process(n_trees, idx_file, dim = 3):
	"""
	Function to preprocess the data to kd trees. Store a 
	mapping from id to vector as a .ann file and a mapping from 
	id to corresponding to star object as a pickle object

	Args:
		n_trees: Number of trees to be built
		idx_file: the file mapping id to 
		Reference: https://github.com/spotify/annoy

	Returns:
		No Return 
	"""
	id_vct = {}
	utils.skip_line(1)
	tree = AnnoyIndex(dim, metric='euclidean')
	idx = 0
	for line in fileinput.input():
		star_name, x, y, z = utils.parse_line(line)
		tree.add_item(idx, [x, y, z])
		id_vct[idx] = star(x,y,z, star_name)
		idx += 1
	pickle_out = open("./dict.pickle","wb")
	pickle.dump(id_vct, pickle_out)
	pickle_out.close()
	tree.build(n_trees)
	tree.save(idx_file)
	
if __name__ == '__main__':
	pre_process(n_trees=500, idx_file=r'./idx_500.ann')