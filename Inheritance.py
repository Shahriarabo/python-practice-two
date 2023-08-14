class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname)
    print(self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Abdullah", "Shahriar")
x.printname()



class rasel:
    car = "BMW"
    taka = "100K"
    home = "kcp"
    house = "big"

class mamun(rasel):
  tree = "mango"
  wecam = "cannon"
  baiek = "Yamaha"

class masum(mamun):
  phone = "samsung"
  face = "beautiful"
  camera = "soney"
  
class rana(masum):
    job = " "
    selali = ""


r = rana()
print(r.car)
print(r.taka)
print(r.home)
print(r.tree)       
print(r.wecam)
print(r.baiek)
print(r.phone)
print(r.face)
print(r.camera)
print(r.house)




class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("RaseL", "Abdullah")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname,self.lastname)

class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("RaseL","Abdullah","2024")
print(x.graduationyear)
x.printname()


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

x = Student("RaseL","Abdullah","2024")
x.welcome()
x.printname()    
