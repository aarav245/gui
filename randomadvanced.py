from tkinter import *
import random
from tkinter import messagebox
screen = Tk()
screen.title("guess the product")
label1 = Label(screen,text = "guess the product of the number and __.",font = ("Arial",15),bg = "white")
label1.pack()
entry1 = Entry(screen,font = ("Arial",15))
entry1.pack()
button1 = Button(screen,text = "guess",font = ("Arial",15),fg = "black")
button1.pack()
button2 = Button(screen,text = "reset",font = ("Arial",15),fg = "black")
button2.pack()
screen.mainloop()