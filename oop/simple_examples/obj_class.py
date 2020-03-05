
class Robot:
	population = 0

	def __init__(self, name):
		self.name = name
		Robot.population += 1
	
	def __del__(self):
		print("{} is dead.".format(self.name))
		Robot.population -= 1
		if not Robot.population:
			print("It was the last one. No fun anymore.")
		else:
			print("{}".format(Robot.population), "robots are" if Robot.population > 1 else "robot is", "still alive.")
	
	def say_your_name(self):
		print("Hey, I'm {}!".format(self.name))

	@staticmethod
	def how_many():
		print("There are {} ones in our population.".format(Robot.population))

	# how_many = staticmethod(how_many)

robo1 = Robot("Alex")
robo1.say_your_name()
Robot.how_many()

robo2 = Robot("Oleg")
robo2.say_your_name()
Robot.how_many()

robo3 = Robot("Michael")
robo3.say_your_name()
Robot.how_many()

robo4 = Robot("Danya")
robo4.say_your_name()
Robot.how_many()

del robo4
del robo3
del robo2
del robo1