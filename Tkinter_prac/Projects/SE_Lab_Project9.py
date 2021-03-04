import os
import smtplib
from pathlib import Path
from dotenv import load_dotenv
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

# conn = sqlite3.connect('SE_Lab_Project9.db')
# c = conn.cursor()

# Create Table Machines
# c.execute('''Create table Machines ([Machine_ID] INTEGER PRIMARY KEY,
# [Machine_Type] text,
# [MTTF] FLOAT,
# [Status] text)''')

# Create Table Adjusters
# c.execute('''Create table Adjusters ([Adjuster_ID] INTEGER PRIMARY KEY,
# [First_Name] text,
# [Last_Name] text,
# [Expertise] text,
# [Email_id] text,
# [Status] text)''')

# Create Table Users
# c.execute('''Create table Users ([Username] text PRIMARY KEY,
# [Email_id] text,
# [Password] text)''')

# Create Table Secret_Key
# c.execute('''Create table Secret_Key ([secret_key] text)''')

# Insert Data values in Users
# query = "Insert Into Users(Username, Email_id, Password) values(?, ?, ?)"
# c.execute(query, ('Gunadeep', 'gunadeep@gmail.com', '6969'))

# Fetching Data from Users
# c.execute("Select * from Users")
# record = c.fetchall()
#
# for rec in record:
#     print(rec)

# Insert secret_key in Secret_Key
# query = "Insert Into Secret_Key(secret_key) values('12345')"
# c.execute(query)

# Fetching Data from Secret_Key
# c.execute("Select * from Secret_Key")
# record = c.fetchone()[0]
# print(record)

# conn.commit()
# conn.close()

# ADMIN: Arijeet
# Secret Key: 12345

# Users = ['Arijeet', 'Aushish', 'Aravind', 'Anwesha', 'Ankit', 'Gunadeep', 'Anamika']
# Password = ['1234', '1999', '4321', '5555', '9876', '6969', '5555']

root = Tk()


class WinLogin:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("370x230+450+150")
        self.root.resizable(width=False, height=False)

        # Bullet Symbol
        self.bullet_symbol = "\u2022"

        # Username Label and Entry
        self.username_label = Label(self.root, text="Username:", font=('Helvetica', 15))
        self.username_label.grid(row=0, column=0, padx=10, pady=(30, 0))
        self.username_entry = Entry(self.root, fg="#BFBFBF", font=('Helvetica', 15), validate="focusin", validatecommand=lambda: self.placeholder_vanish(0))
        self.username_entry.grid(row=0, column=1, padx=10, pady=(30, 0), columnspan=3)

        # Password Label and Entry
        self.password_label = Label(self.root, text="Password:", font=('Helvetica', 15))
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = Entry(self.root, fg="#BFBFBF", font=('Helvetica', 15), validate="focusin", validatecommand=lambda: self.placeholder_vanish(1))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

        # Login Button
        self.login_button = Button(self.root, text="Login", bg="#90EE90", font=('Helvetica', 11), command=self.login_check)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20, padx=(35, 0), ipadx=6)

        # SignUp Button
        self.signup_button = Button(self.root, text="SignUp", bg="#add8e6", font=('Helvetica', 11), command=lambda: self.forgot_signup_window(WinSignup, "SignUp Window"))
        self.signup_button.grid(row=2, column=2, columnspan=2, pady=20, padx=(0, 50), ipadx=6)

        # Forgot Password Button
        self.forgot_pass_button = Button(self.root, text="Forgot Password?", fg="blue", relief=FLAT, command=lambda: self.forgot_signup_window(WinForgotPass, "Forgot Password Window"))
        self.forgot_pass_button.grid(row=3, column=1, padx=(0, 30), columnspan=2)

        # Placeholder for our Entry Boxes and also giving a message to distinguish
        self.username_entry.insert(0, "Username")
        self.password_entry.insert(0, "Password")

    def placeholder_vanish(self, val):
        if val == 0 and self.username_entry.get() == "Username":
            # Deleting the Placeholder and making foreground "black"
            self.username_entry.delete(0, END)
            self.username_entry.config(fg="black")
        if val == 1 and self.password_entry.get() == "Password":
            # Deleting the Placeholder, making foreground "black" and also the "show"
            self.password_entry.delete(0, END)
            self.password_entry.config(fg="black", show=self.bullet_symbol)

    def login_check(self):
        # Storing the Entry Boxes value in variables
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn = sqlite3.connect('SE_Lab_Project9.db')
            c = conn.cursor()

            # Finding Password and OID for the given Username
            query = 'Select Password, oid from Users where Username=?'
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

    def forgot_signup_window(self, _class, title):
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
        self.root.resizable(width=False, height=False)

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
        # Displaying Message Informing that it will take time
        messagebox.showinfo("Information", "It may take some time\nPlease Wait!!!", parent=self.root)
        email = self.email_entry.get()

        try:
            conn = sqlite3.connect('SE_Lab_Project9.db')
            c = conn.cursor()

            # Finding Password for the given Email_id
            query = 'Select Password from Users where Email_id=?'
            c.execute(query, (email,))

            user_password = c.fetchone()

            conn.commit()
            conn.close()

            if user_password is None:
                messagebox.showerror("Error", "Incorrect!!! Email-id", parent=self.root)
            else:
                try:
                    # Sending Email Code
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)

                        subject = 'Forgot Password: Factory Simulation'
                        body = f'Dear User\n\nPlease find your Password of your Factory Simulation Account\n\nPassword: {user_password[0]}'

                        msg = f'Subject: {subject}\n\n{body}'

                        smtp.sendmail(self.EMAIL_ADDRESS, email, msg)

                        # Message to inform that Email has been sent
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
        self.root.resizable(width=False, height=False)

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

        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()

        # Finding Secret Key
        c.execute('''Select secret_key from Secret_Key''')

        record = c.fetchone()[0]

        if not secret_key == record:
            messagebox.showerror("Error", "Secret Key Incorrect!!!", parent=self.root)
        else:
            try:
                conn = sqlite3.connect('SE_Lab_Project9.db')
                c = conn.cursor()

                # Inserting Details of New User
                query = "Insert Into users(Username, Email_id, Password) values(?, ?, ?)"
                c.execute(query, (username, email_id, password))
                conn.commit()

                # Displaying message informing that account was added successfully
                messagebox.showinfo("Information", "Account Successfully Added!!!", parent=self.root)

            except Exception:
                messagebox.showinfo("Information", "Please Try Again!!!", parent=self.root)

        conn.commit()
        conn.close()

        self.close_window()

    def close_window(self):
        level = Tk()
        WinLogin(level, "Login Window")
        self.root.destroy()


class WinHome:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x290+450+130")
        self.root['bg'] = "#90EE90"
        self.root.resizable(width=False, height=False)

        self.head_label = Label(self.root, text="Factory Simulation", fg="purple", bg='#add8e6', bd=4, relief=GROOVE, font=('Monotype Corsiva', 32, "bold"))
        self.head_label.pack(pady=(0, 10), ipadx=28, ipady=5)

        self.but_machine = Button(self.root, text="Machine", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinMachine, "Machine Window", self.user_oid))
        self.but_machine.pack(pady=(32, 0), ipadx=31)
        self.but_adjuster = Button(self.root, text="Adjuster", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinAdjuster, "Adjuster Window", self.user_oid))
        self.but_adjuster.pack(pady=(26, 0), ipadx=31)

        # Create Menu
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)

        # Add File Menu
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        # Add File Menu Items
        self.file_menu.add_command(label="Machine", command=lambda: self.new_window(WinMachine, "Machine Window", self.user_oid))
        self.file_menu.add_command(label="Adjuster", command=lambda: self.new_window(WinAdjuster, "Adjuster Window", self.user_oid))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Logout", command=lambda: self.logout(WinLogin, "Login Window"))
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add Settings Menu
        self.settings_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Settings", menu=self.settings_menu)
        # Add Settings Menu Items
        self.settings_menu.add_command(label="User Details", command=lambda: self.new_window(WinUserDetails, "User Details", self.user_oid))
        self.settings_menu.add_command(label="Change Password", command=lambda: self.new_window(WinChangePassword, "Change Password", self.user_oid))

        # Only for Admin
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
        self.my_popup_menu.add_command(label="Machine", command=lambda: self.new_window(WinMachine, "Machine Window", self.user_oid))
        self.my_popup_menu.add_command(label="Adjuster", command=lambda: self.new_window(WinAdjuster, "Adjuster Window", self.user_oid))
        self.my_popup_menu.add_separator()
        # User Details and Change Password
        self.my_popup_menu.add_command(label="User Details", command=lambda: self.new_window(WinUserDetails, "User Details", self.user_oid))
        self.my_popup_menu.add_command(label="Change Password", command=lambda: self.new_window(WinChangePassword, "Change Password", self.user_oid))
        self.my_popup_menu.add_separator()

        # Only for Admin
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
        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()
        query = 'Select Username from Users where OID=?'
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
        self.root.resizable(width=False, height=False)

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
        self.change_button1 = Button(self.root, text="Change", font=('Helvetica', 10), bg="orange",
                                     command=lambda: self.change_entry(0))
        self.change_button1.grid(row=0, column=2, padx=5, pady=(30, 0))
        self.change_button2 = Button(self.root, text="Change", font=('Helvetica', 10), bg="orange",
                                     command=lambda: self.change_entry(1))
        self.change_button2.grid(row=1, column=2, padx=5, pady=20)

        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()

        # Finding Details of User
        query = 'Select Username, Email_id from Users where OID=?'
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
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11),
                                  command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11),
                                  command=self.save_details)
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
        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()

        # Updating the database with new values
        query = "update Users set Username = ?, Email_id = ? where OID = ?"
        e = (self.username_entry.get(), self.email_entry.get(), self.user_oid)
        c.execute(query, e)

        conn.commit()
        conn.close()

        # Message Informing Successful Saving
        messagebox.showinfo("Information", "Successfully Saved", parent=self.root)
        self.close_window()


class WinChangePassword:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("450x280+440+150")
        self.root.resizable(width=False, height=False)

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
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11),
                                  command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11),
                                  command=self.change_password)
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

        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()

        # Finding password the given user
        query = "Select Password from Users where oid=?"
        c.execute(query, (self.user_oid,))

        record = c.fetchone()[0]

        if record != current_password:
            messagebox.showerror("Error", "Wrong Current Password!!!", parent=self.root)
        else:
            if new_password != confirm_password:
                messagebox.showerror("Error", "Confirm Password is not same\nas New Password!!!", parent=self.root)
            else:
                query = "update Users set Password = ? where OID = ?"
                c.execute(query, (confirm_password, self.user_oid))

                conn.commit()

                messagebox.showinfo("Information", "Password Changed Successfully!!!", parent=self.root)

        conn.commit()
        conn.close()

        self.close_window()


class WinAllUserDetails:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("390x290+450+130")
        self.root.resizable(width=False, height=False)

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

        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()

        c.execute("Select OID, Username, Email_id from Users where oid <> 1")
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
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11),
                                  command=self.close_window)
        self.back_button.grid(row=0, column=0, pady=10, padx=(5, 45), ipadx=5)

        # Remove Button
        self.remove_button = Button(self.button_frame, text="Remove", bg="orange", font=('Helvetica', 11),
                                    command=self.remove_user)
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

                conn = sqlite3.connect('SE_Lab_Project9.db')
                c = conn.cursor()

                c.execute("Delete from Users where oid=?", (OID,))

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
        self.root.geometry("456x290+430+130")
        self.root.resizable(width=False, height=False)

        # Bullet Symbol
        self.bullet_symbol = "\u2022"

        # Current Password Label and Entry
        self.current_secret_key_label = Label(self.root, text="Current Secret Key:", font=('Helvetica', 15))
        self.current_secret_key_label.grid(row=0, column=0, padx=10, pady=(30, 10), sticky=E)
        self.current_secret_key_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.current_secret_key_entry.grid(row=0, column=1, padx=10, pady=(30, 10), sticky=W)

        # Forgot Secret Key Button
        self.forgot_secret_key_button = Button(self.root, text="Forgot Secret Key?", fg="blue", relief=FLAT,
                                               command=lambda: self.new_window(WinForgotSecretKey,
                                                                               "Forgot Secret Key Window",
                                                                               self.user_oid))
        self.forgot_secret_key_button.grid(row=1, column=0, columnspan=2)

        # New Password Label and Entry
        self.new_secret_key_label = Label(self.root, text="New Secret Key:", font=('Helvetica', 15))
        self.new_secret_key_label.grid(row=2, column=0, padx=10, pady=(15, 10), sticky=E)
        self.new_secret_key_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.new_secret_key_entry.grid(row=2, column=1, padx=10, pady=(15, 10), sticky=W)

        # Confirm Password Label and Entry
        self.confirm_secret_key_label = Label(self.root, text="Confirm Secret Key:", font=('Helvetica', 15))
        self.confirm_secret_key_label.grid(row=3, column=0, padx=10, pady=(5, 0), sticky=E)
        self.confirm_secret_key_entry = Entry(self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.confirm_secret_key_entry.grid(row=3, column=1, padx=10, pady=(5, 0), sticky=W)

        # Back and Save Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.grid(row=4, column=0, pady=20, columnspan=2)

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11),
                                  command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(10, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11),
                                  command=self.change_secret_key)
        self.save_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

    def new_window(self, _class, title, oid):
        level = Tk()
        _class(level, title, oid)
        self.root.destroy()

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

        conn = sqlite3.connect('SE_Lab_Project9.db')
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


class WinForgotSecretKey:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("360x200+450+150")
        self.root.resizable(width=False, height=False)

        # Instruction Label
        self.instruction_label = Label(self.root, text="Provide Your Email-id\nwhere Secret Key will be shared.",
                                       font=('Helvetica', 13), fg="green")
        self.instruction_label.grid(row=0, column=0, padx=57, pady=(20, 0), columnspan=4)

        # Email Label and Entry
        self.email_label = Label(self.root, text="Email:", font=('Helvetica', 15))
        self.email_label.grid(row=1, column=0, padx=10, pady=20)
        self.email_entry = Entry(self.root, font=('Helvetica', 15))
        self.email_entry.grid(row=1, column=1, padx=(0, 30), pady=20, columnspan=3)

        # Back Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11),
                                  command=self.close_window)
        self.back_button.grid(row=2, column=0, columnspan=2, pady=10, padx=(40, 0), ipadx=10)

        # Send Button
        self.send_button = Button(self.root, text="Send", bg="#90EE90", font=('Helvetica', 11),
                                  command=self.email_check)
        self.send_button.grid(row=2, column=2, columnspan=2, pady=10, padx=(0, 60), ipadx=10)

        # Loading the Environment Variables from .env file
        env_path = Path('../../../openCV_venv/.env')
        load_dotenv(dotenv_path=env_path)

        self.EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        self.EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    def email_check(self):
        messagebox.showinfo("Information", "It may take some time\nPlease Wait!!!", parent=self.root)
        email = self.email_entry.get()

        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()

        query = 'select oid from Users where email_id=?'
        c.execute(query, (email,))

        OID = c.fetchone()

        if OID is None or OID[0] != 1:
            messagebox.showerror("Error", "Incorrect!!! Email-id", parent=self.root)
        else:
            query = 'Select secret_key from Secret_Key where oid=1'
            c.execute(query)

            secret_key = c.fetchone()

            if secret_key is None:
                messagebox.showerror("Error", "Incorrect!!! Email-id", parent=self.root)
            else:
                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)

                        subject = 'Forgot Secret Key: Address Database'
                        body = f'Dear User\n\nPlease find the Secret Key of the Address Database Account\n\nSecret Key: {secret_key[0]}'

                        msg = f'Subject: {subject}\n\n{body}'

                        smtp.sendmail(self.EMAIL_ADDRESS, email, msg)

                        messagebox.showinfo("Information", "Mail has been sent Successfully:)", parent=self.root)

                except Exception:
                    messagebox.showerror("Error", "Please Try Again!!!", parent=self.root)

        conn.commit()
        conn.close()

        self.close_window()

    def close_window(self):
        level = Tk()
        WinChangeSecretKey(level, "Change Secret Key", self.user_oid)
        self.root.destroy()


class WinMachine:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x380+450+110")
        self.root['bg'] = "#90EE90"
        self.root.resizable(width=False, height=False)

        self.head_label = Label(self.root, text="Machine Database", fg="purple", bg='#add8e6', bd=4, relief=GROOVE,
                                font=('Monotype Corsiva', 32, "bold"))
        self.head_label.pack(pady=(0, 10), ipadx=32, ipady=5)

        # Insert Search Update Delete Buttons
        self.but_insert = Button(self.root, text="Insert", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinMachineInsert, "Machine Insert Window", self.user_oid))
        self.but_insert.pack(pady=(15, 0), ipadx=35)
        self.but_search = Button(self.root, text="Search", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinMachineSearch, "Machine Search Window", self.user_oid))
        self.but_search.pack(pady=(20, 0), ipadx=29)
        self.but_update = Button(self.root, text="Update", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinMachineUpdate, "Machine Update Window", self.user_oid))
        self.but_update.pack(pady=(20, 0), ipadx=29)
        self.but_delete = Button(self.root, text="Delete", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinMachineDelete, "Machine Delete Window", self.user_oid))
        self.but_delete.pack(pady=(20, 0), ipadx=32)

        # Back Button
        self.but_back = Button(self.root, text="Back", font=('Helvetica', 10), bg="#add8e6",
                               command=lambda: self.new_window(WinHome, "Home Window", self.user_oid))
        self.but_back.pack(pady=(10, 0), padx=(5, 0), ipadx=5, anchor=W)

        # Add Right Click Pop Up Menu
        self.my_popup_menu = Menu(self.root, tearoff=False)
        # Insert, Search, Update and Delete
        self.my_popup_menu.add_command(label="Insert",
                                       command=lambda: self.new_window(WinMachineInsert, "Machine Insert Window", self.user_oid))
        self.my_popup_menu.add_command(label="Search",
                                       command=lambda: self.new_window(WinMachineSearch, "Machine Search Window", self.user_oid))
        self.my_popup_menu.add_command(label="Update",
                                       command=lambda: self.new_window(WinMachineUpdate, "Machine Update Window", self.user_oid))
        self.my_popup_menu.add_command(label="Delete",
                                       command=lambda: self.new_window(WinMachineDelete, "Machine Delete Window", self.user_oid))
        self.my_popup_menu.add_separator()

        # Back and Exit
        self.my_popup_menu.add_command(label="Back", command=lambda: self.new_window(WinHome, "Home Window", self.user_oid))

        # Binding the Right click Pop Up Menu
        self.root.bind("<Button-3>", self.my_popup)

        # Finding Username for our Status Bar
        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()
        query = 'Select Username from Users where OID=?'
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

    def new_window(self, _class, title, oid):
        level = Tk()
        _class(level, title, oid)
        self.root.destroy()


class WinAdjuster:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x380+450+110")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)

        self.head_label = Label(self.root, text="Adjuster Database", fg="purple", bg='#add8e6', bd=4, relief=GROOVE,
                                font=('Monotype Corsiva', 32, "bold"))
        self.head_label.pack(pady=(0, 10), ipadx=32, ipady=5)

        # Insert Search Update Delete Buttons
        self.but_insert = Button(self.root, text="Insert", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinAdjusterInsert, "Adjuster Insert Window", self.user_oid))
        self.but_insert.pack(pady=(15, 0), ipadx=35)
        self.but_search = Button(self.root, text="Search", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinAdjusterSearch, "Adjuster Search Window", self.user_oid))
        self.but_search.pack(pady=(20, 0), ipadx=29)
        self.but_update = Button(self.root, text="Update", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinAdjusterUpdate, "Adjuster Update Window", self.user_oid))
        self.but_update.pack(pady=(20, 0), ipadx=29)
        self.but_delete = Button(self.root, text="Delete", font=('Helvetica', 15), bg='#fdebd0',
                                 command=lambda: self.new_window(WinAdjusterDelete, "Adjuster Delete Window", self.user_oid))
        self.but_delete.pack(pady=(20, 0), ipadx=32)

        # Back Button
        self.but_back = Button(self.root, text="Back", font=('Helvetica', 10), bg="#add8e6",
                               command=lambda: self.new_window(WinHome, "Home Window", self.user_oid))
        self.but_back.pack(pady=(10, 0), padx=(5, 0), ipadx=5, anchor=W)

        # Add Right Click Pop Up Menu
        self.my_popup_menu = Menu(self.root, tearoff=False)
        # Insert, Search, Update and Delete
        self.my_popup_menu.add_command(label="Insert",
                                       command=lambda: self.new_window(WinAdjusterInsert, "Adjuster Insert Window", self.user_oid))
        self.my_popup_menu.add_command(label="Search",
                                       command=lambda: self.new_window(WinAdjusterSearch, "Adjuster Search Window", self.user_oid))
        self.my_popup_menu.add_command(label="Update",
                                       command=lambda: self.new_window(WinAdjusterUpdate, "Adjuster Update Window", self.user_oid))
        self.my_popup_menu.add_command(label="Delete",
                                       command=lambda: self.new_window(WinAdjusterDelete, "Adjuster Delete Window", self.user_oid))
        self.my_popup_menu.add_separator()

        # Back and Exit
        self.my_popup_menu.add_command(label="Back",
                                       command=lambda: self.new_window(WinHome, "Home Window", self.user_oid))

        # Binding the Right click Pop Up Menu
        self.root.bind("<Button-3>", self.my_popup)

        # Finding Username for our Status Bar
        conn = sqlite3.connect('SE_Lab_Project9.db')
        c = conn.cursor()
        query = 'Select Username from Users where OID=?'
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

    def new_window(self, _class, title, oid):
        level = Tk()
        _class(level, title, oid)
        self.root.destroy()


class WinMachineInsert:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


class WinMachineSearch:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


class WinMachineUpdate:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


class WinMachineDelete:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


class WinAdjusterInsert:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


class WinAdjusterSearch:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


class WinAdjusterUpdate:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


class WinAdjusterDelete:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x360+450+120")
        self.root['bg'] = "#90EE90"
        # self.root.resizable(width=False, height=False)


WinLogin(root, "Login Window")

mainloop()
