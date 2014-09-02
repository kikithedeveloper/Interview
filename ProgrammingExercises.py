# 1.1
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additonal data structures?

def unique(string):

	uni_dict = {}

	for char in string:

		if char in uni_dict:
			return False

		else:
			uni_dict[char] = True

	return True

# print unique("Aviva") # test should return False.

# print unique("Kimberly") # test should return True.

#__________________________________________

# 1.2
# Implement a function that reverses a string in place.

def reverse(word):

	word_list = list(word)

	for i in range(len(word)/2):
		temp = word_list[i]
		word_list[i] = word_list[-i-1]
		word_list[-i-1] = temp

	reverse = "".join(word_list)

	return reverse

#print reverse("ChiMing") # returns "ginMihC".

#__________________________________________

# 1.3
# Given two strings, 
# write a method to decide if one is a permutation of the other.

import collections

def same_permutation(a, b):

    d = collections.defaultdict(int)
    # print d

    for x in a:
        d[x] += 1
        # print d[x]

    for x in b:
        d[x] -= 1
        # print d[x]

    # print d.itervalues()

    return not any(d.itervalues())

# print same_permutation([1,2,3],[2,3,1])
# returns True

# print same_permutation([1,2,3],[2,3,1,1])
# returns False

#__________________________________________

# 1.4
# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at
# the end of the string to hold the additional characters, and
# that you are given the "true" length of the string. 
# EXAMPLE. Input: "Mr John Smith", 13
#          Output:"Mr%20John%20Smith"

def replace_spaces (string):

	chars = list(string)

	insert = '%20'

	for i in range(len(chars)):
		if chars[i] == " ":
			chars[i] = insert

	newString = "".join(chars)

	return newString

print replace_spaces("Kim love Chi   ")


#__________________________________________

# 1.5
# Implement a method to perform basic string compression 
# using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the 
# original string, your method should return the original
# string. You can assume the string has only upper and 
# lower case letters (a - z).




#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________