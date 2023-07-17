# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def fn_uni_item_list (list1):
    list1 = set(list1)
    list1 = list(list1)
    return list1

list1 = []
lenghtoflist1 = int(input("How Many Elemets want to add in list : "))

for i in range(1,lenghtoflist1+1):
    item = input("Enter Item :")
    list1.append(item)

list1 = set(list1)
list1 = list(list1)
print(fn_uni_item_list(list1))