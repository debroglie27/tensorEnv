from tkinter import *

root = Tk()
root.title('Unicode Characters')
root.geometry("400x400")

# List of Unicode Characters
my_label = Label(root, text='41' + '\u00b0', font=('Helvetica', 32))
my_label.pack()

root.mainloop()
