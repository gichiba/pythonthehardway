
def build_list(n, j):
    i = 0
    numbers = []
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + j
        print "Numbers now:", numbers
        print "At the bottom of i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num

print "How long is this list going to be?"
n = input("> ") + 1

print "Okay, what increment should I use?"
j = input("> ")

print "building the list..."
build_list(n, j)
