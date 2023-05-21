
from tkinter import *

wind = Tk()

# for title
wind.title("Maxy")

# #  for icon
# imj = PhotoImage(file='mic.png')
# wind.iconphoto(False, imj)

# // window size

# wind.maxsize(width=400, height=350)
# wind.minsize(width=400, height=350)
wind.geometry('400x350')

#  for text print

mylabel = Label(wind, text="User Name", bg='red', fg='white',
                width=10, height=5)
mylabel.pack()
# mylabel.grid() for left side
# mylabel.place(x=100,y=100)

wind.mainloop()
