from PyPDF2 import PdfFileMerger
from PyPDF2.pdf import PdfFileReader
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title('PDF Merger')
root.geometry('420x485+420+70')
root.config(bg="#94d1ff")

# Add some style
style = ttk.Style()
# Pick a theme
style.theme_use("vista")
style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="#E3E3E3")

style.map('Treeview',
          background=[('selected', 'yellow')],
          foreground=[('selected', 'black')])

# Create TreeView Frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# TreeView ScrollBar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create TreeView
my_tree = ttk.Treeview(tree_frame, height=7, yscrollcommand=tree_scroll.set)
my_tree.pack()

# Configure ScrollBar
tree_scroll.config(command=my_tree.yview)

# Define our columns
my_tree['columns'] = ("SL_No", "PDF_Name", "First_Page", "Last_Page")

# Format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("SL_No", anchor=CENTER, width=45)
my_tree.column("PDF_Name", anchor=CENTER, width=150, minwidth=25)
my_tree.column("First_Page", anchor=CENTER, width=70)
my_tree.column("Last_Page", anchor=CENTER, width=70)

# Create Headings
my_tree.heading("#0", text="", anchor=CENTER)
my_tree.heading("SL_No", text="SL No.", anchor=CENTER)
my_tree.heading("PDF_Name", text="PDF Name", anchor=CENTER)
my_tree.heading("First_Page", text="First Page", anchor=CENTER)
my_tree.heading("Last_Page", text="Last Page", anchor=CENTER)

# Create Stripped row Tags
my_tree.tag_configure('odd_row', background="white")
my_tree.tag_configure('even_row', background="lightblue")

file_count = 0
file_paths = {}


def add_file():
    global file_count
    file_path = filedialog.askopenfilename(initialdir="C:/Users/HP/Desktop",
                                           title="Select a file",
                                           filetypes=(("PDF Files", "*.pdf"),))

    if file_path:
        num_of_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

        filename = []
        for i in list(file_path)[::-1]:
            if i == '/':
                break
            filename.append(i)

        filename = ''.join(filename[::-1]).replace(".pdf", "")
        file_paths[filename] = file_path

        file_count += 1
        if file_count % 2 == 1:
            my_tree.insert(parent='', index='end', iid=file_count, text="", values=(file_count, filename, "1", num_of_pages),
                           tags=("even_row",))
        else:
            my_tree.insert(parent='', index='end', iid=file_count, text="", values=(file_count, filename, "1", num_of_pages),
                           tags=("odd_row",))


def add_files():
    global file_count, file_paths
    file_paths_tuple = filedialog.askopenfilenames(initialdir="C:/Users/HP/Desktop",
                                                   title="Select a file",
                                                   filetypes=(("PDF Files", "*.pdf"),))

    for file_path in file_paths_tuple:
        num_of_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

        filename = []
        # Looping through file_path in opposite direction until '/' is found
        for i in list(file_path)[::-1]:
            if i == '/':
                break
            filename.append(i)

        # Joining our List and removing .pdf to get File Name
        filename = ''.join(filename[::-1]).replace(".pdf", "")
        file_paths[filename] = file_path

        file_count += 1
        if file_count % 2 == 1:
            my_tree.insert(parent='', index='end', iid=file_count, text="", values=(file_count, filename, "1", num_of_pages),
                           tags=("even_row",))
        else:
            my_tree.insert(parent='', index='end', iid=file_count, text="", values=(file_count, filename, "1", num_of_pages),
                           tags=("odd_row",))


def remove_file():
    global file_count

    # Checking whether anything was selected
    if not my_tree.selection():
        return

    # Removing entry from TreeView
    file = my_tree.selection()[0]
    my_tree.delete(file)

    # Decrementing file_count
    file_count -= 1


def remove_all_files():
    global file_count

    for file in my_tree.get_children():
        my_tree.delete(file)

    file_count = 0


# Moving selected records up and down
def up_down(event):
    if event == "up" or event.char == 'w':
        rows = my_tree.selection()
        for row in rows:
            my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)
    elif event == "down" or event.char == 's':
        rows = my_tree.selection()
        for row in reversed(rows):
            my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)
    else:
        return


def inr_first_page():
    selections = my_tree.selection()

    for selection in selections:
        # Grab the values of the record
        values = my_tree.item(selection, "values")

        first_page = int(values[2])
        last_page = int(values[3])

        if first_page < last_page:
            first_page += 1

            # Saving the updated record
            my_tree.item(selection, text="", values=(values[0], values[1], first_page, values[3]))


def dcr_first_page():
    selections = my_tree.selection()

    for selection in selections:
        # Grab the values of the record
        values = my_tree.item(selection, "values")

        first_page = int(values[2])

        if first_page > 1:
            first_page -= 1

            # Saving the updated record
            my_tree.item(selection, text="", values=(values[0], values[1], first_page, values[3]))


def inr_last_page():
    selections = my_tree.selection()

    for selection in selections:
        # Grab the values of the record
        values = my_tree.item(selection, "values")

        last_page = int(values[3])

        file_path = file_paths[values[1]]
        num_of_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

        if last_page < num_of_pages:
            last_page += 1

            # Saving the updated record
            my_tree.item(selection, text="", values=(values[0], values[1], values[2], last_page))


def dcr_last_page():
    selections = my_tree.selection()

    for selection in selections:
        # Grab the values of the record
        values = my_tree.item(selection, "values")

        first_page = int(values[2])
        last_page = int(values[3])

        if last_page > first_page:
            last_page -= 1

            # Saving the updated record
            my_tree.item(selection, text="", values=(values[0], values[1], values[2], last_page))


def merge():
    pass


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add ADD File Menu
add_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Add Files", menu=add_song_menu)
add_song_menu.add_command(label="Add one file", command=add_file)
add_song_menu.add_command(label="Add many files", command=add_files)

# Add DELETE File Menu
remove_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Remove Files", menu=remove_song_menu)
remove_song_menu.add_command(label="Remove one file", command=remove_file)
remove_song_menu.add_command(label="Remove all files", command=remove_all_files)

# Binding Up_Down func with Keys w and s
root.bind("<Key>", up_down)

# Button Frame for Move Up and Move Down
button_frame1 = Frame(root, bg="#acdafc")
button_frame1.pack(pady=(20, 30), fill=X)

# Move Up Button and Move Down Button
move_up_button = Button(button_frame1, text="Move Up", bg="#ffe5ad", font=('Helvetica', 10), command=lambda: up_down("up"))
move_up_button.grid(row=0, column=0, padx=(103, 25), ipadx=10)
move_down_button = Button(button_frame1, text="Move Down", bg="#ffe5ad", font=('Helvetica', 10), command=lambda: up_down("down"))
move_down_button.grid(row=0, column=1, padx=(25, 0), ipadx=2)

# Button Frame for Inr and Dcr of first and last page
button_frame2 = Frame(root, bg="#acdafc")
button_frame2.pack(fill=X)

# First and Last Page Label
first_page_label = Label(button_frame2, text="First Page:", bg="#acdafc", font=('Helvetica', 12))
first_page_label.grid(row=0, column=0, padx=(119, 0), sticky=E)
last_page_label = Label(button_frame2, text="Last Page:", bg="#acdafc", font=('Helvetica', 12))
last_page_label.grid(row=1, column=0, padx=(119, 0), sticky=E, pady=(10, 0))

# Increment and Decrement First Page
inr_first_button = Button(button_frame2, text="+", relief=GROOVE, bg="#9afca5", font=('Helvetica', 10), command=inr_first_page)
inr_first_button.grid(row=0, column=1, padx=(15, 8), ipadx=5, ipady=2)
dcr_first_button = Button(button_frame2, text="-", relief=GROOVE, bg="#9afca5", font=('Helvetica', 12), command=dcr_first_page)
dcr_first_button.grid(row=0, column=2, padx=(10, 0), ipadx=5)

# Increment and Decrement Last Page
inr_last_button = Button(button_frame2, text="+", relief=GROOVE, bg="#fcb19a", font=('Helvetica', 10), command=inr_last_page)
inr_last_button.grid(row=1, column=1, pady=(10, 0), padx=(15, 8), ipadx=5, ipady=2)
dcr_last_button = Button(button_frame2, text="-", relief=GROOVE, bg="#fcb19a", font=('Helvetica', 12), command=dcr_last_page)
dcr_last_button.grid(row=1, column=2, pady=(10, 0), padx=(10, 0), ipadx=5)

# Merge Button
merge_button = Button(root, text="Merge", font=('Helvetica', 12), bg="#d9acfc", command=merge)
merge_button.pack(pady=(30, 0), ipadx=20)

# source = r"C:\Users\M K DE\Desktop\Semester V\MPMC\Practical\Assignment_pdfs"
#
# merger = PdfFileMerger()
#
# for item in os.listdir(source):
#     if item.endswith(".pdf"):
#         result = source + r'/' + str(item)
#         merger.append(result)
#
# merger.write("118CS0163.pdf")
# merger.close()

mainloop()
