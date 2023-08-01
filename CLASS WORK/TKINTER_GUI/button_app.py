from tkinter import *

screen = Tk()

screen.geometry("500x500")# weigth x highet
screen.title("JAYDIP")

btn = Button(screen,text="button",font=("arial",12,"bold"),bg="black",fg="white",
             activebackground="red",activeforeground="white")

btn.pack(side = LEFT)

btn = Button(screen,text="click here",font = ("arial",12,"bold"))
btn.pack(side=TOP)

screen.mainloop()