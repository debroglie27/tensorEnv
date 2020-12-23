from tkinter import *
from tkinter import ttk

root = Tk()
root.title('TreeView')
root.geometry('500x550')

# Add some style
style = ttk.Style()
# Pick a theme
style.theme_use("clam")      # clam, alt, default
style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="#E3E3E3")

style.map('Treeview',
          background=[('selected', 'yellow')],
          foreground=[('selected', 'black')])

# Create TreeView Frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# TreeView ScrollBar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create TreeView
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
my_tree.pack()

# Configure ScrollBar
tree_scroll.config(command=my_tree.yview)


# Define our columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Format our columns
my_tree.column("#0", width=0, stretch=NO)     # we can add minwidth=25
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100, minwidth=25)
my_tree.column("Favorite Pizza", anchor=W, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Add data
data = [
    ["John", 1, "Pepperoni"], ["Mary", 2, "Cheese"],
    ["Tim", 3, "Mushroom"], ["Erin", 4, "Ham"],
    ["Bob", 5, "Onion"], ["Steve", 6, "Peppers"],
    ["Tina", 7, "Cheese"], ["Mark", 8, "Supreme"],
    ["Ruth", 9, "Vegan"], ["John", 1, "Pepperoni"],
    ["Mary", 2, "Cheese"], ["Tim", 3, "Mushroom"],
    ["Erin", 4, "Ham"], ["Bob", 5, "Onion"],
    ["Steve", 6, "Peppers"], ["Tina", 7, "Cheese"],
    ["Mark", 8, "Supreme"], ["Ruth", 9, "Vegan"],
    ["Bob", 5, "Onion"], ["Steve", 6, "Peppers"],
    ["Tina", 7, "Cheese"], ["Mark", 8, "Supreme"],
    ["Ruth", 9, "Vegan"], ["Mark", 8, "Supreme"]
]

# Create Stripped row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))
    count += 1


# Add Children
# my_tree.insert(parent='0', index='end', iid=6, text="Child", values=("Sony", 1.2, "Paneer"))


# Frame for Label and Entry Boxes
add_frame = Frame(root)
add_frame.pack(pady=10)

# Labels
n1 = Label(add_frame, text="Name")
n1.grid(row=0, column=0)

i1 = Label(add_frame, text="ID")
i1.grid(row=0, column=1)

t1 = Label(add_frame, text="Toppings")
t1.grid(row=0, column=2)

# Entry Boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)


def add_record():
    global count
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=("evenrow",))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=("oddrow",))
    count += 1

    # Clear Boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)


def remove_all():
    for rec in my_tree.get_children():
        my_tree.delete(rec)


def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)


def remove_many():
    for rec in my_tree.selection():
        my_tree.delete(rec)


# Buttons
add_record_but = Button(root, text="Add Record", command=add_record)
add_record_but.pack(pady=(20, 5))

remove_all_but = Button(root, text="Remove All", command=remove_all)
remove_all_but.pack(pady=5)

remove_one_but = Button(root, text="Remove One", command=remove_one)
remove_one_but.pack(pady=5)

remove_many_but = Button(root, text="Remove Many", command=remove_many)
remove_many_but.pack(pady=5)


root.mainloop()
