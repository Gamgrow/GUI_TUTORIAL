


from tkinter import *
from tkinter import ttk

def func():
    topl.destroy()

def func1():
    wind.destroy()

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
#  to open a tiem two window

topl = Toplevel()
btn = Button(topl,text ="Close window",command=func).pack()
btn = Button(wind,text ="Close window",command=func1).pack()



wind.mainloop()
 