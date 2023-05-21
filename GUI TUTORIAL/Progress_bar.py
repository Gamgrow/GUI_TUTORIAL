
# from tkinter import *
# from tkinter import ttk


# wind = Tk()


# # for title
# wind.title("Maxy")


# #  for icon
# imj = PhotoImage(file='mic.png')
# wind.iconphoto(False, imj)

# # // window size

# # wind.maxsize(width=400, height=350)
# # wind.minsize(width=400, height=350)
# wind.geometry('400x350')
# progress = ttk.Progressbar(wind,orient=HORIZONTAL,length=300,
#    mode='determinate')

# def bar():
#     import time

#     progress['value']=20
#     progress.update_idletasks()
#     time.sleep(0.5)


# progress.pack(pady=10)


# btn = Button(wind,text="Start",command=bar).pack(pady=10)


# wind.mainloop()


text = "brighness up dg89%"

brightnessLevel = ""
for i in text:
    if i >= '0' and i <= '9':
        brightnessLevel += i
print(type(int(brightnessLevel)))
