import test

def game():
    room1()
    
def room1():
    print"""To your south is a door dominated by a giant
        number 2.
        
        What will you do?"""
    move = raw_input(">>")
    if move == "go south":
        room2()
    elif move == "look":
        look(1)
        room1()
    else:
        print "I don't understand."
        room1()
def room2():
    print"""To your north a door dominated by a giant
        number 1.
        
        What will you do?"""
    move = raw_input(">>")
    if move == "go north":
        room1()
    elif move == "look":
        look(2)
        room2()
    else:
        print "I don't understand."
        room2()

def look(room):
    if room == 1:
        print """
        You are standing in a room painted 
        to look like a cartoon forest.
        Your feet sink into the emerald 
        astro turf.
        To your south a door dominated by a giant
        number 2, blocks your escape.
        """
    elif room == 2:
        print """
        You are standing in a room painted 
        to look like a cartoon forest.
        Your feet sink into the emerald 
        astro turf.
        To your north a door dominated by a giant
        number 1, blocks your escape.
        """
test.test()
game()
