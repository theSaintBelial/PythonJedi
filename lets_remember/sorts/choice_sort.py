
def choice_sort(A: list):
	for i in range(len(A)):
		for j in range(i + 1, len(A)):
			if (A[j] < A[i]):
				A[i], A[j] = A[j], A[i]


def test_choice_sort():
	A = [4, 2, 5, 1, 3, 0, 5, 3, -1, -2, 17, 10]
	print(A)
	choice_sort(A)
	print(A)

test_choice_sort()