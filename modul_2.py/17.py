def ing_ly (string):# create a function (ing_ly) and pass one parameter
    if len(string) >= 3: # string length greatter then 3 then block is execute
        if string.endswith("ing"): # string end with ing than block is execute
            string+= 'ly' # add ly in string
        else: # string not end with ing and execute
            string+= 'ing'# add ing in string
        return string

# calling fuction 
string = input("Enter the string : ")# taking a variable and accept the value from user.
print(ing_ly(string))# print and pass the parameter.
