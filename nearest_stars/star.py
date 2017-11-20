class star(object):
	"""
	Class to represent star object
	"""
	def __init__(self, x, y, z, star_name):
		self.x = x
		self.y = y
		self.z = z
		if star_name.strip() == '' :
			self.star_name = 'Not Available'
		else:
			self.star_name = star_name

	def print(self):
		print('Star Name: {0}, x: {1}, y: {2}, z: {3}'.format(self.star_name, self.x, self.y, self.z))