
def gcd(a, b):
	"""	Doesnt work is a == 0 or b == 0
		Sad story :(
	"""
	return ((a if b == 0 else gcd(b, a % b)))

def gcd_for_all(a, b):
	"""	The same problem
		:(
	"""
	return (gcd_for_all(a - b, b) if a > b else gcd_for_all(a, b - a))

def test_gcd():
	print("Test #1:", "Ok!" if gcd(10, 15) == 5 else "Fail!")
	print("Test #2:", "Ok!" if gcd(0, 15) == 0 else "Fail!")
	print("Test #3:", "Ok!" if gcd(10, 20) == 10 else "Fail!", end='\n\n')

def test_gcd_for_all():
	print("Test #1:", "Ok!" if gcd(10, 15) == 5 else "Fail!")
	print("Test #2:", "Ok!" if gcd(0, 15) == 0 else "Fail!")
	print("Test #3:", "Ok!" if gcd(10, 20) == 10 else "Fail!")

test_gcd()
test_gcd_for_all()
