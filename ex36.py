salty = [2, 4, 5]	


	
def toffee_road():
	toffee = int(raw_input("How much toffee do you want?" ))
	if toffee < 10 :
		print """
Excellemt, you continue your journey...
now you bump into the witch who offers you a cup of coffee
and you drink...
		"""
		coffee = []
		x = 1
		print "You drink 1 cup"
		for x in range(2, 11):
			x + 1
			print "You drink %d cups" %x
			coffee.append(x) 
		print "it's too much for you, game over"
	else:
		print "too much toffee is not good for you, game over"
		exit()



def salty_road():
	chocolate = raw_input("Does it go well with chocolate?" )
	if chocolate == "yes":
		print "Good job, you got home"	
	else:
		if path == 2:
			prop = "bamba"
			print prop
		elif path == 4:
			prop = "bisli"
		elif path == 5:
			prop = "pretzels"
		else:
			print False
		
		
		print "A witch pops up, do you through %s at her or use magic? " %prop
		
		witch = raw_input("> ")
		if witch == prop:
			print "Good job, you are all safe and you can just go home easily"

		elif witch == "magic":
			print "You don't have magic, game over"
			
		else:
			print "You got all confused, game over"
			

def fudge_road():
	print "There is a hugh river of fudge you must pass"
	vehicle = raw_input("What would you rather take, a canue or a sailing boat? ")
	
	if vehicle == "canue":
		taking_canue()
		
	elif vehicle == "sailing boat":
		print "Tammy decides to sail north, what would be on her right shoulder?"
		direction = raw_input("> ")
		True = "east"
		if direction == True:
			print "Good Job"
		else:
			print "Wrong, next time.."
			exit()
	else: 
		print "game over"
		exit()
	
	
def taking_canue():
	print "Suddenly, a witch turns at you and demands that you will choose a number"
	number = raw_input("> ")
	if "1" in number or "0" in number:
		print "Good job, you got home"
	else: 
		print "This is not what she meant, game over"
		exit()


	
	
	
print """Ami and Tammy had a spare time so they went off to play
Ami was very excited and suggested that they will walk as far as they can 
so they went away, talking and laughing
After a while, Tammy noticed new paths at the beginning of a forest:
1. A path seeded with toffee
2. A path filled with Bamba
3. A path which the soil is pieces of fudge
4. A path filled with Bisli
5. A path with pretzels' trees
Now Ami amd Tammy need to decide...
"""
path = int(raw_input("Which kind of path should they choose? "))
	

if path == 1:
	toffee_road()
elif path in salty:	
	print salty
	print path
	salty_road()
elif path == 3:
	fudge_road()
else:
	print "You got lost, game over"
	exit()