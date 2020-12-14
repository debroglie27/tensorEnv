from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Text Box')
root.geometry("500x500")


def open_text():
    text_file_loc = filedialog.askopenfilename(initialdir="../Projects/TextFiles/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    text_file = open(text_file_loc, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()


def save_text():
    text_file = open("../Projects/TextFiles/sample.txt", 'w')
    text_file.write(my_text.get(1.0, END))
    text_file.close()
    my_text.delete(1.0, END)


my_image = PhotoImage()


def add_image():
    # Add Image
    global my_image
    my_image = PhotoImage(file="../Projects/ImageViewer_Images/car.png")

    position = my_text.index(INSERT)
    my_text.image_create(position, image=my_image)


def select():
    selected = my_text.selection_get()
    my_label.config(text=selected)


def bolder():
    if my_text.get(1.0, END) == "\n" or not my_text.tag_ranges("sel"):
        return

    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold", font=bold_font)
    current_tags = my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


def italics_it():
    if my_text.get(1.0, END) == "\n" or not my_text.tag_ranges("sel"):
        return

    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    my_text.tag_configure("italic", font=italics_font)
    current_tags = my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=38, height=10, font=('Helvetica', 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure the text _scroll
text_scroll.config(command=my_text.yview)

# Button Frame
button_frame = Frame(root)
button_frame.pack(pady=5)

# Our Buttons
open_button = Button(button_frame, text="Open Text File", command=open_text)
open_button.grid(row=0, column=0, pady=5, sticky=W, padx=(0, 30))

save_button = Button(button_frame, text="Save", command=save_text)
save_button.grid(row=0, column=1, pady=5, sticky=W)

image_button = Button(button_frame, text="Add Image", command=add_image)
image_button.grid(row=1, column=0, pady=5, sticky=W)

select_button = Button(button_frame, text="Select Text", command=select)
select_button.grid(row=1, column=1, pady=5, sticky=W)

bold_button = Button(button_frame, text="Bold", command=bolder)
bold_button.grid(row=2, column=0, pady=5, sticky=W)

italics_button = Button(button_frame, text="Italics", command=italics_it)
italics_button.grid(row=2, column=1, pady=5, sticky=W)

undo_button = Button(button_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=3, column=0, pady=5, sticky=W)

redo_button = Button(button_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=3, column=1, pady=5, sticky=W)

# Label
my_label = Label(root, text="")
my_label.pack(pady=5)

root.mainloop()
