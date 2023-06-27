"""
break : break is a statement whic is used  to execute at looping time

using of break statement we can break the statement

syntax:

for i in range(1,6):
    if condition:
        break
        
"""

for i in range(1,6):
    marks = int(input("Enter marks : "))
    if marks>=35:
        print("pass")
    else:
        print("fail")
        break
        
