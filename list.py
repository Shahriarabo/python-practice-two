"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "e" in x]

print(newlist)"""



"""thislist = ["apple", "banana", "cherry"]
print(thislist[1])"""



"""thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "orange")
print(thislist)"""


"""thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)"""





"""thislist = ["apple", "banana", "cherry", "Fokir", "Sakib"]
for x in thislist:
  print(x)"""

"""lists = ["apple", "banana", "cherry", "Fokir", "Sakib"]
for i in range(len(lists)):
  print(i)




thislist = ["apple", "banana", "cherry", "Fokir", "Sakib"]
i = 0
while i < len(thislist):
  print(i,thislist)
  i = i + 1


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]"""

"""<<<<<<<<<<<<<<<<<List Comprehension>>>>>>>>>>>>>>>>"""

"""""numbers = [1, 2, 3, 4, 5]


lists = [number**3 for number in numbers]
print(lists)"""""





"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)



thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)"""



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list2 + list1
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.append(list2)

print(list1)


fruits = ["apple", "banana", "cherry"]
print(fruits[1])

