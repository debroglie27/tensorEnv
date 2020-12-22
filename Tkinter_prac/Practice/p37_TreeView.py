from tkinter import *
from tkinter import ttk

root = Tk()
root.title('TreeView')
root.geometry('500x500')

my_tree = ttk.Treeview(root)

# Define our columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Format our columns
my_tree.column("#0", width=0, stretch=NO)     # we can add minwidth=25
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=120, minwidth=25)
my_tree.column("Favorite Pizza", anchor=W, width=120)

# Create Headings
my_tree.heading("#0", text="", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Add data
my_tree.insert(parent='', index='end', iid=0, text="", values=("John", 1, "Peperoni"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", 2, "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Alice", 3, "Margaret"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Henry", 4, "Ham"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Sam", 5, "Potato"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Tony", 6, "Onion"))

# Add Children
# my_tree.insert(parent='0', index='end', iid=6, text="Child", values=("Sony", 1.2, "Paneer"))

# Pack to the Screen
my_tree.pack(pady=20)


root.mainloop()
