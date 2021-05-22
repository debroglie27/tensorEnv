from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title("ToDo List App")
root.geometry('500x500+370+60')
root['bg'] = "#90EE90"

# Define our Fonts
my_font = Font(family="Brush Script MT",
               size=30,
               weight="bold")

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=(20, 10))

# Create Listbox
my_list = Listbox(my_frame, font=my_font, width=24, height=5, bg="black",
                  fg="yellow", selectbackground="green", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

# Create Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add Scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)


def placeholder():
    if my_entry.get() == "Add Item":
        # Deleting the Placeholder and making foreground "black"
        my_entry.delete(0, END)
        my_entry.config(fg="black")


# Create Entry box to add items
my_entry = Entry(root, fg="#BFBFBF", font=('Helvetica', 24), validate="focusin", validatecommand=placeholder)
my_entry.pack(pady=20)
my_entry.insert(0, "Add Item")


def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    if my_entry.get() == '' or my_entry.get() == 'Add Item':
        return

    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_item():
    if my_list.curselection() == ():
        return

    # Cross Off Item
    my_list.itemconfig(my_list.curselection(), fg="#4d4b01")

    # Clear Selection Bar
    my_list.selection_clear(0, END)


def uncross_item():
    if my_list.curselection() == ():
        return

    # Uncross Off Item
    my_list.itemconfig(my_list.curselection(), fg="yellow")

    # Clear Selection Bar
    my_list.selection_clear(0, END)


def open_list():
    filename = filedialog.askopenfilename(initialdir="C:/Users/HP/Pycharm_Projects/tensorEnv/Tkinter_prac/Projects/ToDo_List_App/ToDo_dat_files", title="Save File",
                                          filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))

    if filename:
        # Delete Currently opened list
        my_list.delete(0, END)

        # open the File
        input_file = open(filename, 'rb')

        # Load the data from the file
        stuff = pickle.load(input_file)

        # output stuff on ListBox
        for item in stuff:
            my_list.insert(END, item)


def save_list():
    filename = filedialog.asksaveasfilename(initialdir="C:/Users/HP/Pycharm_Projects/tensorEnv/Tkinter_prac/Projects/ToDo_List_App/ToDo_dat_files", title="Save File",
                                            filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))

    if filename:
        if filename.endswith(".dat"):
            pass
        else:
            filename = f'{filename}.dat'

        # delete the crossed off items
        delete_crossed()

        # grab all the stuff from list
        stuff = my_list.get(0, END)

        # Open the File
        output_file = open(filename, 'wb')

        # Add Stuff to file
        pickle.dump(stuff, output_file)


def clear_list():
    my_list.delete(0, END)


def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#4d4b01":
            my_list.delete(count)
        else:
            count += 1


# Button Frame
button_frame = Frame(root, bg="#90EE90")
button_frame.pack(pady=20)

add_button = Button(button_frame, text="Add Item", bg='#fdebd0', font=('Helvetica', 11), command=add_item)
add_button.grid(row=0, column=0, pady=(0, 20), ipadx=10)

delete_button = Button(button_frame, text="Delete Item", bg='#fdebd0', font=('Helvetica', 11), command=delete_item)
delete_button.grid(row=1, column=0, ipadx=2)

cross_button = Button(button_frame, text="Cross Item", bg='#fdebd0', font=('Helvetica', 11), command=cross_item)
cross_button.grid(row=0, column=1, padx=(50, 0), pady=(0, 20), ipadx=10)

uncross_button = Button(button_frame, text="Uncross Item", bg='#fdebd0', font=('Helvetica', 11), command=uncross_item)
uncross_button.grid(row=1, column=1, padx=(50, 0), ipadx=2)

# Create a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create File DropDown Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
# Add File Menu commands
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Clear List", command=clear_list)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create Edit DropDown Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
# Add Edit Menu commands
edit_menu.add_command(label="Add Item", command=add_item)
edit_menu.add_command(label="Cross Item", command=cross_item)
edit_menu.add_command(label="Uncross Item", command=uncross_item)
edit_menu.add_separator()
edit_menu.add_command(label="Delete Item", command=delete_item)
edit_menu.add_command(label="Delete Crossed", command=delete_crossed)

root.mainloop()
