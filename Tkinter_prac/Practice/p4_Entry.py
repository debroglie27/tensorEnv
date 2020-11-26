from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Here: ")

# e = Entry(root, width=50, fg="white", bg="black")


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


my_button = Button(root, text="Enter Your Name", fg="blue", bg="yellow", command=my_click)
my_button.pack()

root.mainloop()
