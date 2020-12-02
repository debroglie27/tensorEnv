from tkinter import *

root = Tk()
root.title('Root: H, W, X, Y')
root.geometry("300x300+450+150")


def info():
    geometry_label.config(text=root.winfo_geometry())
    height_width_label.config(text="Height: " + str(root.winfo_height()) + "\nWidth: " + str(root.winfo_width()))
    x_y_label.config(text="X: " + str(root.winfo_x()) + "\nY: " + str(root.winfo_y()))


my_button = Button(root, text="Click Me", command=info)
my_button.pack(pady=20)

# For the Overall Geometry
geometry_label = Label(root, text="")
geometry_label.pack(pady=(20, 0))

# For the Height and Width of our App
height_width_label = Label(root, text="")
height_width_label.pack(pady=(10, 0))

# For X and Y of our App
x_y_label = Label(root, text="")
x_y_label.pack(pady=(5, 0))


root.mainloop()
