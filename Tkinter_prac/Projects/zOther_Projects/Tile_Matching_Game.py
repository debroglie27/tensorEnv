from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tile Matching Game")
root.geometry('520x460')
root.config(bg="#c9a5f0")

# Create our matches
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# Shuffle our matches
random.shuffle(matches)

# Global variables
total_count = 0
count = 0
answer_list = []
answer_dict = {}


def reset():
    global matches, total_count, count, answer_dict, answer_list

    random.shuffle(matches)
    total_count = 0
    count = 0
    answer_list = []
    answer_dict = {}

    # Button List
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    for button in button_list:
        button.config(text=" ", bg="#42cef5", state=NORMAL)


# Function for clicking buttons
def button_click(b, number):
    global total_count, count, answer_dict, answer_list

    if b["text"] == " " and count < 2:
        b["text"] = str(matches[number])
        # Add number to answer list
        answer_list.append(number)
        # Add button and number to answer dict
        answer_dict[b] = matches[number]
        # Increment the Counter
        count += 1

    # Start to determine correct or not
    if count == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            total_count += 2
            for key in answer_dict:
                key['state'] = DISABLED
                key['bg'] = '#adf542'
        else:
            messagebox.showinfo("Information", "Not Matched!!!")
            for key in answer_dict:
                key['text'] = ' '

        count = 0
        answer_list = []
        answer_dict = {}

    if total_count == 12:
        messagebox.showinfo("Information", "Game Over! YOU WON!!")


# Button Frame
my_frame = LabelFrame(root, bd=5, bg="orange")
my_frame.pack(pady=40)

# Define our buttons
b0 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b0, 0))
b1 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b1, 1))
b2 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b2, 2))
b3 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b3, 3))
b4 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b4, 4))
b5 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b5, 5))
b6 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b6, 6))
b7 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b7, 7))
b8 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b8, 8))
b9 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b9, 9))
b10 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b10, 10))
b11 = Button(my_frame, text=" ", bg="#42cef5", font=("Helvetica", 20), height=3, width=6, relief=GROOVE, command=lambda: button_click(b11, 11))

# Grid our Buttons
# Row 1
b0.grid(row=0, column=0)
b1.grid(row=0, column=1, padx=(2, 0))
b2.grid(row=0, column=2, padx=(2, 0))
b3.grid(row=0, column=3, padx=(2, 0))
# Row 2
b4.grid(row=1, column=0, pady=(2, 0))
b5.grid(row=1, column=1, padx=(2, 0), pady=(2, 0))
b6.grid(row=1, column=2, padx=(2, 0), pady=(2, 0))
b7.grid(row=1, column=3, padx=(2, 0), pady=(2, 0))
# Row 3
b8.grid(row=2, column=0, pady=(2, 0))
b9.grid(row=2, column=1, padx=(2, 0), pady=(2, 0))
b10.grid(row=2, column=2, padx=(2, 0), pady=(2, 0))
b11.grid(row=2, column=3, padx=(2, 0), pady=(2, 0))

# Create a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options DropDown Menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)


root.mainloop()
