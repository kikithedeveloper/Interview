'''
==============================
ARRAYS AND STRINGS
==============================
'''

# 1.1 
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

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

# 1.2 
# Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string.
# Revision: Reverse a string in Python without using built-in reverse()

def reverse(str): 

  string = list(str)
  
  for i in range(len(string)/2):
  temp = string[-i-1]
  string[-i-1] = string[i]
  string[i] = temp
   
  newString = "".join(string)

  return newString
  
# print reverse("I love Chi Ming.")

# 1.3 
# Given two strings, write a method to decide if one is a permutation of the other.

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

# print replace_spaces("Kimberly loves dogs  !")

# 1.5
# Implement a method to perform basic string compression 
# using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the 
# original string, your method should return the original
# string. You can assume the string has only upper and 
# lower case letters (a - z).

def string_compression(input):
  
  if len(input) == 0:
    return ""
  
  counter = 1
  output = ''
  
  for i in range(1,len(input)):
  
    if input[i] == input[i-1]:
      counter += 1
  
    else:
      output += input[i-1] + str(counter)
      counter = 1
  
  output += input[-1] + str(counter)
  
  return output
  
# print string_compression("aaaacbbbbbccc")

'''
==============================
LINKED LISTS
==============================
'''

# 2.1 
# Write code to remove duplicates from an unsorted linked list. 
# How would you solve this problem if a temporary buffer is not allowed?

# 2.2
# Implement an algorithm to find the kth to last element of a singly linked list.

# 2.3
# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
# Example
# Input: the node c from the linked list a -> b -> c -> d -> e
# Output: nothing is returned, but the new linked list looks like a -> b -> d -> e

'''
==============================
STACKS AND QUEUES
==============================
'''

# 3.1
# Describe how you could use a single array to implement three stacks.

# 3.2
# How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? 
# Push, pop, and min should all operate in O(1) time.

# 3.3
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
# and should create a new stack once the previous one exceeds capacity. 
# SetOfStacks.push() and SetOfStack.pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

'''
==============================
TREES AND GRAPHS
==============================
'''

# 4.1 
# Implement a function to check if a binary tree is balanced. For the purposes of this question, 
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

# 4.2
# GIven a directed graph, design an algorithm to find out whether there is a route between two nodes.

# 4.3
# Given a sorted (increasing order) array with unique integer elements, 
# write an algorithm to create a binary search tree with minimal height.

'''
==============================
BIT MANIPULATION
==============================
'''

# 5.1
# You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
# Write a method to insert M into N such that M starts at bit j and ends at bit i. 
# You can assume that the bits j through i have enough space to fit all of M.
# That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
# You would not, for example, have j = 3 and i = 2, because M could not fully fit
# EXAMPLE
# Input:   N = 10000000000, M = 10011, i = 2, j = 6
# Output:  N = 10001001100

# 5.2
# Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double,
# print a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bits in their binary representation.

# 5.3
# Given a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bits in their binary representation.

'''
==============================
SORTING AND SEARCHING
==============================
'''

# 11.1 
# You are given two sorted arrays, A and B, where A has a large enough buffer 
# at the end to hold B. Write a method to merge B into A in sorted order.

# 11.2
# Write a method to sort an array of strings so that all the anagrams are next to each other.

# 11.3
# Given a sorted array of n integers that has been rotated an unknown number of times, 
# write code to find an element in the array. You may assume that the array was originally sorted in increasing order.
# Example
# Input: find 5 in [15, 16, 19, 20, 25, 1 , 2, 3, 4, 5, 7, 10, 14]
# Output: 8 (the index of 5 in the array)





