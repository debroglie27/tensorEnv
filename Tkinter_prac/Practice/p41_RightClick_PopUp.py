from tkinter import *

root = Tk()
root.title('Balloon Text Tool Tips')
root.geometry("400x300")


def hello():
    my_label.config(text="Hello World!")


def goodbye():
    my_label.config(text="Goodbye World!")


def my_popup(event):
    my_menu.tk_popup(event.x_root, event.y_root)


my_label = Label(root, text="", font=("Helvetica", 20))
my_label.pack(pady=20)


# Create Menu
my_menu = Menu(root, tearoff=False)
my_menu.add_command(label="Say Hello", command=hello)
my_menu.add_command(label="Say Goodbye", command=goodbye)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)

root.bind("<Button-3>", my_popup)

root.mainloop()
