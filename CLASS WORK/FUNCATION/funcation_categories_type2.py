# funcation without perameter and funcation with return type

def checkevenodd():
    num = int(input("Enter number : "))
    if num%2== 0:
        return "even number"
    else:
        return "odd number"
    
print(checkevenodd())