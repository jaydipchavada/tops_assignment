from tkinter import *
from random import *
from tkinter import messagebox

screen = Tk()

screen.geometry("500x500")  # width x height
screen.title("JAYDIP")
# screen.configure(bg="red")

title = Label(screen,text = "ROCK - PAPER - SCISSOR GAME",font = ('Arial',20,'bold'))
title.pack()

user_var = StringVar()
computer_var = StringVar()
user_score = IntVar()
computer_score = IntVar()

computer_score.set(0)
user_score.set(0)

def myLogic(userchoice):
    l1 = ["ROCK", "PAPER", "SCISSOR"]
    computer_choice = choice(l1)

    user_var.set(userchoice)
    computer_var.set(computer_choice)

    if userchoice == computer_choice:
        pass  # It's a tie, do nothing
    elif (
        (userchoice == "ROCK" and computer_choice == "SCISSOR")
        or (userchoice == "PAPER" and computer_choice == "ROCK")
        or (userchoice == "SCISSOR" and computer_choice == "PAPER")):
        computer_score.set(computer_score.get() + 1)
    else:
        user_score.set(user_score.get() + 1)
   

    # print("USER CHOICE =", userchoice)
    # print("COMPUTER CHOICE =", computer_choice)
    # print(f"USER SCORE: {user_score.get()}")
    # print(f"COMPUTER SCORE: {computer_score.get()}")


def result_show():
    user_score_val = user_score.get()
    computer_score_val = computer_score.get()

    result_msg =(f"User Score: {user_score_val}")
    result_msg =(f"Computer Score: {computer_score_val}")

    if user_score_val > computer_score_val:
        result_msg = "\nCongratulations! You won!"
    elif user_score_val < computer_score_val:
        result_msg = "\nComputer won. Better luck next time!"
    else:
        result_msg = "\nIt's a tie!"

    messagebox.showinfo("GAME RESULT", result_msg)
    

btn_rock = Button(screen,text="ROCK",font=("arial",12,"bold"),bg="black",fg="white",
             activebackground="red",activeforeground="white",command=lambda : myLogic("ROCK"))
btn_rock.place(x=10 , y=40)

btn_paper = Button(screen,text="PAPER",font = ("arial",12,"bold"),bg="black",fg="white" ,command=lambda :myLogic("PAPER"))
btn_paper.place(x=90 , y=40)

btn_scissor = Button(screen,text="SCISSOR",font=("arial",12,"bold"),bg="black",fg="white",
             activebackground="red",activeforeground="white",command=lambda : myLogic("SCISSOR"))
btn_scissor.place(x=180 , y=40)

result_button = Button(screen,text="RESULT",font=("arial",12,"bold"),bg="black",fg="white", command=result_show)
result_button.place(x=280 , y=40)

usechoice_display = Label(screen,text="user_choice : ",font=("arial",12,"bold"))
usechoice_display.place(x=10 , y=100)

usechoice_display = Label(screen,textvariable=user_var,font=("arial",12,"bold"))
usechoice_display.place(x=150 , y = 100)

computer_dispaly = Label(screen,text="computer_choice : ",font=("arial",12,"bold"))
computer_dispaly.place(x=10 , y=140)

computer_dispaly = Label(screen,textvariable=computer_var,font=("arial",12,"bold"))
computer_dispaly.place(x=150 , y = 140)

user_score_label = Label(screen, text="User Score : ", font=("arial", 12, "bold"))
user_score_label.place(x=10, y=190)

user_score_display = Label(screen, textvariable=user_score, font=("arial", 12, "bold"))
user_score_display.place(x=150, y=190)

computer_score_label = Label(screen, text="Computer Score : ", font=("arial", 12, "bold"))
computer_score_label.place(x=10, y=250)

computer_score_display = Label(screen, textvariable=computer_score, font=("arial", 12, "bold"))
computer_score_display.place(x=150, y=250)

screen.mainloop()
