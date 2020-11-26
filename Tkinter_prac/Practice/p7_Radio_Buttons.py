from tkinter import *

root = Tk()

# r = IntVar()
# r.set(0)

topping = StringVar()
topping.set("Nothing")

Toppings = [('Pepperoni', 'Pepperoni'),
            ('Cheese', 'Cheese'),
            ('Mushroom', 'Mushroom'),
            ('Onion', 'Onion')]


def clicked():
    my_label.config(text=f"{topping.get()} Selected")


for text, value in Toppings:
    Radiobutton(root, text=text,  variable=topping, value=value, command=clicked).pack(anchor=W)


# Radiobutton(root, text="Option 1", variable=r, value=1, command=clicked).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=clicked).pack()

my_label = Label(root, text="No Option Selected!")
my_label.pack()

root.mainloop()
