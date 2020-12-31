from tkinter import *

root = Tk()
root.title('Resizing Buttons According to Window')
root.geometry("400x400")

# Config our Rows and Columns
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)

# Create Two Buttons
button_1 = Button(root, text="Button 1", bg="orange")
button_2 = Button(root, text="Button 2")

# Grid them
# button_1.grid(row=0, column=0, sticky=NSEW)
# button_2.grid(row=1, column=0, sticky=NSEW)
button_1.grid(row=0, column=0, sticky=NSEW)
button_2.grid(row=1, column=0, sticky=NSEW)


def resize(e):
    size = int((e.width + 0.3 * e.height)/15)
    button_1.config(font=("Helvetica", size))
    button_2.config(font=("Helvetica", size))


# Configure Bind
root.bind("<Configure>", resize)

root.mainloop()
