
def swap(Array, j):
	"""	Swapping j and j + 1 elements of the Array
		Array - list
		j - index
	"""
	tmp = Array[j]
	Array[j] = Array[j + 1]
	Array[j + 1] = tmp

def bubble_sort(A, size):
	"""	Sorting the A list in the oscending order
		using bubble_sort
		A - list
		size - its lenght
	"""
	if size < 2:
		return
	for i in range(size):
		for j in range(size - 1):
			if (A[j] > A[j + 1]):
				swap(A, j)
	
def test_bubble_sort():
	"""	Testing bubble_sort func using standart
		sorted()
	"""
	Array = [0, 1, 4, 3 , 7, 4, 3, 5, 2, 9]
	bubble_sort(Array, len(Array))
	if (Array == sorted(Array)):
		print("test #1: Ok!")
	else:
		print("test #1: Fail!")

test_bubble_sort()