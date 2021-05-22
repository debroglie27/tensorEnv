from tkinter import *
from tkinter import messagebox
from random import choice
from random import shuffle

root = Tk()
root.title('Word Jumble Game')
root.geometry('600x320+340+130')

# List of State Words
states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts',
          'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota',
          'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana',
          'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina',
          'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas',
          'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin',
          'Delaware', 'Idaho', 'Arkansas', 'Louisiana']

# Global Word
word = ''

my_label = Label(root, text="", font=('Helvetica', 48))
my_label.pack(pady=(20, 0))


def shuffler():

    # Clear Answer Entry
    answer_entry.delete(0, END)

    # Clear Hint Label and Reset hint_count
    hint_label.config(text="")
    global hint_count
    hint_count = 0

    # Choose a Word from the state list
    global word
    word = choice(states)

    # Break Apart Our Word
    word_apart = list(word.lower())
    shuffle(word_apart)

    # Turn shuffle list into word
    shuffled_word = ''.join(word_apart)

    my_label.config(text=shuffled_word)


# Answer Function
def answer():

    if word.lower() == answer_entry.get().lower():
        messagebox.showinfo("Info", "You are Correct!!", parent=root)
    else:
        messagebox.showinfo("Info", "You are Incorrect!!", parent=root)

    answer_entry.delete(0, END)
    shuffler()


# Create Hint Counter
hint_count = 0


# Hint Function
def hint():
    global hint_count

    word_length = len(word)

    if hint_count < word_length:
        hint_label.config(text=hint_label['text'] + ' ' + word[hint_count])

    hint_count += 1


answer_entry = Entry(root, font=('Helvetica', 24))
answer_entry.pack(pady=20)

# Frame for our Buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

# Our Pass Button
pass_button = Button(button_frame, text="Pass", command=shuffler, font=('Helvetica', 15), bg="Orange")
pass_button.grid(row=0, column=0, pady=10, padx=10)

# Our Answer Button
answer_button = Button(button_frame, text="Answer", command=answer, font=('Helvetica', 15), bg="#90EE90")
answer_button.grid(row=0, column=1, pady=10, padx=10)

# Our Hint Button
hint_button = Button(button_frame, text="Hint", command=hint, font=('Helvetica', 15), bg="#add8e6")
hint_button.grid(row=0, column=2, pady=10, padx=10)

# Our Hint Label
hint_label = Label(root, text="", font=('Helvetica', 15))
hint_label.pack(pady=10)

shuffler()

root.mainloop()
