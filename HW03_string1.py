#!/usr/bin/python -tt
# HW03_string1.py
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    # +++your code here+++
    count = count 
    if count > 10 or count == 10:
        print("Number of donuts: many")
        print()
    else:
        print("Number of donuts:", " ", count)
        print()
    return

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    # +++your code here+++
    #This is a Slicing problem where we are slicing the given string
    length_of_the_string = len(s)
    if length_of_the_string < 2:
        empty_string = " "
        return empty_string

    part1 = s[0:1]
    #This is part one of the string which is the same irrespective of the length of the string
    part2 = s[(length_of_the_string)-1:length_of_the_string]
    new_word = part1 + part2
    print (new_word)
    return new_word


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    # +++your code here+++
    first_char = s[0]
    final_word = s[1:].replace(first_char, "*")
    #THis is the main file which needs to be edited -->final_word[0] = first_char. First character of the final word needs to be changed from * to the original character.
    final_word2 = first_char + final_word

    return final_word2


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
    # +++your code here+++
    #Let x and y be the frst two characters of each string which is input as a part of this function. 
    length_of_a = len(a)
    length_of_b = len(b)

    x = a[0] + a[1]
    y = b[0] + b[1]
    #Assignment operators for x and y. 
    a_remain=a[2:length_of_a ]
    b_remain=b[2:length_of_b ]

    new_word4 = y + a_remain
    new_word5 = x + b_remain
    new_word6 =new_word4+" "+new_word5

    return new_word6



# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that
    # call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
