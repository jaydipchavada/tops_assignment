# Write a Python function to get the largest number, smallest num and sum of all from a list.


def lnum(list1):
    largest = list1[0]  

    for i in list1:
        if i > largest:
            largest = i

    return largest 


def snum(list1):
    smallest = list1[0]  

    for i in list1:
        if i < smallest :
            smallest = i

    return smallest 

def sum(list1):
    global sum1
    for a in list1:
        sum1 = sum1 + a
    return sum1
    

sum1 = 0
list1 = []

items= int(input("Enter How Many Items Want To Add In list : "))

for i in range(items):
    iname =int(input("Enter Item : "))
    list1.append(iname)


print("Enterd List : ",list1)
print("Largest Number in List : ",lnum(list1))
print("Smallest Number in List : ",snum(list1))
print("Sum Of All Elements : ", sum(list1))
