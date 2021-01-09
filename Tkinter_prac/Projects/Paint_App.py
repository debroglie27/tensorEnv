from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageGrab


root = Tk()
root.title('Paint App')
root.geometry("700x550+280+50")

canvas_color = 'white'
brush_color = 'red'
brush_size = 25


def paint(event):
    color = brush_color
    size = brush_size // 2

    if brush_type.get() == "Round":
        x1, y1 = event.x - size, event.y - size
        x2, y2 = event.x + size, event.y + size
        my_canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    elif brush_type.get() == "Slash":
        x1, y1 = event.x - size, event.y + size
        x2, y2 = event.x + size, event.y - size
        my_canvas.create_line(x1, y1, x2, y2, fill=color, width=4)
    elif brush_type.get() == "Diamond":
        x1, y1 = event.x, event.y + size
        x2, y2 = event.x + size, event.y
        x3, y3 = event.x, event.y - size
        x4, y4 = event.x - size, event.y
        my_canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=color, outline=color)


# For changing the brush size
def change_brush_size(size):
    global brush_size
    brush_label.config(text=str(int(float(size))))
    brush_size = int(brush_slider.get())


# For changing the brush color
def change_brush_color():
    global brush_color
    temp = colorchooser.askcolor()[1]
    if temp:
        brush_color = temp
        brush_color_label.config(bg=brush_color)


# For changing the background of canvas
def change_canvas_color():
    global canvas_color
    temp = colorchooser.askcolor()[1]
    if temp:
        canvas_color = temp
        my_canvas.configure(bg=canvas_color)
        canvas_color_label.config(bg=canvas_color)


# Clearing the Canvas to Nothing
def clear_canvas():
    my_canvas.delete("all")
    my_canvas.configure(bg="white")


# Converting Canvas drawing to PNG File and storing
def save_image():
    root.geometry("700x550+280+50")
    filename = filedialog.asksaveasfile(defaultextension=".*", initialdir="./PaintApp_Images/", title="Save File",
                                        filetypes=(("PNG File", "*.png"), ("JPG File", "*.jpg")))

    if filename:
        x1 = root.winfo_x() + 242
        y1 = root.winfo_y() + 105
        x2 = x1 + (my_canvas.winfo_width()-4)*1.5
        y2 = y1 + (my_canvas.winfo_height()-4)*1.5
        ImageGrab.grab().crop((x1, y1, x2, y2)).save(filename.name)


my_canvas = Canvas(root, width=580, height=320, bg="white", cursor="circle")
my_canvas.pack(pady=20)

# All Frames Frame
all_frame = Frame(root)
all_frame.pack()

# Brush Size Frame
brush_size_frame = LabelFrame(all_frame, text="Brush Size", pady=10)
brush_size_frame.grid(row=0, column=0, pady=5, padx=(10, 60))

brush_slider = ttk.Scale(brush_size_frame, orient=VERTICAL, from_=50, to=2, length=100, value=25, command=change_brush_size)
brush_slider.pack()

brush_label = Label(brush_size_frame, text=brush_slider.get())
brush_label.pack()

# Brush Type Frame
brush_type_frame = LabelFrame(all_frame, text="Brush Type")
brush_type_frame.grid(row=0, column=1, pady=5, padx=(20, 20))

brush_type = StringVar()
brush_type.set("Round")

Brush_Types = [('Round', 'Round'),
               ('Slash', 'Slash'),
               ('Diamond', 'Diamond')]

for text, value in Brush_Types:
    Radiobutton(brush_type_frame, text=text,  variable=brush_type, value=value).pack(anchor=W)


# Change Colors Frame
change_color_frame = LabelFrame(all_frame, text="Change Colors", padx=8, pady=7)
change_color_frame.grid(row=0, column=2, pady=5, padx=(10, 20))

# Brush Color Button and its Color Label
brush_color_button = Button(change_color_frame, text="Brush Color", command=change_brush_color)
brush_color_button.grid(row=0, column=0, pady=(0, 10), sticky=E)
brush_color_label = Label(change_color_frame, text="", bg=brush_color, borderwidth=2, padx=7, relief=RAISED)
brush_color_label.grid(row=0, column=1, padx=(5, 0), pady=(0, 10))

# Canvas Color Button and its Color Label
canvas_color_button = Button(change_color_frame, text="Canvas Color", command=change_canvas_color)
canvas_color_button.grid(row=1, column=0, sticky=E)
canvas_color_label = Label(change_color_frame, text="", bg=canvas_color, borderwidth=2, padx=7, relief=RAISED)
canvas_color_label.grid(row=1, column=1, padx=(5, 0))


# Program Options Frame
program_options_frame = LabelFrame(all_frame, text="Program Options", padx=10, pady=7)
program_options_frame.grid(row=0, column=3, pady=5, padx=10)

clear_screen_button = Button(program_options_frame, text="Clear Screen", command=clear_canvas)
clear_screen_button.pack(pady=(0, 10))

save_png_button = Button(program_options_frame, text="SAVE Image", command=save_image)
save_png_button.pack()

# Binding the Mouse Button to draw
my_canvas.bind("<B1-Motion>", paint)
my_canvas.bind("<Button-1>", paint)

root.mainloop()
