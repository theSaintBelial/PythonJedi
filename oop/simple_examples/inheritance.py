
class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print(name, "has been created.")

	def tell(self):
		print("Name: {}\nAge: {}".format(self.name, self.age))

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print("Teacher {} has been created.".format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print("Salary:", self.salary, end="\n\n")

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print("Student {} has been created.".format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print("Marks:", self.marks, end="\n\n")

teacher1 = Teacher("Jenny", 35, 20000)
teacher1.tell()
student1 = Student("Oleg", 20, 4)
student1.tell()
teacher2 = Teacher("Stella", 46, 50000)
teacher2.tell()
student2 = Student("Michael", 21, 5)
student2.tell()
teacher3 = Teacher("Anna", 28, 35050)
teacher3.tell()
student3 = Student("Danya", 22, 5)
student3.tell()


