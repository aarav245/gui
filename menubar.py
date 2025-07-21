from tkinter import *
from tkinter.ttk import *
screen = Tk()
screen.geometry("500x500")
screen.title("userbar project")
#creating menubar
menubar = Menu(screen)
#file tab
File = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "File",menu = File)
File.add_command(label = "New File", command = None)
File.add_command(label = "Open File", command = None)
File.add_separator()
File.add_command(label = "Save", command = None)
File.add_command(label = "Save As", command = None)
File.add_separator()
File.add_command(label = "Close File", command = None)
#edit tab
Edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Edit",menu=Edit)
Edit.add_command(label = "Undo", command = None)
Edit.add_command(label = "Redo", command = None)
Edit.add_separator()
Edit.add_command(label = "Cut", command = None)
Edit.add_command(label = "Copy", command = None)
Edit.add_command(label = "Paste", command = None)
#View tab
View = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "View",menu=View)
View.add_command(label = "Command Palette", command = None)
View.add_command(label = "Open view", command = None)
View.add_separator()
View.add_command(label = "Explorer", command = None)
View.add_command(label = "Search", command = None)
View.add_command(label = "Run", command = None)
screen.config(menu = menubar)

#progress bar
progressbar = Progressbar(screen,orient=HORIZONTAL,length=100,mode="determinate")
def bar():
    import time
    progressbar['value'] = 20
    screen.update_idletasks()
    time.sleep(1)
    progressbar['value'] = 40
    screen.update_idletasks()
    time.sleep(1)
    progressbar['value'] = 65
    screen.update_idletasks()
    time.sleep(1)
    progressbar['value'] = 80
    screen.update_idletasks()
    time.sleep(1)
    progressbar['value'] = 100
    screen.update_idletasks()
    time.sleep(1)
progressbar.pack()
button = Button(screen,text="Start",command = bar)
button.pack()
#spinbox
spinbox = Spinbox(screen,from_=0,to=20)
spinbox.pack()

screen.mainloop()
