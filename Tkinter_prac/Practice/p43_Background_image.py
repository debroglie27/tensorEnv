from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Background Image')
root.geometry("800x450")

# Define Background Image
bg = ImageTk.PhotoImage(Image.open('../Projects/ImageViewer_Images/background.jpg'))
bg1 = Image.open("../Projects/ImageViewer_Images/background.jpg")
resized_bg = ''
new_bg = ''

# Create a Canvas
my_canvas = Canvas(root, width=800, height=450, bd=0, highlightthickness=0)
my_canvas.pack(fill=BOTH, expand=1)

# Set Image in Canvas
my_canvas.create_image(0, 0, image=bg, anchor=NW)

# Add a Label
my_canvas.create_text(410, 220, text="Welcome!", font=("Helvetica", 50), fill="white")

# Buttons
button_1 = Button(root, text="Start")
button_2 = Button(root, text="Reset")
button_3 = Button(root, text="Exit")

button_1_window = my_canvas.create_window(10, 10, anchor=NW, window=button_1)
button_2_window = my_canvas.create_window(50, 10, anchor=NW, window=button_2)
button_3_window = my_canvas.create_window(130, 10, anchor=NW, window=button_3)


def resizer(e):
    global new_bg, resized_bg
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resized_bg)

    my_canvas.create_image(0, 0, image=new_bg, anchor=NW)
    my_canvas.create_text(410, 220, text="Welcome!", font=("Helvetica", 50), fill="white")


# Binding Configure
root.bind("<Configure>", resizer)

root.mainloop()
