#!/usr/local/bin/python3

class IntSet(object):
	"""An IntSet is a set of integers"""
	#Value of the set is represented by a list of ints, self.vals.
	#Each int in the set occurs in sel.vals exactly once.

	def __init__(self):
		"""Create an empty set of integers"""
		self.vals = []

	def insert(self, e):
		"""Assumes e is an integer and inserts e into self.vals"""
		if e not in self.vals:
			self.vals.append(e)

	def member(self, e):
		"""Assumes e is an integer
		Returns True if e is in self, and False otherwise"""
		return e in self.vals

	def remove(self, e):
		"""Assumes e is an integers and removes e from self
		Raises ValueError if e is not in self"""
		try:
			self.vals.remove(e)
		except:
			raise ValueError(str(e) + ' not found')

	def getMembers(self):
		"""Returns a list containing the elements of self.
		Nothing can be assumed about the order of the elements"""
		return self.vals[:]

	def __str__(self):
		"""Returns string representation of self"""
		result = ''
		for e in self.vals:
			result = result + str(e) + ','
		return '{' + result[:-1] + '}' #-1 omits trailing comma

if __name__ == '__main__':
	intset = IntSet()
	intset.insert(1)
	intset.insert(2)
	intset.insert(3)
	print(intset.member(4))
	print(intset.getMembers())
	intset.remove(2)
	print(intset)
	intset.remove(2)
