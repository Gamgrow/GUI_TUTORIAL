
from tkinter import *
from tkinter import messagebox

def func():
    if var.get() == "":
         messagebox.showwarning("Warning","Empty")
    else:
        messagebox.showinfo("Success!")
        wind.destroy() # to close window
    
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

# Entry box
var = StringVar()
ent = Entry(wind,textvariable=var)
ent.pack()

btn = Button(wind,text='click me',command=func)
btn.pack()

wind.mainloop()
