from sys import exit 
from random import randint  
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        exit(0) # exit without any problem or error

class Engine(object):

    def __init__(self, scene_map): # scene_map = 'central corridor'
        self.scene_map = scene_map  # self.scene_map = 'central corridor

    def play(self): 
        current_scene = a_map.opening_scene() # connecting Map method with  Map object a_map, current_scene = CentralCorridor()
        last_scene = a_map.next_scene('finished') # Accessing Map method with map object a_map. last_scene  = 'Finished()'
                                                # a_map.next_scene() OR self.scene_map.next_scene()

        while current_scene != last_scene: # while Finished() not equal to Finished(), So as while is false, jumps out of the loop,
            next_scene_name = current_scene.enter() # Next_scene_name = TheBridge().enter(),Return value from 48,52,56,77,80, 91,95,98,110,113,119 
            current_scene = a_map.next_scene(next_scene_name) # current scene = next_scene('finished'), accessing Map method.
            # current_scene = next_scene('finished'), return value Finished(), current_scene = Finished(),  to 21
        current_scene.enter() #From 21, Finished().Enter(), To 115, Return value 'finished', here it ends.....

class Death(Scene):
    quips = [
        "You died. You kinda suck at this",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self): #From 22, Death().enter()
        print(Death.quips[randint(0,len(Death.quips)-1)]), # Death.quips = quips, len(quips)-1, randint(0, 4), Death.quips[0,1,2,3,4]
        exit(0) # Exit the program

class CentralCorridor(Scene):
    def enter(self): # From  22, CentralCorridor().enter()
        print(dedent("The Gothons of .....weapon to blast you"))

        action = input("Select one: shoot!, dodge!, tell joke  :")

        if action in ("shoot!", '1'): # if options are more then ...... in ()
            print(dedent("Quick on the ...... then he eats you"))
            return 'death' # To 23 , next_scene_name = 'death'

        elif action in ("dodge!", '2'):
            print(dedent("Like a world..... and eats you."))
            return 'death' # To 23, next_scene_name = 'death'
 
        elif action in ("tell joke", "3"):
            print(dedent("Lucky  for .... weapon armory door."))
            return 'laser_weapon_armory' # to 23, next_scene_name = 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'  # To 23, next_scene_name = 'central_corridor'
    
class LaserWeaponArmory(Scene): # From 22, 

    def enter(self): # LaserWeaponArmory().enter()
        print(dedent("You do a dive ...... code in 3 digits."))

        code = '123'
        guess = input("keypad : ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZD")
            guesses += 1 # counting guesses
            guess = input("Keypad: ")
        if guess == code:
            print(dedent("The container ... right spot."))
            return 'the_bridge' # To 23, next_scene_name = 'the bridge'
        else:
            print(dedent("The lock .... and you die."))
            return 'death' # To 23, next_scene_name = 'death'

class TheBridge(Scene): #From 22

    def enter(self): # TheBridge().entert()
        print(dedent("You burst .... set it off."))

        action = input("Select one: throw the bomb, slowly place the bomb  :")

        if action in ('throw the bomb', '1'):
            print(dedent("In a panic ... goes off."))
            return  'death'  # To 23, next_scene_name = 'death'

        elif action in ("slowly place the bomb", "2"):
            print(dedent("You point ..... this tin can."))
            return 'escape_pod'  # To 23, next_scene_name =  'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"  # To 23, next_scene_name = "the_bridge"

class EscapePod(Scene):# From 22

    def enter(self): # EscapePod().enter()
        print(dedent("You rush .... do you take?"))

        good_pod = 3
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"You jump into pod {guess}... jam jelly."))
            return 'death'   # To 23, next_scene_name = 'death'
        else:
            print(dedent(f"You jump into pod {guess} .. ship at the same."))
            return 'finished'  # To 23, next_scene_name = 'finished'

class Finished(Scene):  # From 25, 

    def enter(self): # Finished().enter()
        print("You won! Good job.")
        return 'finished' # To 25, as 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene): # start_scene = 'Central corridor'
        self.start_scene = start_scene # self.start_scene = 'Central corridor'

    def next_scene(self, scene_name): # scene_name = 'Central corridor', 'death'
        val = self.scenes.get(scene_name) # class Map (or self) scenes varible get('death') = Death()
        return val # val CentralCorridor(), Death()

    def opening_scene(self):
        return a_map.next_scene(self.start_scene) # self.next_scene, connecting next method next_scene()
                                # self.start_scene = 'Central corridor', return value = CentralCorridor()
a_map = Map("central_corridor")
a_game = Engine(a_map) # a_game = 'Map object, Engine object', a_map = 'Central corridor'
a_game.play() # engine object connecting play() method