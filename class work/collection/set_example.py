"""
set : set is a collection data types 

    set which is immutable , unorderable, unindexable

    set does not contain duplicate element
    set which is represent by {}

"""
#====================================================
s = {10,20,30}
print(s)

#====================================================================================================

s1 = {"java","python","android","php","node.js","android","java"}
print(s1)

#=====================================================================================================

# imp : remove duplicate elements from list or find unique value from th list

l1 = [12.223,34,45,45,12]
s = set(l1) # convert list into set
print(s)

#=====================================================================================================

# imp : remove duplicate elements from list or find unique value from th list without using set

unique_list = []

l1 = ["java","python","php","java","php"]

for i in l1:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)