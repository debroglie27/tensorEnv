from tkinter import *

root = Tk()
root.title('Label')
root.geometry("300x300+450+150")

my_label = Label(root, text="Hello World!")
my_label.pack()

root.mainloop()
