
def insert_sort(A: list):
	for i in range(1, len(A)):
		if (A[i] < A[i - 1]):
			for j in range(i, 0, -1):
				if (A[j] < A[j - 1]):
					A[j], A[j - 1] = A[j - 1], A[j]


def test_insert_sort():
	A = [4, 2, 5, 1, 3, 8, 4, 0, -1, -2, 5, 4, 10, 3]
	print(A)
	insert_sort(A)
	print(A)

test_insert_sort()