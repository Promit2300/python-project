list1 = ["apple","orange","mango"]
print(list1[1])

list2 = ["banana","tetol","guaba","lichi","rasberry"]

print(list2[1:3])

list3 = list1 + list2
print(list3)

list1.append("strawberry")
print(list1)

list2.remove("tetol")
print(list2)

list2.pop(1)
print(list2)

list4 = [x for x in list2]
print(list4)