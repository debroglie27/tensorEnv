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

# ADMIN: Arijeet
# Secret Key: 12345

# Users = ['Arijeet', 'Mrinal', 'Nibedita', 'Hritesh', 'Shubham']
# Password = ['1234', '1967', '1969', '1999', '1010']

root = Tk()


class WinLogin:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("370x230+450+150")

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
        self.forgot_pass_label = Button(self.root, text="Forgot Password?", fg="blue", relief=FLAT, command=lambda: self.signup(WinForgotPass, "Forgot Password Window"))
        self.forgot_pass_label.grid(row=3, column=1, padx=(0, 30), columnspan=2)

    def login_check(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn = sqlite3.connect('address_book.db')
            c = conn.cursor()
            query = 'Select Password, oid from users where Username=?'
            c.execute(query, (username,))

            record, oid = c.fetchone()

            conn.commit()
            conn.close()

            if record == password:
                self.new_window(WinHome, "Home Window", oid)
            else:
                messagebox.showerror("Error", "Incorrect!!! Username or Password", parent=self.root)

        except Exception:
            messagebox.showerror("Error", "Incorrect!!! Username or Password", parent=self.root)

    def forgot_pass_window(self, _class, title):
        level = Tk()
        _class(level, title)
        self.root.destroy()

    def signup(self, _class, title):
        level = Tk()
        _class(level, title)
        self.root.destroy()

    def new_window(self, _class, title, oid):
        level = Tk()
        _class(level, title, oid)
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
        level = Tk()
        WinLogin(level, "Login Window")
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
        self.secret_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.secret_entry.grid(row=3, column=1, padx=10, pady=(20, 10), columnspan=3)

        # Back Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=20, padx=(30, 0), ipadx=4)

        # Submit Button
        self.submit_button = Button(self.root, text="Submit", bg="#90EE90", font=('Helvetica', 11), command=self.signup_check)
        self.submit_button.grid(row=4, column=2, columnspan=2, pady=20, padx=(0, 60), ipadx=4)

    def signup_check(self):
        # Storing the values of Entry Boxes
        username = self.username_entry.get()
        password = self.password_entry.get()
        email_id = self.email_entry.get()
        secret_key = self.secret_entry.get()

        # Clearing the Entry Boxes
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.secret_entry.delete(0, END)

        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        c.execute('''Select secret_key from Secret_Key''')

        record = c.fetchone()[0]

        if not secret_key == record:
            messagebox.showerror("Error", "Secret Key Incorrect!!!", parent=self.root)
            return
        else:
            try:
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
        level = Tk()
        WinLogin(level, "Login Window")
        self.root.destroy()


class WinHome:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+140")
        self.root['bg'] = "#90EE90"

        self.head_label = Label(self.root, text="Welcome to Database", bg='#A0E170', font=('Helvetica', 25))
        self.head_label.pack(pady=(0, 20), ipadx=50, ipady=10)

        self.but_insert = Button(self.root, text="Insert", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinInsert, "Insert Window", self.user_oid))
        self.but_insert.pack(pady=(10, 0), ipadx=40)
        self.but_show = Button(self.root, text="Search", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinSearch, "Search Window", self.user_oid))
        self.but_show.pack(pady=(18, 0), ipadx=34)
        self.but_update = Button(self.root, text="Update", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinUpdate, "Update Window", self.user_oid))
        self.but_update.pack(pady=(18, 0), ipadx=34)
        self.but_delete = Button(self.root, text="Delete", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinDelete, "Delete Window", self.user_oid))
        self.but_delete.pack(pady=(18, 0), ipadx=37)

        # Create Menu
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)

        # Add File Menu
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        # Add File Menu Items
        self.file_menu.add_command(label="Insert", command=lambda: self.new_window(WinInsert, "Insert Window", self.user_oid))
        self.file_menu.add_command(label="Search", command=lambda: self.new_window(WinSearch, "Search Window", self.user_oid))
        self.file_menu.add_command(label="Update", command=lambda: self.new_window(WinUpdate, "Update Window", self.user_oid))
        self.file_menu.add_command(label="Delete", command=lambda: self.new_window(WinDelete, "Delete Window", self.user_oid))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Logout", command=lambda: self.logout(WinLogin, "Login Window"))
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add Settings Menu
        self.settings_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Settings", menu=self.settings_menu)
        # Add Settings Menu Items
        self.settings_menu.add_command(label="User Details", command=lambda: self.new_window(WinUserDetails, "User Details", self.user_oid))
        self.settings_menu.add_command(label="Change Password", command=lambda: self.new_window(WinChangePassword, "Change Password", self.user_oid))

        if self.user_oid == 1:
            # Add Admin Settings Menu
            self.admin_settings_menu = Menu(self.my_menu, tearoff=False)
            self.my_menu.add_cascade(label="Admin Settings", menu=self.admin_settings_menu)
            # Add Settings Menu Items
            self.admin_settings_menu.add_command(label="All User Details", command=lambda: self.new_window(WinAllUserDetails, "All User Details", self.user_oid))
            self.admin_settings_menu.add_command(label="Change Secret Key", command=lambda: self.new_window(WinChangeSecretKey, "Change Secret Key", self.user_oid))

        # Add Right Click Pop Up Menu
        self.my_popup_menu = Menu(self.root, tearoff=False)
        # Insert, Search, Update and Delete
        self.my_popup_menu.add_command(label="Insert", command=lambda: self.new_window(WinInsert, "Insert Window", self.user_oid))
        self.my_popup_menu.add_command(label="Search", command=lambda: self.new_window(WinSearch, "Search Window", self.user_oid))
        self.my_popup_menu.add_command(label="Update", command=lambda: self.new_window(WinUpdate, "Update Window", self.user_oid))
        self.my_popup_menu.add_command(label="Delete", command=lambda: self.new_window(WinDelete, "Delete Window", self.user_oid))
        self.my_popup_menu.add_separator()
        # User Details and Change Password
        self.my_popup_menu.add_command(label="User Details", command=lambda: self.new_window(WinUserDetails, "User Details", self.user_oid))
        self.my_popup_menu.add_command(label="Change Password", command=lambda: self.new_window(WinChangePassword, "Change Password", self.user_oid))
        self.my_popup_menu.add_separator()

        if self.user_oid == 1:
            # All User Details and Change Secret Key
            self.my_popup_menu.add_command(label="All User Details", command=lambda: self.new_window(WinAllUserDetails, "All User Details", self.user_oid))
            self.my_popup_menu.add_command(label="Change Secret Key", command=lambda: self.new_window(WinChangeSecretKey, "Change Secret Key", self.user_oid))
            self.my_popup_menu.add_separator()

        # Logout and Exit
        self.my_popup_menu.add_command(label="Logout", command=lambda: self.logout(WinLogin, "Login Window"))
        self.my_popup_menu.add_command(label="Exit", command=root.quit)

        # Binding the Right click Pop Up Menu
        self.root.bind("<Button-3>", self.my_popup)

        # Finding Username for our Status Bar
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        query = 'Select Username from users where OID=?'
        c.execute(query, (self.user_oid,))

        username = c.fetchone()[0]

        conn.commit()
        conn.close()

        # Finding whether our user is an ADMIN or not
        if self.user_oid == 1:
            text = f'User: {username} (ADMIN) '
        else:
            text = f'User: {username} '

        # Add Status Bar
        self.status_bar = Label(self.root, text=text, anchor=E, bg="#dfdfdf")
        self.status_bar.pack(fill=X, side=BOTTOM, ipady=1)

    def my_popup(self, event):
        self.my_popup_menu.tk_popup(event.x_root, event.y_root)

    def logout(self, _class, title):
        level = Tk()
        _class(level, title)
        self.root.destroy()

    def new_window(self, _class, title, oid):
        level = Tk()
        _class(level, title, oid)
        self.root.destroy()


class WinUserDetails:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("435x220+440+150")

        # Username Label and Entry
        self.username_label = Label(self.root, text="Username:", font=('Helvetica', 15))
        self.username_label.grid(row=0, column=0, padx=10, pady=(30, 0), sticky=E)
        self.username_entry = Entry(self.root, font=('Helvetica', 15), fg="green", width=19)
        self.username_entry.grid(row=0, column=1, padx=10, pady=(30, 0), sticky=W)

        # Email Label and Entry
        self.email_label = Label(self.root, text="Email:", font=('Helvetica', 15))
        self.email_label.grid(row=1, column=0, padx=10, pady=20, sticky=E)
        self.email_entry = Entry(self.root, font=('Helvetica', 15), fg="green", width=19)
        self.email_entry.grid(row=1, column=1, padx=10, pady=20, sticky=W)

        # Change Buttons
        self.change_button1 = Button(self.root, text="Change", font=('Helvetica', 10), bg="orange", command=lambda: self.change_entry(0))
        self.change_button1.grid(row=0, column=2, padx=5, pady=(30, 0))
        self.change_button2 = Button(self.root, text="Change", font=('Helvetica', 10), bg="orange", command=lambda: self.change_entry(1))
        self.change_button2.grid(row=1, column=2, padx=5, pady=20)

        # Finding Details of User
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        query = 'Select Username, Email_id from users where OID=?'
        c.execute(query, (self.user_oid,))

        username, email = c.fetchone()

        conn.commit()
        conn.close()

        # Displaying Values in Username Entry and Email Entry
        self.username_entry.insert(0, username)
        self.email_entry.insert(0, email)

        # Making the Entry Boxes READ-ONLY
        self.username_entry.config(state="readonly")
        self.email_entry.config(state="readonly")

        # Back and Save Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.grid(row=2, column=0, columnspan=3)

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11), command=self.save_details)
        self.save_button.grid(row=0, column=1, pady=20, padx=(40, 0), ipadx=5)

    def close_window(self):
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()

    def change_entry(self, val):
        if val == 0:
            self.username_entry.config(state=NORMAL)
        elif val == 1:
            self.email_entry.config(state=NORMAL)

    def save_details(self):
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        query = "update users set Username = ?, Email_id = ? where OID = ?"
        e = (self.username_entry.get(), self.email_entry.get(), self.user_oid)
        c.execute(query, e)

        conn.commit()
        conn.close()

        messagebox.showinfo("Information", "Successfully Saved", parent=self.root)

        self.close_window()


class WinChangePassword:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("450x280+440+150")

        # Bullet Symbol
        self.bullet_symbol = "\u2022"

        # Current Password Label and Entry
        self.current_password_label = Label(self.root, text="Current Password:", font=('Helvetica', 15))
        self.current_password_label.grid(row=0, column=0, padx=10, pady=(30, 20), sticky=E)
        self.current_password_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.current_password_entry.grid(row=0, column=1, padx=10, pady=(30, 20), sticky=W)

        # New Password Label and Entry
        self.new_password_label = Label(self.root, text="New Password:", font=('Helvetica', 15))
        self.new_password_label.grid(row=1, column=0, padx=10, pady=(20, 10), sticky=E)
        self.new_password_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.new_password_entry.grid(row=1, column=1, padx=10, pady=(20, 10), sticky=W)

        # Confirm Password Label and Entry
        self.confirm_password_label = Label(self.root, text="Confirm Password:", font=('Helvetica', 15))
        self.confirm_password_label.grid(row=2, column=0, padx=10, pady=(5, 0), sticky=E)
        self.confirm_password_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=(5, 0), sticky=W)

        # Back and Save Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.grid(row=3, column=0, pady=20, columnspan=2)

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11), command=self.change_password)
        self.save_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

    def close_window(self):
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()

    def change_password(self):
        # Storing the values of Entry Boxes
        current_password = self.current_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Clearing the Entry Boxes
        self.current_password_entry.delete(0, END)
        self.new_password_entry.delete(0, END)
        self.confirm_password_entry.delete(0, END)

        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        query = "Select password from users where oid=?"
        c.execute(query, (self.user_oid,))

        record = c.fetchone()[0]

        if record != current_password.get():
            messagebox.showerror("Error", "Wrong Current Password!!!", parent=self.root)
            return
        else:
            if new_password != confirm_password:
                messagebox.showerror("Error", "Confirm Password is not same\nas New Password!!!", parent=self.root)
                return
            else:
                query = "update users set password = ? where OID = ?"
                c.execute(query, (confirm_password, self.user_oid))

                messagebox.showinfo("Information", "Password Changed Successfully!!!", parent=self.root)

        conn.commit()
        conn.close()

        self.close_window()


class WinAllUserDetails:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("390x290+450+150")

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
        self.tree_frame.pack(pady=(20, 0), padx=10)

        # TreeView ScrollBar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        # Create TreeView
        self.my_tree = ttk.Treeview(self.tree_frame, height=6, yscrollcommand=self.tree_scroll.set)
        self.my_tree.pack()

        # Configure ScrollBar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Define our columns
        self.my_tree['columns'] = ("OID", "Username", "Email")

        # Format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("OID", anchor=CENTER, width=30)
        self.my_tree.column("Username", anchor=CENTER, width=100)
        self.my_tree.column("Email", anchor=CENTER, width=180)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=CENTER)
        self.my_tree.heading("OID", text="OID", anchor=CENTER)
        self.my_tree.heading("Username", text="Username", anchor=CENTER)
        self.my_tree.heading("Email", text="Email", anchor=CENTER)

        # Count Variable for number of records
        self.count = 0

        # Create Stripped row Tags
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        c.execute("Select OID, Username, Email_id from users where oid <> 1")
        records = c.fetchall()

        conn.commit()
        conn.close()

        # Resetting the Count
        self.count = 0

        for record in records:
            if self.count % 2 == 0:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=record, tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index='end', iid=self.count, text="", values=record, tags=("oddrow",))
            self.count += 1

        # Back and Remove Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=(20, 10))

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, pady=10, padx=(5, 45), ipadx=5)

        # Remove Button
        self.remove_button = Button(self.button_frame, text="Remove", bg="orange", font=('Helvetica', 11), command=self.remove_user)
        self.remove_button.grid(row=0, column=1, pady=10, padx=(25, 0), ipadx=5)

    def close_window(self):
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()

    def remove_user(self):
        if self.my_tree.focus():
            for record in self.my_tree.selection():
                # Getting the OID from the record
                OID = self.my_tree.item(record)['values'][0]

                conn = sqlite3.connect('address_book.db')
                c = conn.cursor()

                c.execute("Delete from users where oid=?", (OID, ))

                conn.commit()
                conn.close()

                # removing the record from the treeview
                self.my_tree.delete(record)

                messagebox.showinfo("Information", "Successfully Removed!")
        else:
            messagebox.showinfo("Information", "Please select a record to remove!!!")


class WinChangeSecretKey:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("456x280+440+150")

        # Bullet Symbol
        self.bullet_symbol = "\u2022"

        # Current Password Label and Entry
        self.current_secret_key_label = Label(self.root, text="Current Secret Key:", font=('Helvetica', 15))
        self.current_secret_key_label.grid(row=0, column=0, padx=10, pady=(30, 20), sticky=E)
        self.current_secret_key_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.current_secret_key_entry.grid(row=0, column=1, padx=10, pady=(30, 20), sticky=W)
        
        # New Password Label and Entry
        self.new_secret_key_label = Label(self.root, text="New Secret Key:", font=('Helvetica', 15))
        self.new_secret_key_label.grid(row=1, column=0, padx=10, pady=(20, 10), sticky=E)
        self.new_secret_key_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.new_secret_key_entry.grid(row=1, column=1, padx=10, pady=(20, 10), sticky=W)

        # Confirm Password Label and Entry
        self.confirm_secret_key_label = Label(self.root, text="Confirm Secret Key:", font=('Helvetica', 15))
        self.confirm_secret_key_label.grid(row=2, column=0, padx=10, pady=(5, 0), sticky=E)
        self.confirm_secret_key_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.confirm_secret_key_entry.grid(row=2, column=1, padx=10, pady=(5, 0), sticky=W)

        # Back and Save Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.grid(row=3, column=0, pady=20, columnspan=2)

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11), command=self.change_secret_key)
        self.save_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

    def close_window(self):
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()

    def change_secret_key(self):
        # Storing the values of Entry Boxes
        current_secret_key = self.current_secret_key_entry.get()
        new_secret_key = self.new_secret_key_entry.get()
        confirm_secret_key = self.confirm_secret_key_entry.get()

        # Clearing the Entry Boxes
        self.current_secret_key_entry.delete(0, END)
        self.new_secret_key_entry.delete(0, END)
        self.confirm_secret_key_entry.delete(0, END)

        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        c.execute('''Select secret_key from Secret_Key''')

        record = c.fetchone()[0]

        if record != current_secret_key:
            messagebox.showerror("Error", "Wrong Current Secret Key!!!", parent=self.root)
            return
        else:
            if new_secret_key != confirm_secret_key:
                messagebox.showerror("Error", "Confirm Secret Key is not same\nas New Secret Key!!!", parent=self.root)
                return
            else:
                query = "update Secret_Key set secret_key = ? where OID = 1"
                c.execute(query, (confirm_secret_key,))

                messagebox.showinfo("Information", "Secret Key Changed Successfully!!!", parent=self.root)

        conn.commit()
        conn.close()

        self.close_window()


class WinInsert:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("395x330+430+150")

        # All Entry Boxes
        self.f_name = Entry(self.root, width=20, font=('Helvetica', 15))
        self.f_name.grid(row=0, column=1, pady=(15, 5), padx=(20, 0))
        self.l_name = Entry(self.root, width=20, font=('Helvetica', 15))
        self.l_name.grid(row=1, column=1, pady=5, padx=(20, 0))
        self.address = Entry(self.root, width=20, font=('Helvetica', 15))
        self.address.grid(row=2, column=1, pady=5, padx=(20, 0))
        self.city = Entry(self.root, width=20, font=('Helvetica', 15))
        self.city.grid(row=3, column=1, pady=5, padx=(20, 0))
        self.state = Entry(self.root, width=20, font=('Helvetica', 15))
        self.state.grid(row=4, column=1, pady=5, padx=(20, 0))
        self.zipcode = Entry(self.root, width=20, font=('Helvetica', 15))
        self.zipcode.grid(row=5, column=1, pady=5, padx=(20, 0))

        # All Labels
        self.f_name_label = Label(self.root, text="First Name:", font=('Helvetica', 15))
        self.f_name_label.grid(row=0, column=0, padx=(20, 0), pady=(15, 5), sticky=E)
        self.l_name_label = Label(self.root, text="Last Name:", font=('Helvetica', 15))
        self.l_name_label.grid(row=1, column=0, padx=(20, 0), pady=5, sticky=E)
        self.address_label = Label(self.root, text="Address:", font=('Helvetica', 15))
        self.address_label.grid(row=2, column=0, padx=(20, 0), pady=5, sticky=E)
        self.city_label = Label(self.root, text="City:", font=('Helvetica', 15))
        self.city_label.grid(row=3, column=0, padx=(20, 0), pady=5, sticky=E)
        self.state_label = Label(self.root, text="State:", font=('Helvetica', 15))
        self.state_label.grid(row=4, column=0, padx=(20, 0), pady=5, sticky=E)
        self.zipcode_label = Label(self.root, text="Zipcode:", font=('Helvetica', 15))
        self.zipcode_label.grid(row=5, column=0, padx=(20, 0), pady=5, sticky=E)

        # Back and Submit Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.grid(row=6, column=0, pady=10, columnspan=2)

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Submit Button
        self.submit_button = Button(self.button_frame, text="Submit", bg="#90EE90", font=('Helvetica', 11), command=self.submit)
        self.submit_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

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
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()


class WinSearch:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("530x365+400+150")

        # Our Search Label and Search Entry
        self.search_label = Label(self.root, text="Search:", anchor=E, font=('Helvetica', 10))
        self.search_label.grid(row=0, column=0, padx=(5, 35), pady=20, ipadx=10)
        self.search_Entry = Entry(self.root, width=20, font=('Helvetica', 10))
        self.search_Entry.grid(row=0, column=1, padx=(0, 10))

        # Drop Down Box for Search Type
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
        if self.search_Entry.get() == "" and a == 1:
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
            value = '%'+self.search_Entry.get()+'%'
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
        self.search_Entry.delete(0, END)
        self.drop.current(0)

        conn.commit()
        conn.close()

    def close_window(self):
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()


class WinUpdate:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("390x430+440+110")

        # Select Label and Entry Box
        self.select_label = Label(self.root, text="Select ID:", anchor=E, font=('Helvetica', 15))
        self.select_label.grid(row=0, column=0, padx=(20, 25), pady=(20, 10), ipadx=18)
        self.select_Entry = Entry(self.root, width=15, font=('Helvetica', 15))
        self.select_Entry.grid(row=0, column=1, padx=(0, 40), pady=(20, 10))

        # Back and Show Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(90, 0), pady=(10, 30), ipadx=6)
        self.show_button = Button(self.root, text="Show", bg="orange", font=('Helvetica', 11), command=self.display)
        self.show_button.grid(row=1, column=1, padx=(0, 60), pady=(10, 30), ipadx=6)

        # Label and Entry Frame
        self.my_frame = Frame(self.root)
        self.my_frame.grid(row=2, column=0, columnspan=2)

        # All Entry Boxes
        self.f_name = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.f_name.grid(row=0, column=1, pady=5)
        self.l_name = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.l_name.grid(row=1, column=1, pady=5)
        self.address = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.address.grid(row=2, column=1, pady=5)
        self.city = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.city.grid(row=3, column=1, pady=5)
        self.state = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.state.grid(row=4, column=1, pady=5)
        self.zipcode = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.zipcode.grid(row=5, column=1, pady=5)

        # All Labels
        self.f_name_label = Label(self.my_frame, text="First Name:", font=('Helvetica', 15))
        self.f_name_label.grid(row=0, column=0, padx=(0, 20), sticky=E)
        self.l_name_label = Label(self.my_frame, text="Last Name:", font=('Helvetica', 15))
        self.l_name_label.grid(row=1, column=0, padx=(0, 20), sticky=E)
        self.address_label = Label(self.my_frame, text="Address:", font=('Helvetica', 15))
        self.address_label.grid(row=2, column=0, padx=(0, 20), sticky=E)
        self.city_label = Label(self.my_frame, text="City:", font=('Helvetica', 15))
        self.city_label.grid(row=3, column=0, padx=(0, 20), sticky=E)
        self.state_label = Label(self.my_frame, text="State:", font=('Helvetica', 15))
        self.state_label.grid(row=4, column=0, padx=(0, 20), sticky=E)
        self.zipcode_label = Label(self.my_frame, text="Zipcode:", font=('Helvetica', 15))
        self.zipcode_label.grid(row=5, column=0, padx=(0, 20), sticky=E)

        # Update Button
        self.update_button = Button(self.root, text="Update", bg="#90EE90", font=('Helvetica', 11), command=self.update)
        self.update_button.grid(row=3, column=0, pady=25, ipadx=10, columnspan=2)

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
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()


class WinDelete:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
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
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()


WinLogin(root, "Login Window")

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
