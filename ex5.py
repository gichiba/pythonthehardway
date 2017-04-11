name = 'Griffin Ichiba Hotchkiss'
age = 27 #nothing to be ashamed of there
height = 184 #centimeters
weight = 84 #last time I checked...
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilos heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#The following line is tricky; try to get it exactly right
print "If I add %d, %d, and %d, I get %d" % (age, height, weight, age + height + weight)
print "Wonder what format %r will take, or %r, or %r?" % (age, height, eyes)
print "Should it be %s or %r?" % (hair, teeth)
