from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file + to_file_file,'r')


print "the input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(from_file)

print "alright, all done"

out_file.close()
in_file.close()