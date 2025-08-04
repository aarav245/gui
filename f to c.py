from tkinter import *
import tkinter.font as font

screen = Tk()
screen.geometry("600x600")
screen.title("Temprature converter")
#function
def conversion():
    recieve = value.get()
    if recieve.isdigit():
        error.place_forget()
        recieve = float(recieve)
        final = (recieve * 9/5) + 32
        finalconvert.config(text = "The temprature in Farenheit is: "+str(final))
    else:
        error.config(text = "Please put in an integer!")


label1 = Label(screen,text = "Celsius --> Farhenheit",font = (font.Font(size = 30)),fg = "gray",bg = "white")
label1.place(x=110,y=100)
label2 = Label(screen,text = "Enter Temprature in Celsius:",font = (font.Font(size = 10)),fg = "black",bg = "white")
label2.place(x=90,y=250)
value = Entry(screen)
value.place(x=290,y=250)
submit = Button(screen,text = "Enter",font=(font.Font(size = 40)),fg = "white",bg = "green",command = conversion)
submit.place(x=225,y=400)
finalconvert = Label(screen,text = "",font = (font.Font(size = 10)),fg = "black",bg = "white")
finalconvert.place(x=225,y=325)
error = Label(screen,text = "",font = (font.Font(size = 10)),fg = "red",bg = "white")
error.place(x=290,y=275)
screen.mainloop()