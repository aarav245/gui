from tkinter import *
from gtts import gTTS
import os
screen = Tk()
screen.geometry("500x500")
#functions
def conversion():
    language = "hi"
    obj = gTTS(text = entry1.get(),lang = language,slow = False)
    obj.save("speech.wav")
    #playing the sound
    os.system("speech.wav")
#design
frame1 = Frame(screen,bg = "blue",height = "100")
frame1.pack(fill = X)
frame2 = Frame(screen,bg = "yellow",height = "400")
frame2.pack(fill=X)
label1 = Label(screen,text = "Text to speech",font = ("Arial",25),fg = "white",bg = "blue")
label1.place(x=150,y=40)
entry1 = Entry(screen,font = ("Arial",20))
entry1.place(x=110,y=200)
button1 = Button(screen,text = "Submit",font = ("Arial",15),fg = "white",bg = "blue",command = conversion)
button1.place(x=205,y=270)
screen.mainloop()