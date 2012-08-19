import look
import room2
import game
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
    elif move == "shoot pony":
        ponyAlive = game.checkPony(0)
        if ponyAlive:
            game.shootPony(0)
        else:
            print "Pony is already dead."
            start()
    else:
        print "I don't understand."
        start()
