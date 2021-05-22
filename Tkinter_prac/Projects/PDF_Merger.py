import os
from PyPDF2 import PdfFileMerger
from PyPDF2.pdf import PdfFileReader
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title('PDF Merger')
root.geometry('420x500+420+60')

# Add some style
style = ttk.Style()
# Pick a theme
style.theme_use("clam")
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
file_paths = []


def add_file():
    global file_count
    file_path = filedialog.askopenfilename(initialdir="C:/Users/HP/Desktop",
                                           title="Select a file",
                                           filetypes=(("PDF Files", "*.pdf"),))

    if file_path:
        file_paths.append(file_path)
        num_of_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

        filename = []
        for i in list(file_path)[::-1]:
            if i == '/':
                break
            filename.append(i)

        filename = ''.join(filename[::-1]).replace(".pdf", "")

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
        file_paths.append(file_path)
        num_of_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

        filename = []
        # Looping through file_path in opposite direction until '/' is found
        for i in list(file_path)[::-1]:
            if i == '/':
                break
            filename.append(i)

        # Joining our List and removing .pdf to get File Name
        filename = ''.join(filename[::-1]).replace(".pdf", "")

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


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add ADD Song Menu
add_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Add Files", menu=add_song_menu)
add_song_menu.add_command(label="Add one file", command=add_file)
add_song_menu.add_command(label="Add many files", command=add_files)

# Add DELETE Song Menu
remove_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Remove Files", menu=remove_song_menu)
remove_song_menu.add_command(label="Remove one file", command=remove_file)
remove_song_menu.add_command(label="Remove all files", command=remove_all_files)


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
