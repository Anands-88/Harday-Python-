class Animal(object):
    pass

#Class Dog that has-a Animal has-a __init__ that takes self and name parameters
class Dog(Animal):

    def __init__(self,name):
        self.name = name # From self, get the name atribute and set it  to name

class Cat(Animal): #Class Cat that has-a Animal has-a __init__ that takes self and name parameters
    
    def __init__(self, name):

        self.name = name # From self, get the name attribute and set it to the name


class person(object): # Class person has-a __init__ that takes self and name parameters.

    def __init__ (self, name):

        self.name = name # from self get the name attribute and set it to name.
        self.pet = None # from self get the pet attribute and set it to None.

class Employee(person): # Class Employee has-a person that has-a __init__ self and name, salary paramters

    def __init__(self, name, salary):
        
        super(Employee, self).__init__ (name)

        self.salary = salary

class Fish(object):
    pass 

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

satan = Cat("Satan")

mary = person("Mary")

mary.pet = satan

frank = Employee("Frank",12000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

























































