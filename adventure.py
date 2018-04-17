question = ""

class game:
    haveKey = False
    fakeKeyHave = False
    familyJewels = False

    def finished():
        print("\n Amazing! You completed this game(though very simplistic), still we have to commend you for your efforts!")
        print("\n Would you like to go again?")
        goAgain = input("\n Would you?")
        goAgain.lower()
        if goAgain == "yes" or goAgain == "y":
            room.start
        else:
            print(done)
        
    def __init__(self):
        door = "Locked"
        name = input("Hello Adventurer what is your name? ")
        print("\n Somewhere in the distance you hear a voice saying, 'Welcome %s. If you wish to exit the dungeon you must find me to get the key. In total there are 9 rooms, you are in the first of these. The instructions are simple. When you are given a choice, you may type 'L' for Left, 'R' for Right, 'U' for up, and 'D' for down." % name)
        ready = input("Are you ready to go %s? " % name)
        ready = ready.upper()
        if ready == "Yes":
            print("\n You will now start. The door in locked and you can't exit the dungeon until you have completed each room")
            room.zero()
        elif ready== "Y":
            print("\n You will now start. The door in locked and you can't exit the dungeon until you have completed each room")
            room.zero()
        else:
            game.start()

class room():
    def zero():
        print("\n Room zero...the starting point of all...you've returned here or have just started. The room has some torches lit in the corners.")
        direction = input("Which way would you like to go? (Left, Up or Down?)")
        direction = direction.lower()
        if direction == "l":
            room.two()
        elif direction == "left":
            room.two()
        elif direction == "u":
            room.four()
        elif direction == "up":
             room.four()
        elif direction == "d":
            room.six()
        elif direction == "down":
            room.six()
        else:
            if game.haveKey == True:
                game.finished()
            elif game.fakeKeyHave == True:
                print("\n You stick the key in the door and try turning it, but it won't budge. You try a little harder and it breaks...turns out that was a fake key...")
                room.zero()
            else:
                print("\n I'm sorry %s, but you appear not to be in possession of the key necessary to leave... please keep looking." % name)
                room.zero()

    def one():
        question = ""
        print("\n Room one... This is a dead end, you look and around and see a old standing in the corner")
        print("  ")
        talk = input("Would you like to talk to him?")
        talk.lower()
        if talk == "yes":
            game.haveKey = True
            print("\n You talk to the old man and he says, 'Congratulations on finding me. I will now give you the key to exit. You have done well in coming this far. You may now leave the dungeon'")
            print("\n You now have the key, you lift it over your head in triumph")
        elif talk == "y":
            game.haveKey = True
            print("\n You talk to the old man and he says, 'Congratulations on finding me. I will now give you the key to exit. You have done well in coming this far. You may now leave the dungeon'")
            print("\n You now have the key, you lift it over your head in triumph")
        else:
            print("\n The old man stares at you in silence")
            room.one()
            print(" ")
        question = input("Would you like to exit the room?")
        question.lower()
        if question == "yes":
            room.five()
        elif question == "y":
            room.five()
        else:
            room.one()

    def two():
        print("\n Room two... You come to a room with two exits and a dim light coming from above")
        print(" ")
        direction = input("Which way would you like to go? (Up or Right?)")
        direction = direction.lower()
        if direction == "u":
            room.three()
        elif direction == "up":
            room.three()
        elif direction == "r":
            room.zero()
        elif direction == "right":
            room.zero()
        else:
            room.two()

    def three():
        print("\n Room three... You enter a room with two exits. You see a few relics and a few torches in the corner.")
        print(" ")
        direction = input("Which way would you like to go? (Right or Down?")
        direction.lower()
        if direction == "r":
            room.four()
        elif direction == "right":
            room.four()
        elif direction == "d":
            room.two()
        elif direction == "down":
            room.two()
        else:
            room.three()

    def four():
        print("\n Room four... The room is lined with expensive family jewels and a deep cackle can be heard in the distance. There are three exits")
        print(" ")
        direction= input("Which way would you like to go? (Up, Left or Down?)")
        direction.lower()
        if direction == "u":
            room.seven()
        elif direction == "up":
            room.seven()
        elif direction == "l":
            room.three()
        elif direction == "left":
            room.three()
        elif direction == "d":
            room.zero()
        elif direction == "down":
            room.zero()
        elif talk == "steal the family jewels":
            game.familyJewles = True
            room.four()
        else:
            print("That is not a viable input")
            room.four()

    def five():
        print("\n Room five... The room you've found looks to be an old dungeon room. The cells are locked and there seems to be some treasure in the one to your right")
        direction = input("Which way would you like to go? (Up or Down?)")
        direction = direction.lower()
        if direction == "u":
            room.eight()
        elif direction == "up":
            room.eight()
        elif direction == "d":
            room.one()
        elif direction == "down":
            room.one()
        elif direction == "r":
            print("You do not have the key to this cell")
            room.five()
        elif direction == "right":
            print("You do not have the key to this cell")
            room.five()
        else:
            print("\n You run into a wall")
            room.five()

    def six():
        print("\n Room six... A furnished bedroom and some candles are lit at the top of the bed. You see a mirror to your right and some moonlight fades in through the window to your left")
        print("\n You see a key on a nightstand and pick it up (Was it really that easy?)")
        game.fakeKeyHave = True
        direction = input("Which way would you like to go? (Right or Up?)")
        direction = direction.lower()
        if direction == "r":
            room.seven()
        elif direction == "right":
            room.seven()
        elif direction == "u":
            room.zero()
        elif direction  == "up":
            room.zero()
        else:
            room.six()

    def seven():
        print("\n Room seven... You walk into a room with three exits one seems to lead to a kitchen, and this seems to be a dining room with a long table that looks recently set and a chandiler hanging from the ceiling with candles burning")
        print("  ")
        direction = input("Which way would you like to go?(Left, Right or Down?)")
        direction = direction.lower()
        if direction == "d":
            room.four()
        elif direction == "down":
            room.four()
        elif direction == "l":
            room.six()
        elif direction == "left":
            room.six()
        elif direction == "right":
            room.eight()
        elif direction == "r":
            room.eight()
        else:
            print("\n I'm sorry that direction is impossible")
            room.seven()

    def eight():
        print("\n Room eight... You enter a kitchen with two exits, and a very expensive looking one at that!")
        print("  ")
        direction = input("Which way would you like to go? (Left or Down?)")
        direction.lower()
        if direction == "l":
            room.seven()
        elif direction == "left":
            room.seven()
        elif direction == "d":
            room.five()
        elif direction == "down":
            room.five()
        else:
            print("I'm sorry %s, but that direction is not possible" % name)


g = game()
# g.start()
print("\n done")



