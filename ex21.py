def add(a, b):
	print "adding %d + %d" % (a, b)
	return a + b
	
def subtract (a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "multiplying %d * %d" %(a,b)
	return a * b
	
def divide (a, b):
	print "dividing %d/%d" %(a, b)
	return a / b

age = add(int(raw_input()), 5)
height = subtract (float(raw_input()), 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print "age: %d, height: %d, weight: %d, iq: %d" %(age, height, weight, iq)

what = add(age, subtract(height, multiply (weight, divide(iq, 2))))
print "that becomes:", what, "can you do it by hand?"

print subtract(add(24, divide(34, 100)),1023)
