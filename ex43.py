from sys import exit # from module sys take exit function .. Visualized from PYTHONTUTOR, 
from random import randint  # from module random take randint function
from textwrap import dedent # from module textwrap take dedent function

class Scene(object): # Declaring class Scene, after import functions, Next line which execute.  ***1

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(0) # exit without any problem or error

class Engine(object): # Declaring class Engine, executes after class Scene ***2

    def __init__(self,scene_map):  # Inilitiazing the Class object's parameter scene_map  ***14
        self.scene_map = scene_map  # creating attribute scene_map *15 (a_map = Map(Central Corridor)
                                     # a_game = Engine(a_map)
    def play(self): # Creating a method play() *17
        current_scene = self.scene_map.opening_scene() # Creating variable current_scene that includes Attribute self.scene_map
        # and a method opening_scene() * 18, self.scene_map or a_map = Map object
        last_scene = self.scene_map.next_scene('finished') # Set attribute  self.scene map and 
    # method next.scene 231 with finished argument to last_scene variable.. **24
        while current_scene != last_scene: # run this loop until current scene is not same as last scene **25
            next_scene_name = current_scene.enter() #  set current_scene that calls method enter() to next_scene_variable. **26 TO 44
            # As enter() returned 'death', next_scene_name = 'death' or laser_weapon_armory. **30
            current_scene = self.scene_map.next_scene(next_scene_name) # setting new values, attribute scene_map and next_scene() to old varible current scene **31
            # again to next_scene method 236 , next_scene('death'or 'laser...') **31
        current_scene.enter() 

class Death(Scene): # Declaring sub class Scene that inherits from Class Scene, Death. Execute after class engine *3

    quips = [
        "You died. You kinda suck at this",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes"
    ] # After 26 to 236 then to 22 (bcs of return..).From 23 to 39. Bcs of enter(), current.scene = 'death'

    def enter(self): # method enter.
        print(Death.quips[randint(0,len(self.quips)-1)]) # quips len = 5 -1 = 4.Out of 0,4, randint selects one out of quips.
        exit(0) # Exits the program without any problem. **32 

class CentralCorridor(Scene): # Declaring sub class Scene,Centralcorridor. execute after Death  *4

    def enter(self): # FROM 23. create Method named enter.
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.
        
            You're running down the central corridor to the Weapons
            Armory when a Gotham jumps out, red scaly skin, dark grimy
            filled body. He's blocking the door to  the Armory and 
            about to pull a weapon to blast you.
            """ )) # prints the value entered.
        action = input("Select one: shoot!, dodge!, tell joke  :")  # asks user to enter here. *27
    
        if action in ("shoot!", '1'):  # if the input of user entered is shoot, then *28
            print(dedent("""
                Quick on the draw you yank out your blaster and fire 
                it at the Gothon. His clown costume is flowing and 
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are 
                dead. then he eats you.
                """))  # If shoot, prints.
            return 'death' # Returns to 23. with value as 'death'

        elif action in ("dodge!", '2'): # if user input is dodge,
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gotham's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out. you wake up shortly after only to 
                die as the  Gothan Stomps on your head and eats you.
                """)) # prints above lines
            return 'death' # Returns to 23. with value as 'death'

        elif action in ("tell joke", '3'): # If user input is tell joke
            print(dedent("""
                Lucky for you they made you learn Gothon insults in 
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in 
                the head putting him down, then jump through the 
                Weapon Armory door.
                """)) # prints the above line
            return 'laser_weapon_armory' # Returns to 23 with value 'laser_weapon_armory **29

        else:
            print("DOES NOT COMPUTE!") # if user action is out of the options.
            return 'central_corridor' # back to central corridor, giving another chance to type correctly

class LaserWeaponArmory(Scene):# Declaring sub class Scene,LaserweaponArmory execute after Central..*5

    def enter(self): # From 95 to 23,24.From 24 to 236(next_scene),239 to 22, 23. Finally 23 to 103.
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's keypad lock on the box and you need code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """)) # prints above lines
        code = "248" # a variable code
        guess = input("[keypad]> ") # asking user enter code, guessing the secret code
        guesses = 0 # counting guesses

        while guess != code and guesses < 10: # while loop, if guess is not same as actual code and also if guesses are less then 10.
            print('BZZZZEDDD!') # prints this if both are True(True and True)
            guesses += 1 # Guess counting starts
            guess = input("[keypad]> ") # again asking  user to enter code inside while loop, so that every guess entered counts
        if guess == code: # if guess is same as code.
            print(dedent("""
                The container clicks open and seal breaks, letting
                gas out, you grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
                """ )) # Prints the line
            return 'the_bridge' # return with the bridge. next_scene_name = 'the_bridge', then to 236 and again to 22, 23 and to 140
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the 
                Gothons blows up the ship from their ship and you die.
                """))
            return 'death' # return with death, result is same as           71 and 82


class TheBridge(Scene): # Declaring sub class Scene,The Bridge. execute after lasor... *6

    def enter(self): # From  22 23 to 142. next_scene_name = the_bridge.enter()
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. Each of them has an even uglier
            clown costume than the last. The haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """)) # prints the line
        action = input("Select one: throw the bomb, slowly place the bomb  :") # asking user to enter thier action

        if action in ("throw the bomb", '1'): # if action is same as 'throw the bomb
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door.
                Gothon shoots you right in the back killing you.
                you die you see another Gothon frantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
                """)) # prints the above line
            return 'death' # return with 'death', same as 72,81, 137.
        elif action in ("slowly place the bomb", '2'): # if user action is same as'slowly place the bomb'
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put thier hands up and starts to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """)) # prints the line.
            return 'escape_pod' # return to 23 as 'escape pod, next_scene_name = 'escape_pod'
# so  again 25, 236, 237, 238 to 22 , 23. next_scene_name = escapepod().enter()
        else:
            print("DOES NOT COMPUTE!") # if user entered different, print this
            return "the_bridge" # Another chance to enter correctly

class EscapePod(Scene):# Declaring sub class Scene, Escape pod, execute after the bridge  *7

    def enter(self): # From 23, next_scene_name = escapepod().enter()
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes.
            like hardly any Gothons are on the ship, so your run is
            clear of interference.
            escape pods, and now need to pick one to take.
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
            """)) # prints the above line

        good_pod = 2 # randint function, randomly picking number from  1 to 3
        guess = input("[pod #]> ") # User input

        if int(guess) != good_pod: # if user input is not equal to good pod(randomly selected number)
            print(dedent(f"""
                You jump into pod  {guess}  and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body into
                jam jelly.
                """)) # then print this
            return 'death' # Return to death, same as 72, 81, 137, 162.
        else: # if good pod is equal to  user input
            print(dedent(f"""
                You jump into pod  {guess}  and hit  eject button
                The pod easily slides out into space heading to the
                planet below. As it flies to the planet, you look
                back  and see your ship impplode the explode like a
                bright star, talking  out the Gothon ship at the same.
                """)) #  prints this
            return 'finished' # Return  to 23 with 'finished' next_scene_name = Finished().enter().
            
class Finished(Scene): # Declaring last sub class Scene,Finished, exceute after escape pod   *8

    def enter(self):
        print('You won! Good job.')
       # return 'finished'



class Map(object): #Creating Third class Map,execute after finished (class only) *9

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished' : Finished()
    } # Dictionary for key values, here string and classes.
 
    def __init__(self, start_scene): # initliazing object's data atribute 'start_scene', OR PARAMETER 'start_scene *11
        self.start_scene = start_scene # creating attributes start.scene    *12 'central corridor'
 
    def next_scene(self, scene_name): # Defining method nect_scene with parameter scene_name **21
        val = Map.scenes.get(scene_name) # creating a variable 'Val' and Assign class attribute scenes with 
        # class Map and using get() to get scene_name. **22
        return val # return the val variable **23
# AFTER RETURN VAL IT RETURNS TO 241. AND THEN RETURNS TO 20...
    def opening_scene(self): # Defining Method 'opening_scene'  **19
        return self.next_scene(self.start_scene) # return the next_scene method with parameter start_scene
                                                # start_scene = 'central corridor' **20
a_map = Map("central_corridor") # Creating Map object a_map with arguments 'central corridor *10
a_game = Engine(a_map) # Creating Engine object with argument a_map *13
a_game.play() # calling play() method on the obejct "a_game". **16





 
