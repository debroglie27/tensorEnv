from PyPDF2 import PdfFileMerger
from PyPDF2.pdf import PdfFileReader
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class PDFMergerApp:
    def __init__(self, master):
        self.root = master
        self.root.title('PDF Merger App')
        self.root.geometry('430x485+420+70')
        self.root.config(bg="#94d1ff")

        # Importing the Images
        self.plus_img = PhotoImage(file="./Images/add.png")
        self.minus_img = PhotoImage(file="./Images/minus.png")

        # Add some style
        self.style = ttk.Style()
        # Pick a theme
        self.style.theme_use("vista")
        self.style.configure("Treeview",
                             background="white",
                             foreground="black",
                             rowheight=25,
                             fieldbackground="#E3E3E3")

        self.style.map('Treeview',
                       background=[('selected', 'yellow')],
                       foreground=[('selected', 'black')])

        # Create TreeView Frame
        self.tree_frame = Frame(self.root)
        self.tree_frame.pack(pady=20)

        # TreeView ScrollBar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        # Create TreeView
        self.my_tree = ttk.Treeview(self.tree_frame, height=7, yscrollcommand=self.tree_scroll.set)
        self.my_tree.pack()

        # Configure ScrollBar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Define our columns
        self.my_tree['columns'] = ("SL_No", "PDF_Name", "First_Page", "Last_Page")

        # Format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("SL_No", anchor=CENTER, width=45)
        self.my_tree.column("PDF_Name", anchor=CENTER, width=170, minwidth=25)
        self.my_tree.column("First_Page", anchor=CENTER, width=70)
        self.my_tree.column("Last_Page", anchor=CENTER, width=70)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=CENTER)
        self.my_tree.heading("SL_No", text="SL No.", anchor=CENTER)
        self.my_tree.heading("PDF_Name", text="PDF Name", anchor=CENTER)
        self.my_tree.heading("First_Page", text="First Page", anchor=CENTER)
        self.my_tree.heading("Last_Page", text="Last Page", anchor=CENTER)

        # Create Stripped row Tags
        self.my_tree.tag_configure('odd_row', background="white")
        self.my_tree.tag_configure('even_row', background="lightblue")

        # Global Variables
        self.file_count = 0        # Keeps count of number of pdf files inside the treeview
        self.file_paths = {}       # Stores file_location for corresponding filename

        # Create Menu
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)

        # Add ADD File Menu
        self.add_file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Add Files", menu=self.add_file_menu)
        self.add_file_menu.add_command(label="Add one file", command=self.add_file)
        self.add_file_menu.add_command(label="Add many files", command=self.add_files)

        # Add DELETE File Menu
        self.remove_file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Remove Files", menu=self.remove_file_menu)
        self.remove_file_menu.add_command(label="Remove one file", command=self.remove_file)
        self.remove_file_menu.add_command(label="Remove all files", command=self.remove_all_files)

        # Binding Up_Down func with Keys 'w' and 's'
        self.root.bind("<Key>", self.up_down)

        # Frame Color
        frame_color = "#acdafc"

        # Button Frame for Move Up and Move Down
        button_frame1 = Frame(self.root, bg=frame_color)
        button_frame1.pack(pady=(20, 30), fill=X)

        # Move Up and Move Down Buttons Color
        buttons1_color = "#d1f754"

        # Move Up Button and Move Down Button
        move_up_button = Button(button_frame1, text="Move Up", bg=buttons1_color, font=('Helvetica', 10),
                                command=lambda: self.up_down("up"))
        move_up_button.grid(row=0, column=0, padx=(106, 25), ipadx=10)
        move_down_button = Button(button_frame1, text="Move Down", bg=buttons1_color, font=('Helvetica', 10),
                                  command=lambda: self.up_down("down"))
        move_down_button.grid(row=0, column=1, padx=(25, 0), ipadx=2)

        # Button Frame for Inr and Dcr of first and last page
        button_frame2 = Frame(self.root, bg=frame_color)
        button_frame2.pack(fill=X)

        # First and Last Page Label
        first_page_label = Label(button_frame2, text="First Page:", bg=frame_color, font=('Helvetica', 12))
        first_page_label.grid(row=0, column=0, padx=(120, 0), sticky=E)
        last_page_label = Label(button_frame2, text="Last Page:", bg=frame_color, font=('Helvetica', 12))
        last_page_label.grid(row=1, column=0, padx=(120, 0), sticky=E, pady=(10, 0))

        # Color for plus button and minus button
        plus_color = "#54f77f"
        minus_color = "#f7c954"

        # Increment and Decrement First Page
        inr_first_button = Button(button_frame2, image=self.plus_img, bg=plus_color, command=self.inr_first_page)
        inr_first_button.grid(row=0, column=1, padx=(15, 8), ipadx=5, ipady=2)
        dcr_first_button = Button(button_frame2, image=self.minus_img, bg=minus_color, command=self.dcr_first_page)
        dcr_first_button.grid(row=0, column=2, padx=(10, 0), ipadx=5, ipady=2)

        # Increment and Decrement Last Page
        inr_last_button = Button(button_frame2, image=self.plus_img, bg=plus_color, command=self.inr_last_page)
        inr_last_button.grid(row=1, column=1, pady=(10, 0), padx=(15, 8), ipadx=5, ipady=2)
        dcr_last_button = Button(button_frame2, image=self.minus_img, bg=minus_color, command=self.dcr_last_page)
        dcr_last_button.grid(row=1, column=2, pady=(10, 0), padx=(10, 0), ipadx=5, ipady=2)

        # Merge Button
        merge_button = Button(self.root, text="Merge", font=('Helvetica', 12), bg="#d9acfc", command=self.merge)
        merge_button.pack(pady=(33, 0), ipadx=20)

    def add_file(self):
        # File path for the pdf file to be added
        file_path = filedialog.askopenfilename(initialdir="C:/Users/HP/Desktop",
                                               title="Select a file",
                                               filetypes=(("PDF Files", "*.pdf"),))

        # Whether User selected any file
        if file_path:
            # Get total number of pages in the pdf file
            total_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

            filename = []
            # Looping through file_path in opposite direction until '/' is found
            for i in list(file_path)[::-1]:
                if i == '/':
                    break
                filename.append(i)

            # Joining our List and removing .pdf to get File Name
            filename = ''.join(filename[::-1]).replace(".pdf", "")
            self.file_paths[filename] = file_path

            # incrementing file_count
            self.file_count += 1
            # This is done to have strip like pattern inside the TreeView
            if self.file_count % 2 == 1:
                self.my_tree.insert(parent='', index='end', iid=self.file_count, text="", values=(self.file_count, filename, "1", total_pages),
                                    tags=("even_row",))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.file_count, text="", values=(self.file_count, filename, "1", total_pages),
                                    tags=("odd_row",))

    def add_files(self):
        # File paths for pdf files to be added
        file_paths_tuple = filedialog.askopenfilenames(initialdir="C:/Users/HP/Desktop",
                                                       title="Select a file",
                                                       filetypes=(("PDF Files", "*.pdf"),))

        for file_path in file_paths_tuple:
            # Get total number of pages in the pdf file
            total_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

            filename = []
            # Looping through file_path in opposite direction until '/' is found
            for i in list(file_path)[::-1]:
                if i == '/':
                    break
                filename.append(i)

            # Joining our List and removing .pdf to get File Name
            filename = ''.join(filename[::-1]).replace(".pdf", "")
            self.file_paths[filename] = file_path

            # Increment file_count and insert
            self.file_count += 1
            # This is done to have strip like pattern inside the TreeView
            if self.file_count % 2 == 1:
                self.my_tree.insert(parent='', index='end', iid=self.file_count, text="", values=(self.file_count, filename, "1", total_pages),
                                    tags=("even_row",))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.file_count, text="", values=(self.file_count, filename, "1", total_pages),
                                    tags=("odd_row",))

    def remove_file(self):
        # Checking whether anything was selected
        if not self.my_tree.selection():
            return

        # Removing entry from TreeView
        file = self.my_tree.selection()[0]
        self.my_tree.delete(file)

        # Decrementing file_count
        self.file_count -= 1

    def remove_all_files(self):
        # get_children() -> gives all the Iids for records
        for selection in self.my_tree.get_children():
            self.my_tree.delete(selection)

        self.file_count = 0

    # Moving selected records up and down
    def up_down(self, event):
        # If nothing is selected in the treeview
        if not self.my_tree.selection():
            return

        try:
            key = event.char
        except Exception:
            key = ''

        # If Move Up Button is clicked or 'w' key is pressed
        if event == "up" or key == 'w':
            rows = self.my_tree.selection()
            for row in rows:
                self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row) - 1)
        # If Move Down Button is clicked or 's' key is pressed
        elif event == "down" or key == 's':
            rows = self.my_tree.selection()
            for row in reversed(rows):
                self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row) + 1)
        else:
            return

    def inr_first_page(self):
        # Grabbing selected items in treeview
        selections = self.my_tree.selection()

        for selection in selections:
            # Grab the values of the record
            values = self.my_tree.item(selection, "values")

            # Grabbing the first_page and last_page
            first_page = int(values[2])
            last_page = int(values[3])

            # first_page should be lesser than last_page
            if first_page < last_page:
                first_page += 1

                # Saving the updated record
                self.my_tree.item(selection, text="", values=(values[0], values[1], first_page, values[3]))

    def dcr_first_page(self):
        # Grabbing selected items in treeview
        selections = self.my_tree.selection()

        for selection in selections:
            # Grab the values of the record
            values = self.my_tree.item(selection, "values")

            # Get first_page from values
            first_page = int(values[2])

            # first_page should be greater than 1
            if first_page > 1:
                first_page -= 1

                # Saving the updated record
                self.my_tree.item(selection, text="", values=(values[0], values[1], first_page, values[3]))

    def inr_last_page(self):
        # Grabbing selected items in treeview
        selections = self.my_tree.selection()

        for selection in selections:
            # Grab the values of the record
            values = self.my_tree.item(selection, "values")

            # Get last_page from values
            last_page = int(values[3])

            # Get filepath from values
            file_path = self.file_paths[values[1]]
            # Finding total_pages
            total_pages = PdfFileReader(open(file_path, "rb"), strict=False).getNumPages()

            # last_page should always be lesser than max_pages
            if last_page < total_pages:
                last_page += 1

                # Saving the updated record
                self.my_tree.item(selection, text="", values=(values[0], values[1], values[2], last_page))

    def dcr_last_page(self):
        # Grabbing selected items in treeview
        selections = self.my_tree.selection()

        for selection in selections:
            # Grab the values of the record
            values = self.my_tree.item(selection, "values")

            # Get first_page and last_page from values
            first_page = int(values[2])
            last_page = int(values[3])

            # last_page should always be greater than first_page
            if last_page > first_page:
                last_page -= 1

                # Saving the updated record
                self.my_tree.item(selection, text="", values=(values[0], values[1], values[2], last_page))

    def merge(self):
        # If there is no records in treeview then no merging
        if not self.my_tree.get_children():
            return

        # Declare our merger object
        merger = PdfFileMerger()

        for selection in self.my_tree.get_children():
            # Grab the values of the record
            values = self.my_tree.item(selection, "values")

            # Get the filename from values
            filename = values[1]

            # Get the first and last page
            first_page = int(values[2])
            last_page = int(values[3])

            # Get the file_path of the corresponding filename
            file_path = self.file_paths[filename]

            # Appending the pdf files in our merger object
            merger.append(file_path, pages=(first_page-1, last_page))

        # Saving our Merged file in desired location
        merged_file_path = filedialog.asksaveasfile(initialdir="C:/Users/HP/Desktop", title="Save File",
                                                    defaultextension=(("PDF File", "*.pdf"),),
                                                    filetypes=(("PDF File", "*.pdf"),))

        # Whether User specified merged file location
        if merged_file_path:
            # Writing our Merged PDF File
            merger.write(merged_file_path.name)
            merger.close()
        else:
            return

        # Message displaying successful merging
        messagebox.showinfo("Information", "PDF Files Merged Successfully:)", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    PDFMergerApp(root)

    mainloop()
