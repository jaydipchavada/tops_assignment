import random

game = """
            GAME = ROCK PAPER SCISSOR

            SELECT YOUR CHOICE

            ROCK
            PAPER
            SCISSOR

        """
print(game)
game_list = ["ROCK","PAPER","SCISSOR"]



status = True

c_score = 0
u_score = 0

while status:
    computer_choice = random.choice(game_list)

    user_choice = input("Enter your choice : ").upper()

    print(f"COMPUTER SELECTED :{computer_choice}")
    print(f"USER SELECTED :{user_choice}")

    if user_choice == computer_choice:
        print("TIE")
    elif user_choice == "ROCK" and computer_choice == "PAPER":
        c_score +=1
        print("COMPUTER WON !!!!!")
    elif user_choice == "ROCK" and  computer_choice == "SCISSOR":
        u_score +=1
        print("USER WON !!!!!!!")
    elif user_choice == "SCISSOR" and computer_choice =="ROCK":
        u_score +=1
        print("USER WON !!!!!!")
    elif user_choice == "SCISSOR" and computer_choice == "PAPER":
        u_score +=1
        print("USER WON !!!!!!")
    elif user_choice == "PAPER" and computer_choice == "ROCK":
        u_score +=1
        print("USER WON !!!!!!!!!!!")
    elif user_choice == "PAPER" and computer_choice == "SCISSOR":
        c_score +=1
        print("COMPUTER WON !!!!!")

    choice = input("do you want to continue press y for yes and n  for no : ")
    if choice == 'n':
        status= False

print (f" USER SCORE : {user_choice}")


