"""thisset = {"apple", "banana", "cherry",1, 3, 7, 8, 7, 5, 4, 6, 8, 5}
print(thisset)"""


"""thisset = {"apple", "banana", "cherry",1, 3, 7, 8, 7, 5, 4, 6, 8, 5}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry",1, 3, 7, 8, 7, 5, 4, 6, 8, 5,"apple", "banana", "cherry"}

print("banana" in thisset)"""



"""thisset = {"apple", "banana", "cherry",1, 3, 7, 8, 7, 5, 4, 6, 8, 5,"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)"""


"""thisset = {"apple", "banana", "cherry",1, 3, 7, 8, 7, 5, 4, 6, 8, 5}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}


thisset.discard("apple")
print(thisset)"""


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
