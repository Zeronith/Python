'''
Python Inheritance 
Нэг классаас өөр класс удамшин тухайн классын бүх гишүүн өгөгдөл болон функцийг өвлөж авахыг удамшил гэдэг .
Parent Class буюу эх класс 
Child Class буюу удамшсан класс
'''

class person :
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self) :
        print(f"Hello my name is {self.fname} {self.lname}")

# Used person class to create object
Male = person("Enguunbayar" , "Ganzorig")

# Удамшуулахдаа 
class student(person) :
    pass 


# Удамшил
x = student("Mike", "Olsen")
x.printname()




'''ЭНДЭЭС ЭХЛЭЭД АЙМАР ЧУХАЛ ЮМ ЯРИХ ГЭЖ БАЙНА ШҮҮ ТЭГЭХЭЭР АНХААРАЛТАЙ УНШААРАЙ'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname): # EXPLAINED ON 1 
    Person.__init__(self, fname, lname) # EXPLAINED ON 2

x = Student("Mike", "Olsen")
x.printname()
 
# 1. When we add __init__() constructor in child class, they use their own constructor not their parent class
# We need to keep parent class's constructor . 

# 2. To keep parent class constructor we call parent class's constructor from child class constructor 





class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname): 
    super().__init__(fname, lname) # Super function allows you to call your parent class's (super class) method
    # So its just calling parent class's constructor 
x = Student("Lebron", "James")
x.printname()



# Adding member variable 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year # Adding student class's member variable .

x = Student("Mike", "Olsen", 2026)
print(x.graduationyear)



# Adding member function 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()


# ABOUT THE ACCESS SPECIFIER .
# PYTHON USES NAME CONVENTION FOR THIS PRETTY WEIRD HUH

# PUBLIC -> PUBLIC
# PROTECTED -> _PROTECTED
# PRIVATE -> __PRIVATE
