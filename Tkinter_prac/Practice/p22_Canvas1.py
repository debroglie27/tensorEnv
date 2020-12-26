from tkinter import *

root = Tk()
root.title('Creating Canvas')
root.geometry("500x500")

my_canvas = Canvas(root, width=300, height=200, bg="white")
my_canvas.pack(pady=20)

# Create Rectangle
# my_canvas.create_rectangle(x1, y1, x2, y2, fill="color")
# x1, y1 -> Bottom Left
# x2, y2 -> Top Right
my_canvas.create_rectangle(50, 150, 250, 50, fill="pink")

# Create Oval
# It is making an oval inside the rectangle defined by the coordinates
my_canvas.create_oval(50, 150, 250, 50, fill="cyan")

# Create Line
# my_canvas.create_line(x1, y1, x2, y2, fill="color")
my_canvas.create_line(0, 100, 300, 100, fill="red")
my_canvas.create_line(150, 0, 150, 200, fill="red")


root.mainloop()
