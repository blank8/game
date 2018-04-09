import random
class game:
    def __inxxit__(self):
        print("hello game")
    def __init__(self):
        door = "Locked"
        global haveKey
        haveKey = False
        global fakeKeyHave
        fakeKeyHave = "False"
        name = input("Hello Adventurer what is your name? ")
        print(" ")
        print("""Somewhere in the distance you hear a voice saying, 'Welcome %s. If you wish to exit the dungeon
                        you must find me to get the key. In total there are 9 rooms, you are in the first of these. The
                        instructions are simple. When you are given a choice, you maytype 'L' for Left, 'U' for up, and
                        'D' for down. Remember to capitalize! ;) """ % name)
        ready = input("Are you ready to go %s? " % name)
        ready = ready.upper()
        if ready == "Yes":
            print(" ")
            print("You will now start. The door in locked and you can't exit the dungeon until you have completed each room")
            room.zero()
        elif ready== "Y":
            print(" ")
            print("You will now start. The door in locked and you can't exit the dungeon until you have completed each room")
            room.zero()
        else:
            game.start()
        def finished():
            print("\n Amazing! You completed this game(though very simplistic), still we have to commend you for your efforts!")
            print("\n Would you like to go again?")
            goAgain = input("\n Would you?")
            goAgain.upper()
            if goAgain == "Yes" or goAgain == "Y":
                room.start
            else:
                print(done)

class room():
    def zero():
        print("""Room zero...the starting point of all...you've returned here or have just started. The room has some torches lit in the corners.""")
        direction = input("Which way would you like to go? (Left, Up, or Down?)")
        direction = direction.upper()
        if direction == "L":
            room.two
        elif direction == "Left":
            room.two()
        elif direction == "U":
            room.four
        elif direction == "Up":
             room.four()
        elif direction == "D":
            room.two()
        elif direction == "Down":
            room.two()
            if haveKey == True:
                game.finished()
            elif fakeKeyHave == "True":
                print("""\n You stick the key in the door and try turning it, but it won't budge. You try a little harder and it breaks...turns out that was a fake key...""")
                room.zero()
            else:
                print("""\n I'm sorry %s, but you appear not to be in possession of the key necessary to leave...
                        please keep looking.""")
                room.zero()
        else:
            print("\n That direction is not possible")
            room.zero()

    def one():
        print("\n Room one... This is a dead end, you look and around and see a old standing in the corner")
        print("  ")
        talk = input("Would you like to talk to him?")
        talk.upper()
        if talk == "Yes":
            haveKey = True
            print("""\n You talk to the old man and he says, 'Congratulations on finding me. I will now give you the key to exit. You have done well in coming this far. You may now leave the dungeon'""")
            print("\n You now have the key, you lift it over your head in triumph")
        elif talk == "Y":
            print("""\n You talk to the old man and he says, 'Congratulations on finding me. I will now give you the key to exit. You have done well in coming this far. You may now leave the dungeon'""")
            print("\n You now have the key, you lift it over your head in triumph")
        else:
            print("\n The old man stares at you in silence")
            room.one()
            print(" ")
            question = input("Would you like to exit the room?")
            question.upper()
        if question == "Yes":
            room.five()
        elif question == "Y":
            room.five()
        else:
            room.one()

    def two():
        print("\n Room two... You come to a room with two exits and a dim light coming from above")
        print(" ")
        direction = input("Which way would you like to go? (Up, or Right?)")
        direction = direction.upper()
        if direction == "U":
            room.three()
        elif direction == "Up":
            room.three()
        elif direction == "R":
            room.zero()
        elif direction == "Right":
            room.zero()
        else:
            room.two()

    def three():
        print("\n Room three... You enter a room with two exits. You see a few relics and a few torches in the corner.")
        print(" ")
        direction = input("Whiich way would you like to go? (Right, or Down?")
        direction.upper()
        if direction == "R":
            room.four()
        elif direction == "Right":
            room.four()
        elif direction == "D":
            room.two()
        elif direction == "Down":
            room.two()
        else:
            room.three()

    def four():
        print("""\n Room four... The room is lined with expensive family jewels and a deep cackle can be heard in the distance. There are three exits""")
        print(" ")
        direction= input("Which way would you like to go? (Up, Left, Down)")
        direction.upper()
        if direction == "U":
            room.seven()
        elif direction == "Up":
            room.seven()
        elif direction == "L":
            room.three()
        elif direction == "Left":
            room.three()
        elif direction == "D":
            room.zero()
        elif direction == "Down":
            room.zero()
        else:
            room.four()

    def five():
        print("""\n Room five... The room you've found looks to be an old dungeon room. The cells are looked and there seems yo be some treasure in the one to your right""")
        direction = input("Which way would you like to go? (Up, or Down?)")
        direction = direction.upper()
        if direction == "U":
            room.eight()
        elif direction == "Up":
            room.eight()
        elif direction == "D":
            room.one()
        elif direction == "Down":
            room.one()
        else:
            print("\n You go that way and run into a wall")
            room.five()

    def six():
        print("""\n Room six... A furnished bedroom and some candles are lit at the top of the bed. You see a mirror to your right and some moonlight fades in through the window to your left""")
        print("\n You see a key on a nightstand and pick it up (Was it really that easy?)")
        fakeKeyHave = True
        direction = input("Would you like to exit the room?")

    def seven():
        print("""\n Room seven... You walk into a room with three exits one seems to lead to a kitchen, and this seems to be a dining room with a long table that looks recently set and a chandiler hanging from the ceiling with candles burning""")
        print("  ")
        direction = input("Which way would you like to go?(Left, Down or Right)")
        direction = direction.upper()
        if direction == "D":
            room.four()
        elif direction == "Down":
            room.four()
        elif direction == "L":
            room.six()
        elif direction == "Lelf":
            room.six()
        elif direction == "Right":
            room.eight()
        elif direction == "R":
            room.eight()
        else:
            print("\n I'm sorry that direction is impossible")
            room.seven()

    def eight():
        print("\n Room eight... You enter a kitchen with two exits, and a very expensive looking one at that!")
        print("  ")
        direction = input("Which way would you like to go? (Letf, or Down?)")
        direction.upper()
        if direction == "L":
            room.seven
        elif direction == "Left":
            room.seven()
        elif direction == "D":
            room.five()
        elif direction == "Down":
            room.five()
g = game()
# g.start()
print(" ")
print(done)


