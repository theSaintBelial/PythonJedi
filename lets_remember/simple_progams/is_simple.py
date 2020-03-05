
def is_prime(nbr: int):
	"""	Return True if the x is prime.
		x - int nbr
		False - in other cases.
	"""
	divisor = 2
	if nbr <= 1:
		return False
	while divisor < nbr:
		if nbr % divisor == 0:
			return False
		divisor += 1
	return True

if (is_prime(int(input("Enter ur nbr: ")))):
	print("Yes! its prime!")
else:
	print("No, this nbr is not prime.")