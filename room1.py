import room2.py
def look():
    print """
    You are standing in a room painted 
to look like a cartoon forest.
Your feet into the spongey texture of a
painfully emerald astro turf.
To your south a door dominated by a giant
number 1, blocks your escape.
""" 
    
move = raw_input(look())
if move == "go south":
    room2()
elif move == "look":
    look()
else:
    print "I don't understand."
    room1()
