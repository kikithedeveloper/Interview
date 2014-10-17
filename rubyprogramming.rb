# Ruby Skills 1

# Things you should be able to do in Ruby! :-)

number_list = [-5, 6, 4, 8, 15, 16, 23, 100, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list)
    newlist = []
    number_list.each do |n|
        if n.odd?
            newlist << n
        end
    end
    return newlist
end

# puts all_odd(number_list).inspect

#__________________________________________

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list)
    newlist = []
    number_list.each do |n|
        if n.even?
            newlist << n
        end
    end
    return newlist
end

# puts all_even(number_list).inspect

#__________________________________________

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list)
    newlist = []
    word_list.each do |word|
        if word.length >= 4
            newlist << word
        end
    end
    return newlist
end

# puts long_words(word_list).inspect

#__________________________________________

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list)
    smallest = number_list[0]
    number_list.each do |n|
        if n < smallest
            smallest = n            
        end        
    end
    return smallest
end

# puts smallest(number_list)

#__________________________________________

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list)
    largest = number_list[0]
    number_list.each do |n|
        if n > largest
            largest = n
        end
    end
    return largest
end

# puts largest(number_list)

#__________________________________________

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list)
    newlist = []
    number_list.each do |n|
        n = n / 2.0
        newlist << n
    end
    return newlist
end

# puts halvesies(number_list).inspect

#__________________________________________

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list)
    newlist = []
    word_list.each do |word|
        newlist << word.length
    end
    return newlist
end

# puts word_lengths(word_list).inspect

#__________________________________________

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list)
    sum_total = 0
    number_list.each do |n|        
        sum_total += n
    end
    return sum_total
end

# puts sum_numbers(number_list)

#__________________________________________

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list)
    total = 1
    number_list.each do |n|
        total *= n
    end
    return total
end

# puts mult_numbers(number_list)

#__________________________________________

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list)
    newstring = ""
    word_list.each do |word|
        newstring << "#{word} "
    end
    return newstring
end

# puts join_strings(word_list)

#__________________________________________

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list)
    average = (sum_numbers(number_list)).to_f / number_list.length
    return average
end

# puts average(number_list)

#__________________________________________


# Ruby Skills 2

string1 = "I do not like green eggs and ham or blue eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1)
	hash = Hash.new
	array = string1.split
	# puts array.inspect
	array.each do |word|
		if hash.include?(word)
			hash[word] += 1
		else
			hash[word] = 1
		end
	end
	return hash.inspect
end

# puts count_unique(string1)

#__________________________________________

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2)
	array = Array.new
	# puts array.inspect
	list1.each do |x|
		list2.each do |y|
			if x == y
				array << x
			end
		end
	end

	return array.inspect
end

# puts common_items(list1, list2)

#__________________________________________

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items(list1, list2)
	hash = Hash.new
	array = Array.new
	# puts array.inspect
	list1.each do |n|
		hash[n] = true		
	end
	list2.each do |n|
		if hash.include?(n)
			array << n
		end
	end
	return array.inspect
end

# puts common_items(list1, list2)

#__________________________________________

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1)
	hash = Hash.new
	array = Array.new
	list1.each do |n|
		hash[n] = true
	end
	hash.each do |key, val|
		if hash[key*-1]
			array << key
		end
	end
	return array.inspect
end

# puts sum_zero(list1)

#__________________________________________

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words)
	hash = Hash.new
	array = Array.new
	words.each do |word|
		if hash.include?(word)
			hash[word] += 1
		else
			hash[word] = 1
		end
	end
	hash.each do |k,v|
		if v == 1
			array << k
		end
	end
	# puts hash.inspect
	return array.inspect
end

# puts find_duplicates(words)

#__________________________________________

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""

def word_length(words)
	hash = Hash.new
	words.each do |word|
		if hash.include?(word.length)
			hash[word.length] += [word]
		else
			hash[word.length] = [word]
		end
	end
	hash.each do |k,v|
		v.each { |x| puts x }
	end
	return nil
end

# word_length(words)

#__________________________________________


l = [1,2,3,4,5,6,7,8,9,10]
string = ["me", "love", "Chi Ming Pun"]
strChi = "Chi Ming Pun"


"""
1) Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""

def reverse(arr)
	for i in 0..(arr.length/2)
		temp = arr[i]
		arr[i] = arr[-i-1]
		# puts "one", l.inspect
		arr[-i-1] = temp
		# puts "two", l.inspect
	end
	return arr.inspect
end

# puts reverse(l)
# puts reverse(string)
# puts reverse("Chi Ming Pun")

#__________________________________________

"""
2) Given dictionary d, print out the key-value pairs 
in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""

h = {"q"=>5, "m"=>3, "z"=>2, "a"=>10}

def printHash(hash)

	hash.sort.each do |key,value|
  		puts "#{key}=>#{value}"
	end

end

# printHash(h)

#__________________________________________


"""
3) Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 4, 6, 8, 10]
l2 = [93, 4, 23, 10, 66]

def combine(arr1, arr2)
	array = arr1+arr2
	array = array.uniq
	return array.inspect
end

# puts combine(l1, l2)

#__________________________________________


# """
# 6) Given the string s, produce a list composed of all the single characters from the original string
# eg:
#     s = "Hello"
#     becomes
#     l = {"H", "e", "l", "l", "o"}
# """
s = "Hi there, my name is Slim"

def array(s)
	s = s.split("")
	p(s)
end

# array(s)

#__________________________________________

# """
# 8) Given two dictionaries, d1 and d2, update the contents of d1 with the contents of d2, overwriting any existing keys
# eg:
#     d1 = {"a":1, "b":2}
#     d2 = {"a":3, "c":4}

#     becomes

#     d1 = {"a":3, "b":2, "c":4}
# """
d1 = {"a"=>5, "c"=>7, "d"=>9, "q"=>15}
d2 = {"a"=>6, "e"=>13, "g"=>6, "q"=>1}

def updateHash(d1,d2)
	d2.each do |k,v|
		d1[k] = v
	end
	return d1.inspect
end

# puts updateHash(d1,d2)

#__________________________________________

# """
# 9) Given two dictionaries, d1 and d2, merge the contents of d1 with the contents of d2, adding to the values of existing keys
# eg:
#     d1 = {"a": 1, "b":2}
#     d2 = {"a": 3, "d": 4}

#     becomes

#     d1 = {"a": 4, "b":2, "d":4}

# """

h1 = {"a"=>5, "c"=>7, "d"=>9, "q"=>15}
h2 = {"a"=>6, "e"=>13, "g"=>6, "q"=>1}

def merge(d1,d2)
	d2.each do |k,v|
		if d1.include?(k)
			d1[k] += v
		else
			d1[k] = v
		end
	end
	return d1.inspect
end

# puts merge(h1,h2)

#__________________________________________


# 10) print out line with their line number by new line

mystr = "Sorry,\nMy people need me\nI must go"

# prints

# 1. Sorry,
# 2. My people need me
# 3. I must go.

def newline(mystr)
	mystr = mystr.split("\n")
	mystr.each do |line|
		puts "#{mystr.index(line)+1}. #{line}"
	end
end

# newline(mystr)


#__________________________________________

# """
# 11) Write a function with the following signature:
#     title(str) -> str

# It should take a string and capitalize it according to book title rules
#     eg:
#     title("a tale of two cities")
#         => A Tale of Two Cities
# """

def title(my_title)
    my_title = my_title.split(" ")
    my_title.each do |word|
    	word.capitalize!
    end
    my_title = my_title.join(" ")
    return my_title
end

# puts title("a tale of two cities")


#__________________________________________


# LINKED LIST

# Implement a singly linked list from scratch

# class Node
#   attr_accessor :data, :next

#   def initialize(data)
#     @data = data
#   end
# end

class Node
	attr_accessor :data, :next

	def initialize(data)
		@data = data
		@next = nil
	end
end

class LinkedList
	attr_accessor :head, :tail

	def initialize
		@head = nil
		@tail = nil
	end

	# append at the end of the linked list
	def append(data)
		
		node = Node.new(data)

		if @head == nil
			@head = node
			@tail = node
		else
			# # Here you can use a while loop to go to the end of the linked list and append it there.
			# n = @head
			# while n.next 
			# 	n = n.next
			# end
			# n.next = node

			# OR use the tail to append it there
			@tail.next = node
			@tail = node
		end

	end

	# insert at a specific location in the linked list
	def insert(data,pos)
		node = Node.new(data)
		n = @head

		if pos == 0
			node.next = n
			@head = node
		else
			counter = 1

			while counter < pos
				n = n.next
				counter += 1
			end

			if n.next != nil
				node.next = n.next
				n.next = node

			else
				n.next = node
			end
		end
	end

	# Remove duplicates from an unsorted linked list.
	def removeDuplicate
		n = @head
		hash = {n.data=>true}

		while n.next != nil
			if hash.include?(n.next.data)
				if n.next.next != nil
					n.next = n.next.next
				else
					@tail = n
					n.next = nil
				end

			else
				hash[n.next.data] = true
				n = n.next
			end
		end
	end

	# Implement an algorithm to find the kth to the 
	# last element of a singly linked list.
	def findkth(k)
		n = @head
		kth = @head
		go = k
		count = 1

		while n
			if count <= go
				n = n.next
				count += 1
			else
				n = n.next
				kth = kth.next
			end
		end

		puts "The #{k}th element to the last is " + kth.data.to_s

	end

	def delete(data)
		n = @head

		if n.data == data
			@head = @head.next
		else
			while n.next	
				if (n.next).data == data
					n.next = (n.next).next
				else
					n = n.next
				end
			end
		end
	end

	def delete_at(pos)
		n = @head

		if pos == 0
			@head = n.next
			temp = n
		else
			counter = 0

			while counter < (pos-1)
				n = n.next
				counter += 1
			end

			temp = n.next
			n.next = n.next.next # points to either another node or nil

			if n.next.nil?
				@tail = n
			end
		end

		puts "Removed the node #{temp.data} at index #{pos}. "
	
	end


	def traverse
		n = @head
		while n
			puts n.data
			n = n.next
		end
	end


end

l = LinkedList.new # pass!

# l.append(1) # pass!

# l.append("meow")

# l.append(3)

# l.append("bark")

# l.append(5)

# # testing to remove duplicates

# l.append("meow")

# l.append(1)

# l.removeDuplicate() # pass!

# l.insert("hello", 0) # pass!

# l.findkth(2) # pass!

# l.delete(5) # pass! 

# l.append("A")
# l.append("B")
# l.append("C")
# l.append("D")
# l.append("E")

# l.delete_at(0) # remove 1st node A - pass!

# l.delete_at(1) # remove the 2nd node B - pass!

# l.delete_at(4) # remove the 5th node E - pass!

l.traverse() 

#__________________________________________

# Binary Search Tree

class Node
	attr_accessor :data, :left, :right

	def initialize(data)
		@data = data
		@left = nil
		@right = nil
	end
end

class BinaryTree
	attr_accessor :root

	def initialize
		@root = nil
	end

	# insert a node in the tree
	def insert(data)
		
		node = Node.new(data)

		if @root == nil
			@root = node
		
		else
			n = @root
			done = false

			while done != true
				if data < n.data
					if n.left
						n = n.left
					else
						n.left = node
						done = true
					end
				elsif data > n.data
					if n.right
						n = n.right
					else
						n.right = node
						done = true
					end
				else
					puts "data already exists."
				end
			end
		end
	end

	def findLeft(root)
		
		if root == nil
			return
		else	
			while root

				if root.left == nil
					puts "The node at the very left is " + (root.data).to_s
				end

				root = root.left

			end
		end
	end

	def findRight(root)
		if root == nil
			return
		else
			while root
				
				if root.right == nil
					puts "The node at the very right is " + (root.data).to_s
				end

				root = root.right

			end
		end
	end

	def preorder(node)
		if node == nil
			return
		else
			puts node.data
			self.preorder(node.left)
			self.preorder(node.right)
		end
	end

	def inorder(node)
		if node == nil
			return
		else
			self.inorder(node.left)
			puts node.data
			self.inorder(node.right)
		end
	end

	def postorder(node)
		if node == nil
			return
		else
			self.postorder(node.left)
			self.postorder(node.right)
			puts node.data
		end
	end

	def dfsWhile(target)
		n = @root
		while n
			if n.data == target
				found = true
				return true
			end

			if n.data < target
				n = n.right
			else
				n = n.left
			end
		end
		return false
	end

	def bfs(target)

		q = [@root]

		begin
			while q
				n = q.pop()
				
				if n.data == target
					return true
				end

				if n.left
					q.push(n.left)
				end

				if n.right
					q.push(n.right)
				end
			end
		rescue NoMethodError
		end
		return false
	end

end

# t = BinaryTree.new

# t.insert(5)

# t.insert(3)

# t.insert(7)

# t.insert(2)

# t.insert(4)

# t.insert(1)

# t.insert(6)

# t.insert(8)

# t.insert(10)

# t.insert(9)

# t.findLeft(t.root)

# t.findRight(t.root)

# t.preorder(t.root)

# t.inorder(t.root)

# t.postorder(t.root)

# puts t.dfsWhile(10) # return true

# puts t.dfsWhile(15) # return false

# puts t.bfs(5) # return true

# puts t.bfs(11) # return false

#__________________________________________

# Implement a Stack in Ruby


class Stack
	
	def initialize
		@elements = []
	end

	def length
		puts @elements.length
	end

	def push(x)
		@elements.push(x)
	end

	def pop
		puts @elements.pop
	end

	def peek
		puts @elements[-1]
	end

	def print
		puts @elements.inspect
	end

end

# stack = Stack.new

# stack.push("A")

# stack.push("B")

# stack.push("C")

# stack.print

# stack.pop

# stack.print

# stack.peek

# stack.length

# stack.push("D")

# stack.push("E")

# stack.push("F")

# stack.print

# stack.length


#__________________________________________

class Queue
	
	def initialize
		@elements = []
	end

	def length
		puts @elements.length
	end

	def push(x)
		@elements.insert(0,x)
	end

	def pop
		puts @elements.pop
	end

	def peek
		puts @elements[-1]
	end

	def print
		puts @elements.inspect
	end

end

# q = Queue.new

# q.push("A")

# q.push("B")

# q.push("C")

# q.print

# q.pop

# q.print


#__________________________________________

# Fibonacci
# Recursively

def fib(n)
	if n <= 1
		return n
	else
		return fib(n-1) + fib(n-2)
	end
end

# puts fib(0)
# puts fib(1)
# puts fib(2)
# puts fib(3)
# puts fib(4)
# puts fib(5)
# puts fib(6)
# puts fib(7)
# puts fib(10)

#__________________________________________

# Fibonacci 
# while loop

def fib(n)
	
	if n <= 1
		puts n
	else	
		first = 0
		second = 1
		counter = 0

		while counter < n	
			third = first + second
			puts third
			
			first = second
			second = third
			
			counter += 1
		end	
	end
end

# fib(10) 

#__________________________________________

# return the factorial of n

def factorial(n)
	if n == 0
		return 1
	else
		return n * factorial(n-1)
	end
end

# puts factorial(6)

#__________________________________________

# need to figure out why it's not working....

def length(arr, l)
	if arr.length > 1
		return length(arr[1,arr.length], l+1)
	else
		return l
	end
end

# puts length([],0)

# puts length([1,2,3,4,5],0)

#__________________________________________

arr = ["a", "b", "c", "d", "e"]

# p(arr)

# p(arr[0,arr.length-1])

# p(arr[0..arr.length-2])

# p(arr[0..arr.length-3])

# p(arr[0..-1])

#__________________________________________

def palindrome(l)

	if l.length <= 1
		return true
	end

	if l[0] == l[-1]
		return palindrome(l[1..-2])
	end

	return false
end

# puts palindrome("aviva")

# puts palindrome("kimberly")

#__________________________________________


def find(l,i)
	if l
		if i == l[0]
			return l[0]
		end

		return find(l[1..-1],i) 
	end
	return "nil"
end

l = [1,2,3,4,5,6,7,8,9,10]

# puts find(l,10)

# puts find(l,11)


#__________________________________________

def fold_paper(width,height,folds)
	
	width = width.to_f
	height = height.to_f

	if folds == 0
		return "#{width}, #{height}"
	end
	if width <= height
		# puts width,height
		return fold_paper(width, height/2, folds-1)
	else
		# puts width,height
		return fold_paper(width/2, height, folds-1)
	end
end

# puts fold_paper(11, 8, 2)

# puts fold_paper(11, 8, 10)

#__________________________________________

# count the sum of the elements in the list

l = [1,2,3,4,5,6,7,8,9,10]

def sum_list(l)
	if l
		puts l[0]
		return l[0] + sum_list(l[1..-1])
	end
	return 0
end

# puts sum_list([1,2,3,4,5,6,7,8,9,10])

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

