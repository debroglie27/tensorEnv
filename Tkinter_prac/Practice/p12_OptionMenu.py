from tkinter import *

root = Tk()
root.title('Working with OptionMenu')
root.geometry("200x200")

options = ['Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
           'Saturday']


def clicked():
    my_label.config(text=var.get())


var = StringVar()
var.set("Monday")

drop = OptionMenu(root, var, *options)
drop.pack()

Button(root, text="Show Selection", command=clicked).pack()


my_label = Label(root, text=options[0])
my_label.pack()

root.mainloop()
