from tkinter import *

root = Tk()
root.title('Spin Boxes')
root.geometry("500x300")


def grab():
    my_label.config(text=my_spin.get())


def reset():
    var.set(0)


var = IntVar(root)
var.set(0)

# names = ("John", "Tim", "Mary", "Tina")

# my_spin = Spinbox(root, from_=0, to=10, font=("Helvetica", 20), increment=2)
# my_spin = Spinbox(root, values=names, font=("Helvetica", 20))
my_spin = Spinbox(root, from_=0, to=100, font=("Helvetica", 20), textvariable=var)
my_spin.pack(pady=20)

my_button = Button(root, text="Submit", command=grab)
my_button.pack(pady=20)

reset_button = Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

my_label = Label(root, text="")
my_label.pack(pady=10)

root.mainloop()
