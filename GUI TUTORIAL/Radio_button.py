
from tkinter import *
from tkinter import ttk


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

# Radio button

radio = Radiobutton(wind, text="Male", value=1).pack()
radio = Radiobutton(wind, text="Female", value=0).pack()


wind.mainloop()
