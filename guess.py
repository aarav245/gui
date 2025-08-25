from tkinter import *
import random
screen = Tk()
screen.geometry("500x300")
screen.title("guesssing game")
attempts = 0
numberselect = random.randint(1,100)
def guess():
    global attempts
    attempts = attempts+1
    userinput = int(entry1.get())
    if userinput < numberselect:
        label2.config(text = "too low!")
    elif userinput > numberselect:
        label2.config(text = "too high!")
    elif userinput == numberselect:
        label2.config(text = f"you won! You took {attempts} attempts",fg = "green")
        button1.config(state = DISABLED)
        entry1.config(state = DISABLED)
    else:
        label2.config("please choose a valid number!",fg = "red")
def reset():
    global attempts
    global numberselect
    numberselect = random.randint(1,100)
    attempts = 0
    label2.config(text = "",fg = "black")
    button1.config(state = NORMAL)
    entry1.config(state = NORMAL)
    entry1.delete(0,END)

label1 = Label(screen,text = "Guess the number",font = ("Arial",25),fg = "blue",bg = "white")
label1.pack()
label2 = Label(screen,text = "",font = ("Arial",15),fg = "black")
label2.pack()
entry1 = Entry(screen,font = ("Arial",10))
entry1.place(x=175,y = 90)
button1 = Button(screen,text = "submit guess",font = ("Arial",15),fg = "white",bg = "lime green",command = guess)
button1.place(x=180,y=130)
button2 = Button(screen,text = "reset game",font = ("Arial",15),fg = "black",bg = "red",command = reset)
button2.place(x=188,y=180)
screen.mainloop()