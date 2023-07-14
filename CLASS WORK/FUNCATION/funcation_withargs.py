"""
args : argument -  funcation with arguments

tuples as a parameter

"""

def myfun(*args):
    sum = 0
    for i in args:
        sum += i

    return sum
print(myfun(1,2,3,4,5,6,7))