from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Working with Keyboard Binding OptionMenu')
root.geometry("400x400")

options = ['Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
           'Saturday',
           'Sunday']

my_label = Label(root, text="")
my_label.pack()


def display1(event):
    if var.get() == "Monday":
        my_label.config(text="Jug suna suna lage")
    elif var.get() == "Friday":
        my_label.config(text="Aaj ki party meri taraf se")
    else:
        my_label.config(text=var.get())


def display2(event):
    my_label.config(text=my_combo.get())


var = StringVar()
var.set(options[0])

drop = OptionMenu(root, var, *options, command=display1)
drop.pack(pady=20)

my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.bind("<<ComboboxSelected>>", display2)
my_combo.pack()

root.mainloop()
