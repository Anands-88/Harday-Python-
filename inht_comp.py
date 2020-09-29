class Parent:
    def altered(self):
        print("Parent altered")
    
    def implicit(self):
        print("Parent implicit")

    def override(self):
        print("Parent Override")

class Child(Parent):
    def override(self):
        print("Child  Override")

    def altered(self):
        print("Child, before after altered")
        super().altered()
        print("Child, after Parent altered")

dad = Parent()
son = Child()
 
dad.implicit()
son.implicit()

dad.altered()
son.altered()

dad.override()
son.override()



class Other:
    def override(self):
        print("Other override")

    def implicit(self):
        print("Other implicit")

    def altered(self):
        print("Other altered")

class Child:
    
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child Override")

    def altered(self):
        print("Child, before other altered")
        self.other.altered()
        print("Child, after Other altered")

son = child()

son.implicit()
son.override()
son.altered()
