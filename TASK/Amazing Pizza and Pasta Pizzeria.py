from datetime import date

jaydip = """
                
                  Welcome to Amazing Pizza and Pasta Pizzeria  

                            press 1: order menu
                            press 2: Exit
                            

        """

print(jaydip)
# print("press 3 : Add customer")




softdrink_discount_quantity = 4
bruschetta_discount_quantity = 4
chocco_brownies_discount_quantity = 4


softdrink_count = 0
bruschetta_count = 0
chocco_brownies_count = 0

total_amount = 0.0
# registered_customers = {}

status = True

while status:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("\n=========================  Pizza  ================================")
        print("\n1 small pizza = 8.99 AUD")
        print("2 medium Pizzas = 15.99 AUD")
        print("3 large Pizzas = 22.99 AUD")
        print("*** Buy 4 or more pizzas and get 1.5lt of soft drink free ***")

        print("\n==========================  Pasta  =================================")
        print("\n1 small pasta = 6.5 AUD")
        print("2 medium pastas = 11.00 AUD")
        print("3 large pastas = 18.50 AUD")
        print("*** Buy 4 or more pastas and get 2 bruschettas free ***")

        print("*** Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free ***")
        print("===========================================================")

        name = input("Enter your name: ")
        print("=================================================")
        print("Welcome,", name)

        # quantity for each pizza size
        small_pizza = int(input("Enter number of small pizzas you want: "))
        medium_pizza = int(input("Enter number of medium pizzas you want: "))
        large_pizza = int(input("Enter number of large pizzas you want: "))

        # quantity for each pasta size
        small_pasta = int(input("Enter number of small pastas you want: "))
        medium_pasta = int(input("Enter number of medium pastas you want: "))
        large_pasta = int(input("Enter number of large pastas you want: "))

        # Calculate total amount for pizzas and pastas
        pizza_total = small_pizza * 8.99 + medium_pizza * 15.99 + large_pizza * 22.99
        pasta_total = small_pasta * 6.5 + medium_pasta * 11.00 + large_pasta * 18.50

        # Calculate total order amount
        total = pizza_total + pasta_total
        print("Your total order amount is:", total)

        # Check for discounts and give free items
        if small_pizza + medium_pizza + large_pizza >= softdrink_discount_quantity:
            print("*** Congratulations! 1.5lt soft drink free ***")
            softdrink_count += 1

        if small_pasta + medium_pasta + large_pasta >= bruschetta_discount_quantity:
            print("*** Congratulations! 2 bruschettas free ***")
            bruschetta_count += 2
            
        if (small_pizza + medium_pizza + large_pizza >= chocco_brownies_discount_quantity) and \
        (small_pasta + medium_pasta + large_pasta >= chocco_brownies_discount_quantity):
            print("*** Congratulations! 2 chocco brownies ice cream free ***")
            chocco_brownies_count += 2
        

        total_amount += total

    elif choice == 2:
        break
    else:
        print("invaid input,please Enter vaild number ")

    
    # elif choice == 3:
    #     # while True:
    #         name = input("Enter customer name: ")
    #         # phone = input("Enter customer phone number: ")
    #         # email = input("Enter customer email address: ")

    #         # registered_customers[name] = {
    #         #     "phone": phone,
    #         #     "email": email
    #         # }

    #         # print("Customer", name, "registered successfully!")

    #         more_orders = input("\nWant to enter order from another customer (Y/N): ").lower()
    #         if more_orders != 'y':
    #             break

    # else:
    #     print("Invalid choice. Please try again.")



date_obj = date.today()
date_str = str(date_obj)

# f= open("registered_customers.txt", "w")  
# for name, data in registered_customers.items():
#         f.write(f"Name: {name}, Phone: {data['phone']}, Email: {data['email']}\n")


f = open(name +date_str + ".txt", "w")
f.write("\n----------- Pizza and pasta Bill --------------")
f.write("\nPayment received today: " + str(total_amount))
f.write("\nNumber of small pizzas sold: " + str(small_pizza))
f.write("\nNumber of medium pizzas sold: " + str(medium_pizza))
f.write("\nNumber of large pizzas sold: " + str(large_pizza))
f.write("\nNumber of small pastas sold: " + str(small_pasta))
f.write("\nNumber of medium pastas sold: " + str(medium_pasta))
f.write("\nNumber of large pastas sold: " + str(large_pasta))
f.write("\nNumber small pizza and pasta sold in one shift:"+str(small_pizza+ small_pasta))
f.write("\nNumber mediam pizza and pasta sold in one shift:"+str(medium_pizza+ medium_pasta))
f.write("\nNumber largepizza and pasta sold in one shift:"+str(large_pizza+ large_pasta))
f.write("\nNumber of 1.5lt soft drink bottles given: " + str(softdrink_count))
f.write("\nNumber of bruschettas given to customers: " + str(bruschetta_count))
f.write("\nNumber of chocco brownies ice cream given to customers: " + str(chocco_brownies_count))

print("\n----------- Pizza and pasta Bill --------------")
print("\nPayment received today:", total_amount)
print("Number of small pizzas sold:", small_pizza)
print("Number of medium pizzas sold:", medium_pizza)
print("Number of large pizzas sold:", large_pizza)
print("Number of small pastas sold:", small_pasta)
print("Number of medium pastas sold:", medium_pasta)
print("Number of large pastas sold:", large_pasta)
print("Number small pizza and pasta sold in one shift:",small_pizza + small_pasta)
print("Number mediam pizza and pasta sold in one shift:",medium_pizza + medium_pasta)
print("Number large pizza and pasta sold in one shift:",large_pizza + large_pasta)
print("Number of 1.5lt soft drink bottles given:", softdrink_count)
print("Number of bruschettas given to customers:", bruschetta_count)
print("Number of chocco brownies ice cream given to customers:", chocco_brownies_count)

f.close()

print("\nThank you for visiting Amazing Pizza and Pasta Pizzeria")
print("Bye Bye!!!")
