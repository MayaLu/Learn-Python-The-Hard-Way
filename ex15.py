from sys import argv

script, filename = argv

txt = open(filename)
print script
print "here's your file %r:" % filename
print txt.read()

print "type the filename again:"
fileagain = raw_input("> ")
txtagain = open(fileagain)

print txtagain.read()




