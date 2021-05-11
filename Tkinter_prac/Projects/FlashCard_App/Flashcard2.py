from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random
from tkinter import messagebox

root = Tk()


def hide_all_frames(args):
    for frame in args:
        for widget in frame.winfo_children():
            widget.destroy()

        frame.pack_forget()


class HomeScreen:

    def __init__(self, master, title, geo):

        self.root = master
        self.root.title(title)
        self.root.geometry(geo)

        # Create our Menu
        self.my_menu = Menu(root)
        self.root.config(menu=self.my_menu)

        # Create File Menu
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        # Create Geography Menu
        self.geography_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Geography", menu=self.geography_menu)
        # Create Maths Menu
        self.maths_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Maths", menu=self.maths_menu)

        # Create File Menu Items
        self.file_menu.add_command(label="Home", command=self.home)
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Create Geography Menu Items
        self.geography_menu.add_command(label="States", command=lambda: self.states(StatesFrame))
        self.geography_menu.add_command(label="State Capitals", command=lambda: self.state_capitals(StateCapitalsFrame))

        # Create Maths Menu Items
        self.maths_menu.add_command(label="Addition", command=lambda: self.mathematics(MathematicsFrame, '+'))
        self.maths_menu.add_command(label="Subtraction", command=lambda: self.mathematics(MathematicsFrame, '-'))
        self.maths_menu.add_separator()
        self.maths_menu.add_command(label="Multiplication", command=lambda: self.mathematics(MathematicsFrame, 'x'))
        self.maths_menu.add_command(label="Division", command=lambda: self.mathematics(MathematicsFrame, '/'))

        # Create our Frames
        self.states_frame = Frame(self.root, width=500, height=500)
        self.state_capitals_frame = Frame(self.root, width=500, height=500)
        self.mathematics_frame = Frame(self.root, width=500, height=500)

        self.background_img = ImageTk.PhotoImage(Image.open("C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/FlashCard_App/FlashCard_Images/background.jpg"))

        # Creating a Canvas
        self.my_canvas = Canvas(self.root, width=600, height=520)
        self.my_canvas.pack(fill=BOTH, expand=1)

        # Set image in canvas
        self.my_canvas.create_image(0, 0, image=self.background_img, anchor="nw")

        # Our Welcome Message on our background label
        self.my_canvas.create_text(300, 160, text="WELCOME", font=('Helvetica', 44), fill="blue")
        self.my_canvas.create_text(300, 220, text="TO OUR", font=('Helvetica', 44), fill="blue")
        self.my_canvas.create_text(300, 280, text="FLASHCARD", font=('Helvetica', 44), fill="blue")
        self.my_canvas.create_text(300, 340, text="APP", font=('Helvetica', 44), fill="blue")

    def states(self, _class):
        self.my_canvas.pack_forget()
        self.root.geometry("600x530")
        _class(self.states_frame, self.state_capitals_frame, self.mathematics_frame)

    def state_capitals(self, _class):
        self.my_canvas.pack_forget()
        self.root.geometry("600x530")
        _class(self.state_capitals_frame, self.states_frame, self.mathematics_frame)

    def mathematics(self, _class, symbol):
        self.my_canvas.pack_forget()
        self.root.geometry("600x300")
        _class(symbol, self.mathematics_frame, self.state_capitals_frame, self.states_frame)

    def home(self):
        self.root.geometry("600x530")
        args = [self.states_frame, self.state_capitals_frame, self.mathematics_frame]
        hide_all_frames(args)

        self.my_canvas.pack(fill=BOTH, expand=1)


class StatesFrame:

    def __init__(self, *args):

        self.root = args[0]
        hide_all_frames(args)
        self.root.pack(fill=BOTH, expand=1)

        self.random_number = 0
        self.state_image = PhotoImage()
        self.answer_input = Entry()
        # List of state names
        self.our_states = ['california', 'florida', 'illinois', 'kentucky', 'nebraska',
                           'nevada', 'newyork', 'oregon', 'texas', 'vermont']

        self.show_state = Label(self.root)
        self.show_state.pack(pady=(15, 0))
        self.random_state(0)

        # Create answer input box
        self.answer_input = Entry(self.root, font=('Helvetica', 18))
        self.answer_input.pack(pady=(25, 0))

        # Create a frame for pass and answer button
        self.pass_answer_frame = Frame(self.root, width=300, height=50)
        self.pass_answer_frame.pack(pady=20)

        # Pass Button
        self.pass_button = Button(self.pass_answer_frame, text="Pass", bg="orange", font=('Helvetica', 12), command=lambda: self.random_state(1))
        self.pass_button.grid(row=0, column=0, pady=(10, 0), padx=(0, 10))

        # Create a button to answer the question
        self.answer_button = Button(self.pass_answer_frame, text="Answer", bg="#90EE90", font=('Helvetica', 12), command=self.state_answer)
        self.answer_button.grid(row=0, column=1, pady=(10, 0), padx=(10, 0))

    def random_state(self, param):

        # Clear the answer entry widget
        self.answer_input.delete(0, END)

        if param == 1:
            if self.our_states[self.random_number] == 'newyork':
                response = "It is New York"
            else:
                response = "It is " + self.our_states[self.random_number].title()

            messagebox.showinfo("Info", response, parent=self.root)

        # Generate a random number
        self.random_number = randint(0, len(self.our_states) - 1)
        state_image_path = 'C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/FlashCard_App/FlashCard_Images/' + self.our_states[self.random_number] + '.png'

        # Create our state images
        self.state_image = PhotoImage(file=state_image_path)
        self.show_state.config(image=self.state_image)

    def state_answer(self):
        ans = self.answer_input.get()
        ans = ans.replace(" ", "")

        if ans.lower() == self.our_states[self.random_number]:
            if self.our_states[self.random_number] == 'newyork':
                response = "CORRECT! " + "New York"
            else:
                response = "CORRECT! " + self.our_states[self.random_number].title()
        else:
            if self.our_states[self.random_number] == 'newyork':
                response = "INCORRECT! " + "New York"
            else:
                response = "INCORRECT! " + self.our_states[self.random_number].title()

        messagebox.showinfo("Info", response, parent=self.root)

        self.random_state(0)


class StateCapitalsFrame:

    def __init__(self, *args):

        self.root = args[0]
        hide_all_frames(args)
        self.root.pack(fill=BOTH, expand=1)

        self.state_image = PhotoImage()
        self.option_var = StringVar()
        self.option_var.set("Nothing")
        self.random_number = 0
        self.answer = ''

        # List of state names
        self.our_states = ['california', 'florida', 'illinois', 'kentucky', 'nebraska',
                           'nevada', 'newyork', 'oregon', 'texas', 'vermont']
        # Dictionary of state and its capitals
        self.our_state_capitals = {'california': 'sacramento',
                                   'florida': 'tallahassee',
                                   'illinois': 'springfield',
                                   'kentucky': 'frankfort',
                                   'nebraska': 'lincoln',
                                   'nevada': 'carson city',
                                   'newyork': 'albany',
                                   'oregon': 'salem',
                                   'texas': 'justin',
                                   'vermont': 'montpelier'}

        self.show_state = Label(self.root)
        self.show_state.pack(pady=(15, 0))

        self.option1 = Radiobutton(self.root)
        self.option1.pack(padx=(260, 0), pady=(10, 0), anchor=W)
        self.option2 = Radiobutton(self.root)
        self.option2.pack(padx=(260, 0), anchor=W)
        self.option3 = Radiobutton(self.root)
        self.option3.pack(padx=(260, 0), anchor=W)

        self.random_state_capitals(0)

        # Create frame for pass and answer button
        self.pass_answer_frame = Frame(self.root, width=300, height=50)
        self.pass_answer_frame.pack(pady=10)

        # Create a button to pass the question
        self.pass_button = Button(self.pass_answer_frame, text="Pass", bg="orange", font=('Helvetica', 12), command=lambda: self.random_state_capitals(1))
        self.pass_button.grid(row=0, column=0, pady=(10, 0), padx=(0, 20))

        # Create a button to answer the question
        self.answer_button = Button(self.pass_answer_frame, text="Answer", bg="#90EE90", font=('Helvetica', 12), command=self.state_capital_answer)
        self.answer_button.grid(row=0, column=1, pady=(10, 0), padx=(20, 0))

    def random_state_capitals(self, param):

        self.option_var.set("Nothing")

        if param == 1:
            response = "It is " + self.our_state_capitals[self.our_states[self.random_number]]

            messagebox.showinfo("Info", response, parent=self.root)

        answer_list = []
        our_states_copy = self.our_states.copy()

        count = 1
        while count < 4:
            # Generate a random number
            self.random_number = randint(0, len(our_states_copy) - 1)

            if count == 1:
                self.answer = our_states_copy[self.random_number]

            # Add the selection to the list
            answer_list.append(self.our_state_capitals[our_states_copy[self.random_number]])

            # Remove the selection from the list
            our_states_copy.remove(our_states_copy[self.random_number])

            # Shuffle the original list
            random.shuffle(our_states_copy)

            count += 1

        # Defining our Display Image path
        state_image_path = 'C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/FlashCard_App/FlashCard_Images/' + self.answer + '.png'

        # Create our state images
        self.state_image = PhotoImage(file=state_image_path)
        self.show_state.config(image=self.state_image)

        random.shuffle(answer_list)

        self.option1.config(text=answer_list[0].title(), variable=self.option_var, value=answer_list[0])
        self.option2.config(text=answer_list[1].title(), variable=self.option_var, value=answer_list[1])
        self.option3.config(text=answer_list[2].title(), variable=self.option_var, value=answer_list[2])

    def state_capital_answer(self):
        ans = self.option_var.get()

        if ans == self.our_state_capitals[self.answer]:
            response = "CORRECT! " + self.our_state_capitals[self.answer].title()
        else:
            response = "INCORRECT! " + self.our_state_capitals[self.answer].title()

        messagebox.showinfo("Info", response, parent=self.root)

        self.random_state_capitals(0)


class MathematicsFrame:

    def __init__(self, *args):

        self.symbol = args[0]
        self.root = args[1]
        hide_all_frames(args[1:])
        self.root.pack(fill=BOTH, expand=1)

        self.random_number1 = 0
        self.random_number2 = 0
        self.answer_input = Entry()
        self.actual_answer = 0

        # Label to show our maths question
        self.my_label = Label(self.root, font=('Helvetica', 50), bg="#aff1ef")
        self.my_label.pack(pady=(35, 0))

        self.random_mathematics(0)

        # Create answer input box
        self.answer_input = Entry(self.root, font=('Helvetica', 18))
        self.answer_input.pack(pady=(35, 0))

        # Create frame for pass and answer button
        self.pass_answer_frame = Frame(self.root, width=300, height=50)
        self.pass_answer_frame.pack(pady=20)

        # Create a button to pass the question
        self.pass_button = Button(self.pass_answer_frame, text="Pass", bg="orange", font=('Helvetica', 12), command=lambda: self.random_mathematics(1))
        self.pass_button.grid(row=0, column=0, pady=(10, 0), padx=(0, 20))

        # Create a button to answer the question
        self.answer_button = Button(self.pass_answer_frame, text="Answer", bg="#90EE90", font=('Helvetica', 12), command=self.mathematics_answer)
        self.answer_button.grid(row=0, column=1, pady=(10, 0), padx=(20, 0))

    def random_mathematics(self, param):

        # Clear the answer entry widget
        self.answer_input.delete(0, END)

        if param == 1:
            response = "Solution: " + str(round(self.actual_answer, 3))

            messagebox.showinfo("Info", response, parent=self.root)

        # Generate 2 random numbers according to the symbol
        if self.symbol == '+' or self.symbol == '-':
            self.random_number1 = randint(1, 1000)
            self.random_number2 = randint(1, 1000)
        elif self.symbol == 'x':
            self.random_number1 = randint(1, 100)
            self.random_number2 = randint(1, 100)
        else:
            self.random_number1 = randint(100, 1000)
            self.random_number2 = randint(10, 100)

        text = str(self.random_number1) + ' ' + self.symbol + ' ' + str(self.random_number2)
        self.my_label.config(text=text)

        if self.symbol == '+':
            self.actual_answer = self.random_number1 + self.random_number2
        elif self.symbol == '-':
            self.actual_answer = self.random_number1 - self.random_number2
        elif self.symbol == 'x':
            self.actual_answer = self.random_number1 * self.random_number2
        elif self.symbol == '/':
            self.actual_answer = self.random_number1 / self.random_number2

    def mathematics_answer(self):

        ans = float(self.answer_input.get())

        if self.actual_answer + 0.005 >= ans >= self.actual_answer - 0.005:
            response = "CORRECT! " + str(round(self.actual_answer, 3))
        else:
            response = "INCORRECT! " + str(round(self.actual_answer, 3))

        messagebox.showinfo("Info", response, parent=self.root)

        self.random_mathematics(0)


HomeScreen(root, "Flashcards", "600x530")

mainloop()
