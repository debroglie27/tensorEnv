from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Progress Bars')
root.geometry("500x300")


def step():
    # my_progress['value'] += 20
    # my_progress.start(10)
    for x in range(10):
        my_progress['value'] += 10
        root.update_idletasks()
        time.sleep(1)


def stop():
    my_progress.stop()


# Mode: "determinate", "indeterminate"
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
my_progress.pack(pady=20)

my_button1 = Button(root, text="Progress", command=step)
my_button1.pack(pady=20)

my_button2 = Button(root, text="Stop", command=stop)
my_button2.pack(pady=10)

root.mainloop()
