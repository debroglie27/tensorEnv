from tkinter import *
import mysql.connector

root = Tk()
root.title('Working with Sliders')
root.geometry("200x200")

my_db = mysql.connector.connect(
                   host="localhost",
                   user="root",
                   password="#debroglie@27",
                   database="codemy"
                 )

# To check if connection to mysql was made
# print(my_db)

# Create a CURSOR and initialise it
my_cursor = my_db.cursor()

# Create Database
# my_cursor.execute("CREATE DATABASE codemy")

# Test to see if Database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#    print(db)

# Drop Table
# my_cursor.execute("DROP Table customers")

# Create a Table
# my_cursor.execute('''Create Table if not exists customers(first_name VARCHAR(50),
#                                            last_name VARCHAR(50),
#                                            zipcode INT(10),
#                                            price_paid DECIMAL(10,2),
#                                            user_id INT AUTO_INCREMENT PRIMARY KEY )''')

# Alter Table
# my_cursor.execute('''Alter Table customers ADD(email VARCHAR(100),
#                                               address_1 VARCHAR(255),
#                                               address_2 VARCHAR(255),
#                                               city VARCHAR(50),
#                                               state VARCHAR(50),
#                                               country VARCHAR(50),
#                                               phone VARCHAR(50),
#                                               payment_method VARCHAR(50),
#                                               discount_code VARCHAR(50))''')


# Show Table
# my_cursor.execute("Select * from customers")
# for thing in my_cursor.description:
#    print(thing)


root.mainloop()
