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
		id_obj: mapping from id to star object
		obj_id: mapping from star name to id
		Reference: https://github.com/spotify/annoy

	Returns:
		No Return 
	"""
	id_obj = {}
	obj_id = {}
	utils.skip_line(1)
	tree = AnnoyIndex(dim, metric='euclidean')
	idx = 0
	for line in fileinput.input():
		star_name, x, y, z = utils.parse_line(line)
		tree.add_item(idx, [x, y, z])
		id_obj[idx] = star(x,y,z, star_name)
		obj_id[star_name] = idx
		idx += 1
	pickle_out = open("./id_obj.pickle","wb")
	pickle.dump(id_obj, pickle_out)
	pickle_out.close()
	pickle_out = open("./obj_id.pickle","wb")
	pickle.dump(obj_id, pickle_out)
	pickle_out.close()
	tree.build(n_trees)
	tree.save(idx_file)
	
if __name__ == '__main__':
	pre_process(n_trees=500, idx_file=r'./idx_500.ann')