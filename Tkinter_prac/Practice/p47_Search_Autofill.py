from tkinter import *

root = Tk()
root.title('Autofill Search')
root.geometry("450x300")


# Update the ListBox
def update(data):
    # Clear the ListBox
    my_list.delete(0, END)

    # Add data to ListBox
    for item in data:
        my_list.insert(END, item)


# Update Entry Box with ListBox clicked
def fill_out(e):
    # Delete whatever is in Entry Box
    my_entry.delete(0, END)

    # Add clicked list item to entry box
    my_entry.insert(END, my_list.get(ANCHOR))


# Create func to check entry with listbox
def check(e):
    # Grab what was typed
    typed = my_entry.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)

    # Update our ListBox with selected items
    update(data)


# Create a Label
my_label = Label(root, text="Start Typing...", font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)

# Create an Entry Box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a ListBox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushrooms",
            "Cheese", "Onions", "Ham", "Taco"]

# Add toppings to our list
update(toppings)

# Create a Binding on the ListBox onclick
my_list.bind("<<ListboxSelect>>", fill_out)

# Create a binding on the Entry Box
my_entry.bind("<KeyRelease>", check)

root.mainloop()
