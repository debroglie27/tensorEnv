from tkinter import *
from tkinter import messagebox

root = Tk()

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.askquestion("This is a popUp", "Hello World!")
    # Label(root, text=response).pack()

    if response == 'yes':
        Label(root, text="You Pressed Yes!").pack()
    else:
        Label(root, text="You pressed No!").pack()


Button(root, text="PopUp", command=popup).pack()

root.mainloop()
