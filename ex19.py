def cheese_and_crackers(cheese_count, cracker_count):
    print "You have %d cheeses." % cheese_count
    print "You have %d crackers." % cracker_count
    print "Man, that's enough for a party!"
    print "You should get some wine.\n"


print "We can just give it numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can give it variables from our script:"
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

print "We can even do math inside, too:"
cheese_and_crackers(20 + 5, 30 + 3)

print "And we can combine the two; variables and math:"
cheese_and_crackers(amount_cheese + 100, amount_crackers + 200)
