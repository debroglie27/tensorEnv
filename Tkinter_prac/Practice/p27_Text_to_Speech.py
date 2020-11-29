from tkinter import *
import pyttsx3

root = Tk()
root.title('Text to Speech')
root.geometry("500x300")


engine = pyttsx3.init()
engine.setProperty('rate', 150)               # Changing the Speed of talking

voices = engine.getProperty('voices')
# Changing the voice Gender: 0->Male, 1->Female
engine.setProperty('voice', voices[1].id)     # By default Male


def talk():
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0, END)


my_entry = Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=20)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)

root.mainloop()
