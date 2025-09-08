from tkinter import *
from tkinter.ttk import *
screen = Tk()
screen.title("multiply")
style = Style()
#generating the multiplication table
def generate():
    screenresult = ""
    radioval = value.get()
    for i in range(1,radioval+1):
        boxval = number.get()
        result = i * boxval
        screenresult+=str(boxval)+"x"+str(i)+"="+str(result)+"\n"
    label3.configure(text = screenresult)
style.configure("TButton",font = ("Arial",20))
style.configure("TLabel",font = ("Arial",20))
style.configure("TCombobox",font = ("Arial",20))
#style.configure("TResult",font = ("Arial",15))
label1 = Label(screen,text = "Mathematical Table",style = "TLabel")
label2 = Label(screen,text = "Number and range:",style = "")
label1.grid(row = 0,column = 0,columnspan=3,pady = 20)
label2.grid(row = 1,column = 0,padx = 30)
label3 = Label(screen,font = ("Arial",15),anchor = "center")
label3.grid(column = 0,row = 4)
#combobox
number = IntVar()
combo = Combobox(screen,text = number, style = "TCombobox")
combo['values'] = tuple(range(101))
combo.grid(row = 1,column=1)
button1 = Button(screen,text = "enter",style = "MyButton.TButton",command = generate)
button1.grid(row = 2,column = 1)
value = IntVar()
radio1 = Radiobutton(screen,text = "10",variable=value,value = 10)
radio2 = Radiobutton(screen,text = "20",variable=value,value = 20)
radio3 = Radiobutton(screen,text = "30",variable=value,value = 30)
value.set(10)
radio1.grid(column=2,row=1,padx = 30,pady=10)
radio2.grid(column=2,row=2,padx=30,pady=10)
radio3.grid(column=2,row=3,padx=30,pady=10)
screen.mainloop()
