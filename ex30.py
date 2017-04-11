people = 30
cars = 45
buses = 55


if cars > people and cars > buses:
    print "We should take the cars."
elif cars > people and buses > cars:
    print "obviously we should each take a bus"
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide."

if buses > cars:
    print "Wow, that's too many buses."
elif buses < cars:
    print "Why don't we take the buses?"
else:
    print "We still can't decide."

if people > buses:
    print "Ok, why don't we just take the buses."
else:
    print "fine, let's just stay home."
