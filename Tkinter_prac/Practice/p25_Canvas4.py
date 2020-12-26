from tkinter import *

root = Tk()
root.title('Moving images inside Canvas')
root.geometry("800x600")

w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# Add Image to canvas
img1 = PhotoImage(file="../Projects/ImageViewer_Images/car.png")
my_image1 = my_canvas.create_image(100, 50, image=img1)

img2 = PhotoImage(file="../Projects/ImageViewer_Images/bike.png")
my_image2 = my_canvas.create_image(400, 200, image=img2)

# Label to show Coordinates
my_label = Label(root, text="")
my_label.pack(pady=20)


class MouseMover:
    def __init__(self):
        self.item = 0
        self.previous = (0, 0)

    def select(self, event):
        widget = event.widget                       # Get handle to canvas
        # Convert screen coordinates to canvas coordinates if viewports are used for Canvas
        # xc = widget.canvasx(event.x)
        # yc = widget.canvasy(event.y)
        self.item = widget.find_closest(event.x, event.y)[0]        # ID for closest
        self.previous = (event.x, event.y)

    def drag(self, event):
        widget = event.widget
        # xc = widget.canvasx(event.x)
        # yc = widget.canvasy(event.y)
        widget.move(self.item, event.x-self.previous[0], event.y-self.previous[1])
        self.previous = (event.x, event.y)
        my_label.config(text=str((event.x, event.y)))


mm = MouseMover()

my_canvas.bind('<Button-1>', mm.select)
my_canvas.bind('<B1-Motion>', mm.drag)


root.mainloop()
