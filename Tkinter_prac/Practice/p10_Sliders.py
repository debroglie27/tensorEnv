from tkinter import *

root = Tk()
root.title('Working with Sliders')
root.geometry("200x200")

my_label = Label(root, text="No value")
my_label.pack()


def change1(x):
    my_label.config(text=f"({x},{vertical.get()})")


def change2(y):
    my_label.config(text=f"({horizontal.get()},{y})")


vertical = Scale(root, from_=0, to=400, bg="grey", activebackground="orange", command=change2)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, troughcolor="green", fg="yellow", bg="grey", activebackground="orange", command=change1)
horizontal.pack()

root.mainloop()
