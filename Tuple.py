"""thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


thistuple = ("apple", "banana", "cherry", "find","well","done","found")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry", "find","well","done","found")
print(type(thistuple))


thistuple = ("apple", "banana", "cherry")
print(thistuple[2])


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[4:7])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[0:])"""


"""x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "kiwi"
x = tuple(y)
print(x)
"""


"""thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)"""



"""fruits = ("apple", "banana", "cherry")

g, y,r = fruits

print(g)
print(y)
print(r)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)"""


"""thistuple = ("apple", "banana", "cherry", "rad","blue","green")
for i in thistuple:
    print(i)


thistuple = ("apple", "banana", "cherry", "rad","blue","green")
for i in range(len(thistuple)):
  print(thistuple[i])"""


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)




fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)
y = thistuple.count(8)
print(x,y)



fruits = ("apple", "banana", "cherry")
print(fruits[0])
