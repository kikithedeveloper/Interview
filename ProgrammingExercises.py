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

	def delete(self,pos):

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


# l = LinkedList()

# l.append(5)

# l.append(10)

# l.append(3)

# l.append(200)

# l.append("hello")

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

# l.insert("Hello", 4)

# l.delete(3)

# l.delete(4)

# l.removeDuplicate()

# l.findkth(4)

# l.deleteNode("hello")

# l.partition(79)

# l.traverse()

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
			print self.root.data

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
						print n.left.data
						done = True
				elif data > n.data:
					if n.right:
						# print n.data
						n = n.right
					else:
						n.right = Node(data)
						print n.right.data
						done = True
				else:
					print "Data already exists."



		# if self.root is None:
		# 	self.root = Node(data)
		# else:
	# 		root = self.root

	# 	if root.data > data:
	# 		if root.left is None:
	# 			root.left = Node(data)
	# 		else:
	# 			root.left.insert(data)

	# 	if root.data < data:
	# 		if root.right is None:
	# 			root.right = Node(data)
	# 		else:
	# 			root.right.insert(data)

	# 	if root.data == data:
	# 		print "data already exist"

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

	# Print the value of every node you find with DFS and BFS.

	# In-Order Traversal
	def dfs(self):

		if self.root is None:
			return None
		else: 
			node = self.root

		print node.data

		if node:
			dfs(node.left)
			print node.data
			dfs(node.right)


			

		# if node:
		# 	dfs(node.left)
		# 	print node.data
		# 	dfs(node.right)

		# if node:
		# 	dfs(node.left)
		# 	print node.data
		# 	dfs(node.right)


# def inorder(t):
#     if t.left:
#         for elem in inorder(t.left):
#             print elem
#     print t
#     if t.right:
#         for elem in inorder(t.right):
#             print elem


	def in_order_list(self, r = []):
		hasLeft = self.left is not None
		hasRight = self.right is not None
		if self is None:
			return
		else:
			if hasLeft:
				self.left.in_order_list(r)
			r.append(self.value)
			if hasRight:
				self.right.in_order_list(r)
		return r


# tree = BinaryTree()

# tree.insert(5)

# tree.insert(4)

# tree.insert(6)

# tree.insert(7)

# tree.insert(2)

# tree.insert(1)

# print tree.getLeft()

# print tree.getRight()

# tree.dfs()

# dfs(tree)

# tree.in_order_list()


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

# print factorial(5)

#__________________________________________

# Count the number of elements in the list l 
# without using loops or the len() function
def count_list_length(l):
	
    if l:
    	return 1 + count_list_length(l[1:])

    return 0

print count_list_length([1,2,3,4,5])

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________

#__________________________________________