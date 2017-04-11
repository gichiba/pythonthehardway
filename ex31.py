print "You enter a dark room with two doors. Do you go in door #1 or door #2?"

door = raw_input("> ")

if door == "1" or door == "door #1":
    print "There's a giant bear there eating cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear politely gives you a slice. Good job!"
    elif bear == "2":
        print "The bear eats your face off. Good job!"
    else:
        print "Well, %r is probably a better course of action, anyways." % bear

elif door == "2" or door == "door #2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow-jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jellow. Good job!"
    else:
        print "The insantiy rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and eventually fall on a knife. Good job!"
