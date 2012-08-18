import look
import room2

def start():
    print"""To your south is a door dominated by a giant
        number 2.
        
        What will you do?"""
    move = raw_input(">>")
    if move == "go south":
        room2.start()
    elif move == "look":
        look.look(1)
        start()
    else:
        print "I don't understand."
        start()
