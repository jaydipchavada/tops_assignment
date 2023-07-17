# Write a Python function that takes two lists and returns true if they have at least one common member.

def fn_Com_check(list1,list2):

    for i in list1:
        if i in list2:
            return "Common Element Available"
    
    return "Common Element Not Available"

list1 = []
list2 = []

lenghtoflist1 = int(input("How Many Elemets want to add in list 1 : "))
for i in range(1,lenghtoflist1+1):
    item = input("Enter Item :")
    list1.append(item)

lenghtoflist2 = int(input("How Many Elemets want to add in list 2 : "))
for j in range(1,lenghtoflist2+1):
    item = input("Enter Item :")
    list2.append(item)

print(fn_Com_check(list1,list2))
