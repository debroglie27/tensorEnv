from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Paint App')
root.geometry("700x550")


def change_brush_size(size):

    brush_label.config(text=str(int(float(size))))


my_canvas = Canvas(root, width=520, height=300, bg="white")
my_canvas.grid(row=0, column=0, padx=90, pady=20, columnspan=4)

brush_size_frame = LabelFrame(root, text="Brush Size", padx=10, pady=10)
brush_size_frame.grid(row=1, column=0, pady=10, padx=(30, 0))

brush_var = IntVar()
brush_slider = ttk.Scale(brush_size_frame, orient=VERTICAL, from_=50, to=5, length=100, variable=brush_var, command=change_brush_size)
brush_var.set(25)
brush_slider.pack()

brush_label = Label(brush_size_frame, text=brush_var.get())
brush_label.pack()


root.mainloop()
