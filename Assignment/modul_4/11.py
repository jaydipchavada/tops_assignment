"""
11) Write a Python program to write a list to a file ?
=>

"""
sub = ['Python', 'Java', 'React Js', 'Node Js', 'Andriod', 'Html']
with open("simple1.txt", "a") as myfile:
        for i in sub:
                myfile.write("\n"+i)

content = open("simple.txt")
print(content.read())