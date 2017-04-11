#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r." % (arg1, arg2)

#Ok, that *args is actually pointless. We can just do it like this:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r." % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

#This one takes no arguments
def print_none():
    print "I got nothin'"

print_two("Griffin","Hotchkiss")
print_two_again("Griffin", "Hotchkiss")
print_one("me")
print_none()

