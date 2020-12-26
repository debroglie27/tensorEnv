from tkinter import *
from tkinter.tix import *

root = Tk()
root.title('Balloon Text Tool Tips')
root.geometry("400x300")

# Create Balloon
tip = Balloon(root)

# Button
my_button = Button(root, text="Click Me!")
my_button.pack(pady=20)

# Label
my_label = Label(root, text="Some Text")
my_label.pack(pady=20)

# Bind tooltip to Button
tip.bind_widget(my_button, balloonmsg="This is my Awesome Tooltip Button")
# Bind tooltip to Label
tip.bind_widget(my_label, balloonmsg="This is my Awesome Tooltip Label")


root.mainloop()
