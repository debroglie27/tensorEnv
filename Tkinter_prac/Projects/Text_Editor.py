from tkinter import *
from tkinter import filedialog
# from tkinter import font
from tkinter import messagebox


root = Tk()
root.title('New File')
root.geometry("900x531")
root.clipboard_clear()

filetypes = (("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"))
current_file_name = False
selected = False


# Checking if file is saved or not before doing something stupid
def check_file_saving():
    if my_text.get('1.0', END) == '\n':
        return False
    if not current_file_name:
        return True

    # Open the Actual File
    text_file = open(current_file_name, 'r')
    stuff = text_file.read()
    text_file.close()
    stuff += "\n"

    if stuff == my_text.get('1.0', END):
        return False
    else:
        return True


# Create a new file
def new_file():
    if check_file_saving():
        messagebox.showwarning("Warning", "File Not Saved!!!")
        return

    # Reset the name of the file
    global current_file_name
    current_file_name = False

    my_text.delete('1.0', END)
    status_bar.config(text="New File      ")
    root.title("New File")


# Open a new file
def open_file():
    # Check if current file is saved or not
    if check_file_saving():
        messagebox.showwarning("Warning", "File Not Saved!!!")
        return

    # Grab file
    text_file = filedialog.askopenfilename(initialdir="./TextFiles/", title="Open File", filetypes=filetypes)

    if text_file:
        # Set aside the name of the file
        global current_file_name
        current_file_name = text_file

        # Update Status Bar
        status_bar.config(text=f'{text_file}      ')
        name = text_file.replace("C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/TextFiles/", "")
        root.title(name)

        # Open the Actual File
        text_file = open(text_file, 'r')
        stuff = text_file.read()

        # Delete the Actual Content inside Text Box
        my_text.delete('1.0', END)

        # Inserting the Stuff in the opened file
        my_text.insert(END, stuff)

        # Close the Text File
        text_file.close()


# Save File
def save_file():
    global current_file_name
    if current_file_name:
        # Save the File
        text_file = open(current_file_name, 'w')
        text_file.write(my_text.get(1.0, END))

        # Close the File
        text_file.close()

        # Show Pop Up
        messagebox.showinfo("Info", "File Saved Successfully")
    else:
        save_as_file()


# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="./TextFiles", title="Save File", filetypes=filetypes)

    if text_file:
        # Set aside the name of the file
        global current_file_name
        current_file_name = text_file

        name = text_file
        # Update Status Bar
        status_bar.config(text=f'{text_file}      ')
        name = name.replace("C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/TextFiles/", "")
        root.title(name)

        # Save the File
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))

        # Close the File
        text_file.close()

        # Show Pop Up
        messagebox.showinfo("Info", "File Saved Successfully")


# Cut Text
def cut_text(e):
    global selected
    if my_text.tag_ranges(SEL):
        # Check to see if we used Keyboard shortcut
        if e:
            selected = root.clipboard_get()
        else:
            # Grab Selected Text from Text Box
            selected = my_text.selection_get()
            # Delete Selected text from Text Box
            my_text.delete("sel.first", "sel.last")
            # Clear the clipboard and then append
            root.clipboard_clear()
            root.clipboard_append(selected)


# Copy Text
def copy_text(e):
    global selected
    if my_text.tag_ranges(SEL):
        # Check to see if we used Keyboard shortcut
        if e:
            selected = root.clipboard_get()
        else:
            # Grab Selected Text from Text Box
            selected = my_text.selection_get()
            # Clear the clipboard and then append
            root.clipboard_clear()
            root.clipboard_append(selected)


# Paste Text
def paste_text(e):
    global selected
    # Check to see if we used Keyboard shortcut
    if e:
        pass
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=1, fill=BOTH, expand=1)

# Add Status Bar
status_bar = Label(my_frame, text='New File      ', anchor=E, bg="#cfcfcf")
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Vertical Scrollbar
text_scroll_y = Scrollbar(my_frame)
text_scroll_y.pack(side=RIGHT, fill=Y)

# Create Horizontal Scrollbar
text_scroll_x = Scrollbar(my_frame, orient=HORIZONTAL)
text_scroll_x.pack(side=BOTTOM, fill=X)

# Create Text Box
my_text = Text(my_frame, width=73, height=20, font=("Helvetica", 16), selectbackground="yellow", undo=True, wrap="none",
               selectforeground="black", yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set)
my_text.pack(fill=BOTH, expand=1)

# Configure Scrollbars
text_scroll_y.config(command=my_text.yview)
text_scroll_x.config(command=my_text.xview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", accelerator="(Ctrl+x)", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy", accelerator="(Ctrl+c)", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste", accelerator="(Ctrl+v)", command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Undo", accelerator="(Ctrl+z)", command=my_text.edit_undo)
edit_menu.add_command(label="Redo", accelerator="(Ctrl+y)", command=my_text.edit_redo)

# Edit Bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

root.mainloop()
