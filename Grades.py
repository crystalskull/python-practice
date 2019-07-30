from MITPerson import UG
from MITPerson import Grad

class Grades(object):
	def __init__(self):
		self.students = []
		self.grades = {}
		self.isSorted = True

	def addStudent(self, student):
		"""Assumes student is of type Student
		Add student to grade book"""
		if student in self.students:
			raise ValueError('Duplicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False

	def addGrade(self, student, grade):
		"""Assumes grade is a float
		Add grade to the list of grades for student"""
		try:
			self.grades[student.getIdNum()].append(grade)
		except:
			raise ValueError('student not in mapping')

	def getGrades(self, student):
		"""Returns copy of list of grades for student"""
		try:
			return self.grades[student.getIdNum()][:]
		except:
			raise ValueError('student not in mapping')

	def getStudents(self):
		"""Return sorted list of students in grade book"""
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		return self.students[:]

def gradeReport(course):
	"""Assumes course is of type Grades"""
	report = ''
	for s in course.getStudents():
		total = 0.0
		numGrades = 0
		for g in course.getGrades(s):
			total += g
			numGrades += 1
		try:
			avg = total / numGrades
			report = report + '\n'\
						+ str(s) + '\'s mean grade is ' + str(avg)
		except ZeroDivisionError:
			report = report + '\n'\
						+ str(s) + ' has no grades'
	return report


if __name__ == '__main__':
	ug1 = UG('Jane Doe', 2014)
	ug2 = UG('John Doe', 2015)
	ug3 = UG('David Henry', 2003)
	g1 = Grad('Billy Buckner')
	g2 = Grad('Bucky Dent')
	oneZeroOne = Grades()
	oneZeroOne.addStudent(ug1)
	oneZeroOne.addStudent(ug2)
	oneZeroOne.addStudent(g1)
	oneZeroOne.addStudent(g2)
	for s in oneZeroOne.getStudents():
		oneZeroOne.addGrade(s, 75)
	oneZeroOne.addGrade(g1, 25)
	oneZeroOne.addGrade(g2, 100)
	oneZeroOne.addStudent(ug3)
	print(gradeReport(oneZeroOne))
	
