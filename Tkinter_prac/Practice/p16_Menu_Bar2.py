from tkinter import *

root = Tk()
root.title('Menu Bars')
root.geometry('400x400')


def new():
    pass


def open_up():
    pass


def disable_new():
    file_menu.entryconfig("New", state=DISABLED)


def enable_new():
    file_menu.entryconfig("New", state=NORMAL)


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Menu items
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
# Add File Menu Items
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open_up)

# Disable_button
disable_button = Button(root, text="Disable New", command=disable_new)
disable_button.pack(pady=20)

enable_button = Button(root, text="Enable New", command=enable_new)
enable_button.pack(pady=10)

root.mainloop()
