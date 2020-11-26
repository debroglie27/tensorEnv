from tkinter import *

root = Tk()


def my_click():
    my_label = Label(root, text="I got clicked!")
    my_label.pack()


my_button = Button(root, text="Click Me!", fg="blue", bg="yellow", command=my_click)

# We can change the size of buttons like this:
# my_button = Button(root, text="Click Me!", padx=50, pady=10)

my_button.pack()

root.mainloop()
