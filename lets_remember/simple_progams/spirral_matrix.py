
def init_matrix(size): # create a size*size matrix
	return [[0] * size for i in range(size)]

def on_clock_spirral_matrix(Matrix, size):
	"""	Fill Matrix with numbers in ascending order.
		On clock direction.
	"""
	x, y = 0, 0
	dx, dy = 1, 0
	nx, ny = 0, 0

	for i in range(1, size ** 2 + 1):
		Matrix[x][y] = i

		nx, ny = x + dx, y + dy

		if (0 <= nx < size and 0 <= ny < size and not Matrix[nx][ny]):
			x, y = nx, ny
		else:
			dx, dy = -dy, dx
			x, y = x + dx, y + dy

def non_clock_spirral_matrix(Matrix, size):
	"""	Fill Matrix with numbers in ascending order.
		Non clock direction.
	"""
	x, y = 0, 0
	dx, dy = 1, 0
	nx, ny = 0, 0

	for i in range(1, size ** 2 + 1):
		Matrix[y][x] = i

		nx, ny = x + dx, y + dy

		if (0 <= nx < size and 0 <= ny < size and not Matrix[ny][nx]):
			x, y = nx, ny
		else:
			dx, dy = -dy, dx
			x, y = x + dx, y + dy

def print_matrix(Matrix): # printing matrix in a cute way))
	for i in range(len(Matrix)):
		for j in range(len(Matrix)):
			print("{:2d}".format(Matrix[i][j]), end=' ')
		print()
	print()

def test_spirral_matrix():
	"""	Testing spiral_matrix filling in a right way:
		1)on_clock way;
		2)non_clock way.
	"""

	print(test_spirral_matrix.__doc__)

	size = 5

	matrix = init_matrix(size)
	on_clock_spirral_matrix(matrix, size)
	print_matrix(matrix)
	matrix2 = init_matrix(size)
	non_clock_spirral_matrix(matrix2, size)
	print_matrix(matrix2)

def new_way_snail(array):
	return (list(array[0]) + new_way_snail(list(zip(*array[1:]))[: :-1])) if len(array) else []

def test_snail():
	"""	Testing snail func that returns
		a snail list from matrix. (non-clock direction)
	"""

	print(test_snail.__doc__)

	size = 3

	matrix = init_matrix(size)
	non_clock_spirral_matrix(matrix, size)
	print_matrix(matrix)
	print("Result:", *new_way_snail(matrix))
	
test_spirral_matrix()

print("-----------------------------------------------------------------\n")

test_snail()