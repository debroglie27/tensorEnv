from tkinter import *

root = Tk()
root.title('Working with Check Button')
root.geometry("200x200")

# var = IntVar()
var2 = StringVar()
var2.set("Off")


def click():
    my_label.config(text=var2.get())


# Checkbutton(root, text="Click it", variable=var, command=click).pack()
c = Checkbutton(root, text="Click it", variable=var2, onvalue="On", offvalue="Off", command=click)
# c.deselect()
c.pack()

my_label = Label(root, text=var2.get())
my_label.pack()

root.mainloop()
