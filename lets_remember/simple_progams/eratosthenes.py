

size = int(input("Enter the size of an array: "))
Array = [True] * size
Array[0] = Array[1] = False
for i in range(2, size):
	if (Array[i]):
		for j in range(i * 2, size, i):
			Array[j] = False

# printing

for i in range(size):
	print(i, '-', "prime" if (Array[i]) else "compound")