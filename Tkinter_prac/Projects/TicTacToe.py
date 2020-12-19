from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TicTacToe Game")
# root.geometry("200, 200")


# X starts so True
clicked = True
count = 0
winner = False


# Start the Game again
def reset():
    global clicked, count, winner
    clicked = True
    count = 0
    winner = False

    b1.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b2.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b3.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b4.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b5.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b6.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b7.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b8.config(text=" ", bg="SystemButtonFace", state=ACTIVE)
    b9.config(text=" ", bg="SystemButtonFace", state=ACTIVE)


# Disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Buttons background change
def change_button_background(bool1, bool2, bool3, bool4, bool5, bool6, bool7, bool8):
    if bool1:
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
    elif bool2:
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
    elif bool3:
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
    elif bool4:
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
    elif bool5:
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
    elif bool6:
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
    elif bool7:
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
    elif bool8:
        b7.config(bg="red")
        b5.config(bg="red")
        b3.config(bg="red")


# Check to see if someone won
def check_if_won():
    global winner, count

    for symbol in ['X', 'O']:

        bool1 = b1["text"] == b2["text"] == b3["text"] == symbol
        bool2 = b4["text"] == b5["text"] == b6["text"] == symbol
        bool3 = b7["text"] == b8["text"] == b9["text"] == symbol
        bool4 = b1["text"] == b4["text"] == b7["text"] == symbol
        bool5 = b2["text"] == b5["text"] == b8["text"] == symbol
        bool6 = b3["text"] == b6["text"] == b9["text"] == symbol
        bool7 = b1["text"] == b5["text"] == b9["text"] == symbol
        bool8 = b7["text"] == b5["text"] == b3["text"] == symbol

        if bool1 or bool2 or bool3 or bool4 or bool5 or bool6 or bool7 or bool8:
            winner = True
            change_button_background(bool1, bool2, bool3, bool4, bool5, bool6, bool7, bool8)
            disable_all_buttons()
            messagebox.showinfo("Tic Tac Toe", f"Congratulations!! {symbol} Wins!")
            return

    if count == 9:
        disable_all_buttons()
        messagebox.showinfo("Tic Tac Toe", "It is a Draw!!")


# When Buttons are clicked
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked:
        b["text"] = "X"
        clicked = False
        count += 1
        check_if_won()
    elif b["text"] == " " and not clicked:
        b["text"] = "O"
        clicked = True
        count += 1
        check_if_won()
    else:
        return


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)

options_menu.add_command(label="Reset Game", command=reset)
options_menu.add_command(label="Exit", command=root.quit)


# Build our buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: b_click(b9))


# Grid our buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


root.mainloop()
