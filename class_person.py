import datetime

class Person(object):

	def __init__(self, name):
		"""create a person"""
		self.name = name
		try:
			lastBlank = name.rindex(' ')
			self.lastName = name[lastBlank+1:]
		except:
			self.lastName = name
		self.birthDay = None

	def getName(self):
		"""returns self's full name"""
		return self.name

	def getLastName(self):
		"""returns self's last name"""
		return self.lastName

	def setBirthday(self, birthDate):
		"""assumes birthDate is of type datetime.date
			Sets self's birthDay"""
		self.birthDay = birthDate

	def getAge(self):
		"""return self's current age in days"""
		if self.birthDay == None:
			raise ValueError
		return (datetime.date.today() - self.birthDay).days

	def __lt__(self, other):
		"""returns True if self precedes other in alphabetical
			order, and False otherwise.Comparison is based on
			last name, but if these are the same full names are
			compared"""
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName

	def __str__(self):
		"""returns self name"""
		return self.name

if __name__ == '__main__':
	p1 = Person('Mickey Mouse')
	p2 = Person('Donald Duck')
	p1.setBirthday(datetime.date(1961, 8, 4))
	p2.setBirthday(datetime.date(1958, 8, 16))
	print(p1)
	print(p2)
	print(p1.getLastName())
	print(p2.getLastName())
	print(p1, 'Age in days:', p1.getAge())
	print(p2, 'Age in days:', p2.getAge())
