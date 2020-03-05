
def reverse_list(List):
	"""	Reverse list List
		LoL :D
	"""
	lenght = len(List)
	for i in range(lenght // 2):
		List[i], List[lenght - 1 - i] = List[lenght - 1 - i], List[i]


def test_reverse_list():
	List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(List)
	reverse_list(List)
	print(List)

test_reverse_list()