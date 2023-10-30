#Create class called Cat.
class Cat:
    def miaow(self):
        print('Miaow!')
        
my_cat = Cat()
my_cat.miaow()

#Creating variable and using it to store cat's name.
class Cat:
    name = 'Cleo'
    
    def miaow(self):
        print('Miaow!')
        
my_first_cat = Cat()
my_second_cat = Cat()

print(my_first.cat.name)
print(my_second.cat.name)

#Creating cat objects and giving them names.
class Cat:
    def __init__(self, name):
        self.name = name
        
    def miaow(self):
        print('Miaow!')
        
my_first_cat = Cat('Cleo')
my_second_cat = Cat('Tinkerbell')

print(my_first.cat.name)
print(my_second.cat.name)

#Creating classes that will inherit from cat class and extend it's functionality.
class Cat:
    
    def __init__(self, name):
        self.name = name
        
    def purr(self):
        print('Purr!')
        
class Lion(Cat):
    
    def roar(self):
        print('ROAR!')

class DomesticCat(Cat):
    
    def miaow(self):
        print('Miaow!')
        
my_lion = Lion('Leo')
my_lion.purr()
my_lion.roar()
        
my.cat = DomesticCat('Cleo')
my.cat.purr()
my.car.miaow()
#Both my_cat and my_lion can purr but only lions can roar and only domestic cats can miaow.

#Check the type of our objects.
data_type = type(my_cat)
print(data_type)
data_type = type(my_lion)
print(data_type)

#Program that models students and teaches, they are both types of person.
#Basic idea
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#With first and last names.
class Person:
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

#With student class, which inherits person class's __init__ function.
class Person:
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Pug","Dog")
x.printname()

#Add _init__() function to student class (it will no longer inherit person class's __init__() function).
class Person:
    
    def__init(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
x = Student("Pug", "Dog")
x.printname()

#Add methods to student class.
class Person:
    
    def__init(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = year
        
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
        
x = Student ("Pug", "Dog", 2023)
x.welcome()