# Write a Python program to find the highest 3 values in a dictionary

d= {'a':1,'b':2,'c':3,'d':4}

list1 = list(d.values())
list1.sort()
max3 = list1[-1:-4:-1]
print(max3)
