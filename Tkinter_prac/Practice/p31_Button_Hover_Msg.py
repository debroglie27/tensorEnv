from tkinter import *

root = Tk()
root.title('Button Hover Message')
root.geometry('500x400')


def button_enter(e):

    my_button['bg'] = "white"
    status_label.config(text="I am Hovering Over the Button")


def button_leave(e):

    my_button['bg'] = "SystemButtonFace"
    status_label.config(text="")


my_button = Button(root, text="Click Me!", font=('Helvetica', 28))
my_button.pack(pady=50)

status_label = Label(root, text="", bd=1, relief=SUNKEN, anchor=E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)

my_button.bind("<Enter>", button_enter)
my_button.bind("<Leave>", button_leave)

root.mainloop()
