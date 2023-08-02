# Write a Python program to print all unique values in a dictionary.

d1 = {'a': 100, 'b': 200, 'c':300, 'd': 300, 'e': 200, 'f':400 }
list1 = []
for i in d1.values():
    list1.append(i)

list1 = set(list1)
print(list1)