from tkinter import *

root = Tk()
root.title("Event Binding")
root.geometry("400x400")


def clicker(event):
    my_label = Label(root, text="You Clicked a Button! " + str(event.x) + " " + str(event.y))
    # my_label = Label(root, text="You Clicked a Button! " + event.keysym)
    # my_label = Label(root, text="You Clicked a Button! " + event.char)
    my_label.pack()


my_Button = Button(root, text="Click Me")
my_Button.bind("<Button-3>", clicker)          # Only Right Click works
# my_Button.bind("<Enter>", clicker)
# my_Button.bind("<Leave>", clicker)
# my_Button.bind("<Return>", clicker)
# my_Button.bind("<FocusIn>", clicker)
# my_Button.bind("<Key>", clicker)
my_Button.pack(pady=20)

root.mainloop()
