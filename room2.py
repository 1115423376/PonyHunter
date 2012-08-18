import look
import room1

def start():
    print"""To your north a door dominated by a giant
        number 1.
        
        What will you do?"""
    move = raw_input(">>")
    if move == "go north":
        room1.start()
    elif move == "look":
        look.look(2)
        start()
    else:
        print "I don't understand."
        start()

