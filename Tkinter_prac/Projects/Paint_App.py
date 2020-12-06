from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Paint App')
root.geometry("700x550")


def change_brush_size(size):
    brush_label.config(text=str(int(float(size))))


def change_brush_type():
    pass


my_canvas = Canvas(root, width=550, height=300, bg="white")
my_canvas.pack(pady=20)

# All Frames Frame
all_frame = Frame(root)
all_frame.pack()

# Brush Size Frame
brush_size_frame = LabelFrame(all_frame, text="Brush Size", pady=10)
brush_size_frame.grid(row=0, column=0, pady=10, padx=(0, 60))

brush_slider = ttk.Scale(brush_size_frame, orient=VERTICAL, from_=50, to=5, length=100, value=25, command=change_brush_size)
brush_slider.pack()

brush_label = Label(brush_size_frame, text=brush_slider.get())
brush_label.pack()

# Brush Type Frame
brush_type_frame = LabelFrame(all_frame, text="Brush Type")
brush_type_frame.grid(row=0, column=1, pady=10, padx=(20, 20))

brush_type = StringVar()
brush_type.set("Round")

Brush_Types = [('Round', 'Round'),
               ('Slash', 'Slash'),
               ('Diamond', 'Diamond')]

for text, value in Brush_Types:
    Radiobutton(brush_type_frame, text=text,  variable=brush_type, value=value, command=change_brush_type).pack(anchor=W)


# Change Colors Frame
change_color_frame = LabelFrame(all_frame, text="Change Colors", padx=10, pady=10)
change_color_frame.grid(row=0, column=2, pady=5, padx=(10, 20))

brush_color_button = Button(change_color_frame, text="Brush Color")
brush_color_button.pack(pady=(0, 10))

canvas_color_button = Button(change_color_frame, text="Canvas Color")
canvas_color_button.pack()


# Program Options Frame
program_options_frame = LabelFrame(all_frame, text="Change Colors", padx=10, pady=10)
program_options_frame.grid(row=0, column=3, pady=5, padx=10)

clear_screen_button = Button(program_options_frame, text="Clear Screen")
clear_screen_button.pack(pady=(0, 10))

save_png_button = Button(program_options_frame, text="Save To PNG")
save_png_button.pack()


root.mainloop()
