
size = int(input("Enter array's size: "))
Source = [0] * size
Dest = [0] * size

for i in range(size):
	Source[i] = int(input("Enter element #{}: ".format(i + 1)))
	Dest[i] = Source[i]

print(Source, Dest, sep='\n')