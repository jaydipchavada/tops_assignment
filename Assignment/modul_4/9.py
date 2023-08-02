"""
9) Write a Python program to count the number of lines in a text file ?
=>

"""
botlines = 0
with open("simple.txt","r") as f:
    for lines in f:
        botlines += 1
print(botlines)