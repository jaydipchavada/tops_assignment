# Write a Python program to remove an empty tuple(s) from a list of tuples.

list1 = [(10,20),(),(30,30),(40,50),(),(60,20)]

for i in list1:
    if len(i) ==0:
        list1.remove(i)

print(list1)