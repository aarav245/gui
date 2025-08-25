from tkinter import *
import random
screen = Tk()
screen.geometry("700x300")
screen.title("Rock Paper Scissors game")
title = Label(screen,text = "Rock Paper Scissors game!",font = ("Arial",20),fg = "Brown",bg = "White")
title.pack()
#adding functionality
playerscore = 0
compscore = 0
computerchoose = [("rock",0),("paper",1),("scissors",2)]
def cpuwin():
    global playerscore, compscore
    compscore += 1
    score4.config(text = "Computer score: "+str(compscore))
    score2.config(text = "Player score: "+str(playerscore))
    win.config(text = "Computer wins!")
def playerwin():
    global playerscore, compscore
    playerscore += 1
    score4.config(text = "Computer score: "+str(compscore))
    score2.config(text = "Player score: "+str(playerscore))
    win.config(text = "Player wins!")
def tie():
    global playerscore, compscore
    score4.config(text = "Computer score: "+str(compscore))
    score2.config(text = "Player score: "+str(playerscore))
    win.config(text = "Tie!")
def compselect():
    return random.choice(computerchoose)
def playerselect(playerselection):
    global playerscore, compscore
    print(playerselection)
    computerselection = compselect()
    print(computerselection)
    score1.config(text = "You selected: "+playerselection[0])
    score3.config(text = "Computer selected: "+computerselection[0])
    if playerselection == computerselection:
        tie()
    if playerselection[1] == 0:
        if computerselection[1] == 1:
            cpuwin()
        if computerselection[1] == 2:
            playerwin()
    if playerselection[1] == 1:
        if computerselection[1] == 0:
            playerwin()
        if computerselection[1] == 2:
            cpuwin()
    if playerselection[1] == 2:
        if computerselection[1] == 0:
            cpuwin()
        if computerselection[1] == 1:
            playerwin()

        
win = Label(screen,text = "",font = ("Arial",15),fg = "green",bg = "white")
win.pack()
option = Label(screen,text = "Your options:",font = ("Arial",15),fg = "black",bg = "white")
option.place(x=30,y=100)
buttonframe = Frame(screen)
buttonframe.pack(pady = (30,0))
button1 = Button(buttonframe, text = "Rock",font = ("Arial",15),fg = "White",bg = "pink",command = lambda: playerselect(computerchoose[0]))
button1.pack(side = LEFT,padx = 10)
button2 = Button(buttonframe, text = "Paper",font = ("Arial",15),fg = "White",bg = "aqua",command = lambda: playerselect(computerchoose[0]))
button2.pack(side = LEFT,padx = 10)
button3 = Button(buttonframe, text = "Scissors",font = ("Arial",15),fg = "White",bg = "green",command = lambda: playerselect(computerchoose[0]))
button3.pack(side = LEFT,padx = 10)
score = Label(screen,text = "Score:",font = ("Arial",15),fg = "black",bg = "white")
score.place(x=30,y=200)
score1 = Label(screen,text = "You selected:",font = ("Arial",15),fg = "Brown",bg = "White")
score1.place(x=120,y=200)
score2 = Label(screen,text = "Player score:",font = ("Arial",15),fg = "Brown",bg = "White")
score2.place(x=400,y=200)
score3 = Label(screen,text = "Computer selected:",font = ("Arial",15),fg = "Brown",bg = "White")
score3.place(x=120,y=250)
score4 = Label(screen,text = "Computer score:",font = ("Arial",15),fg = "Brown",bg = "White")
score4.place(x=400,y=250)
screen.mainloop()
