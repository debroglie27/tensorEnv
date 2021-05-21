from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser


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
        name = text_file.replace("C:/Users/HP/Pycharm_Projects/tensorEnv/Tkinter_prac/Projects/Text_Editor_App/TextFiles/", "")
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
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="./TextFiles",
                                             title="Save File", filetypes=filetypes)

    if text_file:
        # Set aside the name of the file
        global current_file_name
        current_file_name = text_file

        name = text_file
        # Update Status Bar
        status_bar.config(text=f'{text_file}      ')
        name = name.replace("C:/Users/HP/Pycharm_Projects/tensorEnv/Tkinter_prac/Projects/Text_Editor_App/TextFiles/", "")
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


# Select All Text
def select_all(e):
    my_text.tag_add("sel", "1.0", "end")


# Clear All Text
def clear_all(e):
    my_text.delete(1.0, END)


# Bold Text
def bold_it(e):
    if my_text.get(1.0, END) == "\n" or not my_text.tag_ranges("sel"):
        return

    current_tags = my_text.tag_names("sel.first")

    if "bold_italic" in current_tags:
        my_text.tag_remove("bold_italic", "sel.first", "sel.last")
        my_text.tag_add("italic", "sel.first", "sel.last")
    elif "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
        my_text.tag_add("bold_italic", "sel.first", "sel.last")
    elif "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


# Italics Text
def italics_it(e):
    if my_text.get(1.0, END) == "\n" or not my_text.tag_ranges("sel"):
        return

    current_tags = my_text.tag_names("sel.first")

    if "bold_italic" in current_tags:
        my_text.tag_remove("bold_italic", "sel.first", "sel.last")
        my_text.tag_add("bold", "sel.first", "sel.last")
    elif "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
        my_text.tag_add("bold_italic", "sel.first", "sel.last")
    elif "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


# To change the foreground of our TEXT EDITOR
def fg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)


# To change the background of our TEXT EDITOR
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)


# Night Mode Variable
night_mode_bool = False


# Changing NIGHT Mode ON/OFF
def night_mode():
    global night_mode_bool
    if night_mode_bool:
        main_color = "SystemButtonFace"
        status_color = "#cfcfcf"
        second_color = "white"
        text_color = "black"
        night_mode_bool = False
    else:
        main_color = "#272727"
        status_color = "#272727"
        second_color = "#373737"
        text_color = "yellow"
        night_mode_bool = True

    root.config(bg=main_color)
    status_bar.config(bg=status_color, fg=text_color)
    my_text.config(bg=second_color, fg=text_color)
    file_menu.config(bg=main_color, fg=text_color)
    edit_menu.config(bg=main_color, fg=text_color)
    property_menu.config(bg=main_color, fg=text_color)
    options_menu.config(bg=main_color, fg=text_color)


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
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator="(Ctrl+a)", command=lambda: select_all(True))
edit_menu.add_command(label="Clear", accelerator="(Ctrl+r)", command=lambda: clear_all(True))

# Add Property Menu
property_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Property", menu=property_menu)
property_menu.add_command(label="Bold", accelerator="(Ctrl+b)", command=lambda: bold_it(False))
property_menu.add_command(label="Italics", accelerator="(Ctrl+i)", command=lambda: italics_it(False))
property_menu.add_separator()
property_menu.add_command(label="Foreground Color", command=fg_color)
property_menu.add_command(label="Background Color", command=bg_color)

# Add Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Night Mode ON", command=night_mode)
options_menu.add_command(label="Night Mode OFF", command=night_mode)


# Edit Bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)
root.bind("<Control-Key-a>", select_all)
root.bind("<Control-Key-r>", clear_all)

# Property Bindings
root.bind("<Control-Key-b>", bold_it)
root.bind("<Control-Key-l>", italics_it)

# Bold Font
bold_font = font.Font(my_text, my_text.cget("font"))
bold_font.configure(weight="bold")
# Italics Font
italic_font = font.Font(my_text, my_text.cget("font"))
italic_font.configure(slant="italic")
# Bold Italics Font
bold_italic_font = font.Font(my_text, my_text.cget("font"))
bold_italic_font.configure(weight="bold", slant="italic")

# Creating Tags
my_text.tag_configure("bold", font=bold_font)
my_text.tag_configure("italic", font=italic_font)
my_text.tag_configure("bold_italic", font=bold_italic_font)


root.mainloop()
