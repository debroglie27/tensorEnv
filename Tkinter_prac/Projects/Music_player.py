from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Music Player')
root.geometry("600x360+350+120")

# Initialize Pygame Mixer
mixer.init()


# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir="./Audios", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    # Strip out the Directory info and .mp3 extension from SONG NAME
    song = song.replace("C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/Audios/", "")
    song = song.replace(".mp3", "")

    song_box.insert(END, song)


# Play Selected Song
def play():

    song = song_box.get(ACTIVE)
    song = f'./Audios/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play(loops=0)


# Stop Playing Current Song
def stop():

    mixer.music.stop()
    song_box.selection_clear(ACTIVE)


# Create Playlist Box
song_box = Listbox(root, bg="black", fg="green", width=40, font=("Helvetica", 15), selectbackground="grey", selectforeground="black")
song_box.pack(pady=20)

# Define Player Control Images
back_btn_img = PhotoImage(file="./Music_Player_Images/back50.png")
forward_btn_img = PhotoImage(file="./Music_Player_Images/forward50.png")
play_btn_img = PhotoImage(file="./Music_Player_Images/play50.png")
pause_btn_img = PhotoImage(file="./Music_Player_Images/pause50.png")
stop_btn_img = PhotoImage(file="./Music_Player_Images/stop50.png")

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add ADD Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to Playlist", command=add_song)


root.mainloop()
