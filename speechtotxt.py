from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import speech_recognition as sr

screen = Tk()
screen.geometry("600x300")
#functions
def record():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start speaking")
        audio = recognize.listen(source)
        try:
            text = recognize.recognize_google(audio)
        except:
            text = "The voice cannot be heard"
        box.delete(1.0,END)
        box.insert(END,text)
def save():
    fileextension = filedialog.asksaveasfile(defaultextension=".txt")
    if fileextension:
        fileextension.write(box.get(1.0,END))
        fileextension.close()
    else:
        messagebox.showerror("error","The file cannot be saved!")

#design
label1 = Label(screen,text = "Speech to text",font = ("Arial",20))
label1.pack()
button1 = Button(screen,text = "Click to record",font = ("Arial",15),command = record)
button1.place(x=0,y=100)
box = Text(screen,height = 5,width = 35)
box.place(x=150,y=100)
button2 = Button(screen,text = "save text",font = ("Arial",15),command = save)
button2.place(x=500,y=100)
screen.mainloop()
