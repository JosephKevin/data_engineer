import sys
from annoy import AnnoyIndex
import pickle
#from star import star

def get_k_nearest(k, point_star, dim = 3, idx_file=r'./idx_500.ann', id_obj=r'./id_obj.pickle', obj_id=r'./obj_id.pickle'):
	"""
	Function to load in data used by annoy query
	Reference: https://github.com/spotify/annoy

	Args:
		k: the number of closest neighbors to find
		point_star: the name of the star whose neighbors are to be found
	    dim: the dimension of the point
		idx_file: mapping from id to vector
		id_obj: mapping from id to corresponding to star object

	Returns:
		Prints the list of k closest stars to point_star
	"""
	u = AnnoyIndex(dim, metric='euclidean')
	u.load(idx_file)
	pickle_in = open(id_obj,'rb')
	id_vct = pickle.load(pickle_in)
	pickle_in = open(obj_id,'rb')
	obj_id_vct = pickle.load(pickle_in)
	(annoy_idx, dist) = u.get_nns_by_item(int(obj_id_vct[point_star]), k+1, include_distances=True)
	for i in range(1, len(annoy_idx)):
		id_vct[annoy_idx[i]].print()

if __name__ == '__main__':
	k = int(sys.argv[1])
	point_star = sys.argv[2]
	get_k_nearest(k, point_star)