from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import os,ast

screen =Tk()
screen.title("Adressbook")
screen.geometry("600x700")
#functions
book = {}
def clearbox():
    namebox.delete(0,END)
    addressbox.delete(0,END)
    phonebox.delete(0,END)
    emailbox.delete(0,END)
    birthbox.delete(0,END)
def updatelist():
    key = namebox.get()
    if key == "":
        messagebox.showinfo("Error","You have to put a name")
    else:
        if key not in book.keys():
            listbox.insert(END,key)
        book[key] = (addressbox.get(),phonebox.get(),emailbox.get(),birthbox.get())
        clearbox()
def display(event):
    screen2 = Toplevel(screen)
    listboxindex = listbox.curselection()
    details = ""
    if listboxindex:
        key = listbox.get(listboxindex)
        details = "NAME   :"+key+"\n\n"
        takebook = book[key]
        details +="ADDRESS   :"+takebook[0]+"\n"
        details +="PHONE   :"+takebook[1]+"\n"
        details +="EMAIL   :"+takebook[2]+"\n"
        details +="BIRTHDAY   :"+takebook[3]+"\n"
    labelnew = Label(screen2)
    labelnew.grid(row=0,column=0)
    labelnew.configure(text = details)
def reset():
    clearbox()
    listbox.delete(0,END)
    book.clear()

def savefile():
    fileextension = asksaveasfile(defaultextension=".txt")
    if fileextension:
        print(book,file=fileextension)
        reset()
    else:
        messagebox.showinfo("info","addressbook isn't saved!")
def editfile():
    clearbox()
    index = listbox.curselection()
    if index:
        namebox.insert(0,listbox.get(index))
        contact = book[namebox.get()]
        addressbox.insert(0,contact[0])
        phonebox.insert(0,contact[1])
        emailbox.insert(0,contact[2])
        birthbox.insert(0,contact[3])
    else:
        messagebox.showinfo("error","you must select a contact first")
def deletecontact():
    index = listbox.curselection()
    if index:
        del book[listbox.get(index)]
        listbox.delete(index)
        clearbox()
    else:
        messagebox.showinfo("error","you must select a contact first")

        

#designing
title = Label(screen,text = "My address book",font = ("Arial",15))
title.place(x=170,y=10)
open = Button(screen,text = "Open",font = ("Arial",15))
open.place(x=335,y=10)
name = Label(screen,text = "Name:",font = ("Arial",15))
name.place(x=335,y=100)
namebox = Entry(screen,font = ("Arial",10))
namebox.place(x=425,y=105)
address = Label(screen,text = "Address:",font = ("Arial",15))
address.place(x=335,y=200)
addressbox = Entry(screen,font = ("Arial",10))
addressbox.place(x = 425,y=205)
Phone = Label(screen,text = "Phone:",font = ("Arial",15))
Phone.place(x=335,y=300)
phonebox = Entry(screen,font = ("Arial",10))
phonebox.place(x=425,y=305)
email = Label(screen,text = "Email:",font = ("Arial",15))
email.place(x=335,y=400)
emailbox = Entry(screen,font = ("Arial",10))
emailbox.place(x=425,y=405)
Birthday = Label(screen,text = "Birthday:",font = ("Arial",15))
Birthday.place(x=335,y=500)
birthbox = Entry(screen,font = ("Arial",10))
birthbox.place(x=425,y=505)
update = Button(screen,text = "Update/add",font = ("Arial",15),command = updatelist)
update.place(x=425,y=555)
save = Button(screen,text = "Save",font = ("Arial",15),width = 45,command = savefile)
save.place(x=50,y=650)
listbox = Listbox(screen,font = ("Arial",20),width = 15,height = 15)
listbox.place(x=50,y=50)
listbox.bind('<<ListboxSelect>>',display)
edit = Button(screen,text = "Edit",font = ("Arial",15),command = editfile)
edit.place(x=50,y=560)
delete = Button(screen,text = "delete",font = ("Arial",15),command = deletecontact)
delete.place(x=145,y=560)
screen.mainloop()