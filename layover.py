hours = int(3)
minutes = int(23)
time = "%d:%d" % (hours, minutes)

balance = int(16)

def time_passes():
    global minutes
    global time
    minutes += 3
    hourchange()
    time = "%d:%d" % (hours, minutes)

def hourchange():
    global minutes
    global hours
    if minutes >= int(60):
        minutes = minutes - 60
        hours += 1

def intro():
    print """
    You wake up in an airport. \n
    It's not exactly clear which one, but through the jet-lag you're vaguely aware of asian languages being spoken around you.\n
    You remember that you've been here before, and that you've been waiting for your phone to charge at the free plug in front of you.\n
    Everything else is still quite hazy.\n
    """
    first()

def first():
    print "What do you do next?"

    next = raw_input("> ")

    if "check" in next or "phone" in next or 'time' in next:
        print "You reach for the phone charging in the socket. It reads %s." % time
    elif 'go' in next or 'up' in next:
        print "You force yourself to stand on unsteady legs, and have a look around."
        print "There happens to be a ticket counter nearby to the right."
        print "The baggage claim and terminal is to the left."
        print "And, of course, the seat in front of you is still warm, and you're exhausted."
        print "..."
        go()
    elif 'sleep' in next:
        sleep()
    else:
        wrong()

def wrong():
    print "You're not all there, mentally. What you typed is too much to handle right now. Keep it simple."
    first()

def go():
    next = raw_input("> ")

    if "right" in next or "ticket" in next:
        ticket_counter()
    elif "left" in next or "baggage" in next or "terminal" in next:
        terminal()
    elif 'sleep' in next or 'sit' in next:
        sleep()
    else:
        wrong()

def sleep():
    print "Sitting in the slightly uncomfortable chair as people pass around you, you drift off to sleep... "
    time_passes()
    print "You are jolted awake before too long. You check your phone. It's now %s. You should do something." % time
    first()

def ticket_counter():
    print "Approaching the counter, you check your phone again. It has an Ethereum wallet attached,"
    print "The balance reads %s" % balance
    print "Tickets happen to cost 4 ETH anywhere."
    print "What shall you do?"

    next = raw_input("> ")

    if 'buy' in next or 'purchase' in next:
        travel()
    else:
        print "In a stupor you wander back to the chair you were sitting in and sit back down."
        sleep()

def travel():
    global balance
    if balance <= 4:
        print "You don't have the money for that. Too bad."
        print "You wander back to the chairs and sit down."
        sleep()
    else:
        print "Well, where do you want to go?"
        dest = raw_input("> ")
        print "Ticket purchased for %s" % dest
        print "You walk to the gate, and get on the plane."
        balance -= 4
        first()

def terminal():
    print "You walk towards the terminal, weary and unaware of the outstanding warrant for your arrest."
    print "As you enter the line for security, five plain-clothes agents quickly bring you down."
    print "You are sent to a holding cell, and await trial for an unknown crime."
    exit(0)

intro()
