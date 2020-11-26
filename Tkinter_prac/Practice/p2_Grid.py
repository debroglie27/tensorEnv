from tkinter import *

root = Tk()

my_label1 = Label(root, text="Hello World!")
my_label2 = Label(root, text="My name is Arijeet De")

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=4)

# There is nothing in column 1, 2 and 3
# So label2 appears to be side by side of column 0

root.mainloop()
