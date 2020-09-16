from sys import exit # from module sys take exit function
from random import randint  # 
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        exit(0) # exit without any problem or error

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You kinda suck at this",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("The Gothons of .....weapon to blast you"))

        action = input("Select one: shoot!, dodge!, tell joke  :")

        if action == "shoot!":
            print(dedent("Quick on the ...... then he eats you"))
            return 'death'

        elif action == "dodge!":
            print(dedent("Like a world..... and eats you."))

            return 'death'

        elif action == "tell joke":
            print(dedent("Lucky  for .... weapon armory door."))

            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
    
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("You do a dive ...... code in 3 digits."))

        code = '123'
        guess = input("keypad : ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZD")
            guesses += 1
            guess = input("Keypad")
        if guess == code:
            print(dedent("The container ... right spot."))

            return 'the_bridge'
        else:
            print(dedent("The lock .... and you die."))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("You burst .... set it off."))

        action = input("Select one: throw the bomb, slowly place the bomb  :")

        if action == 'throw the bomb':
            print(dedent("In a panic ... goes off."))
            return  'death'

        elif action == "slowly place the bomb":
            print(dedent("You point ..... this tin can."))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("You rush .... do you take?"))

        good_pod = randint(1,3)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("You jump into pod {guess}... jam jelly."))
            return 'death'
        else:
            print(dedent("You jump into pod {guess} .. ship at the same."))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()