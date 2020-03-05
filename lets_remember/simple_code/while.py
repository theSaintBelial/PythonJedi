
nbr = 25
flag = True

while flag:
	guess = int(input("Enter ur number: "))
	if guess == nbr:
		print("WOW! U r right!\n")
		flag = False
	elif guess > nbr:
		print("Sry, but nbr is lower :( Try again!")
	else:
		print("Sry, but nbr is higher :( Try again!")
else:
	print("while is dead...\n") # WTF BRO IS IT 'ELSE' USING BY WHILE???????????
print("Nice play, c u!")

print("U have 5 attempts to prove ur brain!")
for i in range(0, 5):
	str = input("Enter ur string: ")
	if len(str) < 3:
		print("U deserve this 0! Try again.")
	else:
		print("Yap, u did it!")
		break
	if i == 4:
		print("Sry, u r max stupid!")
	