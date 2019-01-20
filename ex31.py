print "you enter a dark room with two doors. do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
	print "there's a giant bear here eating a cheese cake. what do you do?"
	print "1. take the cake"
	print "2. scream at the bear"
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "the bear eats your face off. good job!"
	elif bear == "2":
		print "the bear eats your leggs off. good job!"
	else:
		print "well, doing %s is probably better. bear runs away" %bear
		
elif door == "2":
	print "you stare into the endless abyss at Cthulhu's retina"
	print "1. blueberries"
	print "2. yellow jacket clothespins"
	print "3. understanding revolvers yelling melodies"
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "your body survives powered by a mind of jello. good job!"
	else: 
		print "the insanity rots your eyes into a pool of muck. good job!"

elif door == "3":
	print "you bath in chocolate, but the tide is high, what do you do?"
	print "1. swim"
	print "2. eats it all"
	
	bath = raw_input("> ")
	
	if bath == "1":
		print "Good job!"
	elif bath > "1" and bath < "3":
		print "you die from a high level of suger. good job!"
	else:
		print "I don't know what you did but it worked!!"

		
else:
	print "you stumble around and fall on a knife and die. good job!"