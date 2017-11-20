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
	
	def __hash__(self):
		return hash((self.x, self.y, self.z, self.star_name))

	def __eq__(self, other):
		return (self.x, self.y, self.z, self.star_name) == (other.x, other.y, other.z, other.star_name)

	def __ne__(self, other):
		# Not strictly necessary, but to avoid having both x==y and x!=y
		# True at the same time
		return not(self == other)