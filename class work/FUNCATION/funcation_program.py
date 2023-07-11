"""
funcation : funcation is a block code that code are used to again and again

using of funcation we can reduce code and save time

we can call code multiple times

there are 2 types of funcation

1) built-in funcation
2) user defined funcation

--> 1) built in funcation :

    which is predefined by python

    e.g  print(), input(), len(), renge() ..............

    2) user defined funcation :

        a funcation which is defined by user defined funcation

        there are 2 steps to create user defined funcation

        1)funcation declaration or defination
        2)funcation calling

        => funcation defination :
        def   <funname>():
            statement
            // block of code
"""

def greeting(): # funcation defination
    print("hello welome to python ")

for i in range(1,4):
    greeting()