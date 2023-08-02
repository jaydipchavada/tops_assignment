num = int(input("Enter the range number :"))
first_val = 0
secound_val = 1
for n in range(0,num):
    if(n<=1):
        next = n
    else:
        next = first_val + secound_val
        first_val = secound_val
        secound_val = next
    print(next)