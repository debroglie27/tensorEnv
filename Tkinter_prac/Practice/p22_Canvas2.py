from tkinter import *

root = Tk()
root.title('Moving objects inside Canvas')
root.geometry("800x500")

w = 600
h = 400
x = w//2
y = h//2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

my_circle = my_canvas.create_oval(x-5, y-5, x+5, y+5)


def left(event):
    x = -10
    y = 0
    my_canvas.move(my_circle, x, y)


def right(event):
    x = 10
    y = 0
    my_canvas.move(my_circle, x, y)


def up(event):
    x = 0
    y = -10
    my_canvas.move(my_circle, x, y)


def down(event):
    x = 0
    y = 10
    my_canvas.move(my_circle, x, y)


def pressing(event):
    x1 = 0
    y1 = 0
    if event.char == 'a':
        x1 = -10
    if event.char == 'd':
        x1 = 10
    if event.char == 'w':
        y1 = -10
    if event.char == 's':
        y1 = 10

    my_canvas.move(my_circle, x1, y1)


root.bind("<Key>", pressing)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()
