from annoy import AnnoyIndex
import pickle
from star import star

def get_k_nearest(k, dim = 3, idx_file=r'./idx_500.ann', dict_pkl='./dict.pickle'):
	"""
	Function to load in data used by annoy query
	Reference: https://github.com/spotify/annoy

	Args:
		k: the number of closest neighbors to find
	    dim: the dimension of the point
		idx_file: mapping from id to vector
		dict_pkl: mapping from id to corresponding to star object

	Returns:
		Prints the list of k closest stars to point_star
	"""
	u = AnnoyIndex(dim, metric='euclidean')
	u.load(idx_file)
	pickle_in = open(dict_pkl,'rb')
	id_vct = pickle.load(pickle_in)
	(annoy_idx, dist) = u.get_nns_by_item(0, 10, include_distances=True)
	for i in range(len(annoy_idx)):
		id_vct[annoy_idx[i]].print()
		print('The above star is at a distance: {0}'.format(dist[i]))

if __name__ == '__main__':
	k = int(sys.argv[1])
	get_k_nearest(k)