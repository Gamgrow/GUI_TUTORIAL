
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

cnv = Canvas(wind)
cord = 10,50,270,210
cnv.create_arc(cord,start= 0, extent= 180 ,fill ="red")
cnv.create_line(cord)
cnv.pack()

wind.mainloop()
 