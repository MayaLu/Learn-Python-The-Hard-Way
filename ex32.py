the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this goes through a list
for number in the_count:
	print "this is count %d" %number
	
for Maya in the_count:
	print Maya

for fruit in fruits:
	print "a fruit of type: %s" %fruit

#mixed lists - where we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" %i

#we can also build lists, first start with an empty one
elements = []

#the range function:
for i in range(0, 6):
	print "adding %d to the list" %i
	#append is a function that lists understand
	elements.append(i)
	
#now we can print them out too
for i in elements:
	print "element was %d" %i