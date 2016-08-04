#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
###############################################################################
# Exercise 6.2
# See 6.1: "write a compare function takes two values, x and y, and returns 1
# if x > y, 0 if x == y, and -1 if x < y."
# When you submit only include your final function: compare
def compare(x,y):
	#First we define the reuslt as zero by default. The result variable will be returend from all the cases based on the comparison of the two values of x and y. 
	result = 0
	if (x>y):
		result = 1
		return result

	if (x==y):
		result =0 
		return result

	if (x<y):
		result=-1
		return result

###############################################################################
# Exercise 6.2
# See 6.2: "use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given the
# lengths of the other two legs as arguments."
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share in your final push your incremental
# work.
def hypotenuse(x,y):
	#In this function we are finding the lenght of the hypotenuse and x and y are the length of the two sides of the rectangle. 
	import math
	x1 = x * x
	y1 = y * y
	z1 = x1 + y1

	#This is the varibale used for storing the result of the Pythagoreous Theorem. 
	result10 = math.sqrt(z1)
	return result10

###############################################################################
# Exercise 6.4
# See 6.4: "write a function is_between(x, y, z) that returns True if x ≤ y ≤ z
# or False otherwise"
# When you submit only include your final function: is_between
def is_between(x,y,z):
	result44="False"
	#We plan on returning the value of the above variable result44 at the end to ensure the correct value is returned.
	if ((x < y) or (x==y)) and ((y < z) or (y==z)):
		result44="True"
	
	return result44

###############################################################################
# Exercise 3.2
# See "Exercise 3, part 2": "Write a function called is_palindrome that takes a
# string argument and returns True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length of a
# string."
# When you submit only include your final function: is_palindrome

def is_palindrome(string44):
	result444="False"
	string_length_44 = len (string44)
	string45 = string44[- string_length_44:]
	if string45 is string44:
		result444 = "True"

	else:
		result444 = "False"
	return result444

###############################################################################
# Exercise 4
# See "Exercise 4": "A number, a, is a power of b if it is divisible by b and
# a/b is a power of b. Write a function called is_power that takes parameters a
# and b and returns True if a is a power of b. Note: you will have to think
# about the base case."
# Note: Please use the provided definition and only plan for positive integers
# (whole numbers not including zero)
# When you submit only include your final function: is_power
def is_power(a,b):

	div_check = a % b
	if (div_check != 0):
		return False 
	c = a / b

	while temp=="True":
		temp = is_power(c,b)

	return temp


	
###############################################################################
def main():
    """Your functions will be called within this function."""
    ###########################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")






    ###########################################################################
    # # Uncomment the below to test and before commiting:
    # # Exercise 1
    # print(compare(1, 1))
    # print(compare(1, 2))
    # print(compare(2, 1))
    # # # Exercise 2
    # print(hypotenuse(1, 1))
    # print(hypotenuse(3, 4))
    # print(hypotenuse(1.2, 12))
    # # # Exercise 3
    # print(is_between(1, 2, 3))
    # print(is_between(2, 1, 3))
    # print(is_between(3, 1, 2))
    # print(is_between(1, 1, 2))
    # # # Exercise 6
    # print(is_palindrome("Python"))
    # print(is_palindrome("evitative"))
    # print(is_palindrome("sememes"))
    # print(is_palindrome("oooooooooooo"))
    # # # Exercise 7
    # print(is_power(28, 3))
    # print(is_power(27, 3))
    # print(is_power(248832, 12))
    # print(is_power(248844, 12))


if __name__ == "__main__":
    main()
