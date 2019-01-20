

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" %cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "or we can use variables from our script:"
amount_of_crackers = 50
amount_of_cheese = 10

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def Maya_is_awsome(cool, funny):
	print "You are %d funny" %funny
	print "You have %d coolness" %cool 

Maya_is_awsome(int(raw_input()), int(raw_input()))

