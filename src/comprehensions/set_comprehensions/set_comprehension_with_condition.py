mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet = set()
for element in mySet:
    if element % 2 == 0:
        newSet.add(element)
print("The existing set is:")
print(mySet)
print("The Newly Created set is:")
print(newSet)

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet = {element for element in mySet if element % 2 == 0}
print("The existing set is:")
print(mySet)
print("The Newly Created set is:")
print(newSet)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newSet = {element * 3 for element in myList if element % 2 == 0}
print("The existing list is:")
print(myList)
print("The Newly Created set is:")
print(newSet)
