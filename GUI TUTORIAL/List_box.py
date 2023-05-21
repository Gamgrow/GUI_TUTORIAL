
from tkinter import *
from tkinter import ttk


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

# list box
lst = Listbox(wind, width=40)
lst.insert(
    END, "Apple  rfghj fghj rdtfyghj \n rdtfgyhj rddtfgyhj \ntdtrfgyhj trdtfygu htfyguhi rdtfyguh", index='\n')
lst.insert(END, "Mango")
lst.insert(END, "Banana")
lst.pack()


wind.mainloop()
