
def bin_search(Array: list, number: int, left:int=0, right:int=-1) ->int:
	"""	In ascending ordered array finding the first index 
		when the value of Array's k-elem equals to number 
	"""
	if not len(Array):
		return None
	if (right - left < 2 and right - left > 0):
		return (left)
	right = len(Array) - 1 if right == -1 else right
	if (Array[(left + right) // 2] > number):
		return bin_search(Array, number, left, (left + right) // 2)
	elif (Array[(left + right) // 2] <= number):
		return bin_search(Array, number, (left + right) // 2, right)
	return None

def test_bin_search():
	A = [x for x in range(10)]
	print("Test #1 is", "Ok!" if bin_search(A, 5) == 5 else "Fail!")
	print("Test #2 is", "Ok!" if bin_search(A, 0) == 0 else "Fail!")
	print("Test #3 is", "Ok!" if bin_search(A, 1) == 1 else "Fail!")
	print("Test #4 is", "Ok!" if bin_search(A, 9) == 9 else "Fail!")
	print("Test #5 is", "Ok!" if bin_search(A, 10) == None else "Fail!")
	print("Test #6 is", "Ok!" if bin_search(A, -1) == None else "Fail!")

test_bin_search()
