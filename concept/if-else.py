#!/usr/bin/python3

a, b = 10, 12

# Normal if else 
if a > b :
 	print("a ({}) is greater than b ({})".format(a, b))
else:
 	print("a ({}) is less than b ({})".format(a, b))

# Ternary Operator
c = ("Greater" if a > b else "Lesser")

print("Value of a is {}".format(c))