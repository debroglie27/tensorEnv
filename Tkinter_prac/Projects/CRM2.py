from tkinter import *
import mysql.connector
import csv
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('CRM Database')
root.geometry("400x530")

my_db = mysql.connector.connect(
                   host="localhost",
                   user="root",
                   password="#debroglie@27",
                   database="codemy")

# Create a CURSOR and initialise it
my_cursor = my_db.cursor()


# clear fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)


# add customer to database
def add_customer():

    sql_command = "Insert into customers(first_name, last_name, address_1, address_2, city,\
                   state, zipcode, country, phone, email, payment_method, discount_code, price_paid)\
                   values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (first_name_box.get(), last_name_box.get(), address1_box.get(), address2_box.get(),
              city_box.get(), state_box.get(), zipcode_box.get(), country_box.get(), phone_box.get(),
              email_box.get(), payment_method_box.get(), discount_code_box.get(), price_paid_box.get())

    my_cursor.execute(sql_command, values)

    # Commit changes to the database
    my_db.commit()

    # Clear the fields
    clear_fields()


# search customers
def search_customers():
    search_customer = Tk()
    search_customer.title('Search Customers')
    search_customer.geometry("720x300")

    my_label = Label(search_customer, text="")
    my_label.grid(row=3, column=0, pady=10, columnspan=4)

    # searching
    def search():
        selection = drop.get()
        if selection == 'Search by...':
            messagebox.showwarning("Warning", "Please Select an Option to be Searched!!!", parent=search_customer)
            return

        sql = "select * from customers where "+selection+"=%s"
        value = search_box.get()
        my_cursor.execute(sql, (value, ))
        records = my_cursor.fetchall()

        print_records = ""
        if not records:
            print_records = "No record Found"
        else:
            for record in records:
                for item in record:
                    print_records += str(item) + " "
                print_records += "\n"

        my_label.config(text=print_records)
        search_box.delete(0, END)

    # Search Label
    search_label = Label(search_customer, text="Search:")
    search_label.grid(row=0, column=0, padx=(20, 0), pady=20)
    # Search Entry Box
    search_box = Entry(search_customer)
    search_box.grid(row=0, column=1, padx=(30, 0), pady=20, ipadx=20)
    # Search Button
    search_button = Button(search_customer, text="Search", bg="#90EE90", command=search)
    search_button.grid(row=1, column=0, padx=30, columnspan=2, ipadx=20)
    # drop down box
    drop = ttk.Combobox(search_customer, value=['Search by...', 'First_Name', 'Last_Name', 'Email', 'User_ID'])
    drop.current(0)
    drop.grid(row=0, column=2, padx=40)

    Label(search_customer, text="\t\t\t\t\t").grid(row=0, column=3)


# list customers
def list_customers():
    list_of_customers = Tk()
    list_of_customers.title('List of Customers')
    list_of_customers.geometry("1100x300")

    # write to CSV
    def write_to_csv(res):
        with open('customers.csv', 'w', newline='') as f:
            w = csv.writer(f)
            for record in res:
                w.writerow(record)

    # query the database
    my_cursor.execute("Select * from customers")
    result = my_cursor.fetchall()

    for index, x in enumerate(result):
        num = 0
        for y in x:
            Label(list_of_customers, text=y).grid(row=index, column=num, pady=2, padx=10)
            num += 1

    export_button = Button(list_of_customers, text="Export", command=lambda: write_to_csv(result))
    export_button.grid(row=len(result)+1, column=0, padx=10, pady=10)


# Create a Label
title_label = Label(root, text="Codemy Customer Database", font=('Helvetica', 18))
title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=42)

# Create Main Form to enter customer data
first_name_label = Label(root, text="First Name:").grid(row=1, column=0, sticky=W, pady=3, padx=(25, 0))
last_name_label = Label(root, text="Last Name:").grid(row=2, column=0, sticky=W, pady=3, padx=(25, 0))
address1_label = Label(root, text="Address1:").grid(row=3, column=0, sticky=W, pady=3, padx=(25, 0))
address2_label = Label(root, text="Address2:").grid(row=4, column=0, sticky=W, pady=3, padx=(25, 0))
city_label = Label(root, text="City:").grid(row=5, column=0, sticky=W, pady=3, padx=(25, 0))
state_label = Label(root, text="State:").grid(row=6, column=0, sticky=W, pady=3, padx=(25, 0))
zipcode_label = Label(root, text="Zipcode:").grid(row=7, column=0, sticky=W, pady=3, padx=(25, 0))
country_label = Label(root, text="Country:").grid(row=8, column=0, sticky=W, pady=3, padx=(25, 0))
phone_label = Label(root, text="Phone Number:").grid(row=9, column=0, sticky=W, pady=3, padx=(25, 0))
email_label = Label(root, text="Email Address:").grid(row=10, column=0, sticky=W, pady=3, padx=(25, 0))
payment_method_label = Label(root, text="Payment Method:").grid(row=11, column=0, sticky=W, pady=3, padx=(25, 0))
discount_code_label = Label(root, text="Discount Code:").grid(row=12, column=0, sticky=W, pady=3, padx=(25, 0))
price_paid_label = Label(root, text="Price Paid:").grid(row=13, column=0, sticky=W, pady=3, padx=(25, 0))

# Create Entry Boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=3, ipadx=35)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=3, ipadx=35)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=3, ipadx=35)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=3, ipadx=35)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=3, ipadx=35)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=3, ipadx=35)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=3, ipadx=35)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=3, ipadx=35)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=3, ipadx=35)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=3, ipadx=35)

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=3, ipadx=35)

discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=3, ipadx=35)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=3, ipadx=35)

# Add Buttons
clear_fields_button = Button(root, text="Clear", bg="#add8e6", command=clear_fields)
clear_fields_button.grid(row=14, column=0, pady=(20, 0), ipadx=20, padx=(60, 0))

add_customer_button = Button(root, text="Submit", bg="#90EE90", command=add_customer)
add_customer_button.grid(row=14, column=1, pady=(20, 0), ipadx=20, padx=(0, 30))

list_customer_button = Button(root, text="List Customers", bg="orange", command=list_customers)
list_customer_button.grid(row=15, column=0, pady=10, ipadx=20, padx=(10, 0))

search_customer_button = Button(root, text="Search Customers", bg="pink", command=search_customers)
search_customer_button.grid(row=15, column=1, pady=10, ipadx=20, padx=(0, 30))

# To see our rows from customers table
# my_cursor.execute("Select * from customers")
# result = my_cursor.fetchall()
# for x in result:
#     print(x)

root.mainloop()
