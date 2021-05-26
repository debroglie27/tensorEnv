from tkinter import *
from random import randint
import random
from tkinter import messagebox

root = Tk()
root.title("Flashcard App")
root.geometry('600x530+330+50')

# Global Variables
state_image = PhotoImage()
random_number = 0

# List of state names
our_states = ['california', 'florida', 'illinois', 'kentucky', 'nebraska',
              'nevada', 'newyork', 'oregon', 'texas', 'vermont']

# Dictionary of state and its capitals
our_state_capitals = {'california': 'sacramento',
                      'florida': 'tallahassee',
                      'illinois': 'springfield',
                      'kentucky': 'frankfort',
                      'nebraska': 'lincoln',
                      'nevada': 'carson city',
                      'newyork': 'albany',
                      'oregon': 'salem',
                      'texas': 'justin',
                      'vermont': 'montpelier'
                      }
answer_input = Entry()
show_state = Label()
answer = ''
# For State Capitals Options
option_var = StringVar()
option_var.set("Nothing")
option1 = Radiobutton()
option2 = Radiobutton()
option3 = Radiobutton()


def random_state(param):

    global answer_input
    global our_states
    global random_number

    # Clear the answer entry widget
    answer_input.delete(0, END)

    if param == 1:
        if our_states[random_number] == 'newyork':
            response = "It is New York"
        else:
            response = "It is " + our_states[random_number].title()
        messagebox.showinfo("Info", response, parent=root)

    # Generate a random number
    random_number = randint(0, len(our_states) - 1)
    state_image_path = './Images/' + our_states[random_number] + '.png'

    # Create our state images
    global state_image
    state_image = PhotoImage(file=state_image_path)
    global show_state
    show_state.config(image=state_image)


def state_answer():
    ans = answer_input.get()
    ans = ans.replace(" ", "")

    if ans.lower() == our_states[random_number]:
        if our_states[random_number] == 'newyork':
            response = "CORRECT! " + "New York"
        else:
            response = "CORRECT! " + our_states[random_number].title()
    else:
        if our_states[random_number] == 'newyork':
            response = "INCORRECT! " + "New York"
        else:
            response = "INCORRECT! " + our_states[random_number].title()

    messagebox.showinfo("Info", response, parent=root)

    random_state(0)


# State Flashcard Function
def states():
    hide_all_frames()
    states_frame.pack(fill=BOTH, expand=1)

    global show_state
    show_state = Label(states_frame)
    show_state.pack(pady=(15, 0))

    # Create answer input box
    global answer_input
    answer_input = Entry(states_frame, font=('Helvetica', 18))
    answer_input.pack(pady=(15, 0))
    
    random_state(0)

    # Pass Button
    random_button = Button(states_frame, text="Pass", font=('Helvetica', 12), command=lambda: random_state(1))
    random_button.pack(pady=(10, 0))

    # Create a button to answer the question
    answer_button = Button(states_frame, text="Answer", font=('Helvetica', 12), command=state_answer)
    answer_button.pack(pady=(10, 0))


def random_state_capitals():
    global our_states
    global random_number
    global answer, option_var
    option_var.set("Nothing")

    answer = ''
    answer_list = []
    our_states_copy = our_states.copy()

    count = 1
    while count < 4:
        # Generate a random number
        random_number = randint(0, len(our_states_copy) - 1)

        if count == 1:
            answer = our_states_copy[random_number]

        # Add the selection to the list
        answer_list.append(our_state_capitals[our_states_copy[random_number]])

        # Remove the selection from the list
        our_states_copy.remove(our_states_copy[random_number])

        # Shuffle the original list
        random.shuffle(our_states_copy)

        count += 1

    # Defining our Display Image path
    state_image_path = './Images/' + answer + '.png'

    # Create our state images
    global state_image
    state_image = PhotoImage(file=state_image_path)
    global show_state
    show_state.config(image=state_image)

    random.shuffle(answer_list)

    global option1, option2, option3
    option1.config(text=answer_list[0].title(), variable=option_var, value=answer_list[0])
    option2.config(text=answer_list[1].title(), variable=option_var, value=answer_list[1])
    option3.config(text=answer_list[2].title(), variable=option_var, value=answer_list[2])


def state_capital_answer():
    global answer
    ans = option_var.get()

    if ans == our_state_capitals[answer]:
        response = "CORRECT! " + our_state_capitals[answer].title()
    else:
        response = "INCORRECT! " + our_state_capitals[answer].title()

    messagebox.showinfo("Info", response, parent=root)

    random_state_capitals()


# State Capitals Flashcard Function
def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=1)

    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack(pady=(15, 0))

    global option1, option2, option3
    option1 = Radiobutton(state_capitals_frame)
    option1.pack(padx=(260, 0), pady=(10, 0), anchor=W)
    option2 = Radiobutton(state_capitals_frame)
    option2.pack(padx=(260, 0), anchor=W)
    option3 = Radiobutton(state_capitals_frame)
    option3.pack(padx=(260, 0), anchor=W)

    random_state_capitals()

    # Create a button to answer the question
    answer_button = Button(state_capitals_frame, text="Answer", font=('Helvetica', 12), command=state_capital_answer)
    answer_button.pack(pady=(20, 0))


# Hide all previous frames
def hide_all_frames():
    for widget in states_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    states_frame.pack_forget()
    state_capitals_frame.pack_forget()


# Create our Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Geography Menu Items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

# Create our Frames
states_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)

root.mainloop()
