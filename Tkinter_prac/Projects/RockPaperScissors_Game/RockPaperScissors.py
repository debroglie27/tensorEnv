from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("430x360+420+120")
root.config(bg="#add8e6")

image_list = ['rock', 'paper', 'scissor']
selection = ''

# Default Image will be shown known as all.jpg
image1 = ImageTk.PhotoImage(Image.open('./Images/all.jpg'))
image2 = ImageTk.PhotoImage(Image.open('./Images/all.jpg'))


def select(event):
    global image2, selection
    selection = drop.get().lower()
    image2 = ImageTk.PhotoImage(Image.open('./Images/' + selection + '.jpg'))
    img_label2.config(image=image2)


def play():
    if drop.get() == "Select...":
        return

    global image1, selection
    choice = random.choice(image_list)
    image1 = ImageTk.PhotoImage(Image.open('./Images/' + choice + '.jpg'))
    img_label1.config(image=image1)

    if selection == choice:
        my_label.config(text="Its A Tie!!!")
        return

    text = ''
    if selection == "rock":
        if choice == "scissor":
            text = "Rock Smashes Scissor - You Win!!!"
        elif choice == "paper":
            text = "Paper Covers Rock - You Lose!!!"
    elif selection == "paper":
        if choice == "scissor":
            text = "Scissor Cuts Paper - You Lose!!!"
        elif choice == "rock":
            text = "Paper Covers Rock - You Win!!!"
    elif selection == "scissor":
        if choice == "rock":
            text = "Rock Smashes Scissor - You Lose!!!"
        elif choice == "paper":
            text = "Scissor Cuts Paper - You Win!!!"

    my_label.config(text=text)


image_frame = Frame(root, bg="#add8e6")
image_frame.pack(pady=20)

# Computer Label
comp_label = Label(image_frame, text="Computer", font=('Helvetica', 15), bg="#add8e6")
comp_label.grid(row=0, column=0, pady=(0, 5))

# Player Label
player_label = Label(image_frame, text="Player", font=('Helvetica', 15), bg="#add8e6")
player_label.grid(row=0, column=2, pady=(0, 5))

# Label Showing the Image for Computer
img_label1 = Label(image_frame,  image=image1, relief=GROOVE, bd=4)
img_label1.grid(row=1, column=0)

# Label showing VS
vs_label = Label(image_frame, text="VS", font=('Helvetica', 15), bg="#add8e6")
vs_label.grid(row=1, column=1, padx=10)

# Label Showing the Image for Player
img_label2 = Label(image_frame,  image=image2, relief=GROOVE, bd=4)
img_label2.grid(row=1, column=2)

# Drop Down Box for Search Type
drop = ttk.Combobox(root, value=['Select...', 'Rock', 'Paper', 'Scissor'], font=('Helvetica', 14))
drop.current(0)
drop.pack(pady=10)

drop.bind("<<ComboboxSelected>>", select)

# Button to spin
spin_button = Button(root, text="Spin", bg="#90EE90", font=('Helvetica', 12), command=play)
spin_button.pack(pady=(15, 10), ipadx=5)

# Result Label
my_label = Label(root, text="Select and Spin to play!!!", bg="#add8e6", font=('Helvetica', 14))
my_label.pack(pady=(15, 0))

root.mainloop()
