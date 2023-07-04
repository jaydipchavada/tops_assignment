"""
=>  difference between list and tuple :

=> list is a collection data types which is contain similar and dis-similar data element
list which is represent by [] braces when tuples is a collection data types and which contain similar and dis-similar
data element but which is represent by () braces

=> list which is mutable( we can change it value ) - we can perfrom append,insert,remove all operation but same way

=> list is a immutable ( we can't change it value ) - we can perfrom append,insert,remove operation

=> list is slower than tuple
    and tuple is faster than list

"""

#===================================================

t = (1,2,3,4)
print(t)

#==================================================

for i in t:
    print(i)

#=================================================

print(len(t))

#================================================

t1 = ("python","java","android")

l1 = list(t1) # convert tuple into list

l1.append("node.js")

t1 = tuple(l1) # convert list into tiple

print(t1)

#======================================================

t = ("python")
print(type(t)) # type is an inbulit function which is used to check which type of value store in varible

t = ("python",)

print(type(t))