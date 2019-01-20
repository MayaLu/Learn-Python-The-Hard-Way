## Animal is-a object 
class Animal(object):
	pass
	
##Dog is-a Animal 
class Dog(Animal):

	def __init__(self, name):
		##Dog has a name
		self.name = name
		
##Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		##cat has a name
		self.name = name


##rover is-a Dog
rover = Dog("Rover")

##satan is-a Cat
satan = Cat("Satan")

print rover.name
print satan.name



		
##Person is-a object
class Person(object):
	
	def __init__(self, name):
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None

##mary is-a person
Mary = Person("MaryJ")

	
##Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		##employee has a name and a salary 
		super(Employee, self).__init__(name)
		self.salary = salary

##frank is-a Employee
Frank = Employee("FrankJ", 120000)

print Frank.salary
print Frank.name
print Mary.name


##mary has-a pet, satan is-a pet
Mary.pet = "Satan"

##frank has-a pet, rover is-a pet
Frank.pet = "Rover"

print Mary.pet



		
##Fish is-a object
class Fish(object):
	def __init__(self,kind):
		self.kind = kind
	
##Salmon is-a Fish 
class Salmon(Fish):

	def __init__(self, kind, fish_n):
		super(Salmon, self).__init__(kind)
		self.fish_n = fish_n
	
##Halibut is-a Fish 
class Halibut(Fish):
	def __init__(self, kind, fish_n):
		super(Halibut, self).__init__(kind)
		self.fish_n = fish_n

##flipper is-a Fish
flipper = Fish("small fish")

##crouse is-a Salmon
crouse = Salmon("Salmon", "Nemo")

##harry is-a Halibut
harry = Halibut("Halibut", "Harry")


print flipper.kind
print crouse.kind
print crouse.fish_n
print harry.kind
print harry.fish_n