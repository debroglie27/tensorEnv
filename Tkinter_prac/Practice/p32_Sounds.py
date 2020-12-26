from tkinter import *
from pygame import mixer

root = Tk()
root.title('Sounds and Music')
root.geometry('500x300')

mixer.init()


def play():
    mixer.music.load("../Projects/Audios/tech-house-vibes-130.mp3")
    mixer.music.play(loops=0)


def stop():
    mixer.music.stop()


my_button = Button(root, text="Play Song", font=("Helvetica", 32), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica", 32), command=stop)
stop_button.pack(pady=20)

root.mainloop()
