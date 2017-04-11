from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

#we could do these next two lines in one. How?
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r." %  exists(to_file)
print "Ready. To continue hit RETURN. To abort hit CTRL+C"
raw_input()

open(to_file,'w').write(indata)

print "Alright, all done."

