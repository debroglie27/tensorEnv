from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('Color Picker')
root.geometry("400x400")


def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color)
    my_label.pack(pady=20)
    Label(root, text="You Picked a Color", font=('Helvetica', 25), bg=my_color).pack()


my_button = Button(root, text="Pick a Color", command=color)
my_button.pack()


root.mainloop()
