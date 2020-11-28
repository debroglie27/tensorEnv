import sys


class Account:

    def __init__(self):
        self.issued_books = []
        self.returned_books = []
        self.lost_books = []
        self.fine_amount = 0

    def calc_fine(self):
        self.fine_amount += len(self.lost_books)*10

    def reset_fine(self):
        self.fine_amount = 0
        self.lost_books = []


class User:

    account = Account()
    global Librarian
    librarian = Librarian("Mukesh", "1234", "")

    def __init__(self, name, _id):
        self.name = name
        self._id = _id

    def verify(self):
        _id = input('ID: ')

        if _id == self._id:
            print("User Verified!")
        else:
            print("Wrong ID! Not Verified!")

    def check_account(self):
        print("Issued Books: ")
        for item in self.account.issued_books:
            item.show_details()
        print("Returned Books: ")
        for item in self.account.returned_books:
            item.show_details()
        print("Lost Books: ")
        for item in self.account.lost_books:
            item.show_details()

    def issue_book(self, value):
        book = self.librarian.search(value)
        self.account.issued_books.append(book)

    def return_book(self, value):
        book = self.librarian.search(value)
        self.account.returned_books.append(book)
        self.account.issued_books.remove(book)

    def get_book_info(self, value):
        book = self.librarian.search(value)
        book.show_details()


class Staff(User):

    def __init__(self, name, _id, department, empid):
        super().__init__(name, _id)
        self.department = department
        self.empid = empid


class Student(User):

    def __init__(self, name, _id, _class, roll):
        super().__init__(name, _id)
        self._class = _class
        self.roll = roll


class Book:

    def __init__(self, title, author, isbn, publication):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication = publication
        self.reservation = False
        self.rating = 5
        self.renew = False

    def show_details(self):
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('ISBN: ', self.isbn)
        print('Publication: ', self.publication)
        print('Reservation: ', self.reservation)
        print('Rating: ', self.rating)
        print('Renew: ', self.renew)

    def reservation_status(self):
        return self.reservation

    def book_review(self):
        return self.rating

    def requested_details(self):
        return self.reservation, self.rating, self.renew

    def renew_info(self):
        return self.renew


class LibraryDatabase:

    list_of_books = []

    def add(self, book_object):

        if isinstance(book_object, Book):
            self.list_of_books.append(book_object)
        else:
            print("Incorrect Book Object")

    def delete(self, key):
        self.list_of_books.remove(key)

    def update(self, key):
        title = input('Title: ')
        author = input('Author: ')
        isbn = input('ISBN: ')
        publication = input('Publication: ')

        self.list_of_books.remove(key)
        self.list_of_books.append(Book(title, author, isbn, publication))

    def display(self, key):

        book = self.list_of_books[key]
        print("Title: ", book.title)
        print("Author: ", book.author)
        print("ISBN: ", book.author)
        print("Publication: ", book.publication)

    def search(self, search_key):

        if search_key.lower() == "title":
            s = input('Name: ')
            for book in self.list_of_books:
                if book.name == s:
                    return book

        elif search_key.lower() == "author":
            s = input('Author: ')
            for book in self.list_of_books:
                if book.author == s:
                    return book

        elif search_key.lower() == "publication":
            s = input('Publication: ')
            for book in self.list_of_books:
                if book.publication == s:
                    return book


class Librarian:
    search_key = ''
    library_database = LibraryDatabase()

    def __init__(self, name, _id, password):
        self.name = name
        self.id = _id
        self.password = password

    def verify_lib(self):

        password = input('Password: ')

        if password == self.password:
            print("Librarian Verified!")
        else:
            print("Wrong Password! Not Verified!")

    def search(self, value):

        self.search_key = value
        search_result = self.library_database.search(self.search_key)
        return search_result


class LibraryManagementSystem:

    staff_list = []
    student_list = []
    user_dict = {}
    librarian = Librarian("Mukesh", 1, "1234")

    def __init__(self, usertype, username, password, userdetails):

        self.usertype = usertype
        self.user_dict[username] = password

        if self.usertype.lower() == "staff":
            self.staff_list.append(Staff(userdetails[0], userdetails[1], userdetails[2], userdetails[3]))
        elif self.usertype.lower() == "student":
            self.student_list.append(Student(userdetails[0], userdetails[1], userdetails[2], userdetails[3]))
        else:
            print("Error!!")
            sys.exit(0)

    def login(self):

        username = input("Username: ")
        password = input("Password: ")

        if self.user_dict[username] == password:
            print("Login Successful")
        else:
            print("Login Unsuccessful")

    def register(self, name, _id, password):
        self.librarian = Librarian(name, _id, password)

    def logout(self):

        print("Logout Successful")
        sys.exit(0)
