from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL+C (^C)"
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for 3 lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to a file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "First we have to close the file and re-open it"
target.close()

print "Here's what you wrote:"
readfile = open(filename)
print readfile.read()

print "Does that look alright to you? If it does, hit RETURN. If it doesn't, too bad! It's already been written to the file!"
raw_input("!")

