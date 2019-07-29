from Person import Person

class MITPerson(Person):
	#class variable
	nextIdNum = 0

	#override init
	def __init__(self, name):
		Person.__init__(self, name)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1

	def getIdNum(self):
		return self.idNum

	def isStudent(self):
		return isinstance(self, Student)

	#override lt
	def __lt__(self, other):
		return self.idNum < other.idNum

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        super().__init__(name)
        self.year = classYear
    def getYear(self):
        return self.year

class Grad(Student):
    pass

if __name__ == '__main__':
	p1 = MITPerson('Huey Duck')
	p2 = MITPerson('Duey Duck')
	print(p1, ', id num is', p1.getIdNum())
	print(p2, ', id num is', p2.getIdNum())
