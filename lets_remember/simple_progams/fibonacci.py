
def fibonacci_search(index: int):
	prev_elem = 1
	cur_elem = 1

	if index < 1:
		return (-1)
	if index < 2:
		return (0)
	if index < 4:
		return (1)
	for i in range(3, index):
		tmp = cur_elem
		cur_elem = cur_elem + prev_elem
		prev_elem = tmp
	return (cur_elem)

index = int(input("Enter the index of Fibonacci sequence element u want to see: "))

print(fibonacci_search(index))