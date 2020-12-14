from tkinter import *
from tkinter import filedialog
# from tkinter import font

root = Tk()
root.title('New File')
root.geometry("900x536")

filetypes = (("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"))


# Create a new file
def new_file():
    my_text.delete('1.0', END)
    status_bar.config(text="New File      ")
    root.title("New File")


# Open a new file
def open_file():
    my_text.delete('1.0', END)

    # Grab file
    text_file = filedialog.askopenfilename(initialdir="./TextFiles/", title="Open File", filetypes=filetypes)

    if text_file:
        # Update Status Bar
        status_bar.config(text=f'{text_file}      ')
        name = text_file.replace("C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/TextFiles/", "")
        root.title(name)

        # Open the Actual File
        text_file = open(text_file, 'r')
        stuff = text_file.read()

        # Inserting the Stuff in the opened file
        my_text.insert(END, stuff)

        # Close the Text File
        text_file.close()


# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="./TextFiles", title="Save File", filetypes=filetypes)

    if text_file:
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


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=3)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=73, height=21, font=("Helvetica", 16), selectbackground="yellow",
               selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar
status_bar = Label(root, text='New File      ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


root.mainloop()
