from tkinter import *
import random
from tkinter import messagebox
def generate():
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    return num1,num2,num1*num2
#calling the generate function
first,second,result = generate()
def guess():
    global result
    product = int(entry1.get())
    if product == result:
        messagebox.showinfo("correct","you are correct!")
    elif product != result:
        messagebox.showerror("wrong","your answer is incorrect!")
    else:
        messagebox.showwarning("error","please put a valid answer!")

screen = Tk()
screen.title("guess the product")
label1 = Label(screen,text = "guess the product of the number and __.",font = ("Arial",15),bg = "white")
label1.pack()
entry1 = Entry(screen,font = ("Arial",15))
entry1.pack()
def reset():
    global first
    global second
    global result
    global label1
    first,second,result = generate()
    label1.config(text = "guess the product of the {} and __.".format(first))
    messagebox.showinfo("question","A random number is {}".format(first))
    entry1.delete(0,END)
#reset()
button1 = Button(screen,text = "guess",font = ("Arial",15),fg = "black",command = guess)
button1.pack()
button2 = Button(screen,text = "new game",font = ("Arial",15),fg = "black",command = reset)
button2.pack()
screen.mainloop()
