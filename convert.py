from tkinter import *
screen = Tk()
screen.title("Weight Converter")
#function for weight conversion
def weight():
    convert = float(userinput.get())
    gr = convert * 1000
    lb = convert * 2.20462
    oz = convert * 35.274
    gramsconvert.delete("1.0",END)
    poundsconvert.delete("1.0",END)
    ouncesconvert.delete("1.0",END)
    gramsconvert.insert(END,gr)
    poundsconvert.insert(END,lb)
    ouncesconvert.insert(END,oz)
enter = Label(screen,text="Enter Weight in Kg",bg = "white",font=("Times New Roman",10))
enter.grid(row=0,column=0)
userinput = Entry(screen)
userinput.grid(row=0,column = 1)
button1 = Button(screen,text="Enter",bg = "white",font=("Times New Roman",15),command = weight)
button1.grid(row=0,column =2)
Grams = Label(screen,text="Grams",bg = "White",font=("Times New Roman",10))
Grams.grid(row=1,column = 0)
Pounds = Label(screen,text="Pounds",bg = "White",font=("Times New Roman",10))
Pounds.grid(row=1,column = 1)
Ounces = Label(screen,text="Ounces",bg = "White",font=("Times New Roman",10))
Ounces.grid(row=1,column = 2)
#Creating text widgets
gramsconvert = Text(screen,height = 1,width = 20)
gramsconvert.grid(row = 2,column = 0)
poundsconvert = Text(screen,height = 1,width = 20)
poundsconvert.grid(row = 2,column = 1)
ouncesconvert = Text(screen,height = 1,width = 20)
ouncesconvert.grid(row = 2,column = 2)
screen.mainloop()