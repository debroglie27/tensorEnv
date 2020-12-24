import os
import smtplib
from pathlib import Path
from dotenv import load_dotenv
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

# conn = sqlite3.connect('address_book.db')
# c = conn.cursor()
# query = "Insert Into users(Username, Password) values(?, ?)"
# c.execute(query, ('Admin', '1234'))
# conn.commit()
# conn.close()

# Username: Admin
# Password: 1234
# Secret Key: 12345

# User1: Mrinal
# Password: 1967

# User2: Nibedita
# Password: 1969

root = Tk()


class WinLogin:

    def __init__(self, master, title, geo):
        self.root = master
        self.root.title(title)
        self.root.geometry(geo)

        # Bullet Symbol
        self.bullet_symbol = "\u2022"

        # Username Label and Entry
        self.username_label = Label(self.root, text="Username:", font=('Helvetica', 15))
        self.username_label.grid(row=0, column=0, padx=10, pady=(30, 0))
        self.username_entry = Entry(self.root, font=('Helvetica', 15))
        self.username_entry.grid(row=0, column=1, padx=10, pady=(30, 0), columnspan=3)

        # Password Label and Entry
        self.password_label = Label(self.root, text="Password:", font=('Helvetica', 15))
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

        # Login Button
        self.login_button = Button(self.root, text="Login", bg="#90EE90", font=('Helvetica', 11), command=self.login_check)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20, padx=(40, 0), ipadx=10)

        # SignUp Button
        self.signup_button = Button(self.root, text="SignUp", bg="#add8e6", font=('Helvetica', 11), command=lambda: self.signup(WinSignup, "SignUp Window"))
        self.signup_button.grid(row=2, column=2, columnspan=2, pady=20, padx=(0, 45), ipadx=10)

        # Forgot Password Label
        self.forgot_pass_label = Button(root, text="Forgot Password?", fg="blue", relief=FLAT, command=lambda: self.signup(WinForgotPass, "Forgot Password Window"))
        self.forgot_pass_label.grid(row=3, column=1, padx=(0, 30), columnspan=2)

    def login_check(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn = sqlite3.connect('address_book.db')
            c = conn.cursor()
            query = 'Select Password from users where Username=?'
            c.execute(query, (username,))

            record = c.fetchone()[0]

            conn.commit()
            conn.close()

            if record == password:
                self.new_window(WinHome, "Home Window")
            else:
                messagebox.showerror("Error", "Incorrect!!! Username or Password", parent=self.root)

        except Exception:
            messagebox.showerror("Error", "Please Try Again!!!", parent=self.root)

    def forgot_pass_window(self, _class, t):
        level = Tk()
        title = t
        _class(level, title)
        self.root.destroy()

    def signup(self, _class, t):
        level = Tk()
        title = t
        _class(level, title)
        self.root.destroy()

    def new_window(self, _class, t):
        level = Tk()
        title = t
        _class(level, title)
        self.root.destroy()


# Forgot Password Window
class WinForgotPass:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("360x200+450+150")

        # Instruction Label
        self.instruction_label = Label(self.root, text="Provide Your Email-id\nwhere password will be shared.", font=('Helvetica', 13), fg="green")
        self.instruction_label.grid(row=0, column=0, padx=65, pady=(20, 0), columnspan=4)

        # Email Label and Entry
        self.email_label = Label(self.root, text="Email:", font=('Helvetica', 15))
        self.email_label.grid(row=1, column=0, padx=10, pady=20)
        self.email_entry = Entry(self.root, font=('Helvetica', 15))
        self.email_entry.grid(row=1, column=1, padx=(0, 30), pady=20, columnspan=3)

        # Back Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=2, column=0, columnspan=2, pady=10, padx=(40, 0), ipadx=10)

        # Send Button
        self.send_button = Button(self.root, text="Send", bg="#90EE90", font=('Helvetica', 11), command=self.email_check)
        self.send_button.grid(row=2, column=2, columnspan=2, pady=10, padx=(0, 60), ipadx=10)

        # Loading the Environment Variables from .env file
        env_path = Path('../../../openCV_venv/.env')
        load_dotenv(dotenv_path=env_path)

        self.EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        self.EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    def email_check(self):
        messagebox.showinfo("Information", "It may take some time\nPlease Wait!!!", parent=self.root)
        email = self.email_entry.get()

        try:
            conn = sqlite3.connect('address_book.db')
            c = conn.cursor()
            query = 'Select Password from users where email_id=?'
            c.execute(query, (email,))

            user_password = c.fetchone()

            conn.commit()
            conn.close()

            if user_password is None:
                messagebox.showerror("Error", "Incorrect!!! Email-id", parent=self.root)
            else:
                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)

                        subject = 'Forgot Password: Address Database'
                        body = f'Dear User\n\nPlease find your Password of your Address Database Account\n\nPassword: {user_password[0]}'

                        msg = f'Subject: {subject}\n\n{body}'

                        smtp.sendmail(self.EMAIL_ADDRESS, email, msg)

                        messagebox.showinfo("Information", "Mail has been sent Successfully:)", parent=self.root)
                        self.close_window()

                except Exception:
                    messagebox.showerror("Error", "Please Try Again!!!", parent=self.root)

        except Exception:
            messagebox.showerror("Error", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        global root
        root = Tk()
        WinLogin(root, "Login Window", "377x230+450+150")
        self.root.destroy()


# Window for SignUp
class WinSignup:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry('380x280+450+150')

        # Bullet Symbol
        self.bullet_symbol = "\u2022"

        # Username Label and Entry
        self.username_label = Label(self.root, text="Username:", font=('Helvetica', 15))
        self.username_label.grid(row=0, column=0, padx=10, pady=(30, 0), sticky=E)
        self.username_entry = Entry(self.root, font=('Helvetica', 15))
        self.username_entry.grid(row=0, column=1, padx=10, pady=(30, 0), columnspan=3)

        # Password Label and Entry
        self.password_label = Label(self.root, text="Password:", font=('Helvetica', 15))
        self.password_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky=E)
        self.password_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.password_entry.grid(row=1, column=1, padx=10, pady=(10, 0), columnspan=3)

        # Email Label and Entry
        self.email_label = Label(self.root, text="Email:", font=('Helvetica', 15))
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky=E)
        self.email_entry = Entry(self.root, font=('Helvetica', 15))
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

        # Admin Secret Key
        self.secret_label = Label(self.root, text="Secret Key:", font=('Helvetica', 15))
        self.secret_label.grid(row=3, column=0, padx=10, pady=(20, 10), sticky=E)
        self.secret_entry = Entry(self.root, font=('Helvetica', 15))
        self.secret_entry.grid(row=3, column=1, padx=10, pady=(20, 10), columnspan=3)

        # Back Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=20, padx=(30, 0))

        # Submit Button
        self.submit_button = Button(self.root, text="Submit", bg="#90EE90", font=('Helvetica', 11), command=self.login_check)
        self.submit_button.grid(row=4, column=2, columnspan=2, pady=20, padx=(0, 60))

    def login_check(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email_id = self.email_entry.get()
        secret_key = self.secret_entry.get()

        if not secret_key == '12345':
            messagebox.showerror("Error", "Secret Key Incorrect!!!", parent=self.root)
            return
        else:
            try:
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.email_entry.delete(0, END)
                self.secret_entry.delete(0, END)

                conn = sqlite3.connect('address_book.db')
                c = conn.cursor()
                query = "Insert Into users(Username, Password, email_id) values(?, ?, ?)"
                c.execute(query, (username, password, email_id))

                conn.commit()
                conn.close()

                messagebox.showinfo("Information", "Account Successfully Added!!!", parent=self.root)

                self.close_window()

            except Exception:
                messagebox.showinfo("Information", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        global root
        root = Tk()
        WinLogin(root, "Login Window", "377x230+450+150")
        self.root.destroy()


class WinHome:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("377x360+450+150")
        self.root['bg'] = "#90EE90"

        self.head_label = Label(self.root, text="Welcome to Database", bg='#e67e22', font=('Helvetica', 20))
        self.head_label.grid(row=0, column=0, pady=20, ipadx=50)

        self.but_insert = Button(self.root, text="Insert", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinInsert, "Insert Window"))
        self.but_insert.grid(row=1, column=0, pady=(20, 0), ipadx=60)
        self.but_show = Button(self.root, text="Search", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinSearch, "Search Window"))
        self.but_show.grid(row=2, column=0, pady=(15, 0), ipadx=54)
        self.but_update = Button(self.root, text="Update", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinUpdate, "Update Window"))
        self.but_update.grid(row=3, column=0, pady=(15, 0), ipadx=54)
        self.but_delete = Button(self.root, text="Delete", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinDelete, "Delete Window"))
        self.but_delete.grid(row=4, column=0, pady=(15, 0), ipadx=57)

    def new_window(self, _class, t):
        level = Tk()
        title = t
        _class(level, title)
        self.root.destroy()


class WinInsert:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("360x280+450+150")

        self.f_name = Entry(self.root, width=30)
        self.f_name.grid(row=0, column=1, pady=(15, 5))
        self.l_name = Entry(self.root, width=30)
        self.l_name.grid(row=1, column=1, pady=5)
        self.address = Entry(self.root, width=30)
        self.address.grid(row=2, column=1, pady=5)
        self.city = Entry(self.root, width=30)
        self.city.grid(row=3, column=1, pady=5)
        self.state = Entry(self.root, width=30)
        self.state.grid(row=4, column=1, pady=5)
        self.zipcode = Entry(self.root, width=30)
        self.zipcode.grid(row=5, column=1, pady=5)

        self.f_name_label = Label(self.root, text="First Name")
        self.f_name_label.grid(row=0, column=0, padx=(40, 0), pady=(15, 5), sticky=W)
        self.l_name_label = Label(self.root, text="Last Name:")
        self.l_name_label.grid(row=1, column=0, padx=(40, 0), sticky=W)
        self.address_label = Label(self.root, text="Address:")
        self.address_label.grid(row=2, column=0, padx=(40, 0), sticky=W)
        self.city_label = Label(self.root, text="City:")
        self.city_label.grid(row=3, column=0, padx=(40, 0), sticky=W)
        self.state_label = Label(self.root, text="State:")
        self.state_label.grid(row=4, column=0, padx=(40, 0), sticky=W)
        self.zipcode_label = Label(self.root, text="Zipcode:")
        self.zipcode_label.grid(row=5, column=0, padx=(40, 0), pady=(0, 5), sticky=W)

        self.back_button = Button(self.root, text="Back", bg="#add8e6", command=self.close_window)
        self.back_button.grid(row=6, column=0, padx=(60, 0), pady=30, ipadx=25)
        self.submit_button = Button(self.root, text="Submit", bg="#90EE90", command=self.submit)
        self.submit_button.grid(row=6, column=1, padx=20, ipadx=30)

    def submit(self):
        if self.f_name.get() == self.l_name.get() == self.address.get() == self.city.get() == self.state.get() == self.zipcode.get() == '':
            messagebox.showwarning("Warning", "Please Fill The Details!", parent=self.root)
        else:
            conn = sqlite3.connect('address_book.db')
            c = conn.cursor()

            query = "Insert Into addresses(first_name, last_name, address, city, state, zipcode) values(?, ?, ?, ?, ?, ?)"

            c.execute(query, (self.f_name.get(), self.l_name.get(), self.address.get(), self.city.get(), self.state.get(), self.zipcode.get()))

            self.f_name.delete(0, END)
            self.l_name.delete(0, END)
            self.address.delete(0, END)
            self.city.delete(0, END)
            self.state.delete(0, END)
            self.zipcode.delete(0, END)

            messagebox.showinfo("Information", "Successfully Inserted", parent=self.root)

            conn.commit()
            conn.close()

    def close_window(self):
        global root
        root = Tk()
        WinHome(root, "Home Window")
        self.root.destroy()


class WinSearch:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("530x360+450+150")

        self.select_label = Label(self.root, text="Search:", anchor=E, font=('Helvetica', 10))
        self.select_label.grid(row=0, column=0, padx=(5, 35), pady=20, ipadx=10)
        self.select_Entry = Entry(self.root, width=20, font=('Helvetica', 10))
        self.select_Entry.grid(row=0, column=1, padx=(0, 10))

        self.drop = ttk.Combobox(self.root, value=['Search by...', 'OID', 'First_Name', 'Last_Name', 'Address', 'City', 'State', 'Zipcode'])
        self.drop.current(0)
        self.drop.grid(row=0, column=2, padx=(0, 20))

        # Buttons
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 10), command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(10, 0), pady=15, ipadx=10)
        self.show_button = Button(self.root, text="Search", bg="#90EE90", font=('Helvetica', 10), command=lambda: self.show(1))
        self.show_button.grid(row=1, column=1, padx=0, ipadx=10)
        self.show_all_button = Button(self.root, text="Show All", bg="orange", font=('Helvetica', 10), command=lambda: self.show(0))
        self.show_all_button.grid(row=1, column=2, padx=(25, 30), ipadx=10)

        # Add some style
        self.style = ttk.Style()
        # Pick a theme
        self.style.theme_use("clam")
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
        self.tree_frame.grid(row=2, column=0, columnspan=3, pady=20, padx=10)

        # TreeView ScrollBar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        # Create TreeView
        self.my_tree = ttk.Treeview(self.tree_frame, height=7, yscrollcommand=self.tree_scroll.set)
        self.my_tree.pack()

        # Configure ScrollBar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Define our columns
        self.my_tree['columns'] = ("OID", "F_Name", "L_Name", "Address", "City", "State", "Zipcode")

        # Format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("OID", anchor=CENTER, width=30)
        self.my_tree.column("F_Name", anchor=CENTER, width=80)
        self.my_tree.column("L_Name", anchor=CENTER, width=80)
        self.my_tree.column("Address", anchor=CENTER, width=80)
        self.my_tree.column("City", anchor=CENTER, width=80)
        self.my_tree.column("State", anchor=CENTER, width=80)
        self.my_tree.column("Zipcode", anchor=CENTER, width=60)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=CENTER)
        self.my_tree.heading("OID", text="OID", anchor=CENTER)
        self.my_tree.heading("F_Name", text="F_Name", anchor=CENTER)
        self.my_tree.heading("L_Name", text="L_Name", anchor=CENTER)
        self.my_tree.heading("Address", text="Address", anchor=CENTER)
        self.my_tree.heading("City", text="City", anchor=CENTER)
        self.my_tree.heading("State", text="State", anchor=CENTER)
        self.my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)

        # Count Variable for number of records
        self.count = 0

        # Create Stripped row Tags
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

    def show(self, a):
        if self.select_Entry.get() == "" and a == 1:
            messagebox.showwarning("Warning", "Please Provide the Value to be Searched", parent=self.root)
            return

        selection = self.drop.get()
        if selection == 'Search by...' and a == 1:
            messagebox.showwarning("Warning", "Please Select an Option to be Searched!!!", parent=self.root)
            return

        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        if a == 0:
            c.execute("Select OID, * from addresses")
        else:
            query = "select OID, * from addresses where " + selection + " LIKE ?"
            value = '%'+self.select_Entry.get()+'%'
            c.execute(query, (value,))

        records = c.fetchall()

        # Removing the Preexisting Records(if any)
        for rec in self.my_tree.get_children():
            self.my_tree.delete(rec)

        # Resetting the Count
        self.count = 0

        if records:
            for record in records:
                if self.count % 2 == 0:
                    self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=record, tags=("evenrow",))
                else:
                    self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=record, tags=("oddrow",))
                self.count += 1
        else:
            messagebox.showinfo("Information", "No Record Found!!!", parent=self.root)

        # Clearing the Entry Box and Resetting the Drop Down Box
        self.select_Entry.delete(0, END)
        self.drop.current(0)

        conn.commit()
        conn.close()

    def close_window(self):
        global root
        root = Tk()
        WinHome(root, "Home Window")
        self.root.destroy()


class WinUpdate:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("360x400+450+150")

        self.select_label = Label(self.root, text="Select ID:", anchor=E)
        self.select_label.grid(row=0, column=0, padx=(30, 38), pady=(20, 10), ipadx=18)
        self.select_Entry = Entry(self.root, width=20)
        self.select_Entry.grid(row=0, column=1, padx=(0, 40))

        self.back_button = Button(self.root, text="Back", bg="#add8e6", command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(90, 0), pady=(10, 30), ipadx=10)
        self.show_button = Button(self.root, text="Show", bg="orange", command=self.display)
        self.show_button.grid(row=1, column=1, padx=(0, 60), pady=(10, 30), ipadx=10)

        self.f_name = Entry(self.root, width=30)
        self.f_name.grid(row=2, column=1, pady=5)
        self.l_name = Entry(self.root, width=30)
        self.l_name.grid(row=3, column=1, pady=5)
        self.address = Entry(self.root, width=30)
        self.address.grid(row=4, column=1, pady=5)
        self.city = Entry(self.root, width=30)
        self.city.grid(row=5, column=1, pady=5)
        self.state = Entry(self.root, width=30)
        self.state.grid(row=6, column=1, pady=5)
        self.zipcode = Entry(self.root, width=30)
        self.zipcode.grid(row=7, column=1, pady=5)

        self.f_name_label = Label(self.root, text="First Name")
        self.f_name_label.grid(row=2, column=0, padx=(30, 0), sticky=W)
        self.l_name_label = Label(self.root, text="Last Name:")
        self.l_name_label.grid(row=3, column=0, padx=(30, 0), sticky=W)
        self.address_label = Label(self.root, text="Address:")
        self.address_label.grid(row=4, column=0, padx=(30, 0), sticky=W)
        self.city_label = Label(self.root, text="City:")
        self.city_label.grid(row=5, column=0, padx=(30, 0), sticky=W)
        self.state_label = Label(self.root, text="State:")
        self.state_label.grid(row=6, column=0, padx=(30, 0), sticky=W)
        self.zipcode_label = Label(self.root, text="Zipcode:")
        self.zipcode_label.grid(row=7, column=0, padx=(30, 0), sticky=W)

        self.update_button = Button(self.root, text="Update", bg="#90EE90", command=self.update)
        self.update_button.grid(row=8, column=0, pady=15, ipadx=20, columnspan=2)

    def display(self):
        self.f_name.delete(0, END)
        self.l_name.delete(0, END)
        self.address.delete(0, END)
        self.city.delete(0, END)
        self.state.delete(0, END)
        self.zipcode.delete(0, END)

        if self.select_Entry.get() == '':
            messagebox.showwarning("Warning", "Please Select an ID!", parent=self.root)

        else:
            conn = sqlite3.connect('address_book.db')
            c = conn.cursor()

            c.execute("Select * from addresses where OID=?", self.select_Entry.get())
            record = c.fetchone()

            if not record:
                messagebox.showinfo("Information", "No Record Found!", parent=self.root)
            else:
                self.f_name.insert(0, record[0])
                self.l_name.insert(0, record[1])
                self.address.insert(0, record[2])
                self.city.insert(0, record[3])
                self.state.insert(0, record[4])
                self.zipcode.insert(0, record[5])

            conn.commit()
            conn.close()

    def update(self):
        if self.select_Entry.get() == '':
            messagebox.showwarning("Warning", "Please Select an ID!", parent=self.root)
        elif (self.f_name.get(), self.l_name.get(), self.address.get(), self.city.get(), self.state.get(), self.zipcode.get()) == ('', '', '', '', '', ''):
            messagebox.showwarning("Warning", "Please Fill The Details!", parent=self.root)
        else:
            conn = sqlite3.connect('address_book.db')
            c = conn.cursor()

            query = "update addresses set first_name = ?, last_name = ?,\
                                        address = ?, city = ?, state = ?, zipcode = ?\
                                        where OID = ?"
            e = (self.f_name.get(), self.l_name.get(), self.address.get(), self.city.get(), self.state.get(), self.zipcode.get(), self.select_Entry.get())
            c.execute(query, e)

            self.f_name.delete(0, END)
            self.l_name.delete(0, END)
            self.address.delete(0, END)
            self.city.delete(0, END)
            self.state.delete(0, END)
            self.zipcode.delete(0, END)
            self.select_Entry.delete(0, END)

            messagebox.showinfo("Information", "Successfully Updated", parent=self.root)

            conn.commit()
            conn.close()

    def close_window(self):
        global root
        root = Tk()
        WinHome(root, "Home Window")
        self.root.destroy()


class WinDelete:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("350x200+450+150")

        self.select_label = Label(self.root, text="Select ID:", anchor=E)
        self.select_label.grid(row=0, column=0, padx=(30, 38), pady=(20, 10), ipadx=18)
        self.select_Entry = Entry(self.root, width=20)
        self.select_Entry.grid(row=0, column=1, padx=(0, 40), pady=(20, 10))

        self.back_button = Button(self.root, text="Back", bg="#add8e6", command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(90, 0), pady=30, ipadx=10)
        self.del_button = Button(self.root, text="Delete", bg="orange", command=self.delete_record)
        self.del_button.grid(row=1, column=1, padx=(0, 60), pady=30, ipadx=10)

    def delete_record(self):
        if self.select_Entry.get() == '':
            messagebox.showwarning("Warning", "Please Select an ID!", parent=self.root)
        else:
            conn = sqlite3.connect('address_book.db')
            c = conn.cursor()

            query1 = "Select * from addresses where oid=?"
            c.execute(query1, (self.select_Entry.get(),))

            if c.fetchone() is None:
                messagebox.showerror("Error", "No Record Found to Delete\nPlease Try Again!!!", parent=self.root)
            else:
                query2 = "Delete from addresses where oid=?"
                c.execute(query2, (self.select_Entry.get(),))

                self.select_Entry.delete(0, END)

                messagebox.showinfo("Information", "Successfully Deleted", parent=self.root)

            conn.commit()
            conn.close()

    def close_window(self):
        global root
        root = Tk()
        WinHome(root, "Home Window")
        self.root.destroy()


WinLogin(root, "Login Window", "377x230+450+150")

mainloop()


# conn = sqlite3.connect('./address_book.db')
# c = conn.cursor()
#
# c.execute('''CREATE TABLE addresses(
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer)''')
#
# conn.commit()
# conn.close()
