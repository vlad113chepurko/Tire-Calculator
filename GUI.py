from tkinter import *

frame = Tk()
frame.geometry("600x600")

_label_title = Label(text='Tire', font='Arial 13px')
_label_title.grid(column=0, row=5)

_label_width = Label(text='Enter width', font='Arial 13px')
_label_width.grid(column=0, row=0)

frame.mainloop()