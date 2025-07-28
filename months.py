from tkinter import *
import calendar

screen = Tk()
screen.geometry("400x300")
screen.title("homepage")
#Function for showing calendar
def showcal():
    screen2 = Tk()
    screen2.geometry("550x700")
    screen2.title("calendar")
    yearstore = int(enteryear.get())
    yearfetch = calendar.calendar(yearstore)
    yearshow = Label(screen2,text=yearfetch,bg="gray",font = ("Times New Roman",12))
    yearshow.grid(row=5,column =1,padx=20,pady=20)
    screen2.mainloop()
cal = Label(screen,text="Calendar",bg = "white",font = ("Times New Roman",50))
cal.place(x=75,y=40)
year = Label(screen,text="Year",bg = "light green",font = ("Times New Roman",15))
year.place(x=175,y=130)
enteryear = Entry(screen)
enteryear.place(x=135,y=160)
showcalendar = Button(screen,text="Show calendar",bg="cyan",fg="purple",font = ("Times New Roman",15),command = showcal)
showcalendar.place(x=130,y=185)
exit = Button(screen,text="Exit",bg="red",fg="black",font = ("Times New Roman",15),command=screen.destroy)
exit.place(x=175,y=250)
screen.mainloop()