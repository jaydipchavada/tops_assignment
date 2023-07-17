# Write a Python program to check multiple keys exists in a dictionary

d={"a":1,"b":2}
list1=[]

for i in d:
        list1.append(i)

if len(list1) > 1:
        print("Dictionary has more then one key")
