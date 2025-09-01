from tkinter import *
from tkinter.ttk import *
screen = Tk()
screen.title("multiply")
label1 = Label(screen,text = "Mathematical Table",font = ("Arial",15))
label2 = Label(screen,text = "Number and range:",font = ("Arial",15))
label1.grid(row = 0,column = 0,columnspan=3,pady = 20)
label2.grid(row = 1,column = 0,padx = 30)
#combobox
number = IntVar()
combo = Combobox(screen,text = number)
combo['values'] = tuple(range(101))
combo.grid(row = 1,column=1)
button1 = Button(screen,text = "enter",font = ("Arial",15))
button1.grid(row = 2,column = 1)
screen.mainloop()