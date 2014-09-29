# STRING AND ARRAY

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

# print reverse("ChiMing") ## returns "ginMihC".

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

# Write a recursive function for generating all permutations 
# of an input string. Return them as an array.

def get_permutations(string):
	# base case
	if len(string) <= 1:
		return [string]

	all_chars_except_last = string[:-1]
	last_char = string[-1]
	
	# recursive call: get all possible permutations for all chars except last
	permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
	
	# put the last char in all possible positions for each of the above permutations
	possible_positions_to_put_last_char = range(len(all_chars_except_last)+1)
	permutations = []
	for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
		for position in possible_positions_to_put_last_char:
			permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
			permutations.append(permutation)
	return permutations

# print get_permutations("Hello")

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

# print replace_spaces("Kim love Chi  ")


#__________________________________________

# 1.5
# Implement a method to perform basic string compression 
# using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the 
# original string, your method should return the original
# string. You can assume the string has only upper and 
# lower case letters (a - z).

def compress (string):

	compressedStr = ""

	count = 1

	for i in range(len(string)):

		if i == len(string)-1:
			newStr = string[i] + str(count)
			compressedStr += newStr

		else:

			if string[i] != string[i+1]:
				newStr = string[i] + str(count)
				compressedStr += newStr
				count += 1

	return compressedStr

# print compress("aabccccczzzzzaaaaa")

#__________________________________________

# Determine if an integer is whole number, x = x**2
# Example. 4 = 2^2. 9 = 3^2. 16 = 4^2.

import math

def is_square(integer):
	number = math.sqrt(integer)
	if int(number + 0.5)**2 == integer: 
		return True
	else:
		return False

# for i in range(4, 20):
#    print i, is_square(i)

#__________________________________________

# LINKED LIST

# Implement a singly linked list from scratch

class Node(object):

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def append(self,data):

		n = Node(data)

		if not self.head:
			self.head = n
			self.tail = n

		else: 
			self.tail.next = n
			self.tail = n

	def insert(self,data,pos):

		new_node = Node(data)
		n = self.head

		if pos == 0:
			new_node.next = n
			self.head = new_node

		else:

			counter = 1

			while counter < pos:
				n = n.next
				counter += 1

			if n.next != None:
				new_node.next = n.next
				n.next = new_node

			else:
				n.next = new_node

	def traverse(self):

		n = self.head

		while n:
			print n.data
			n = n.next

	def delete_at(self,pos):

		n = self.head

		counter = 1

		while (counter < (pos-1)):
			n = n.next
			counter += 1

		if n.next.next != None:
			n.next = n.next.next
			n = n.next
			del(n)

		else:
			self.tail = n
			n = n.next
			del(n)


	# 2.1
	# Write code to remove duplicates from an unsorted linked list.
	# FOLLOW UP. How would you solve this problem if a temporary
	# buffer is not allowed?

	def removeDuplicate(self):

		n = self.head

		unique = {n.data: True}

		while n.next:
		
			if n.next.data not in unique:

				unique[n.next.data] = True

				n = n.next

			else:

				if n.next.next != None:
					n.next = n.next.next

				else:
					self.tail = n
					n.next = None

	# 2.2
	# Implement an algorithm to find the kth to the 
	# last element of a singly linked list.

	def findkth(self, k):

		n = self.head

		kth = self.head

		go = k

		count = 1

		while n:
			if count <= go:
				n = n.next
				count += 1
			else:
				n = n.next
				kth = kth.next

		print "The kth to the last element is " + str(kth.data)

	# 2.3
	# Implement an algorithm to delete a node in the middle
	# of a singly linked list, given only access to that node.
	# Example. Input: the node c from the linked list, a-b-c-d-e.
	# Output: return nothing, but the linked list is now a-b-d-e.

	def deleteNode(self,data):

		n = self.head

		if n.data == data:
			self.head = n.next
			print "deleted the node " + str(n.data)
			del(n)

		else:

			while n.next:

				if n.next.data == data:
					print "deleted the node " + str(n.next.data)					
					n.next = n.next.next

				else:
					n = n.next

	# 2.4 
	# Write code to partition a linked list around a value x, 
	# such that all nodes less than x come before all nodes 
	# greater than or equal to x.

	def partition(self, x):

		n = self.head

		left, middle, right = [], [], []

		while n:

			if n.data < x:
				left.append(n.data)

			elif n.data > x:
				right.append(n.data)

			else:
				middle.append(n.data)

			n = n.next

		whole = left + middle + right

		print "left: ", left
		print "middle: ", middle
		print "right: ", right
		print "whole: ", whole

		newList = LinkedList()

		for data in whole:

			node = Node(data)

			if whole[0]:
				newList = node
				print node.data

			else:
				newList.next = node
				print node.data

	# def reverse(self):
	# 	current = self.head
	# 	previous = None
	# 	next = None

	# 	# until we have 'fallen off' the end of the list
	# 	while (current is not None):

	# 		# copy a pointer to the next element 
	# 		# before we overwrite current.next
	# 		next = current.next

	# 		# reverse the 'next' pointer
	# 		current.next = previous

	# 		# step forward in the list
	# 		previous = current
	# 		current = next

	# 	return previous

# l = LinkedList()

# l.append(1)

# l.append(2)

# l.append(3)

# l.append(4)

# l.append(5)

# # l.reverse()

# l.traverse()

# l.append(3)

# l.append(4)

# l.append(4)

# l.append(5)

# l.append(40)

# l.append(79)

# l.append(70)

# l.append(9)

# l.append(100)

# l.append(5)

# l.append(5)

# l.insert("Hello", 0)

# l.delete_at(3)

# l.delete_at(4)

# l.removeDuplicate()

# l.findkth(4)

# l.deleteNode("hello")

# l.partition(79)

l.traverse()




#__________________________________________

# BINARY TREE

# Implement a tree from scratch.

class Node(object):
	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree():

	def __init__(self):
		self.root = None

	# class Node(object):
	
	# 	def __init__(self, data):
	# 		self.data = data
	# 		self.left = None
	# 		self.right = None

	def insert(self, data):

		if self.root is None:
			self.root = Node(data)
			# print self.root.data

		else:

			n = self.root
			done = False

			while not done:
				if data < n.data:
					if n.left:
						# print n.data
						n = n.left
					else:
						n.left = Node(data)
						# print n.left.data
						done = True
				elif data > n.data:
					if n.right:
						# print n.data
						n = n.right
					else:
						n.right = Node(data)
						# print n.right.data
						done = True
				else:
					print "Data already exists."

	def getLeft(self):

		if self.root is None:
			return None
		
		else:
			root = self.root

			while root:

				if root.left is None:
					return "The node at the very left is " + str(root.data)

				root = root.left

	def getRight(self):

		if self.root is None:
			return None

		else:
			root = self.root

			while root:

				if root.right is None:
					return "The node at the very right is " + str(root.data)

				root = root.right

	# Pre-Order Traversal
	def preorder(self, node):

		if node == None:
			return
		else:
			print node.data
			self.preorder(node.left)
			self.preorder(node.right)

	# In-Order Traversal
	def inorder(self, node):
		if (node == None):
			return
		else:
			self.inorder(node.left)
			print(node.data)
			self.inorder(node.right)		

	# Post-Order Traversal
	def postorder(self,node):
		if node == None:
			return 
		else:
			self.postorder(node.left)
			self.postorder(node.right)
			print node.data

	def dfsWhile(self,target):

		n = self.root

		while n:

			if n.data == target:
				found = True
				return True

			if n.data > target:
				n = n.left

			if n.data < target:
				n = n.right

		return False

	def bfs(self, target):

		q = []

		q.append(self.root)

		while q:

			n = q.pop()

			if n.data == target:
				return True

			if n.left:
				q.append(n.left)

			if n.right:
				q.append(n.right)

		return False

	# I don't know how to work this... :-( Get help.
	# def dfsRecursive(self, node, target):

	# 	n = node

	# 	if n is None:
	# 		return None

	# 	if n.data == target:
	# 		return True

	# 	if n.data > target:
	# 		return self.dfsRecursive(n.left, target)

	# 	else:
	# 		return self.dfsRecursive(n.right, target)


tree = BinaryTree()

tree.insert(5)

tree.insert(4)

tree.insert(6)

tree.insert(7)

tree.insert(2)

tree.insert(1)

# print tree.getLeft()

# print tree.getRight()

# tree.dfs(tree.root)

# tree.inorder(tree.root)

# tree.preorder(tree.root)

# tree.postorder(tree.root)

# dfs(tree)

# tree.in_order_list()

# print tree.bfs(7)

# print tree.dfsWhile(4)




#__________________________________________

# RECURSION

# Fibonacci

def fib(n):

	if n <= 1:
		
		return n

	else:

		return fib(n-1) + fib(n-2)

# print fib(0)
# print fib(1)
# print fib(2)
# print fib(3)
# print fib(4)
# print fib(5)
# print fib(6)
# print fib(7)

#__________________________________________

# Multiply all the elements in a list using recursion
def multiply_list(l):

	if len(l) == 1:
		return l[0]

	return l[0] * multiply_list(l[1:])

# print multiply_list([1,2,3,4,5])

#__________________________________________

# Return the factorial of n
def factorial(n):
	if n == 0:
		return 1 # 1 is still a factorial of 0.
	else:
		return n * factorial(n-1)

# print factorial(3)

#__________________________________________

# Count the number of elements in the list l 
# without using loops or the len() function
def count_list_length(l):
	
	if l:
		return 1 + count_list_length(l[1:])

	return 0

# print count_list_length([1,2,3,4,5])

#__________________________________________

# Sum all of the elements in a list without 
# using loops or the sum() function
def sum_list(l):
	
	if l:
		return l[0] + sum_list(l[1:])

	return 0

# print sum_list([1,2,3,4,5,6,7,8,9,10])

#__________________________________________

# Reverse a list recursively without loops, 
# the reverse() function or list[::-1]
def reverse(l):

	if l:
		temp = l[0]
		l[0] = l[-1]
		l[-1] = temp
		print l
		return reverse(l[1:-1])

# reverse([1,2,3,4,5,6,7,8,9,10])

#__________________________________________

# Fibonacci

def fib(n):

	if n <= 1:
		
		return n

	else:

		return fib(n-1) + fib(n-2)

# print fib(0)
# print fib(1)
# print fib(2)
# print fib(3)
# print fib(4)
# print fib(5)
# print fib(6)
# print fib(7)

#__________________________________________

# Finds the item i in the list l.... RECURSIVELY
# Return the item if it is in the list or None if not found.
def find(l, i):
	
	if l:

		if i == l[0]:
			return l[0]

		return find(l[1:],i)

	return None

l = [1,2,3,4,5,6,7,8,9,10]

# print find(l, 10)

#__________________________________________

# Determines if a string is a palindrome
# A palindrome is any string that is the 
# same forwards and backwords.
# (e.g. radar, racecar, aibohphobia)
# Solve recursively.

def palindrome(l):
	
	if len(l) <= 1:
		return True

	if l[0] == l[-1]:
		return palindrome(l[1:-1])

	return False

# print palindrome("aviva")

# print palindrome("kimberly")

#__________________________________________

# Given the width and height of a sheet of paper, and the number of times to fold it,
# return the final dimensions of the sheet as a tuple. 
# NOTE: Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
	
	if folds == 0:

		return (width, height)

	if width <= height:

		print (width, height)
		return fold_paper(width, height/2, folds-1)

	else:
		print (width, height)
		return fold_paper(width/2, height, folds-1)

# print fold_paper(11, 8, 5)

#__________________________________________

# Count up
# Print all the numbers from 0 to target.
# Use n to keep track of where you're at
# ex, to count from 1 - 100, call count_up(100, 1)
#
# Note: we don't have a test case for this one, so just run this
#       script directly
#
# Note #2: We're printing out the numbers, so this script does not 
#          need to return anything!
def count_up(target, n):
	
	if n == target:
		print n

	else:
		print n
		return count_up(target,n+1)

# count_up(100, 0)

#__________________________________________

# Python Lambda Functions

def increment (n): 
	return lambda x: x + n

f = increment(2)
g = increment(6)

# print f(42), g(42)
# print increment (22) (33)

#__________________________________________

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print filter(lambda x: x % 3 == 0, foo)
# print map(lambda x: x * 2 + 10, foo) 
# print reduce(lambda x, y: x + y, foo)

#__________________________________________

nums = range(2,50)
for i in range(2,8):
	nums = filter(lambda x: x==i or x % i, nums)
# print nums

#__________________________________________

sentence = "It is raining cats and dogs"
words = sentence.split()
# print words

# return the length of each word
length = map(lambda word: len(word), words)
# print length

#__________________________________________

# same thing, but in one line
# print map(lambda w: len(w), "it is raining cats and dogs".split())

student_tuples = [
	('ChiMing', 'F', 28), # how sad...!
	('Kimberly', 'F', 24), # in the same boat TT_TT
	('john', 'A', 15),
	('jane', 'B', 12),
	('dave', 'B', 10),
]

age = sorted(student_tuples, key=lambda student: student[2]) #sort by age

# print age

#__________________________________________

# SORTING ALGORITHMS

# MergeSort

def merge(left, right):
	result = []
	i ,j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def mergesort(list):
	if len(list) < 2:
		return list
	middle = len(list) / 2
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])
	return merge(left, right)

# print mergesort([6,3,1,2,4,5,7,0])

# def merge(left, right):
#     result = []
#     i ,j = 0, 0
#     while i < len(left) and j < len(right):
#         print('left[i]: {} right[j]: {}'.format(left[i],right[j]))
#         if left[i] <= right[j]:
#             print('Appending {} to the result'.format(left[i]))           
#             result.append(left[i])
#             print('result now is {}'.format(result))
#             i += 1
#             print('i now is {}'.format(i))
#         else:
#             print('Appending {} to the result'.format(right[j]))
#             result.append(right[j])
#             print('result now is {}'.format(result))
#             j += 1
#             print('j now is {}'.format(j))
#     print('One of the list is exhausted. Adding the rest of one of the lists.')
#     result += left[i:]
#     result += right[j:]
#     print('result now is {}'.format(result))
#     return result

# def mergesort(L):
#     print('---')
#     print('mergesort on {}'.format(L))
#     if len(L) < 2:
#         print('length is 1: returning the list withouth changing')
#         return L
#     middle = len(L) / 2
#     print('calling mergesort on left {}'.format(L[:middle]))
#     left = mergesort(L[:middle])
#     print('calling mergesort on right {}'.format(L[middle:]))
#     right = mergesort(L[middle:])
#     print('Merging left: {} and right: {}'.format(left,right))
#     out = merge(left, right)
#     print('exiting mergesort on {}'.format(L))
#     print('#---')
#     return out


# mergesort([6,2,4,3,5,1])

#__________________________________________

# Bubble Sort

def bubblesort(list):

	for j in range(len(list)-1,0,-1):
		for i in range(j):
			# print list[i], list[i+1]
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp

	return list

list = [54,26,93,17,77,31,44,55,20]
# print bubblesort(list)

#__________________________________________

def fizzbuzz(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
  
    for i in range(1,n+1):
      
        if i % 15 == 0:
            print "FizzBuzz"
        elif i % 5 == 0:
            print "Buzz"
        elif i % 3 == 0:
            print "Fizz"
       	else:
       		print i

# fizzbuzz(15)

# def fizzbuzz(n):
#     # Write your code here.
#     for i in range(1, n+1):
#         print "Fizz"*(i%3 == 0) + "Buzz"*(i%5 == 0) or i

# fizzbuzz(15)

#__________________________________________

def find_missing_number(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    firstList = v
    secondList = range(1,len(v)+2)

    d=collections.defaultdict(int)

    for num in firstList:
    	d[num]+=1

    for num in secondList:
    	if d[num] == 0:
    		return num
    	else:
        	d[num]-=1

# print find_missing_number([1,2,3,4,6])


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

# Coding exercises for LaunchCode

def LaunchCode(n):
	
	# better start with the highest then to lowest.
	
	for i in range(1, n+1):
		
		if i % 56 == 0:
			print "LaunchCodeSTL"
		
		elif i % 4 == 0 and i % 7 == 0:
			print "LaunchCode"
		
		elif i % 7 == 0:
			print "Code"
		
		elif i % 4 == 0:
			print "Launch"
		
		else:
			print i

# LaunchCode(60)

# def findKdiff(n, k):

# 	intList = (list(range(1,n+1)))

# 	intList.reverse()

# 	pairs = 0

# 	for i in intList:
# 		for j in intList:
# 			if i - j == k:
# 				print (i,j)
# 				pairs += 1

# 	print "The total pairs are " + str(pairs)

# findKdiff(5,2)

# Find the difference of K

def findKdiff(n, k):

	intList = n

	intList.reverse()

	pairs = 0

	for i in intList:
		for j in intList:
			if i - j == k:
				print (i,j)
				pairs += 1

	#print "The total pairs are " + str(pairs)
	print pairs

# findKdiff([363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254, 879792181, 1069262793],1)



def getIntegerComplement(n):

	# print bin(n) 110010   -> 011011

	# print bin(50) # 110010 -> 001101
 
	# print int('001101', 2)

	# print n

	# print bin(n)

	intList = list(bin(n))

	newList = intList[2:]

	# print newList

	for i in range(len(newList)):
		if newList[i] == '0':
			newList[i] = '1'
		elif newList[i] == '1':
			newList[i] = '0'

	inverseBin = "".join(newList)

	# print inverseBin

	print int(inverseBin, 2)


# getIntegerComplement(100)


#__________________________________________

def findTop10ID (filetext):

	filename = open(filetext) # open the file

	fileStrip = filename.read().splitlines() # removes the \n

	idDict = {} # declare an empty dict
 
	for i in fileStrip: # count to idDict
		if i in idDict:
			idDict[i] += 1
		else:
			idDict[i] = 1

	print idDict

	val = 0 # declare an empty val

	for i in idDict.values(): # finds the highest value
		if i > val:
			val = i

	topTen = False # declare a boolean value

	is10 = 0 # decare an empty counter

	idList = [] # declare an empty list

	while not topTen: # while loop

		for k, v in idDict.iteritems():

			if v >= val: 
				is10 += 1  # count to is10
				idList.append(k) # add to idList

				if is10 == 10: # if is10 reaches 10, then execute the block				
					print "The top ten IDs are: " + str(idList)
					topTen = True # return opposite boolean value to stop while loop

		# if it reaches here, then it means it doesn't have 10 ids.
		is10 = 0 # reset
		idList = [] # reset
		val -= 1 # subtract val by 1 to cover more ids.

# findTop10ID("ids.txt")
