from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Full Scrollbar for App')
root.geometry("500x400")

# Create a Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a Scrollbar to the Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the Canvas
my_canvas.config(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create Another Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New Frame to a window  in the Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor=NW)


# Second Frame from now on becomes our root
for i in range(50):
    Button(second_frame, text=f"Button {i+1}").grid(row=i, column=0, padx=10, pady=10)


root.mainloop()
