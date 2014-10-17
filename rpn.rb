# Kimberly Lin
# Hackbright Graduate

# -------------------- ASSIGNMENT --------------------
# Implement a RPN evaluator in Ruby. It should be able to evaluate 
# the following strings and answer with the corresponding numbers:

#    “1 2 +” = 3
#    “4 2 /” = 2
#    “2 3 4 + *” = 14
#    “3 4 + 5 6 + *” = 77
#    “13 4 -” = 9

# And should provide an error message for the following types of errors:

#    “1 +” (not enough arguments)
#    “a b +” (invalid number)

# We should be able to evaluate a string from the command line in the following way:

#   $ ruby rpn.rb "1 2 +"

# Implement your own string to number conversion function. (Make your own functions from scratch).

# Do not use the following: 
#   send, eval, to_i, to_f, Integer(str), Float(str), or any similar method 
#   to convert your strings to numbers in your RPN evaluator.
#    You will definitely need "atoi" - converts an ASCII string to an integer. 
#       E.g., atoi("251") returns the integer 251.
#    You may also need "atof" - converts an ASCII string to a float. 
#       E.g., atof("341.72") returns the float 341.72.

# __________________________________________________________


class RPNCalculator

	def evaluate()
		
		print "Enter your math sequence: "
		sequence = gets.chomp.split()
		inputArray = []

		# if sequence.length < 3
		# 	puts "Not enough arguments"
		# else
		if sequence
			# puts sequence.inspect
			sequence.each do |i|
				# if i.match(/[a-zA-Z]/) != nil
				# 	puts "Invalid input"
				if i.match(/[0-9]/) != nil
					inputArray.push(i)
				else
				# 	# Order of Operations - Multiply or Divide before Add or Subtract
				# elsif i == "*"
				# 	inputArray.push(multiply(inputArray.pop(2)))
				# elsif i == "/"
				# 	inputArray.push(divide(inputArray.pop(2)))
				# elsif i == "+"
				# 	inputArray.push(add(inputArray.pop(2)))
				# elsif i == "-"
				# 	inputArray.push(subtract(inputArray.pop(2)))
				# 	puts "array: #{inputArray}"
				# 	puts "op: #{i}"
					
					# if i != "sum"
					# 	inputArray.push(operator(inputArray.pop(2), i))
					# else
						inputArray = operator(inputArray.pop(inputArray.length), i)
					# end
					

				end
			end


			if inputArray.length == 1
				# puts inputArray[0]
				# begin
				if !inputArray[0].nil?
					if inputArray[0] % 1 == 0 # check for decimals
						split = inputArray[0].to_s.split(".")
						puts atoi(split[0])
					else # no decimal, all go
						puts inputArray[0]
						# puts
					end
				end
				# rescue NoMethodError # avoid this error message1
				# end
			end
		end
	end

	# new method to make this more concise and shorter than 
	# having four methods using the same lines over and over
	def operator(array, operator)
		if operator != "sum"
			
			if array.length >= 2
				b, a = atof(array.pop), atof(array.pop)
				# puts "array: #{array}"
				# puts "op: #{operator}"
				# a = atof(array[0])
				# b = atof(array[1])
				# [2, 4, 5, '*', '+']
				# [4, 5] '*' ==> 20
				# [2, 4, 5] '*' ==> [2, 20]
				# [2, 20] '+'
				# if else stmts for operators
				result = if operator == "*"
				 a * b
				elsif operator == "/"
					a / b
				elsif operator == "+"
					a + b
				else #operator == "-"
					a - b
				end
			

				array.push(result)

				return array if !result.nil?

			# else
			# 	puts "Invalid input"

			end

		else

			num = 0

			array.each do |n|
				num += atof(n)
			end

			return [num]

		end	
	end

	# def add(array)
	# 	if array.length == 2
	# 		a = atof(array[0])
	# 		b = atof(array[1])
	# 		result = a + b
	# 		return result
	# 	else
	# 		puts "Invalid input"
	# 	end
	# end

	# def subtract(array)
	# 	if array.length == 2
	# 		a = atof(array[0])
	# 		b = atof(array[1])
	# 		result = a - b
	# 		return result
	# 	else
	# 		puts "Invalid input"
	# 	end
	# end

	# def multiply(array)
	# 	if array.length == 2
	# 		a = atof(array[0])
	# 		b = atof(array[1])
	# 		result = a * b
	# 		return result
	# 	else
	# 		puts "Invalid input"
	# 	end
	# end

	# def divide(array)
	# 	if array.length == 2
	# 		a = atof(array[0])
	# 		b = atof(array[1])
	# 		result = a / b
	# 		return result
	# 	else
	# 		puts "Invalid input"
	# 	end
	# end

	def atoi(strNum)
		
		# found = false
		
		# for i in strNum.split("")
		# 	if i == "."
		# 		found = true
		# 	end 
		# end

		# if found == true
		# 	ascii = strNum.bytes
		# 	puts ascii.inspect
		# 	asciiValue = ascii.map do |num|
		# 		num - 48 # 48 starts at 0 in ascii
		# 	end
		# 	print asciiValue
		# 	result = asciiValue.inject do |value, concat_to_value| 
		# 		tempValue = value * 10 # avoids overlapping
		# 		concatenate = tempValue + concat_to_value
		# 	end
		# else
			ascii = strNum.bytes
			# puts "bytes: #{ascii.inspect}"
			asciiValue = ascii.map do |num|
				num - 48 # 48 starts at 0 in ascii
			end
			# puts "converts to right number: #{asciiValue.inspect}"

			result = asciiValue.inject do |value, concat_to_value| 
				# puts "first value: #{value}"
				tempValue = value * 10 # avoids overlapping
				# puts "new value: #{tempValue}"
				concatenate = tempValue + concat_to_value
				# puts "concatenated together: #{concatenate}"
				# concatenate
			end
		# end
		return result
	end

	def atof(strNum) 
		
		found = false

		strNum = strNum.to_s
		
		# this validates whether or not it has a decimal
		for i in strNum.split("")
			# puts i
			if i == "."
				found = true
			end 
		end 

		# this will pass only if the string is validated
		if found == true
			array = strNum.split(".")
			# puts array
			a = atoi(array[0])
			# puts a
			b = atoi(array[1]) / (10.0 ** array[1].length) # this will ensure the right length in the decimal
			# puts b
			return a + b
		else
			convertFloat = atoi(strNum) + (0 / 10.0)
			return convertFloat		
		end

	end

end

rpn = RPNCalculator.new

# type in the terminal "ruby rpn.rb (insert your math sequence)"
rpn.evaluate() 

# test case no.1 - Pass!
	# i: 1 2 + 
	# o: => 3

# test case no.2 - Pass!
	# i: 4 2 / 
	# o: => 2

# test case no.3 - Pass!
	# i: 2 3 4 + * 
	# o: => 14

# test case no.4 - Pass!
	# i: 3 4 + 5 6 + * 
	# o: => 77

# test case no.5 - Pass!
	# i: “13 4 -” 
	# o: => 9

# test case no.6 - Pass!
	# i: 4 4 + 10 2 / * 4 4 + 10 2 / * + 
	# o: => 80

# test case no.7 - Pass!
	# i: 2.5 2.5 +
	# o: 5

# test case no.8 - Pass!
	# i: 2.5 2 -
	# o: 0.5

# test case no.9 - Pass!
	# i: 30 40 * 100 - 10 /
	#    ((30 * 40) - 100) / 10
	# o: 110

# test case no.10 - Pass!
  # i: 45243.235 10 / 200 - 500 + 2 *
	#   ((45243.235 / 10 ) - 200 + 500 ) * 2
	#    4524.3235 + 300
	# o: 9648.647

# test case no.11 - Pass!
	# i: 1 + 
	# o: "Not enough arguments"

# test case no.12 - Pass!
	# i: a b +
	# o: "Invalid input"

	# Note: Previously, this error message show right after "Invalid input".
	# 'rpn.rb:64:in `evaluate': undefined method `%' for nil:NilClass (NoMethodError)'.
	# I still need the "if inputArray[0] % 1 == 0" on line 65 to check if there are decimals.
	# So I used begin and rescue functions to catch the unneccessary error.

# puts rpn.atoi("123") # - pass!

# puts rpn.atof("255.55") # - Pass!

# puts rpn.atof("15876") # - Pass!






















# Ignore everything below. These are my notes and tried attempts with atoi() and atof()
# __________________________________________________________

# def allNum()
# 	for number in 0..100 do
# 		print "number #{number} and ascii ", "#{number}".bytes, "\n"
# 	end
# end

# allNum()

# number 0 and ascii [48]
# number 1 and ascii [49]
# number 2 and ascii [50]
# number 3 and ascii [51]
# number 4 and ascii [52]
# number 5 and ascii [53]
# number 6 and ascii [54]
# number 7 and ascii [55]
# number 8 and ascii [56]
# number 9 and ascii [57] 
# ......
# number 99 and ascii [57, 57]
# number 100 and ascii [49, 48, 48] # .btyes is better than .chr or .ord

# Then now... Convert the bytes to integer. Use 48 for subtraction!

# def rpn_calculator()

# 	print "Enter your math sequence: "
# 	sequence = gets.chomp.split(" ")

# 	s = []
	# puts s.count

	# s.push(sequence[0])

	# puts s.count

	# puts sequence.count

	# for i in (sequence.count-1)

	# fruits.each do |fruit|
	#   puts "A fruit of type: #{fruit}"
	# end

	# sequence.each do |element|
	# 	if atoi(element)
	# 		s.push(atoi(element))
	# 		print s, "\n"
	# end

	# # http://ruby.about.com/od/rubyfeatures/a/loops.htm

# end

# puts rpn_calculator()


# def atoi(strNum)

# 	getASCII = strNum.bytes 
	# print getASCII, "\n"

	# for loop example in Ruby (http://ruby.learncodethehardway.org/book/ex32.html)
	# fruits.each do |fruit|
	#   puts "A fruit of type: #{fruit}"
	# end
	# another example, change.each {|i| puts "I got #{i}" }

	# Subtract the bytes from the base num
	# minusASCII = getASCII.map do |asciiNum|
	# 	asciiNum - 48 
	# end
	# print minusASCII, "\n"

	# .inject example in Ruby (http://www.gabekoss.com/blog/2013/12/why_i_love_ruby_enumerable_inject/)
	# def sum(array)
	#   array.inject(0) do |sum, i|
	#     sum += i
	#   end
	# end
	# sum([1,2,3])
	# #=> 6

	# .join doesn't work in this case. .each doesn't work, but .inject works with fixnum integer.
	# intResult = minusASCII.inject do |value, concat_to_value| 
	# 	# puts "firstValue: ", value
	# 	# puts "addtoValue: ", concat_to_value
	# 	tempValue = value * 10 # to avoid overlapping
	# 	concatenate = tempValue + concat_to_value
	# end

# 	return intResult

# end
# end 


# def atof(strNum) 
# 	# check thru the string if it has a decimal
# 	for i in strNum.split("")
# 		if i == "."
# 			result = []
# 			array = strNum.split(".")
# 			array.each do |element|
# 				result.push(atoi(element))
# 			end
# 			last_digits = result[1] / (10.0 ** array.last.length)
# 			float = result[0] + last_digits
# 			return float
# 		end
# 	end
# end


# def atof(strNum) 

# 	strNum = strNum.to_s
	
# 	array = strNum.split(".")

# 	float = atoi(array[0])
# 	# puts float
# 	decimals = atoi(array[1]) / (10.0 ** array[1].length)
# 	# puts decimals
# 	return float + decimals

# end



