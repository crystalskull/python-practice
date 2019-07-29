import MITPerson

class Grades(object):
	def __init__(self):
		self.students = []
		self.grades = {}
		self.isSorted = True

	def addStudetnt(self, student):
		"""Assumes student is of type Student
		Add student to grade book"""
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
			self.grades[student.getIdNum()][:]
		except:
			raise ValueError('student not in mapping')

	def getStudents(self):
		"""Return sorted list of students in grade book"""
		if not self.isSorted:
			self.students.sort()
			self.students.isSorted = True
		return self.students[:]
