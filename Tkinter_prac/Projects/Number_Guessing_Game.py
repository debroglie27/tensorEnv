from tkinter import *
from random import randint

root = Tk()
root.title('Number Guessing Game')
root.geometry("480x450+400+70")

# Global variable
num = 0
num_guesses = 0
num_label = Label()
guess_box = Entry()
guess_button = Button()
rand_button = Button()
i0, i1, i2, i3, i4, i5, i6, i7 = Label(), Label(), Label(), Label(), Label(), Label(), Label(), Label()
c1, c2, c3, c4, c5, c6, c7 = Label(), Label(), Label(), Label(), Label(), Label(), Label()


def my_guess():
    # Whether the value provided is a number
    if guess_box.get().isdigit():
        # Whether the number provided is between 1 and 100
        if 1 <= int(guess_box.get()) <= 100:
            # reset the Num Label
            num_label.config(text="Pick A Number\nBetween 1 to 100!")

            # Increment Number of guesses
            global num_guesses
            num_guesses += 1

            # Finding Difference between actual and guessed number
            diff = abs(int(guess_box.get()) - num)

            if diff == 0:
                num_label.config(text=f"Correct!!!\nNumber Of Guesses: {num_guesses}")
                guess_button.config(state=DISABLED)
                num_label.config(bg="red")
                root['bg'] = "red"
            elif diff <= 3:
                num_label.config(bg="red")
                root['bg'] = "red"
            elif diff <= 8:
                num_label.config(bg="#fc4a4a")
                root['bg'] = "#fc4a4a"
            elif diff <= 15:
                num_label.config(bg="#fc8686")
                root['bg'] = "#fc8686"
            elif diff <= 25:
                num_label.config(bg="#ff91fd")
                root['bg'] = "#ff91fd"
            elif diff <= 40:
                num_label.config(bg="#8686fc")
                root['bg'] = "#8686fc"
            elif diff <= 60:
                num_label.config(bg="#4a4afc")
                root['bg'] = "#4a4afc"
            else:
                num_label.config(bg="#0000ff")
                root['bg'] = "#0000ff"

            # Clearing the Guess Box
            guess_box.delete(0, END)

        else:
            guess_box.delete(0, END)
            num_label.config(text="Hey! Please Select A Number\nBetween 1 and 100!!!")

    else:
        guess_box.delete(0, END)
        num_label.config(text="Hey!\nThat's Not A Number!!!")


def new_random():
    # Clear Guess Box
    guess_box.delete(0, END)

    # reset the Num Label
    num_label.config(text="Pick A Number\nBetween 1 to 100!")

    # Reset the Background colors
    num_label.config(bg="SystemButtonFace")
    root['bg'] = "SystemButtonFace"

    # State of Submit button back to Normal
    guess_button.config(state=NORMAL)

    global num, num_guesses
    # Selecting a new random Number
    num = randint(1, 100)
    # Reset the Number of guesses
    num_guesses = 0


def game():
    root.geometry("480x450+400+70")

    global num_label, guess_box, guess_button, rand_button, \
        i0, i1, i2, i3, i4, i5, i6, i7, c1, c2, c3, c4, c5, c6, c7
    num_label.pack_forget()
    guess_box.pack_forget()
    guess_button.pack_forget()
    rand_button.pack_forget()

    instr_labels = [i0, i1, i2, i3, i4, i5, i6, i7, c1, c2, c3, c4, c5, c6, c7]
    for widget in instr_labels:
        widget.grid_forget()

    num_label = Label(root, text="Pick A Number\nBetween 1 to 100!", font=("Brush Script MT", 32))
    num_label.pack(pady=20)

    guess_box = Entry(root, font=("Helvetica", 80), width=3)
    guess_box.pack(pady=(15, 20))

    guess_button = Button(root, text="Submit", bg="#90EE90", font=("Helvetica", 11), command=my_guess)
    guess_button.pack(pady=20, ipadx=25)

    rand_button = Button(root, text="New Number", bg="yellow", font=("Helvetica", 11), command=new_random)
    rand_button.pack(pady=10, ipadx=5)


def instruction():
    root.geometry("480x330+400+100")

    global num_label, guess_box, guess_button, rand_button, \
        i0, i1, i2, i3, i4, i5, i6, i7, c1, c2, c3, c4, c5, c6, c7
    num_label.pack_forget()
    guess_box.pack_forget()
    guess_button.pack_forget()
    rand_button.pack_forget()

    instr_labels = [i0, i1, i2, i3, i4, i5, i6, i7, c1, c2, c3, c4, c5, c6, c7]
    for widget in instr_labels:
        widget.grid_forget()

    i0 = Label(root, text="Instructions", font=("Brush Script MT", 32))
    i0.grid(row=0, column=0, columnspan=2, pady=(10, 5))

    i1 = Label(root, text="Diff b/w Guess and Number - (60, 100] :", font=("Helvetica", 11))
    i1.grid(row=1, column=0, sticky=E, pady=(5, 0), padx=25)
    i2 = Label(root, text="Diff b/w Guess and Number - (40, 60] :", font=("Helvetica", 11))
    i2.grid(row=2, column=0, sticky=E, pady=(10, 0), padx=25)
    i3 = Label(root, text="Diff b/w Guess and Number - (25, 40] :", font=("Helvetica", 11))
    i3.grid(row=3, column=0, sticky=E, pady=(10, 0), padx=25)
    i4 = Label(root, text="Diff b/w Guess and Number - (15, 25] :", font=("Helvetica", 11))
    i4.grid(row=4, column=0, sticky=E, pady=(10, 0), padx=25)
    i5 = Label(root, text="Diff b/w Guess and Number - (8, 15] :", font=("Helvetica", 11))
    i5.grid(row=5, column=0, sticky=E, pady=(10, 0), padx=25)
    i6 = Label(root, text="Diff b/w Guess and Number - (3, 8] :", font=("Helvetica", 11))
    i6.grid(row=6, column=0, sticky=E, pady=(10, 0), padx=25)
    i7 = Label(root, text="Diff b/w Guess and Number - [0, 3] :", font=("Helvetica", 11))
    i7.grid(row=7, column=0, sticky=E, pady=(10, 0), padx=25)

    c1 = Label(root, text="", bg="#0000ff", width=17)
    c1.grid(row=1, column=1, padx=6, pady=(5, 0))
    c2 = Label(root, text="", bg="#4a4afc", width=17)
    c2.grid(row=2, column=1, padx=6, pady=(10, 0))
    c3 = Label(root, text="", bg="#8686fc", width=17)
    c3.grid(row=3, column=1, padx=6, pady=(10, 0))
    c4 = Label(root, text="", bg="#ff91fd", width=17)
    c4.grid(row=4, column=1, padx=6, pady=(10, 0))
    c5 = Label(root, text="", bg="#fc8686", width=17)
    c5.grid(row=5, column=1, padx=6, pady=(10, 0))
    c6 = Label(root, text="", bg="#fc4a4a", width=17)
    c6.grid(row=6, column=1, padx=6, pady=(10, 0))
    c7 = Label(root, text="", bg="red", width=17)
    c7.grid(row=7, column=1, padx=6, pady=(10, 0))


# Create our Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Add file menu commands
file_menu.add_command(label="Game", command=game)
file_menu.add_command(label="Instruction", command=instruction)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

game()
new_random()

root.mainloop()
