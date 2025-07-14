from tkinter import *
screen = Tk()
screen.geometry("400x400")
#displaying text
label1 = Label(screen,text = "Click the button below",background="yellow",fg = "black", font = ("Arial",25))
label1.place(x=50,y=50)
#adding a button
button = Button(screen,text = "click me!",background = "blue", fg = "white", font = ("Arial",25),command = screen.destroy)
button.place(x=125,y=200)
#adding input
entry = Entry(screen)
entry.place(x=140,y=125)
screen.mainloop()
