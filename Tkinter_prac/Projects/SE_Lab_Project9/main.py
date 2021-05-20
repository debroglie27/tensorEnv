########################################################################################
########################################################################################

# ********** FACTORY SIMULATION PROJECT **********
# Written By: Arijeet De
# Last Updated: 13/05/2021

########################################################################################
########################################################################################

import os
import smtplib
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
from dotenv import load_dotenv
from cryptography.fernet import Fernet

########################################################################################
########################################################################################

# conn = sqlite3.connect('C:/Users/HP/PycharmProjects/tensorEnv/Tkinter_prac/Projects/SE_Lab_Project9/FS_DATABASE.db')
# c = conn.cursor()

# Create Table Machines
# c.execute('''Create table Machines ([Machine_ID] text PRIMARY KEY,
# [Machine_Type] text,
# [MTTF] FLOAT,
# [Status] text)''')

# Dropping a Table Machines
# c.execute('''Drop table Machines''')

# Create Table Adjusters
# c.execute('''Create table Adjusters ([Adjuster_ID] text PRIMARY KEY,
# [First_Name] text,
# [Last_Name] text,
# [Expertise] text,
# [Email_id] text,
# [Status] text)''')

# Dropping a Table Adjusters
# c.execute('''Drop table Adjusters''')

# Create Table Users
# c.execute('''Create table Users ([Username] text PRIMARY KEY,
# [Email_id] text,
# [Password] blob)''')

# Create Table Maintenance
# c.execute('''Create table Maintenance ([Machine_ID] text,
# [Adjuster_ID] text)''')

# Create Table Secret_Key
# c.execute('''Create table Secret_Key ([secret_key] blob)''')

# Encryption Code
# path = Path('C:/Users/M K DE/PycharmProjects/openCV_venv/.env')
# load_dotenv(dotenv_path=path)
# key = os.environ.get('ENCRYPTION_KEY')
# fernet = Fernet(key)
# message = "7777"
# encMessage = fernet.encrypt(message.encode())

# Insert Data values in Users
# query = "Insert Into Users(Username, Email_id, Password) values(?, ?, ?)"
# c.execute(query, ('Mrinal', 'mrinal@gmail.com', encMessage))

# Decryption Code
# path = Path('C:/Users/M K DE/PycharmProjects/openCV_venv/.env')
# load_dotenv(dotenv_path=path)
# key = os.environ.get('ENCRYPTION_KEY')
# fernet = Fernet(key)
# query = "Select Password from Users where OID=1"
# c.execute(query)
# password = c.fetchone()[0]
# decMessage1 = fernet.decrypt(password).decode()

# Fetching Data from Users
# c.execute("Select * from Users")
# record = c.fetchall()

# for rec in record:
#     print(rec)

# Insert secret_key in Secret_Key after Encryption
# path = Path('C:/Users/M K DE/PycharmProjects/openCV_venv/.env')
# load_dotenv(dotenv_path=path)
# key = os.environ.get('ENCRYPTION_KEY')
# fernet = Fernet(key)
# message = "12345"
# encMessage = fernet.encrypt(message.encode())
# query = "Insert Into Secret_Key(secret_key) values(?)"
# c.execute(query, (encMessage,))

# Fetching Data from Secret_Key
# c.execute("Select * from Secret_Key")
# record = c.fetchone()[0]
# print(record)

# Fetching Data from Machines/Adjusters
# query = "Select * from Adjusters"
# c.execute(query)
# record = c.fetchall()
# print(record)

# Adding column to Machines Table
# query = "Alter table Machines add column nfails INTEGER"
# c.execute(query)
# query = "Alter table Machines rename column nfails to nFails"
# c.execute(query)

# Making the newly added column in Machines filled with zeros
# query = "Update Machines set nfails=0 where exists (select oid from Machines)"
# c.execute(query)

# Adding column to Adjusters Table
# query = "Alter table Adjusters add column nfixes INTEGER"
# c.execute(query)
# query = "Alter table Adjusters rename column nfixes to nFixes"
# c.execute(query)

# Making the newly added column in Adjusters filled with zeros
# query = "Update Adjusters set nfixes=0 where exists (select oid from Adjusters)"
# c.execute(query)

# conn.commit()
# conn.close()

#######################################################################################
#######################################################################################

# ADMIN: Arijeet
# Secret Key: 12345

# Users = ['Arijeet', 'Aushish', 'Aravind', 'Anwesha', 'Ankit', 'Gunadeep', 'Mrinal']
# Password = ['1234', '1999', '4321', '5555', '9876', '6969', '7777']

########################################################################################
########################################################################################


# Window for Login
class WinLogin:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("380x230+450+150")
        self.root.resizable(width=False, height=False)

        # Bullet Symbol
        self.bullet_symbol = "\u2022"

        # Username Label and Entry
        self.username_label = Label(self.root, text="Username:", font=('Helvetica', 15))
        self.username_label.grid(row=0, column=0, padx=(15, 10), pady=(30, 0), sticky=E)
        self.username_entry = Entry(self.root, fg="#BFBFBF", font=('Helvetica', 15),
                                    validate="focusin", validatecommand=lambda: self.placeholder_vanish(0))
        self.username_entry.grid(row=0, column=1, padx=10, pady=(30, 0), columnspan=3)

        # Password Label and Entry
        self.password_label = Label(self.root, text="Password:", font=('Helvetica', 15))
        self.password_label.grid(row=1, column=0, padx=(15, 10), pady=10, sticky=E)
        self.password_entry = Entry(self.root, fg="#BFBFBF", font=('Helvetica', 15),
                                    validate="focusin", validatecommand=lambda: self.placeholder_vanish(1))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

        # Login Button
        self.login_button = Button(self.root, text="Login", bg="#90EE90", font=('Helvetica', 11), command=self.login_check)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20, padx=(25, 0), ipadx=6)

        # SignUp Button
        self.signup_button = Button(self.root, text="SignUp", bg="#add8e6", font=('Helvetica', 11),
                                    command=lambda: self.forgot_signup_window(WinSignup, "SignUp Window"))
        self.signup_button.grid(row=2, column=2, columnspan=2, pady=20, padx=(0, 50), ipadx=6)

        # Forgot Password Button
        self.forgot_pass_button = Button(self.root, text="Forgot Password?", fg="blue", relief=FLAT,
                                         command=lambda: self.forgot_signup_window(WinForgotPass, "Forgot Password Window"))
        self.forgot_pass_button.grid(row=3, column=1, padx=(0, 30), columnspan=2)

        # Placeholder for our Entry Boxes and also giving a message to distinguish
        self.username_entry.insert(0, "Username")
        self.password_entry.insert(0, "Password")

        # Loading our .env file
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        # Getting the ENCRYPTION_KEY
        key = os.environ.get('ENCRYPTION_KEY')
        self.fernet = Fernet(key)

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
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            # Finding Password and OID for the given Username
            query = 'Select Password, oid from Users where Username=?'
            c.execute(query, (username,))

            en_user_password, oid = c.fetchone()
            # Decrypting user password
            de_user_password = self.fernet.decrypt(en_user_password).decode()

            conn.commit()
            conn.close()

            # Checking whether password provided matched
            if de_user_password == password:
                self.new_window(WinHome, "Home Window", oid)
            else:
                messagebox.showerror(
                    "Error", "Incorrect!!! Username or Password", parent=self.root)

        except Exception:
            messagebox.showerror(
                "Error", "Incorrect!!! Username or Password", parent=self.root)

    def forgot_signup_window(self, _class, title):
        level = Tk()
        _class(level, title)
        self.root.destroy()

    def new_window(self, _class, title, oid):
        level = Tk()
        _class(level, title, oid)
        self.root.destroy()


# Window for Forgot Password
class WinForgotPass:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("360x200+450+150")
        self.root.resizable(width=False, height=False)

        # Instruction Label
        self.instruction_label = Label(
            self.root, text="Provide Your Email-id\nwhere password will be shared.", font=('Helvetica', 13), fg="green")
        self.instruction_label.grid(
            row=0, column=0, padx=65, pady=(20, 0), columnspan=4)

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
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        self.EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        self.EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

        # Getting the ENCRYPTION_KEY
        key = os.environ.get('ENCRYPTION_KEY')
        self.fernet = Fernet(key)

    def email_check(self):
        # Displaying Message Informing that it will take time
        messagebox.showinfo(
            "Information", "It may take some time\nPlease Wait!!!", parent=self.root)
        email = self.email_entry.get()

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            # Finding Password for the given Email_id
            query = 'Select Password from Users where Email_id=?'
            c.execute(query, (email,))

            user_password = c.fetchone()

            conn.commit()
            conn.close()

            if user_password is None:
                messagebox.showerror(
                    "Error", "Incorrect!!! Email-id", parent=self.root)
            else:
                try:
                    # Decrypting user password
                    user_password = self.fernet.decrypt(user_password[0]).decode()

                    # Sending Email Code
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)

                        subject = 'Forgot Password: Factory Simulation Software'
                        body = f'Dear User\n\nPlease find your Password of your Factory Simulation Account\n\nPassword: {user_password}'

                        msg = f'Subject: {subject}\n\n{body}'

                        smtp.sendmail(self.EMAIL_ADDRESS, email, msg)

                        # Message to inform that Email has been sent
                        messagebox.showinfo(
                            "Information", "Mail has been sent Successfully:)", parent=self.root)
                        self.close_window()

                except Exception:
                    messagebox.showerror(
                        "Error", "Unable to send mail\nPlease Try Again!!!", parent=self.root)

        except Exception:
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)

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
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11),
                                  command=self.close_window)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=20, padx=(30, 0), ipadx=4)

        # Submit Button
        self.submit_button = Button(self.root, text="Submit", bg="#90EE90", font=('Helvetica', 11),
                                    command=self.signup_check)
        self.submit_button.grid(row=4, column=2, columnspan=2, pady=20, padx=(0, 60), ipadx=4)

        # Loading the Environment Variables from .env file
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        # Getting the ENCRYPTION_KEY
        key = os.environ.get('ENCRYPTION_KEY')
        self.fernet = Fernet(key)

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

        conn = sqlite3.connect(database_file_path)
        c = conn.cursor()

        # Finding Secret Key
        c.execute("Select secret_key from Secret_Key")

        encrypted_secret_key = c.fetchone()[0]
        # Decrypting Secret Key
        decrypted_secret_key = self.fernet.decrypt(encrypted_secret_key).decode()

        if not secret_key == decrypted_secret_key:
            messagebox.showerror(
                "Error", "Secret Key Incorrect!!!", parent=self.root)
        else:
            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                # Encrypting user password
                password = self.fernet.encrypt(password.encode())

                # Inserting Details of New User
                query = "Insert Into users(Username, Email_id, Password) values(?, ?, ?)"
                c.execute(query, (username, email_id, password))
                conn.commit()

                # Displaying message informing that account was added successfully
                messagebox.showinfo(
                    "Information", "Account Successfully Added!!!", parent=self.root)

                conn.commit()
                conn.close()

                self.close_window()
            except Exception:
                messagebox.showinfo(
                    "Information", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinLogin(level, "Login Window")
        self.root.destroy()


########################################################################################
########################################################################################

# Window for Home
class WinHome:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x340+450+130")
        self.root['bg'] = "#90EE90"
        self.root.resizable(width=False, height=False)

        # Heading Label
        self.head_label = Label(self.root, text="Factory Simulation", fg="purple",
                                bg='#add8e6', bd=4, relief=GROOVE, font=('Monotype Corsiva', 32, "bold"))
        self.head_label.pack(pady=(0, 10), ipadx=28, ipady=5)

        # Machine, Adjuster and Maintenance Window Button
        self.but_machine = Button(self.root, text="Machine", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinMachine, "Machine Window", self.user_oid))
        self.but_machine.pack(pady=(32, 0), ipadx=32)
        self.but_adjuster = Button(self.root, text="Adjuster", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinAdjuster, "Adjuster Window", self.user_oid))
        self.but_adjuster.pack(pady=(26, 0), ipadx=32)
        self.but_maintenance = Button(self.root, text="Maintenance", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinMaintenance, "Maintenance Window", self.user_oid))
        self.but_maintenance.pack(pady=(26, 0), ipadx=12)

        # Create Menu
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)

        # Add File Menu
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        # Add File Menu Items
        self.file_menu.add_command(label="Machine", command=lambda: self.new_window(WinMachine, "Machine Window", self.user_oid))
        self.file_menu.add_command(label="Adjuster", command=lambda: self.new_window(WinAdjuster, "Adjuster Window", self.user_oid))
        self.file_menu.add_command(label="Maintenance", command=lambda: self.new_window(WinMaintenance, "Maintenance Window", self.user_oid))
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
        self.my_popup_menu.add_command(label="Machine", command=lambda: self.new_window(
            WinMachine, "Machine Window", self.user_oid))
        self.my_popup_menu.add_command(label="Adjuster", command=lambda: self.new_window(WinAdjuster, "Adjuster Window", self.user_oid))
        self.my_popup_menu.add_command(label="Maintenance", command=lambda: self.new_window(WinMaintenance, "Maintenance Window", self.user_oid))
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

        try:
            # Finding Username for our Status Bar
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()
            query = 'Select Username from Users where OID=?'
            c.execute(query, (self.user_oid,))

            username = c.fetchone()[0]

            conn.commit()
            conn.close()
        except Exception:
            username = ''
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)

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


# Window for Displaying User Details
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
        self.change_button1 = Button(self.root, text="Change", font=('Helvetica', 10), bg="orange", command=lambda: self.change_entry(0))
        self.change_button1.grid(row=0, column=2, padx=5, pady=(30, 0))
        self.change_button2 = Button(self.root, text="Change", font=('Helvetica', 10), bg="orange", command=lambda: self.change_entry(1))
        self.change_button2.grid(row=1, column=2, padx=5, pady=20)

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            # Finding Details of User
            query = 'Select Username, Email_id from Users where OID=?'
            c.execute(query, (self.user_oid,))

            username, email = c.fetchone()

            conn.commit()
            conn.close()
        except Exception:
            username = ''
            email = ''
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)

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
        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            # Updating the database with new values
            query = "update Users set Username = ?, Email_id = ? where OID = ?"
            e = (self.username_entry.get(), self.email_entry.get(), self.user_oid)
            c.execute(query, e)

            conn.commit()
            conn.close()

            # Message Informing Successful Saving
            messagebox.showinfo(
                "Information", "Successfully Saved", parent=self.root)
            self.close_window()
        except Exception:
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)


# Window for Changing Password
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
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11), command=self.change_password)
        self.save_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

        # Loading the Environment Variables from .env file
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        # Getting the ENCRYPTION_KEY
        key = os.environ.get('ENCRYPTION_KEY')
        self.fernet = Fernet(key)

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

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            # Finding password for the given user
            query = "Select Password from Users where oid=?"
            c.execute(query, (self.user_oid,))

            encrypted_password = c.fetchone()[0]
            # Decrypting password
            decrypted_password = self.fernet.decrypt(encrypted_password).decode()

            if decrypted_password != current_password:
                messagebox.showerror(
                    "Error", "Wrong Current Password!!!", parent=self.root)
            else:
                if new_password != confirm_password:
                    messagebox.showerror(
                        "Error", "Confirm Password is not same\nas New Password!!!", parent=self.root)
                else:
                    # Encrypting user password
                    confirm_password = self.fernet.encrypt(confirm_password.encode())

                    query = "update Users set Password = ? where OID = ?"
                    c.execute(query, (confirm_password, self.user_oid))

                    conn.commit()

                    messagebox.showinfo(
                        "Information", "Password Changed Successfully!!!", parent=self.root)
    
            conn.commit()
            conn.close()
            
            self.close_window()
        except Exception:
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)


# Window for Displaying All User Details
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
        self.my_tree = ttk.Treeview(
            self.tree_frame, height=6, yscrollcommand=self.tree_scroll.set)
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

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            c.execute("Select OID, Username, Email_id from Users where oid <> 1")
            records = c.fetchall()

            conn.commit()
            conn.close()
        except Exception:
            records = []
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)

        # Resetting the Count
        self.count = 0

        for record in records:
            if self.count % 2 == 0:
                self.my_tree.insert(
                    parent='', index='end', iid=self.count, text="", values=record, tags=("evenrow",))
            else:
                self.my_tree.insert(
                    parent='', index='end', iid=self.count, text="", values=record, tags=("oddrow",))
            self.count += 1

        # Back and Remove Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=(20, 10))

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, pady=10, padx=(5, 45), ipadx=5)

        # Remove Button
        self.remove_button = Button(self.button_frame, text="Remove", bg="orange", font=('Helvetica', 11),
                                    command=self.remove_user)
        self.remove_button.grid(
            row=0, column=1, pady=10, padx=(25, 0), ipadx=5)

    def close_window(self):
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()

    def remove_user(self):
        if self.my_tree.focus():
            for record in self.my_tree.selection():
                # Getting the OID from the record
                oid = self.my_tree.item(record)['values'][0]

                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()
                try:
                    c.execute("Delete from Users where oid=?", (oid,))

                    conn.commit()
                    conn.close()
                except Exception:
                    messagebox.showwarning(
                        "Warning", "Please Try Again!!!", parent=self.root)
                # removing the record from the treeview
                self.my_tree.delete(record)

                messagebox.showinfo("Information", "Successfully Removed!")
        else:
            messagebox.showinfo(
                "Information", "Please select a record to remove!!!")


# Window for Changing Secret Key
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
        self.current_secret_key_label = Label(
            self.root, text="Current Secret Key:", font=('Helvetica', 15))
        self.current_secret_key_label.grid(
            row=0, column=0, padx=10, pady=(30, 10), sticky=E)
        self.current_secret_key_entry = Entry(
            self.root, show=self.bullet_symbol, font=('Helvetica', 15))
        self.current_secret_key_entry.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky=W)

        # Forgot Secret Key Button
        self.forgot_secret_key_button = Button(self.root, text="Forgot Secret Key?", fg="blue", relief=FLAT,
                                               command=lambda: self.new_window(WinForgotSecretKey, "Forgot Secret Key Window", self.user_oid))
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
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(10, 40), ipadx=5)

        # Save Button
        self.save_button = Button(self.button_frame, text="Save", bg="#90EE90", font=('Helvetica', 11), command=self.change_secret_key)
        self.save_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

        # Loading the Environment Variables from .env file
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        # Getting the ENCRYPTION_KEY
        key = os.environ.get('ENCRYPTION_KEY')
        self.fernet = Fernet(key)

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

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            c.execute("Select secret_key from Secret_Key")

            encrypted_secret_key = c.fetchone()[0]
            # Decrypting Secret Key
            decrypted_secret_key = self.fernet.decrypt(encrypted_secret_key).decode()

            if decrypted_secret_key != current_secret_key:
                messagebox.showerror(
                    "Error", "Wrong Current Secret Key!!!", parent=self.root)
                return
            else:
                if new_secret_key != confirm_secret_key:
                    messagebox.showerror(
                        "Error", "Confirm Secret Key is not same\nas New Secret Key!!!", parent=self.root)
                    return
                else:
                    # Encrypting user password
                    confirm_secret_key = self.fernet.encrypt(confirm_secret_key.encode())

                    query = "update Secret_Key set secret_key = ? where OID = 1"
                    c.execute(query, (confirm_secret_key,))

                    messagebox.showinfo(
                        "Information", "Secret Key Changed Successfully!!!", parent=self.root)

            conn.commit()
            conn.close()

            self.close_window()
        except Exception:
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)


# Window for Forgetting Secret Key
class WinForgotSecretKey:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("360x200+450+150")
        self.root.resizable(width=False, height=False)

        # Instruction Label
        self.instruction_label = Label(self.root, text="Provide Your Email-id\nwhere Secret Key will be shared.", font=('Helvetica', 13), fg="green")
        self.instruction_label.grid(row=0, column=0, padx=57, pady=(20, 0), columnspan=4)

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
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        self.EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        self.EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

        # Getting the ENCRYPTION_KEY
        key = os.environ.get('ENCRYPTION_KEY')
        self.fernet = Fernet(key)

    def email_check(self):
        messagebox.showinfo(
            "Information", "It may take some time\nPlease Wait!!!", parent=self.root)
        email = self.email_entry.get()

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            query = 'select oid from Users where email_id=?'
            c.execute(query, (email,))

            oid = c.fetchone()

            if oid is None or oid[0] != 1:
                messagebox.showerror(
                    "Error", "Incorrect!!! Email-id", parent=self.root)
            else:
                query = 'Select secret_key from Secret_Key where oid=1'
                c.execute(query)

                secret_key = c.fetchone()

                if secret_key is None:
                    messagebox.showerror(
                        "Error", "Incorrect!!! Email-id", parent=self.root)
                else:
                    try:
                        # Decrypting Secret Key
                        decrypted_secret_key = self.fernet.decrypt(secret_key[0]).decode()

                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)

                            subject = 'Forgot Secret Key: Factory Simulation Software'
                            body = f'Dear User\n\nPlease find the Secret Key of the Address Database Account\n\nSecret Key: {decrypted_secret_key}'

                            msg = f'Subject: {subject}\n\n{body}'

                            smtp.sendmail(self.EMAIL_ADDRESS, email, msg)

                            messagebox.showinfo(
                                "Information", "Mail has been sent Successfully:)", parent=self.root)
                            self.close_window()
                    except Exception:
                        messagebox.showerror(
                            "Error", "Unable to send mail\nPlease Try Again!!!", parent=self.root)

            conn.commit()
            conn.close()
        except Exception:
            messagebox.showwarning("Warning", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinChangeSecretKey(level, "Change Secret Key", self.user_oid)
        self.root.destroy()


########################################################################################
########################################################################################

# Window for Machine Database
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
        self.my_popup_menu.add_command(label="Insert", command=lambda: self.new_window(WinMachineInsert, "Machine Insert Window", self.user_oid))
        self.my_popup_menu.add_command(label="Search", command=lambda: self.new_window(WinMachineSearch, "Machine Search Window", self.user_oid))
        self.my_popup_menu.add_command(label="Update", command=lambda: self.new_window(WinMachineUpdate, "Machine Update Window", self.user_oid))
        self.my_popup_menu.add_command(label="Delete", command=lambda: self.new_window(WinMachineDelete, "Machine Delete Window", self.user_oid))
        self.my_popup_menu.add_separator()

        # Back
        self.my_popup_menu.add_command(label="Back", command=lambda: self.new_window(
            WinHome, "Home Window", self.user_oid))

        # Binding the Right click Pop Up Menu
        self.root.bind("<Button-3>", self.my_popup)

        try:
            # Finding Username for our Status Bar
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            query = 'Select Username from Users where OID=?'
            c.execute(query, (self.user_oid,))

            username = c.fetchone()[0]

            conn.commit()
            conn.close()
        except Exception:
            username = ''
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)

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


# Window for Adjuster Database
class WinAdjuster:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("377x380+450+110")
        self.root['bg'] = "#90EE90"
        self.root.resizable(width=False, height=False)

        self.head_label = Label(self.root, text="Adjuster Database", fg="purple", bg='#add8e6', bd=4, relief=GROOVE, font=('Monotype Corsiva', 32, "bold"))
        self.head_label.pack(pady=(0, 10), ipadx=32, ipady=5)

        # Insert Search Update Delete Buttons
        self.but_insert = Button(self.root, text="Insert", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinAdjusterInsert, "Adjuster Insert Window", self.user_oid))
        self.but_insert.pack(pady=(15, 0), ipadx=35)
        self.but_search = Button(self.root, text="Search", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinAdjusterSearch, "Adjuster Search Window", self.user_oid))
        self.but_search.pack(pady=(20, 0), ipadx=29)
        self.but_update = Button(self.root, text="Update", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinAdjusterUpdate, "Adjuster Update Window", self.user_oid))
        self.but_update.pack(pady=(20, 0), ipadx=29)
        self.but_delete = Button(self.root, text="Delete", font=('Helvetica', 15), bg='#fdebd0', command=lambda: self.new_window(WinAdjusterDelete, "Adjuster Delete Window", self.user_oid))
        self.but_delete.pack(pady=(20, 0), ipadx=32)

        # Back Button
        self.but_back = Button(self.root, text="Back", font=('Helvetica', 10), bg="#add8e6", command=lambda: self.new_window(WinHome, "Home Window", self.user_oid))
        self.but_back.pack(pady=(10, 0), padx=(5, 0), ipadx=5, anchor=W)

        # Add Right Click Pop Up Menu
        self.my_popup_menu = Menu(self.root, tearoff=False)
        # Insert, Search, Update and Delete
        self.my_popup_menu.add_command(label="Insert", command=lambda: self.new_window(WinAdjusterInsert, "Adjuster Insert Window", self.user_oid))
        self.my_popup_menu.add_command(label="Search", command=lambda: self.new_window(WinAdjusterSearch, "Adjuster Search Window", self.user_oid))
        self.my_popup_menu.add_command(label="Update", command=lambda: self.new_window(WinAdjusterUpdate, "Adjuster Update Window", self.user_oid))
        self.my_popup_menu.add_command(label="Delete", command=lambda: self.new_window(WinAdjusterDelete, "Adjuster Delete Window", self.user_oid))
        self.my_popup_menu.add_separator()

        # Back and Exit
        self.my_popup_menu.add_command(label="Back", command=lambda: self.new_window(WinHome, "Home Window", self.user_oid))

        # Binding the Right click Pop Up Menu
        self.root.bind("<Button-3>", self.my_popup)

        # Finding Username for our Status Bar
        conn = sqlite3.connect(database_file_path)
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


# Window for Maintenance Database
class WinMaintenance:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("320x250+480+150")
        self.root.resizable(width=False, height=False)

        # Create TreeView Frame
        self.tree_frame = Frame(self.root)
        self.tree_frame.pack(pady=(20, 0), padx=10)

        # TreeView ScrollBar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        # Create TreeView
        self.my_tree = ttk.Treeview(
            self.tree_frame, height=6, yscrollcommand=self.tree_scroll.set)
        self.my_tree.pack()

        # Configure ScrollBar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Define our columns
        self.my_tree['columns'] = ("OID", "Machine_ID", "Adjuster_ID")

        # Format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("OID", anchor=CENTER, width=40)
        self.my_tree.column("Machine_ID", anchor=CENTER, width=110)
        self.my_tree.column("Adjuster_ID", anchor=CENTER, width=110)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=CENTER)
        self.my_tree.heading("OID", text="OID", anchor=CENTER)
        self.my_tree.heading("Machine_ID", text="Machine_ID", anchor=CENTER)
        self.my_tree.heading("Adjuster_ID", text="Adjuster_ID", anchor=CENTER)

        # Count Variable for number of records
        self.count = 0

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            c.execute("Select OID, Machine_ID, Adjuster_ID from Maintenance")
            records = c.fetchall()

            conn.commit()
            conn.close()
        except Exception:
            records = []
            messagebox.showwarning("Warning", "Please Try Again!!!", parent=self.root)

        # Resetting the Count
        self.count = 0

        for record in records:
            self.my_tree.insert(parent='', index='end',
                                iid=self.count, text="", values=record)
            self.count += 1

        # Back Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.pack(pady=(25, 0), ipadx=10)

    def close_window(self):
        level = Tk()
        WinHome(level, "Home Window", self.user_oid)
        self.root.destroy()


########################################################################################
########################################################################################

# Window for Inserting into Machine Table
class WinMachineInsert:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("420x235+440+150")
        self.root.resizable(width=False, height=False)

        # All Entry Boxes
        self.machine_id = Entry(self.root, width=20, font=('Helvetica', 15))
        self.machine_id.grid(row=0, column=1, pady=(20, 8), padx=(20, 0))
        self.machine_type = Entry(self.root, width=20, font=('Helvetica', 15))
        self.machine_type.grid(row=1, column=1, pady=8, padx=(20, 0))
        self.mttf = Entry(self.root, width=20, font=('Helvetica', 15))
        self.mttf.grid(row=2, column=1, pady=8, padx=(20, 0))

        # All Labels
        self.machine_id_label = Label(self.root, text="Machine ID:", font=('Helvetica', 15))
        self.machine_id_label.grid(row=0, column=0, padx=(16, 0), pady=(20, 8), sticky=E)
        self.machine_type_label = Label(self.root, text="Machine Type:", font=('Helvetica', 15))
        self.machine_type_label.grid(row=1, column=0, padx=(16, 0), pady=8, sticky=E)
        self.mttf_label = Label(self.root, text="MTTF:", font=('Helvetica', 15))
        self.mttf_label.grid(row=2, column=0, padx=(16, 0), pady=8, sticky=E)

        # Back and Submit Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.grid(row=3, column=0, pady=10, columnspan=2)

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11),
                                  command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Submit Button
        self.submit_button = Button(self.button_frame, text="Submit", bg="#90EE90", font=('Helvetica', 11),
                                    command=self.submit)
        self.submit_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

    def submit(self):
        # If any of the entry boxes not filled then warning message shown
        if self.machine_id.get() == '' or self.machine_type.get() == '' or self.mttf.get() == '':
            messagebox.showwarning(
                "Warning", "Please Fill ALL The Details!", parent=self.root)
        else:
            # Check whether mttf was provided as a Real Number
            try:
                float(self.mttf.get())
            except Exception:
                messagebox.showwarning(
                    "Warning", "MTTF should be a Real Number!", parent=self.root)
                return

            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                # Default values when inserting
                status = "Working"
                nfails = 0

                query = "Insert Into Machines(Machine_ID, Machine_Type, MTTF, Status, nFails) values(?, ?, ?, ?, ?)"
                
                c.execute(query, (self.machine_id.get(), self.machine_type.get(), self.mttf.get(), status, nfails))

                # Clearing the originally filled values
                self.machine_id.delete(0, END)
                self.machine_type.delete(0, END)
                self.mttf.delete(0, END)

                # Displaying confirmation message informing Successful Insertion
                messagebox.showinfo(
                    "Information", "Successfully Inserted", parent=self.root)

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning(
                    "Warning", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinMachine(level, "Machine Window", self.user_oid)
        self.root.destroy()


# Window for Searching the Machine Table
class WinMachineSearch:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("510x385+400+120")
        self.root.resizable(width=False, height=False)

        # Our Search Label and Search Entry
        self.search_label = Label(
            self.root, text="Search:", anchor=E, font=('Helvetica', 15))
        self.search_label.grid(row=0, column=0, padx=(5, 0), pady=20)
        self.search_Entry = Entry(self.root, width=15, font=('Helvetica', 15))
        self.search_Entry.grid(row=0, column=1, padx=(0, 20), pady=20)

        # Drop Down Box for Search Type
        self.drop = ttk.Combobox(self.root, value=['Search by...', 'OID', 'Machine_ID', 'Machine_Type', 'MTTF', 'Status', "nFails"],
                                 font=('Helvetica', 11))
        self.drop.current(0)
        self.drop.grid(row=0, column=2, padx=(0, 27))

        # Buttons (Back, Show, Show_All)
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(55, 0), pady=15, ipadx=5)
        self.search_button = Button(self.root, text="Search", bg="#90EE90", font=('Helvetica', 11), command=lambda: self.show(1))
        self.search_button.grid(row=1, column=1, pady=15, ipadx=5)
        self.show_all_button = Button(self.root, text="Show All", bg="orange", font=('Helvetica', 11), command=lambda: self.show(0))
        self.show_all_button.grid(row=1, column=2, padx=(15, 20), pady=15, ipadx=5)

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
        self.my_tree['columns'] = ("OID", "Machine_ID", "Machine_Type", "MTTF", "Status", "nFails")

        # Format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("OID", anchor=CENTER, width=30)
        self.my_tree.column("Machine_ID", anchor=CENTER, width=80)
        self.my_tree.column("Machine_Type", anchor=CENTER, width=120)
        self.my_tree.column("MTTF", anchor=CENTER, width=70)
        self.my_tree.column("Status", anchor=CENTER, width=80)
        self.my_tree.column("nFails", anchor=CENTER, width=50)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=CENTER)
        self.my_tree.heading("OID", text="OID", anchor=CENTER)
        self.my_tree.heading("Machine_ID", text="Machine_ID", anchor=CENTER)
        self.my_tree.heading("Machine_Type", text="Machine_Type", anchor=CENTER)
        self.my_tree.heading("MTTF", text="MTTF", anchor=CENTER)
        self.my_tree.heading("Status", text="Status", anchor=CENTER)
        self.my_tree.heading("nFails", text="nFails", anchor=CENTER)

        # Count Variable for number of records
        self.count = 0

        # Change Status Button
        self.change_status_button = Button(self.root, text="Change Status", bg="#f2f547", font=('Helvetica', 11), command=self.change_status)
        self.change_status_button.grid(row=3, column=0, columnspan=3, ipadx=5)

    def change_status(self):
        if self.my_tree.selection():
            # Grab the Record number
            selected = self.my_tree.focus()
            # Grab the values of the record
            values = self.my_tree.item(selected, "values")

            # Finding the OID and nFails value for that record
            oid = values[0]
            nfails = int(values[5])

            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                if values[4] == "U/M":
                    return
                else:
                    # Asking for confirmation whether user wants to change status or not
                    user_ans = messagebox.askyesno(
                                    "Confirmation", "Do you want to Change Status?", parent=self.root)
                    # If User pressed 'No' nothing will happen
                    if not user_ans:
                        return

                    if values[4] == "Working":
                        status = "Failure"
                        nfails += 1

                        query = "Select OID, Machine_ID, Machine_Type from Machines where OID = ?"
                        c.execute(query, (oid,))
                        machine_failure_list.append(c.fetchone())
                    else:
                        status = "Working"
                        nfails -= 1

                        query = "Select OID, Machine_ID, Machine_Type from Machines where OID = ?"
                        c.execute(query, (oid,))
                        machine_failure_list.pop(machine_failure_list.index(c.fetchone()))

                # Updating Machine status and nFails
                query = "Update Machines set Status=?, nFails=? where OID=?"
                c.execute(query, (status, nfails, oid))

                # Update the Treeview
                self.my_tree.item(selected, text="", values=(values[0], values[1], values[2], values[3], status, nfails))

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning(
                    "Warning", "Please Try Again!!!", parent=self.root)

    def show(self, a):
        # Whether user has provided value to search_entry box and
        # User clicked search button
        if self.search_Entry.get() == "" and a == 1:
            messagebox.showwarning(
                "Warning", "Please Provide the Value to be Searched", parent=self.root)
            return

        # Whether User has chosen some Search by value
        selection = self.drop.get()
        if selection == 'Search by...' and a == 1:
            messagebox.showwarning(
                "Warning", "Please Select an Option to be Searched!!!", parent=self.root)
            return

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            # a->0 then show_all button was clicked
            # a->1 then search button was clicked
            if a == 0:
                c.execute("Select OID, * from Machines")
            else:
                query = "select OID, * from Machines where " + selection + " LIKE ?"
                value = '%' + self.search_Entry.get() + '%'
                c.execute(query, (value,))

            records = c.fetchall()

            conn.commit()
            conn.close()
        except Exception:
            records = []
            messagebox.showwarning(
                "Warning", "Please Try Again!!!", parent=self.root)

        # Removing the Preexisting Records(if any)
        for rec in self.my_tree.get_children():
            self.my_tree.delete(rec)

        # Resetting the Count
        self.count = 0

        if records:
            for record in records:
                self.my_tree.insert(parent='', index='end',
                                    iid=self.count, text="", values=record)
                self.count += 1
        else:
            messagebox.showinfo(
                "Information", "No Record Found!!!", parent=self.root)

        # Clearing the Entry Box and Resetting the Drop Down Box
        self.search_Entry.delete(0, END)
        self.drop.current(0)

    def close_window(self):
        level = Tk()
        WinMachine(level, "Machine Window", self.user_oid)
        self.root.destroy()


# Window for Updating the Machine Table
class WinMachineUpdate:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("400x330+440+120")
        self.root.resizable(width=False, height=False)

        # Select Label and Entry Box
        self.select_label = Label(
            self.root, text="Select OID:", anchor=E, font=('Helvetica', 15))
        self.select_label.grid(row=0, column=0, padx=(
            5, 25), pady=(20, 10), ipadx=18)
        self.select_Entry = Entry(self.root, width=15, font=('Helvetica', 15))
        self.select_Entry.grid(row=0, column=1, padx=(0, 40), pady=(20, 10))

        # Back and Show Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(
            90, 0), pady=(10, 30), ipadx=6)
        self.show_button = Button(self.root, text="Show", bg="orange", font=('Helvetica', 11), command=self.display)
        self.show_button.grid(row=1, column=1, padx=(
            0, 60), pady=(10, 30), ipadx=6)

        # Label and Entry Frame
        self.my_frame = Frame(self.root)
        self.my_frame.grid(row=2, column=0, columnspan=2)

        # All Entry Boxes
        self.machine_id = Entry(self.my_frame, width=20,
                                font=('Helvetica', 15))
        self.machine_id.grid(row=0, column=1, pady=5)
        self.machine_type = Entry(
            self.my_frame, width=20, font=('Helvetica', 15))
        self.machine_type.grid(row=1, column=1, pady=5)
        self.mttf = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.mttf.grid(row=2, column=1, pady=5)

        # All Labels
        self.machine_id_label = Label(self.my_frame, text="Machine ID:", font=('Helvetica', 15))
        self.machine_id_label.grid(row=0, column=0, padx=(7, 20), pady=5, sticky=E)
        self.machine_type_label = Label(self.my_frame, text="Machine Type:", font=('Helvetica', 15))
        self.machine_type_label.grid(row=1, column=0, padx=(7, 20), pady=5, sticky=E)
        self.mttf_label = Label(self.my_frame, text="MTTF:", font=('Helvetica', 15))
        self.mttf_label.grid(row=2, column=0, padx=(7, 20), pady=5, sticky=E)

        # Update Button
        self.update_button = Button(self.root, text="Update", bg="#90EE90", font=('Helvetica', 11), command=self.update)
        self.update_button.grid(row=3, column=0, pady=25, ipadx=10, columnspan=2)

    def display(self):
        # Clearing the Entry Boxes
        self.machine_id.delete(0, END)
        self.machine_type.delete(0, END)
        self.mttf.delete(0, END)

        # Whether select_entry was filled
        if self.select_Entry.get() == '':
            messagebox.showwarning(
                "Warning", "Please Select an ID!", parent=self.root)
        else:
            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                # Fetching Machine data for corressponding OID provided
                c.execute("Select * from Machines where OID=?", self.select_Entry.get())
                record = c.fetchone()

                # Whether no record was found
                if not record:
                    messagebox.showinfo(
                        "Information", "No Record Found!", parent=self.root)
                else:
                    # Inserting the fetched data into entry boxes
                    self.machine_id.insert(0, record[0])
                    self.machine_type.insert(0, record[1])
                    self.mttf.insert(0, record[2])

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning(
                    "Warning", "Please Try Again!!!", parent=self.root)

    def update(self):
        if self.select_Entry.get() == '':
            messagebox.showwarning(
                "Warning", "Please Select an OID!", parent=self.root)
        elif self.machine_id.get() == self.machine_type.get() == self.mttf.get() == '':
            messagebox.showwarning(
                "Warning", "Please Fill The Details!", parent=self.root)
        else:
            # Check whether mttf was provided as a Real Number
            try:
                float(self.mttf.get())
            except Exception:
                messagebox.showwarning(
                    "Warning", "MTTF should be a Real Number!", parent=self.root)
                return

            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                query = "update Machines set Machine_ID = ?, Machine_Type = ?, mttf = ? where OID = ?"
                e = (self.machine_id.get(), self.machine_type.get(), self.mttf.get(), self.select_Entry.get())
                c.execute(query, e)

                self.machine_id.delete(0, END)
                self.machine_type.delete(0, END)
                self.mttf.delete(0, END)
                self.select_Entry.delete(0, END)

                messagebox.showinfo(
                    "Information", "Successfully Updated", parent=self.root)

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning(
                    "Warning", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinMachine(level, "Machine Window", self.user_oid)
        self.root.destroy()


# Window for Deleting from Machine Table
class WinMachineDelete:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("400x160+450+150")
        self.root.resizable(width=False, height=False)

        # Select Label and Select Entry
        self.select_label = Label(self.root, text="Select MID:", font=('Helvetica', 15), anchor=E)
        self.select_label.grid(row=0, column=0, padx=(10, 38), pady=(20, 10), ipadx=10)
        self.select_Entry = Entry(self.root, width=17, font=('Helvetica', 15))
        self.select_Entry.grid(row=0, column=1, padx=(0, 40), pady=(20, 10))

        # Back and Delete Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(90, 0), pady=30, ipadx=10)
        self.del_button = Button(self.root, text="Delete", bg="orange", font=('Helvetica', 11), command=self.delete_record)
        self.del_button.grid(row=1, column=1, padx=(0, 50), pady=30, ipadx=10)

    def delete_record(self):
        # Whether value for select_entry was provided
        if self.select_Entry.get() == '':
            messagebox.showwarning(
                "Warning", "Please Select a Machine_ID!", parent=self.root)
        else:
            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                # Fetching Machine info for corresponding Machine_ID
                query1 = "Select * from Machines where Machine_ID=?"
                c.execute(query1, (self.select_Entry.get(),))

                # Whether any record was fetched
                if c.fetchone() is None:
                    messagebox.showerror(
                        "Error", "No Record Found to Delete\nPlease Try Again!!!", parent=self.root)
                else:
                    # Deleting record for the corresponding Machine_ID
                    query2 = "Delete from Machines where Machine_ID=?"
                    c.execute(query2, (self.select_Entry.get(),))

                    # Clearing the select_entry box
                    self.select_Entry.delete(0, END)

                    # Displaying info for successful deletion
                    messagebox.showinfo(
                        "Information", "Successfully Deleted", parent=self.root)

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning(
                    "Warning", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinMachine(level, "Machine Window", self.user_oid)
        self.root.destroy()


########################################################################################
########################################################################################

# Window for Inserting into Adjuster Table
class WinAdjusterInsert:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("390x320+440+150")
        self.root.resizable(width=False, height=False)

        # All Entry Boxes
        self.adjuster_id = Entry(self.root, width=20, font=('Helvetica', 15))
        self.adjuster_id.grid(row=0, column=1, pady=(20, 8), padx=(20, 0))
        self.first_name = Entry(self.root, width=20, font=('Helvetica', 15))
        self.first_name.grid(row=1, column=1, pady=8, padx=(20, 0))
        self.last_name = Entry(self.root, width=20, font=('Helvetica', 15))
        self.last_name.grid(row=2, column=1, pady=8, padx=(20, 0))
        self.expertise = Entry(self.root, width=20, font=('Helvetica', 15))
        self.expertise.grid(row=3, column=1, pady=8, padx=(20, 0))
        self.email_id = Entry(self.root, width=20, font=('Helvetica', 15))
        self.email_id.grid(row=4, column=1, pady=8, padx=(20, 0))

        # All Labels
        self.adjuster_id_label = Label(self.root, text="Adjuster ID:", font=('Helvetica', 15))
        self.adjuster_id_label.grid(row=0, column=0, padx=(16, 0), pady=(20, 8), sticky=E)
        self.first_name_label = Label(self.root, text="First Name:", font=('Helvetica', 15))
        self.first_name_label.grid(row=1, column=0, padx=(16, 0), pady=8, sticky=E)
        self.last_name_label = Label(self.root, text="Last Name:", font=('Helvetica', 15))
        self.last_name_label.grid(row=2, column=0, padx=(16, 0), pady=8, sticky=E)
        self.expertise_label = Label(self.root, text="Expertise:", font=('Helvetica', 15))
        self.expertise_label.grid(row=3, column=0, padx=(16, 0), pady=8, sticky=E)
        self.email_id_label = Label(self.root, text="Email:", font=('Helvetica', 15))
        self.email_id_label.grid(row=4, column=0, padx=(16, 0), pady=8, sticky=E)

        # Back and Submit Button Frame
        self.button_frame = Frame(self.root)
        self.button_frame.grid(row=5, column=0, pady=10, columnspan=2)

        # Back Button
        self.back_button = Button(self.button_frame, text="Back", bg="#add8e6", font=("Helvetica", 11), command=self.close_window)
        self.back_button.grid(row=0, column=0, padx=(20, 40), ipadx=5)

        # Submit Button
        self.submit_button = Button(self.button_frame, text="Submit", bg="#90EE90", font=('Helvetica', 11),
                                    command=self.submit)
        self.submit_button.grid(row=0, column=1, pady=20, padx=(30, 0), ipadx=5)

    def submit(self):
        # if any entry not filled then warning message displayed
        if self.adjuster_id.get() == '' or self.first_name.get() == '' or self.last_name.get() == '' or\
                self.expertise.get() == '' or self.email_id.get() == '':
            messagebox.showwarning(
                "Warning", "Please Fill The Details!", parent=self.root)
        else:
            # Check whether valid email was provided
            if '@' not in self.email_id.get() or '.' not in self.email_id.get():
                messagebox.showwarning("Warning", "Please provide a valid email!", parent=self.root)
                return

            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                # Default values when inserting
                status = "Idle"
                nfixes = 0

                query = "Insert Into Adjusters(Adjuster_ID, First_Name, Last_Name, Expertise, Email_id, Status, nFixes) values(?, ?, ?, ?, ?, ?, ?)"

                c.execute(query, (self.adjuster_id.get(), self.first_name.get(), self.last_name.get(),
                                  self.expertise.get(), self.email_id.get(), status, nfixes))

                # Clearing the originally filled values
                self.adjuster_id.delete(0, END)
                self.first_name.delete(0, END)
                self.last_name.delete(0, END)
                self.expertise.delete(0, END)
                self.email_id.delete(0, END)

                # Displaying info for successfully insertion
                messagebox.showinfo("Information", "Successfully Inserted", parent=self.root)

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning("Warning", "Please Try Again!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinAdjuster(level, "Adjuster Window", self.user_oid)
        self.root.destroy()


# Window for Searching the Adjuster Table
class WinAdjusterSearch:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("584x385+365+120")
        self.root.resizable(width=False, height=False)

        # Our Search Label and Search Entry
        self.search_label = Label(self.root, text="Search:", anchor=E, font=('Helvetica', 15))
        self.search_label.grid(row=0, column=0, padx=(5, 0), pady=20)
        self.search_Entry = Entry(self.root, width=15, font=('Helvetica', 15))
        self.search_Entry.grid(row=0, column=1, padx=(0, 20), pady=20)

        # Drop Down Box for Search Type
        self.drop = ttk.Combobox(self.root, value=['Search by...', 'OID', 'Adjuster_ID', 'First_Name', 'Last_Name', 'Expertise', 'Email_id', 'Status', 'nFixes'],
                                 font=('Helvetica', 11))
        self.drop.current(0)
        self.drop.grid(row=0, column=2, padx=(0, 27))

        # Buttons (Back, Show, Show_All)
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(55, 0), pady=15, ipadx=5)
        self.search_button = Button(self.root, text="Search", bg="#90EE90", font=('Helvetica', 11), command=lambda: self.show(1))
        self.search_button.grid(row=1, column=1, pady=15, ipadx=5)
        self.show_all_button = Button(self.root, text="Show All", bg="orange", font=('Helvetica', 11), command=lambda: self.show(0))
        self.show_all_button.grid(row=1, column=2, padx=(15, 20), pady=15, ipadx=5)

        # Create TreeView Frame
        self.tree_frame = Frame(self.root)
        self.tree_frame.grid(row=2, column=0, columnspan=3, pady=20, padx=15)

        # TreeView ScrollBar
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        # Create TreeView
        self.my_tree = ttk.Treeview(
            self.tree_frame, height=7, yscrollcommand=self.tree_scroll.set)
        self.my_tree.pack()

        # Configure ScrollBar
        self.tree_scroll.config(command=self.my_tree.yview)

        # Define our columns
        self.my_tree['columns'] = ("OID", "Adjuster_ID", "First_Name", "Last_Name", "Expertise", "Email_ID", "Status", "nFixes")

        # Format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("OID", anchor=CENTER, width=30)
        self.my_tree.column("Adjuster_ID", anchor=CENTER, width=70)
        self.my_tree.column("First_Name", anchor=CENTER, width=75)
        self.my_tree.column("Last_Name", anchor=CENTER, width=75)
        self.my_tree.column("Expertise", anchor=CENTER, width=65)
        self.my_tree.column("Email_ID", anchor=CENTER, width=120)
        self.my_tree.column("Status", anchor=CENTER, width=50)
        self.my_tree.column("nFixes", anchor=CENTER, width=50)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=CENTER)
        self.my_tree.heading("OID", text="OID", anchor=CENTER)
        self.my_tree.heading("Adjuster_ID", text="Adjuster_ID", anchor=CENTER)
        self.my_tree.heading("First_Name", text="First Name", anchor=CENTER)
        self.my_tree.heading("Last_Name", text="Last Name", anchor=CENTER)
        self.my_tree.heading("Expertise", text="Expertise", anchor=CENTER)
        self.my_tree.heading("Email_ID", text="Email_ID", anchor=CENTER)
        self.my_tree.heading("Status", text="Status", anchor=CENTER)
        self.my_tree.heading("nFixes", text="nFixes", anchor=CENTER)

        # Count Variable for number of records
        self.count = 0

        # Change_Status Button
        self.change_status_button = Button(self.root, text="Change Status", bg="#f2f547", font=('Helvetica', 11), command=self.change_status)
        self.change_status_button.grid(row=3, column=0, columnspan=3, ipadx=5)

        # Loading the Environment Variables from .env file
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        self.EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        self.EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    def send_mail(self, email, machine_id):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)

            # Subject and Body
            subject = 'Machine Fixing Duty: Factory Simulation Software'
            body = f'Dear Adjuster\n\nPlease find the Machine_ID which you need to fix\n\nMachine ID: {machine_id}'

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(self.EMAIL_ADDRESS, email, msg)

            # Message to inform that Email has been sent
            messagebox.showinfo("Information", "Mail has been sent Successfully:)", parent=self.root)

    def change_status(self):
        if self.my_tree.selection():
            # Grab the Record number
            selected = self.my_tree.focus()
            # Grab the values of the record
            values = self.my_tree.item(selected, "values")

            # Finding the OID, nFixes and Adjuster_ID value for that record
            oid = values[0]
            adjuster_id = values[1]
            nFixes = int(values[7])

            # Adjuster is Idle
            if values[6] == "Idle":
                # Asking for confirmation whether user wants to change status or not
                user_ans = messagebox.askyesno(
                                "Confirmation", "Do you want to Change Status?\nIt will take some time please be patient!", parent=self.root)
                # If User pressed 'No' nothing will happen
                if not user_ans:
                    return

                for machine in machine_failure_list:
                    # Machine Type == Adjuster Expertise
                    if machine[2] == values[4]:
                        # Finding Machine_ID for which Adjuster Expertise matched
                        machine_id = machine_failure_list.pop(
                            machine_failure_list.index(machine))[1]
                        status = "Busy"

                        try:
                            conn = sqlite3.connect(database_file_path)
                            c = conn.cursor()

                            # Adjuster status becomes busy
                            query = "Update Adjusters set Status=? where OID=?"
                            c.execute(query, (status, oid))

                            # Finding email of the Adjuster
                            query = "Select Email_id from Adjusters where OID=?"
                            c.execute(query, oid)
                            email = c.fetchone()[0]

                            # Machine status becomes U/M
                            query = "Update Machines set Status=? where Machine_ID=?"
                            c.execute(query, ("U/M", machine_id))

                            # Entry made to Maintenance table
                            query = "Insert Into Maintenance(Machine_ID, Adjuster_ID) values(?, ?)"
                            c.execute(query, (machine_id, adjuster_id))

                            self.send_mail(email, machine_id)

                            conn.commit()
                            conn.close()

                            # Update the Treeview
                            self.my_tree.item(selected, text="", values=(values[0], values[1], values[2], values[3], values[4], values[5], status, values[7]))
                        except Exception:
                            messagebox.showwarning(
                                "Warning", "Please Try Again!!!", parent=self.root)
            # Adjuster is Busy
            else:
                # Asking for confirmation whether user wants to change status or not
                user_ans = messagebox.askyesno(
                                "Confirmation", "Do you want to Change Status?", parent=self.root)
                # If User pressed 'No' nothing will happen
                if not user_ans:
                    return

                status = "Idle"

                try:
                    conn = sqlite3.connect(database_file_path)
                    c = conn.cursor()

                    nFixes += 1
                    # Making Status of the Adjuster "Idle" and also updating nFixes
                    query = "Update Adjusters set Status=?, nFixes=? where OID=?"
                    c.execute(query, (status, nFixes, oid))

                    # Finding corresponding Machine_ID for Adjuster_ID
                    query = "Select Machine_ID from Maintenance where Adjuster_ID=?"
                    c.execute(query, (adjuster_id,))
                    machine_id = c.fetchone()[0]

                    # Deleting the record from Maintenance Table for given Adjuster_ID
                    query = "Delete from Maintenance where Adjuster_ID=?"
                    c.execute(query, (adjuster_id,))

                    # Updating the status of Machine
                    query = "Update Machines set Status=? where Machine_ID=?"
                    c.execute(query, ("Working", machine_id))

                    conn.commit()
                    conn.close()

                    # Update the Treeview
                    self.my_tree.item(selected, text="", values=(values[0], values[1], values[2], values[3], values[4], values[5], status, nFixes))
                except Exception:
                    messagebox.showwarning(
                        "Warning", "Please Try Again!!!", parent=self.root)

    def show(self, a):
        # Whether user has provided value to search_entry box and
        # User clicked search button
        if self.search_Entry.get() == "" and a == 1:
            messagebox.showwarning(
                "Warning", "Please Provide the Value to be Searched", parent=self.root)
            return

        # Whether User has chosen some Search by value
        selection = self.drop.get()
        if selection == 'Search by...' and a == 1:
            messagebox.showwarning(
                "Warning", "Please Select an Option to be Searched!!!", parent=self.root)
            return

        try:
            conn = sqlite3.connect(database_file_path)
            c = conn.cursor()

            # a->0 then show_all button was clicked
            # a->1 then search button was clicked
            if a == 0:
                c.execute("Select OID, * from Adjusters")
            else:
                query = "select OID, * from Adjusters where " + selection + " LIKE ?"
                value = '%' + self.search_Entry.get() + '%'
                c.execute(query, (value,))

            records = c.fetchall()

            # Removing the Preexisting Records(if any)
            for rec in self.my_tree.get_children():
                self.my_tree.delete(rec)

            # Resetting the Count
            self.count = 0

            if records:
                for record in records:
                    self.my_tree.insert(parent='', index='end',
                                        iid=self.count, text="", values=record)
                    self.count += 1
            else:
                messagebox.showinfo(
                    "Information", "No Record Found!!!", parent=self.root)

            # Clearing the Entry Box and Resetting the Drop Down Box
            self.search_Entry.delete(0, END)
            self.drop.current(0)

            conn.commit()
            conn.close()
        except Exception:
            messagebox.showwarning(
                        "Warning", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinAdjuster(level, "Adjuster Window", self.user_oid)
        self.root.destroy()


# Window for Updating the Adjuster Table
class WinAdjusterUpdate:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("390x410+440+100")
        self.root.resizable(width=False, height=False)

        # Select Label and Entry Box
        self.select_label = Label(self.root, text="Select OID:", anchor=E, font=('Helvetica', 15))
        self.select_label.grid(row=0, column=0, padx=(5, 25), pady=(20, 10), ipadx=18)
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
        self.adjuster_id = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.adjuster_id.grid(row=0, column=1, pady=5)
        self.first_name = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.first_name.grid(row=1, column=1, pady=5)
        self.last_name = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.last_name.grid(row=2, column=1, pady=5)
        self.expertise = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.expertise.grid(row=3, column=1, pady=5)
        self.email_id = Entry(self.my_frame, width=20, font=('Helvetica', 15))
        self.email_id.grid(row=4, column=1, pady=5)

        # All Labels
        self.adjuster_id_label = Label(self.my_frame, text="Adjuster ID:", font=('Helvetica', 15))
        self.adjuster_id_label.grid(row=0, column=0, padx=(0, 20), pady=5, sticky=E)
        self.first_name_label = Label(self.my_frame, text="First Name:", font=('Helvetica', 15))
        self.first_name_label.grid(row=1, column=0, padx=(0, 20), pady=5, sticky=E)
        self.last_name_label = Label(self.my_frame, text="Last Name:", font=('Helvetica', 15))
        self.last_name_label.grid(row=2, column=0, padx=(0, 20), pady=5, sticky=E)
        self.expertise_label = Label(self.my_frame, text="Expertise:", font=('Helvetica', 15))
        self.expertise_label.grid(row=3, column=0, padx=(0, 20), pady=5, sticky=E)
        self.email_id_label = Label(self.my_frame, text="Email_ID:", font=('Helvetica', 15))
        self.email_id_label.grid(row=4, column=0, padx=(0, 20), pady=5, sticky=E)

        # Update Button
        self.update_button = Button(self.root, text="Update", bg="#90EE90", font=('Helvetica', 11), command=self.update)
        self.update_button.grid(row=3, column=0, pady=25, ipadx=10, columnspan=2)

    def display(self):
        # Clearing all the Entry Boxes
        self.adjuster_id.delete(0, END)
        self.first_name.delete(0, END)
        self.last_name.delete(0, END)
        self.expertise.delete(0, END)
        self.email_id.delete(0, END)

        # Whether or not User has provided value for oid
        if self.select_Entry.get() == '':
            messagebox.showwarning(
                "Warning", "Please Select an ID!", parent=self.root)
        else:
            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                # Fetching info for a Particular Adjuster
                c.execute("Select * from Adjusters where OID=?", self.select_Entry.get())
                record = c.fetchone()

                # Checking whether record was found
                if not record:
                    messagebox.showinfo(
                        "Information", "No Record Found!", parent=self.root)
                else:
                    # Displaying information
                    self.adjuster_id.insert(0, record[0])
                    self.first_name.insert(0, record[1])
                    self.last_name.insert(0, record[2])
                    self.expertise.insert(0, record[3])
                    self.email_id.insert(0, record[4])

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning(
                    "Warning", "Please Try Again!", parent=self.root)

    def update(self):
        # Check whether the User has provided any OID
        if self.select_Entry.get() == '':
            messagebox.showwarning(
                "Warning", "Please Select an OID!", parent=self.root)
        # Check whether all the Entry fields were filled or not
        elif self.adjuster_id.get() == '' or self.first_name.get() == '' or self.last_name.get() == '' or \
                self.expertise.get() == '' or self.email_id.get() == '':
            messagebox.showwarning("Warning", "Please Fill The Details!", parent=self.root)
        else:
            # Check whether valid email was provided
            if '@' not in self.email_id.get() or '.' not in self.email_id.get():
                messagebox.showwarning("Warning", "Please provide a valid email!", parent=self.root)
                return

            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()
                
                # Updating the Database with the newly provided values
                query = "update Adjusters set Adjuster_ID = ?, First_Name = ?, Last_Name = ?, Expertise = ?, Email_id = ? where OID = ?"
                e = (self.adjuster_id.get(), self.first_name.get(), self.last_name.get(),
                     self.expertise.get(), self.email_id.get(), self.select_Entry.get())
                c.execute(query, e)

                # Clearing our Entry Fields
                self.adjuster_id.delete(0, END)
                self.first_name.delete(0, END)
                self.last_name.delete(0, END)
                self.expertise.delete(0, END)
                self.email_id.delete(0, END)
                self.select_Entry.delete(0, END)

                # Displaying info for successfully updation
                messagebox.showinfo("Information", "Successfully Updated", parent=self.root)

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning("Warning", "Please Try Again!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinAdjuster(level, "Adjuster Window", self.user_oid)
        self.root.destroy()


# Window for Deleting from Adjuster Table
class WinAdjusterDelete:

    def __init__(self, master, title, user_oid):
        self.root = master
        self.user_oid = user_oid
        self.root.title(title)
        self.root.geometry("400x160+450+150")
        self.root.resizable(width=False, height=False)

        # Select Label and Entry
        self.select_label = Label(self.root, text="Select AID:", font=('Helvetica', 15), anchor=E)
        self.select_label.grid(row=0, column=0, padx=(10, 38), pady=(20, 10), ipadx=10)
        self.select_Entry = Entry(self.root, width=17, font=('Helvetica', 15))
        self.select_Entry.grid(row=0, column=1, padx=(0, 40), pady=(20, 10))

        # Back and Delete Button
        self.back_button = Button(self.root, text="Back", bg="#add8e6", font=('Helvetica', 11), command=self.close_window)
        self.back_button.grid(row=1, column=0, padx=(90, 0), pady=30, ipadx=10)
        self.del_button = Button(self.root, text="Delete", bg="orange", font=('Helvetica', 11), command=self.delete_record)
        self.del_button.grid(row=1, column=1, padx=(0, 50), pady=30, ipadx=10)

    def delete_record(self):
        # Checking if an OID was given
        if self.select_Entry.get() == '':
            messagebox.showwarning(
                "Warning", "Please Select an AID!", parent=self.root)
        else:
            try:
                conn = sqlite3.connect(database_file_path)
                c = conn.cursor()

                # Selecting Adjuster whose OID was given
                query1 = "Select * from Adjusters where Adjuster_ID=?"
                c.execute(query1, (self.select_Entry.get(),))

                # Checking whether AID given has any Adjuster corresponding to it
                if c.fetchone() is None:
                    messagebox.showerror(
                        "Error", "No Record Found to Delete\nPlease Try Again!!!", parent=self.root)
                else:
                    # Deleting the Adjuster with corresponding AID
                    query2 = "Delete from Adjusters where Adjuster_ID=?"
                    c.execute(query2, (self.select_Entry.get(),))

                    # Clearing the Entry Box
                    self.select_Entry.delete(0, END)

                    # Displaying info for successfully deletion
                    messagebox.showinfo(
                        "Information", "Successfully Deleted", parent=self.root)

                conn.commit()
                conn.close()
            except Exception:
                messagebox.showwarning("Warning", "Please Try Again!!!", parent=self.root)

    def close_window(self):
        level = Tk()
        WinAdjuster(level, "Adjuster Window", self.user_oid)
        self.root.destroy()


########################################################################################
########################################################################################

# Function for finding Machines which have already failed
def find_machine_failures():
    machineFailureList = []

    try:
        # This will put Failed machines inside a list
        connection = sqlite3.connect(database_file_path)
        cur = connection.cursor()

        # Query for selecting Machines that has failed
        # Info like: 'OID', 'Machine_ID' and 'Machine_Type' are collected
        q = "Select OID, Machine_ID, Machine_Type from Machines where Status=?"
        cur.execute(q, ("Failure",))
        machineFailureList = cur.fetchall()

        connection.commit()
        connection.close()
    except Exception:
        messagebox.showwarning("Warning", "Please Try Again!!!", parent=root)

    return machineFailureList


# Executed when file is run directly
if __name__ == "__main__":
    # Declaring File Paths
    env_file_path = 'C:/Users/HP/PycharmProjects/openCV_venv/.env'
    database_file_path = 'C:/Users/HP/PycharmProjects/tensorEnv/Tkinter_prac/Projects/SE_Lab_Project9/FS_DATABASE.db'

    # Initialising the Interface
    root = Tk()

    # Calling Main Function for 'machine_failure_list'
    machine_failure_list = find_machine_failures()

    # The First Window which appears
    WinLogin(root, "Login Window")

    mainloop()

########################################################################################
########################################################################################
