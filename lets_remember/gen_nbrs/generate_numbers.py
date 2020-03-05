
def generate_numbers(Dim: int, Mod: int, prefix=None):
	prefix = prefix or [] # its so hot! omg...
	if (Mod == 0):
		print(*prefix)
		return
	for number in range(Dim):
		prefix.append(number)
		generate_numbers(Dim, Mod - 1, prefix)
		prefix.pop()

generate_numbers(3, 3)