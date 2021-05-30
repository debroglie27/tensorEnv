from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry("460x300+390+140")
root.config(bg="#ffeac7")


# Generate Random Password
def new_password():
    # Change state to NORMAL
    pw_entry.config(state=NORMAL)
    # Clear our password entry box
    pw_entry.delete(0, END)
    # Change state to readonly
    pw_entry.config(state="readonly")

    # Get password length
    try:
        pw_length = abs(int(my_entry.get()))
    except Exception:
        messagebox.showwarning("Warning", "Please Provide an Integer Value!!!", parent=root)
        return

    # Create variable to hold our password
    my_password = ''

    # Loop through password length
    for x in range(pw_length):
        # Random Ascii character added to my_password
        my_password += chr(randint(33, 126))

    # Change state to NORMAL
    pw_entry.config(state=NORMAL)
    # Output password onto the Entry Box
    pw_entry.insert(0, my_password)
    # Change state to readonly
    pw_entry.config(state="readonly")


# Copy Password to Clipboard
def copy_password():
    # Clear Clipboard
    root.clipboard_clear()

    # Copy to Clipboard
    root.clipboard_append(pw_entry.get())

    # Message informing successful Copy
    messagebox.showinfo("Information", "Successfully Copied!", parent=root)


# Label Frame
my_frame = LabelFrame(root, text="How Many Characters?", bg="#ffd794")
my_frame.pack(pady=(25, 15))

# Entry Box to designate number of characters
my_entry = Entry(my_frame, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create Entry Box for Password that is returned
pw_entry = Entry(root, text='', state="readonly", readonlybackground="#f7ff8c", font=("Helvetica", 24))
pw_entry.pack(pady=15)

# Create Frame for our Buttons
button_frame = Frame(root, bg="#ffeac7")
button_frame.pack(pady=(24, 0))

# Create our Buttons
copy_button = Button(button_frame, text="Copy", bg="#dfff94", font=("Helvetica", 11), command=copy_password)
copy_button.grid(row=0, column=0, padx=(0, 15), ipadx=4)
generate_button = Button(button_frame, text="Generate Password", bg="#dfff94", font=("Helvetica", 11), command=new_password)
generate_button.grid(row=0, column=1, padx=(15, 0), ipadx=8)


root.mainloop()
