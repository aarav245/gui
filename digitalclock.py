from tkinter import *
from time import strftime
from tkinter.ttk import *
screen = Tk()
screen.title("clock")
def clock():
    string = strftime('%H:%M:%S %p')
    label1.config(text = string)
    label1.after(1000,clock)
label1 = Label(screen,font = ("Arial",60),background = "blue",foreground = "white")
label1.pack()
clock()
screen.mainloop()