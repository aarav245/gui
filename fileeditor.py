from tkinter import *
from tkinter.filedialog import *
screen = Tk()
screen.title("file editor")
#functions
def fileopen():
    openfile = askopenfile(title="Open a file")
    if openfile is not None:
        listbox.delete(0,END)
        readfile = openfile.readlines
        for i in readfile():
            listbox.insert(END,i.strip())
def filesave():
    savefile = asksaveasfile(defaultextension=".txt")
    if savefile is not None:
        for i in listbox.get(0,END):
            print(i.strip(),file = savefile)
            listbox.delete(0,END)
def deleting():
    selection = listbox.curselection()
    listbox.delete(selection)
def adding():
    listbox.insert(END,entry.get())
    entry.delete(0,END)

frame = Frame(screen)
save = Button(screen,text = "Save",font = ("Arial",15),command = filesave)
add = Button(screen,text = "Add",font = ("Arial",15),command=adding)
add.pack(padx = 10,pady=10)
open = Button(screen,text = "Open",font = ("Arial",15),command = fileopen)
open.pack(side = LEFT, padx = 10,pady=10)
save.pack(side = RIGHT,padx = 10,pady = 10)
entry = Entry(screen,font = ("Arial",15))
entry.pack()
delete = Button(screen,text="Delete",font = ("Arial",15),command = deleting)
delete.pack(padx=10,pady=10)
scrollbar = Scrollbar(frame,orient = VERTICAL)
scrollbar.pack(side = RIGHT,fill = Y)
#listbox
listbox = Listbox(frame,width = 75,yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(END,"list"+str(i))
listbox.pack(side = LEFT,padx = 10,pady = 10)
scrollbar.config(command = listbox.yview)
frame.pack(side = RIGHT)
screen.mainloop()