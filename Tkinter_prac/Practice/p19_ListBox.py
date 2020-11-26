from tkinter import *

root = Tk()
root.title('List Box')
root.geometry("400x400")

# Creating a Frame for ListBox and ScrollBar
my_frame = Frame(root)
my_frame.pack()

# Creating a ScrollBar
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

# List Box
# SINGLE, BROWSE, MULTIPLE, EXTENDED
my_listbox = Listbox(my_frame, width=40, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)

# Configuring the Scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y, pady=(15, 0))

my_listbox.pack(pady=(15, 0))

# Adding list of items
my_list = ['One', 'Two', 'Three', 'Four', 'Five', 'One', 'Two', 'Three', 'Four', 'Five',
           'One', 'Two', 'Three', 'Four', 'Five', 'One', 'Two', 'Three', 'Four', 'Five',
           'One', 'Two', 'Three', 'Four', 'Five', 'One', 'Two', 'Three', 'Four', 'Five']

for i in my_list:
    my_listbox.insert(END, i)


def delete():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)


def select():
    # my_label.config(text=my_listbox.get(ANCHOR))

    result = ''
    for item in my_listbox.curselection():
        result = result + my_listbox.get(item) + " "

    my_label.config(text=result)


def delete_all():
    my_listbox.delete(0, END)


my_button1 = Button(root, text="Delete", command=delete)
my_button1.pack(pady=(10, 0))

my_button2 = Button(root, text="Select", command=select)
my_button2.pack(pady=(5, 0))

my_button3 = Button(root, text="Delete All", command=delete_all)
my_button3.pack(pady=(5, 0))

my_label = Label(root, text="")
my_label.pack(pady=15)


root.mainloop()
