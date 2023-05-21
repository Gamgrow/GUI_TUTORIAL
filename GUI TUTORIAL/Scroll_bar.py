
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

# scroll bar
scroll  = Scrollbar(wind)
scroll.pack(side=RIGHT,fill=Y)

mylist = Listbox(wind,yscrollcommand=Y)
for i in range(1000):
    mylist.insert(END,"hello"+str(i))
mylist.pack(side=LEFT,fill=Y)
scroll.config(command=mylist.yview)


wind.mainloop()
 