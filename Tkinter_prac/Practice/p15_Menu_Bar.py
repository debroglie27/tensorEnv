from tkinter import *

root = Tk()
root.title('Menu Bars')
root.geometry('400x400')


def our_command():
    pass


def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    Label(file_new_frame, text="You Clicked File >> New Menu!").pack()


def edit_new():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    Label(edit_cut_frame, text="You Clicked Edit >> Cut Menu!").pack()
    Button(edit_cut_frame, text="Fake!").pack(pady=10)

    print(edit_cut_frame.winfo_children())


def hide_all_frames():
    # deleting every widget from all frames
    for widget in file_new_frame.winfo_children():
        widget.destroy()

    for widget in edit_cut_frame.winfo_children():
        widget.destroy()

    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


my_menu = Menu(root)
root.config(menu=my_menu)

# File Menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit Menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_new)
edit_menu.add_command(label="Copy", command=our_command)

# Option Menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

# File New Frame and Edit Cut Frame
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")

root.mainloop()
