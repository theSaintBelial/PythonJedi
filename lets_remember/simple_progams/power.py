
def power(nbr: int, pow: int):
	return (power(nbr, pow - 1) * nbr if pow else 1)

def power_advanced(nbr: int, pow: int):
	"""	Lol, is it everything ok
		with this option?????
	"""
	return ((power(nbr, pow - 1) if nbr % 2 else power(nbr ** 2, pow // 2)) if pow else 1)

def test_power():
	print(power(-2, 9), end="\n\n")

def test_power_advanced():
	print(power(-2, 9))

test_power()
test_power_advanced()