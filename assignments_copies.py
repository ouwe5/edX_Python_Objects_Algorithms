import os; os.system("clear")

class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def capitalizeName(name):
    name.firstname = name.firstname.upper()
    name.lastname = name.lastname.upper()

def capitalizeString(instring):
    instring = instring.upper()

myPerson = Person(Name("David", "Joyner"), "brown", 30)
capitalizeString(myPerson.name.firstname)
capitalizeString(myPerson.name.lastname)
print(myPerson.name.firstname)
print(myPerson.name.lastname)

myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = myPerson1
myPerson2.eyecolor = "blue"
print("myPerson1's eyecolor: " + myPerson1.eyecolor)
print("myPerson2's eyecolor: " + myPerson2.eyecolor)
myPerson = Person(Name("David", "Joyner"), "brown", 30)
capitalizeName(myPerson.name)
print(myPerson.name.firstname)
print(myPerson.name.lastname)

myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = Person(myPerson1.name, myPerson1.eyecolor, myPerson1.age)
myPerson2.eyecolor = "blue"
print(myPerson1.eyecolor)
print(myPerson2.eyecolor)
myPerson2.name.firstname = "Vrushali"
print(myPerson1.name.firstname)
print(myPerson2.name.firstname)

myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = Person(Name(myPerson1.name.firstname, myPerson1.name.lastname),
                   myPerson1.eyecolor, myPerson1.age)
myPerson2.eyecolor = "blue"
print(myPerson1.eyecolor)
print(myPerson2.eyecolor)
myPerson2.name.firstname = "Vrushali"
print(myPerson1.name.firstname)
print(myPerson2.name.firstname)
