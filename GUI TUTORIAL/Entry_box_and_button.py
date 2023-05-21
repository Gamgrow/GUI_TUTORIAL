from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
# from notepad import file_menu
# from notepad import edit_menu
# from notepad import format_menu
# from notepad import help_menu
# from notepad import config

root = Tk()

# root.title(f"Text Editor-Untiltled Made by {config.name}")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

btn2 = Button(wind, text="search", command=doooo,activebackground="#108cff",bg="#108cff",border=2).place(x=690,y=610)

menubar = Menu(root)

# # file_menu.main(root, text, menubar)
# edit_menu.main(root, text, menubar)
# format_menu.main(root, text, menubar)
# help_menu.main(root, text, menubar)
root.mainloop()
