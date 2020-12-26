from tkinter import *

root = Tk()
root.title('Text Box')
root.geometry("500x450")


def clear():
    my_text.delete(1.0, END)


def get_text():
    my_label.config(text=my_text.get(1.0, END))


my_text = Text(root, width=40, height=10, font=('Helvetica', 16))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0, pady=10, padx=10)

get_text_button = Button(button_frame, text="Get Text", command=get_text)
get_text_button.grid(row=0, column=1, pady=10)

my_label = Label(root, text='')
my_label.pack(pady=20)


root.mainloop()
