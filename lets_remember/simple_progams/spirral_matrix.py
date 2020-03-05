
def init_matrix(size):
	Matrix = [[0] * size for i in range(size)]
	return Matrix

def on_clock_spirral_matrix(Matrix, size):
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

def print_matrix(Matrix, size):
	for i in range(size):
		for j in range(size):
			print("{:2d}".format(Matrix[i][j]), end=' ')
		print()


size = 5

matrix = init_matrix(size)
print_matrix(matrix, size)
on_clock_spirral_matrix(matrix, size)
print_matrix(matrix, size)
matrix2 = init_matrix(size)
non_clock_spirral_matrix(matrix2, size)
print_matrix(matrix2, size)