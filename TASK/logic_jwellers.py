def shopping(yourname,gender,age,productname,productgram):

    # print("Enter your name : ",yourname)   
    # print("enter your gender : ",gender)
    # print("Enter your age : ",age)
    # print("Enter product name : ",productname)
    # print("Enter product gram : ",productgram)
 
    print("Current gold price (1 gram) : 5752")
    total_gold_price = productgram * 5752
    print("Your total gold price is : ",total_gold_price)
    print("Malking charge (1 gram) : 845")
    total_making_charges = productgram * 845
    print("total making charge is :",total_making_charges)
    
    total_amount = total_gold_price + total_making_charges
    print("total amount is : ",total_amount)
    
    if gender == "male":
            if age >= 65:
                if total_amount > 200000 and total_amount < 300000:
                    print("20% Discount on purchase of 2 lakh to 3 lakh")
                    total_net_amount =  total_amount - (total_amount * 0.2)
                    print("Your total net amount is : ",total_net_amount)
                elif total_amount > 300000 and total_amount < 500000:
                    print("30% Discount on purchase of 3 lakh to 5 lakh")
                    total_net_amount =  total_amount - (total_amount * 0.3)
                    print("Your total net amount is : ",total_net_amount)
                elif total_amount > 500000:
                    print("35% Discount on purchase to above 5 lakh")
                    total_net_amount =  total_amount - (total_amount * 0.35)
                    print("Your total net amount is : ",total_net_amount)
            else:
                if age < 65:
                    if total_amount > 200000 and total_amount < 300000:
                        print("10% Discount on purchase of 2 lakh to 3 lakh")
                        total_net_amount =  total_amount - (total_amount * 0.1)
                        print("Your total net amount is : ",total_net_amount)
                    elif total_amount > 300000 and total_amount < 500000:
                        print("20% Discount on purchase of 3 lakh to 5 lakh")
                        total_net_amount =  total_amount - (total_amount * 0.2)
                        print("Your total net amount is : ",total_net_amount)
                    elif total_amount > 500000:
                        print("25% Discount on purchase to above 5 lakh")
                        total_net_amount =  total_amount - (total_amount * 0.25)
                        print("Your total net amount is : ",total_net_amount)
    elif gender == "female":
            if age >= 65:
                    if total_amount > 200000 and total_amount < 300000:
                        print("25% Discount on purchase of 2 lakh to 3 lakh")
                        total_net_amount =  total_amount - (total_amount * 0.25)
                        print("Your total net amount is : ",total_net_amount)
                    elif total_amount > 300000 and total_amount < 500000:
                        print("35% Discount on purchase of 3 lakh to 5 lakh")
                        total_net_amount =  total_amount - (total_amount * 0.35)
                        print("Your total net amount is : ",total_net_amount)
                    elif total_amount > 500000:
                        print("40% Discount on purchase to above 5 lakh")
                        total_net_amount =  total_amount - (total_amount * 0.4)
                        print("Your total net amount is : ",total_net_amount)
            else:
                if total_amount > 200000 and total_amount < 300000:
                    print("15% Discount on purchase of 2 lakh to 3 lakh")
                    total_net_amount =  total_amount - (total_amount * 0.15)
                    print("Your total net amount is : ",total_net_amount)
                elif total_amount > 300000 and total_amount < 500000:
                    print("25% Discount on purchase of 3 lakh to 5 lakh")
                    total_net_amount =  total_amount - (total_amount * 0.25)
                    print("Your total net amount is : ",total_net_amount)
                elif total_amount > 500000:
                    print("30% Discount on purchase to above 5 lakh")
                    total_net_amount =  total_amount - (total_amount * 0.3)
                    print("Your total net amount is : ",total_net_amount)
    else: 
        print("Thank you visit again\N{person with Folded Hands}")
    return total_gold_price,total_making_charges,total_amount,total_net_amount
                    

                        
                       