
from tkinter import *
from tkinter import ttk

def func():
    print(checkbtn1.get())
    print(checkbtn2.get())


wind = Tk()

# for title
wind.title("Maxy")


#  for icon
imj = PhotoImage(file='mic.png')
wind.iconphoto(False, imj)

# // window size

# wind.maxsize(width=400, height=350)
# wind.minsize(width=400, height=350)
wind.geometry('400x350')

# check button
checkbtn1 = IntVar()
checkbtn2 = IntVar()
select = Checkbutton(wind,text="male", variable =checkbtn1,command=func )
select.pack()
select = Checkbutton(wind,text="male", variable =checkbtn2,command=func )
select.pack()




wind.mainloop()
