import sys
from scipy import spatial
from star import star
import utils

def find_stars(k, qry_point, processed_data=r'./proc_data.tree', lookup=r'./id_star.lkp'):
	kd_tree = utils.read_pickle_obj(processed_data)
	id_star_dct = utils.read_pickle_obj(lookup)
	k_closest = kd_tree.query(qry_point, k=k+1, p=2)[1]
	for i in range(1, len(k_closest)):
		id_star_dct[k_closest[i]].print()

if __name__ == '__main__':
	k = int(sys.argv[1])
	qry_point = [float(elt) for elt in sys.argv[2:5]]
	find_stars(k=k, qry_point=qry_point)
