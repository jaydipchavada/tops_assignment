import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)
engine.setProperty

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

status = True 

while status:
    print("Welcome to kalyan Jwellers")
    engine.say(".Welcome to kalyan Jwellers!")
    engine.runAndWait()

    engine.say(".Enter your Name!")
    engine.runAndWait()
    name = input("Enter your Name : ")
    
    engine.say(".Enter your Gender(male,female)!")
    engine.runAndWait()
    gender = input("Enter your Gender(male,female) : ")
    
    engine.say(".Enter your age!")
    engine.runAndWait()
    age = int(input("Enter your age : "))
    
    print("--------------------------------------------------")

    engine.say(".Enter product name : !")
    engine.runAndWait()
    product = input("Enter product name : ")
    
    engine.say(".Entern product Gram : !")
    engine.runAndWait()
    gram = int(input("Enter product gram : "))
    
    engine.say("Current Gold Price (1 Gram) : 5752")
    engine.runAndWait()
    print("Current gold price (1 gram) : 5752")
    total_gold_price = gram * 5752

    print("---------------------------------------------------")

    engine.say("Your total price is :" , total_gold_price)
    engine.runAndWait()
    print("Your total gold price is : ",total_gold_price)

    engine.say("Making Charges (1 Gram)")
    engine.runAndWait()
    print("Making charges (1 gram) : 845")
    total_making_charges = gram * 845

    engine.say("total making charges is: ",total_making_charges)
    print("Total making charges is : ",total_making_charges)

    print("----------------------------------------------------")

    total_amount = total_gold_price + total_making_charges
    
    engine.say("total amount is : ", total_amount)
    engine.runAndWait()
    print("Total amount is : ",total_amount)



    if gender == "male":
        if age >= 65:
            if total_amount > 210000 and total_amount < 310000:
                print("20% Discount on purchase of 2 lakh to 3 lakh")
                total_net_amount =  total_amount - (total_amount * 0.2)
                print("Your total net amount is : ",total_net_amount)
            
        elif total_amount > 310000 and total_amount < 510000:
            print("30% Discount on purchase of 3 lakh to 5 lakh")
            total_net_amount =  total_amount - (total_amount * 0.3)
            print("Your total net amount is : ",total_net_amount)

        elif total_amount > 510000:
            print("35% Discount on purchase to above 5 lakh")
            total_net_amount =  total_amount - (total_amount * 0.35)
            print("Your total net amount is : ",total_net_amount)
    else:
       if age < 65:

        if total_amount > 210000 and total_amount < 310000:
            print("10% Discount on purchase of 2 lakh to 3 lakh")
            total_net_amount =  total_amount - (total_amount * 0.1)
            print("Your total net amount is : ",total_net_amount)

        elif total_amount > 310000 and total_amount < 510000:
            print("20% Discount on purchase of 3 lakh to 5 lakh")
            total_net_amount =  total_amount - (total_amount * 0.2)
            print("Your total net amount is : ",total_net_amount)

        elif total_amount > 510000:
            print("25% Discount on purchase to above 5 lakh")
            total_net_amount =  total_amount - (total_amount * 0.25)
            print("Your total net amount is : ",total_net_amount)

        elif gender == "female":
            if age >= 65:
            
                if total_amount > 210000 and total_amount < 310000:
                    print("25% Discount on purchase of 2 lakh to 3 lakh")
                total_net_amount =  total_amount - (total_amount * 0.25)
                print("Your total net amount is : ",total_net_amount)

            elif total_amount > 310000 and total_amount < 510000:
                print("35% Discount on purchase of 3 lakh to 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.35)
                print("Your total net amount is : ",total_net_amount)

            elif total_amount > 510000:
                print("40% Discount on purchase to above 5 lakh")
                total_net_amount =  total_amount - (total_amount * 0.4)
                print("Your total net amount is : ",total_net_amount)
       else:
         
         if total_amount > 210000 and total_amount < 310000:
            print("15% Discount on purchase of 2 lakh to 3 lakh")
            total_net_amount =  total_amount - (total_amount * 0.15)
            print("Your total net amount is : ",total_net_amount)
            
         elif total_amount > 310000 and total_amount < 510000:
            print("25% Discount on purchase of 3 lakh to 5 lakh")
            total_net_amount =  total_amount - (total_amount * 0.25)
            print("Your total net amount is : ",total_net_amount)
            
         elif total_amount > 510000:
            print("30% Discount on purchase to above 5 lakh")
            total_net_amount =  total_amount - (total_amount * 0.3)
            print("Your total net amount is : ",total_net_amount)
    check = input("do you want to contiue ? press y  for yes and n for no :  ")
    if check == 'y' or  check == 'yes' :
        status = True
    else:
        status = False
else:
    engine.say("thank you visiting again...!")
    print("Thank you visiting again \N{Person with Folded Hands}")
  
engine.runAndWait()

