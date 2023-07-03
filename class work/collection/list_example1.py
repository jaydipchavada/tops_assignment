l1= ["c","c++","java"]

# add some values in list 

# list index always start from 0 index

"""
there are 3 ways to add data in existing list

1) append() : to store data in existing list
2) extend() : to add more then 1 value in list
3) insert() : to store element in list at specific position


"""


# 1) append() : to store data in existing list

"""
for i in range(1,4):
    name = input("Enter Your Subject :")
    l1.append(name)
print(l1)   
"""

# 2) extend() : to add more then 1 value in list

"""

l1.extend(["react","node","javascript"])
print(l1)

"""

# 3) insert() : to store element in list at specific position
"""
l1.insert(1,"python programing")
print(l1)
"""

"""
there are 3 ways to remove element from the list

1) remove() : using remove element from list value wise
2) pop() : using pop we can remove last element of the list and we can pop(index) specific index value
3) clear() : using clear we can remve all the elements from list
4) del : del is keyword using of del keyword we can delete list from memory

"""

l1=[10,20,30,40,50,60,70,80,90,100]
print(l1)

l1.remove(20)
print(l1)

l1.pop()
print(l1)

l1.pop(4)
print(l1)

l1.clear()
print(l1)

# del l1
# print(l1)

l2=[100,200,300]
print(l2.index(200))
