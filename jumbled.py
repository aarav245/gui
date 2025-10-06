from tkinter import *
import random
from tkinter import messagebox
screen = Tk()
screen.geometry("500x400")
screen.title("Jumbled letters game")
screen.configure(background="black")
#lists
correct = ["apple", "banana", "cherry", "dragonfruit", "elephant",
    "forest", "galaxy", "harmony", "island", "jungle",
    "knowledge", "lemon", "mountain", "nebula", "ocean",
    "penguin", "quartz", "river", "sunset", "tiger"]
scrambled = ['alppe', 'naaban', 'ceyrrh', 'gdiutnrafor', 'tenaelph',
 'frtose', 'glxaya', 'nrohamy', 'nslida', 'gunlej',
 'woelkndge', 'moenl', 'tnmouani', 'ebnalu', 'ceona',
 'upginen', 'zurtqa', 'eivrr', 'ssunet', 'rgiet']
index = random.randint(0,19)
correctanswers = 0
attempts = 0
playerscore = ""
#functionality
def display():
    global index
    global correct
    global scrambled
    jumbled.configure(text = scrambled[index])
def resetgame():
    global index
    global correct
    global scrambled
    index = random.randint(0,19)
    jumbled.configure(text = scrambled[index])
    entry.delete(0,END)
def checkanswer():
    global correct
    global index
    global correctanswers
    global attempts
    global playerscore
    global scrambled
    attempts = attempts+1
    userinput = entry.get()
    if userinput == correct[index]:
        messagebox.showinfo("correct","you got the answer correct!")
        correctanswers = correctanswers + 1

    else:
        messagebox.showerror("wrong","wrong answer!")
    playerscore = "score:"+str(correctanswers)+"/"+str(attempts)
    score.configure(text = playerscore)   
    
#design
label1 = Label(screen,text = "Jumbled word game",font = ("Arial",30),bg = "black",fg = "white")
label1.pack()
jumbled = Label(screen,text="",font = ("Arial",25),bg = "black",fg="white")
jumbled.place(x=190,y=90)
entry = Entry(screen,font = ("Arial",15))
entry.place(x=135,y=150)
check = Button(screen,text = "Check",font = ("Arial",20),fg="green",bg = "black",command = checkanswer)
check.place(x=190,y=200)
reset = Button(screen,text = "reset",font = ("Arial",20),fg = "red",bg = "black",command = resetgame)
reset.place(x=200,y=265)
score = Label(screen,text = "",font = ("Arial",20),bg = "black",fg = "white")
score.place(x=0,y=360)
display()
screen.mainloop()