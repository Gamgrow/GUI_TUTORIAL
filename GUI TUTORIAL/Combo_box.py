
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

# // combo box
com = ttk.Combobox(wind, width=27)
com["values"] = ("jan", "feb", "march")
com["state"] = "readonly"  # we cant change
com.place(x=29, y=12)

wind.mainloop()
