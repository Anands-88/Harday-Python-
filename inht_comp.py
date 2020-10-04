class Parent: # creating a class Parent
    def altered(self): # creating method, altered
        print("Parent altered") 
    
    def implicit(self): # another method implcit
        print("Parent implicit")

    def override(self): # 3rd method of class Override
        print("Parent Override")

class Child(Parent): # creating child class or sub classs of Parent class
    def override(self): # method override, same as parent class
        print("Child  Override")

    def altered(self): # method altered
        print("Child, before after altered")
        super().altered() # calling altered method of Parent class using super function.
        print("Child, after Parent altered")

dad = Parent() # Creating instance of Parent class, Dad object
son = Child() # Creating instance of Child class, Son object
 
dad.implicit() # using Parent object calling implcit method
son.implicit() # using Child object calling implicit method, however as there is no  impllicit in the child, it gets from Parent class

dad.altered() # Parent object, altered method
son.altered() # child object, altered method

dad.override() # parent object, override method
son.override() # Child object, override method

#----------------------------------------------------------------------------------#
# creating both new classes which has parent child relationship, that is independent class
class Other: # creating Other class
    def override(self): # Creating method
        print("Other override")

    def implicit(self): # Method implcit
        print("Other implicit")

    def altered(self): # method altered
        print("Other altered")

class Child: # Another new class Child
    
    def __init__(self): # using init function to initialize and to create class property or attribute
        self.other = Other() # CReating attribute name and assigning to Other() class
 
    def implicit(self): # Method implcit, 
        self.other.implicit() # calling implicit method using self.other attribute that is Other(class), Other().implicit()

    def override(self): # method override
        print("Child Override")

    def altered(self): # Method altered
        print("Child, before other altered")
        self.other.altered() # calling altered method slef.other attribute, that is Other().altered()
        print("Child, after Other altered")

son = child() # Creating object of Child only

son.implicit() # calling implicit method using son object
son.override() # calling override
son.altered() # calling altered
