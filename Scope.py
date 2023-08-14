def rasel():
    r = 100
    print(r)

rasel()

def myfunc():
  x = 500
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#########Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)



def myfunc():
  global x
  x = 3000000000000000

myfunc()

print(x)
