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


my_text = Text(root, width=40, height=10, font=('Helvetica', 16))
my_text.pack(pady=20)

open_button = Button(root, text="Open Text File", command=open_text)
open_button.pack(pady=10)

save_button = Button(root, text="Save", command=save_text)
save_button.pack(pady=10)


root.mainloop()
