
from tkinter import *
from tkinter import ttk


wind = Tk()


# for title
wind.title("Maxy")


#  for icon
imj = PhotoImage(file='mic.png')
wind.iconphoto(False, imj)

# // window size

wind.maxsize(width=590, height=410)
wind.minsize(width=590, height=410)


# how to add photo
# file = PhotoImage(file="anuska.png",)

# label = Label(wind, image=file).place(height=400, width=456)

wind.mainloop()
