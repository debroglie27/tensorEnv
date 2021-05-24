from tkinter import *

root = Tk()
root.title('On Off Switch')
root.geometry("500x300")

# Keep track of button state
is_on = True

# Create a Label
my_label = Label(root, text="The Switch is On!", fg="green", font=("Helvetica", 32))
my_label.pack(pady=20)


def switch():
    global is_on

    if is_on:
        switch_button.config(image=off)
        my_label.config(text="The Switch is Off!", fg="grey")
        is_on = False
    else:
        switch_button.config(image=on)
        my_label.config(text="The Switch is On!", fg="green")
        is_on = True


# Define our Images
on = PhotoImage(file="../Projects/ImageViewer_App/ImageViewer_Images/on.png")
off = PhotoImage(file="../Projects/ImageViewer_App/ImageViewer_Images/off.png")

switch_button = Button(root, image=on, bd=0, command=switch)
switch_button.pack(pady=50)


root.mainloop()
