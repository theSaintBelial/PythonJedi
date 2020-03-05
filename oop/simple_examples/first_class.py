
class Person:
	def __init__(self, name):
		self.name = name
	def say_hi(self):
		print("Hi, {}!".format(self.name))

example = Person('Kek')
example.say_hi()