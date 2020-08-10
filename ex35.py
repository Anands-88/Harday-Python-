from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = int(input(":> "))
    if choice < 100:
        how_much = int(choice)
    else: 
        dead("Man, learn to type a number.")

    if how_much < 50:
        dead("Nice, you're not greedy, you win!")
        exit(0)
    else:
        print("You greedy bastard!")



def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to  move the bear?")
    bear_moved = False


    while True:
        choice = input(":> ")

        if choice == "Take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not  bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthuhu_room():
    print("Her you see the great evil Cthulhu.")
    print("He, it, whatever stared at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("flee or head :> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start(): # this comes first.
    print("You are in dark room.")
    print("There are 3 doors , right, centre and left.")
    print("Which one do you take?")

    choice = input("right, centre or left:> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthuhu_room()
    elif choice == "centre":
        gold_room()
    else:
        dead("You stumble around the room until you starve.")

start()