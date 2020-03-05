
def factorize_nbr(nbr: int):
	"""	Present the nbr using prime mults.
		x - int nbr
	"""
	divisor = 2
	while nbr > 1:
		if nbr % divisor == 0:
			print(divisor)
			nbr //= divisor
		else:
			divisor += 1

number = int(input("Enter ur number: "))

factorize_nbr(number)