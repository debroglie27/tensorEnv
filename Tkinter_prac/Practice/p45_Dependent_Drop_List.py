from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Dependent Drop Down and List Boxes')
root.geometry("400x400")

# Creating a list of sizes
sizes = ['Small', 'Medium', 'Large']

# Create a List of colors
small_colors = ["Red", "Green", "Blue", "Black"]
medium_colors = ["Red", "Green"]
large_colors = ["Blue", "Black"]


def pick_color(event):
    if my_combo.get() == "Small":
        color_combo.config(value=small_colors)
        color_combo.current(0)
    elif my_combo.get() == "Medium":
        color_combo.config(value=medium_colors)
        color_combo.current(0)
    elif my_combo.get() == "Large":
        color_combo.config(value=large_colors)
        color_combo.current(0)


# Create a Drop Down Box for Sizes
my_combo = ttk.Combobox(root, value=sizes)
my_combo.current(0)
my_combo.pack(pady=20)

# Bind Combo box
my_combo.bind("<<ComboboxSelected>>", pick_color)

# Create a Drop Down Box for Colors
color_combo = ttk.Combobox(root, value=small_colors)
color_combo.current(0)
color_combo.pack(pady=20)

# Frame for list Box
my_frame = Frame(root)
my_frame.pack(pady=20)

# List Box for sizes
my_list1 = Listbox(my_frame)
my_list1.grid(row=0, column=0)
# list Box for Colors
my_list2 = Listbox(my_frame)
my_list2.grid(row=0, column=1, padx=(20, 0))

# Add items to list1
for item in sizes:
    my_list1.insert(END, item)


def list_color(event):
    my_list2.delete(0, END)
    if my_list1.get(ANCHOR) == "Small":
        for i in small_colors:
            my_list2.insert(END, i)
    elif my_list1.get(ANCHOR) == "Medium":
        for i in medium_colors:
            my_list2.insert(END, i)
    elif my_list1.get(ANCHOR) == "Large":
        for i in large_colors:
            my_list2.insert(END, i)


# Bind the List1
my_list1.bind("<<ListboxSelect>>", list_color)


root.mainloop()
