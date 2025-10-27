from tkinter import *
from tkinter.colorchooser import askcolor

#variables
pensize = 5
pencolor = "black"
Xpos = None
Ypos = None
color = pencolor
eraser = False
activebutton = None
penthickness = pensize

#functions
def penuse():
    global activebutton, eraser
    activate(pen)
    eraser = False
def brushuse():
    global activebutton, eraser
    activate(brush)
    eraser = False
def eraseruse():
    global activebutton, eraser
    activate(eraserbutton)
    eraser = True
def coloruse():
    global activebutton,eraser,color
    eraser = False
    picked = askcolor(color=color)[1]
    if picked:
        color = picked
def activate(button):
    global activebutton
    if activebutton:
        activebutton.config(relief = RAISED)
    button.config(relief = SUNKEN)
    activebutton = button
def paint(event):
    global Xpos,Ypos,color
    size = slider.get()
    if activebutton == brush:
        penthickness = size*2
    else:
        penthickness = size
    paint_color = 'white' if eraser else color
    if Xpos and Ypos:
        canvas.create_line(Xpos,Ypos,event.x,event.y,width = penthickness,fill = paint_color,capstyle=ROUND,smooth = TRUE,splinesteps=20)
    Xpos,Ypos = event.x,event.y
def reset(event):
    global Xpos,Ypos
    Xpos,Ypos = None,None


#design
screen = Tk()
screen.title("Canvas")
pen = Button(screen,text = "Pen",command = penuse)
pen.grid(row=0,column = 0)
brush = Button(screen,text = "brush",command = brushuse)
brush.grid(row=0,column=1)
colorbutton = Button(screen,text = "color",command = coloruse)
colorbutton.grid(row=0,column=2)
eraserbutton = Button(screen,text = "eraser",command = eraseruse)
eraserbutton.grid(row=0,column=3)
slider = Scale(screen,from_=1,to=10,orient = "horizontal")
slider.grid(row=0,column=4)
canvas = Canvas(screen,bg = "white",width = 500,height = 500)
canvas.grid(row=1,columnspan=5)
canvas.bind('<B1-Motion>',paint)
canvas.bind('<ButtonRelease-1>',reset)
activate(pen)
screen.mainloop()