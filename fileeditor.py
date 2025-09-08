from tkinter import *
from tkinter.filedialog import *
screen = Tk()
screen.title("file editor")
frame = Frame(screen)
save = Button(screen,text = "Save",font = ("Arial",15))
save.pack(side = RIGHT,padx = 5,pady = 5)
entry = Entry(screen,font = ("Arial",15))
entry.pack()
screen.mainloop()