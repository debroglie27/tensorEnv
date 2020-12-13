from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Text Box')
root.geometry("500x450")


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


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=38, height=10, font=('Helvetica', 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set)
my_text.pack()

# Configure the text _scroll
text_scroll.config(command=my_text.yview)

# Our Buttons
open_button = Button(root, text="Open Text File", command=open_text)
open_button.pack(pady=10)

save_button = Button(root, text="Save", command=save_text)
save_button.pack(pady=10)

image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=5)

root.mainloop()
