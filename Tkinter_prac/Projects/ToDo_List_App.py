from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("ToDo List App")
root.geometry('500x500+370+60')
root['bg'] = "#90EE90"

# Define our Font
my_font = Font(family="Brush Script MT",
               size=30,
               weight="bold")

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Listbox
my_list = Listbox(my_frame, font=my_font, width=24, height=5, bg="black",
                  fg="yellow", selectbackground="green", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

my_list.insert(END, "Hello")
my_list.insert(END, "GoodBye")

# Create Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add Scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create Entry box to add items
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)


def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_item():
    pass


def uncross_item():
    pass


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

root.mainloop()
