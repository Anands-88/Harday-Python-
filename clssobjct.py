class Person:
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("First name is :"," Last name is :", sep='   ')

#Use the Person class to create an object, and then execute the printname method:

fullname = Person("John","Doe")
fullname.printname()


print(fullname.firstname.rjust(18), end=' ') # put attribute here , self.firstname, firstname is attribute
print(fullname.lastname.rjust(17))# put attribute here , self.lastname, lastname is attribute
