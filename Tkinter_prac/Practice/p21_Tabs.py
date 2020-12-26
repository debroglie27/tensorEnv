from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Creating Tabs')
root.geometry("400x400")


def hide():
    my_notebook.hide(1)


def show():
    my_notebook.add(my_frame2, text="Red Tab")


def select():
    my_notebook.select(1)


my_notebook = ttk.Notebook(root, width=400, height=374)
my_notebook.pack()

my_frame1 = Frame(my_notebook, bg="blue")
my_frame2 = Frame(my_notebook, bg="red")

my_frame1.pack(fill=BOTH, expand=1)
my_frame2.pack(fill=BOTH, expand=1)

my_notebook.add(my_frame1, text="Blue Tab")
my_notebook.add(my_frame2, text="Red Tab")

# Hide a tab
my_button2 = Button(my_frame1, text="Hide Tab2", command=hide)
my_button2.pack(pady=10)

# Show a tab
my_button2 = Button(my_frame1, text="Show Tab2", command=show)
my_button2.pack(pady=10)

# Navigate to a tab
my_button3 = Button(my_frame1, text="Navigate to Tab2", command=select)
my_button3.pack(pady=10)

root.mainloop()
