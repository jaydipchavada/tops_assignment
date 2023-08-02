"""
12) Write a Python program to copy the contents of a file to another file ?
=>
"""
with open("simple.txt","r") as file1:
    a=file1.read()

with open("simple1.txt","a") as file2:
    file2.write(a)