#!/usr/bin/env python3

# its my first program on py3 (no)

print("Hello, World!\n") 

age = 19
name = 'Alex'

print("I'm {0} and my age is {1}\n".format(name, age))
print("Why is {0} doing this simple things?\n".format(name))

# lets play with numbers

print("Ohh, no, its a float... \n{0:.3}\nI can't believe my eyes! So easy!".format(1 / 3))

# ..or with something else

print("\nHmm, look at this! : {0:_^13}\n".format("hello"))

# ..or using key words

print("Hey, I'm {name} and my age is {age}!".format(name = name, age = age))

# other int PEP 3101