from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pygame import mixer
import time
from mutagen.mp3 import MP3

root = Tk()
root.title('Music Player')
root.geometry("600x470+350+80")

# Initialize Pygame Mixer
mixer.init()

# Variable for keeping the count for number of songs
song_count = 0
# Song Length
song_length = 0


# Grab song length time info
def play_time():
    if not song_box.curselection():
        return
    # Grab Current time Elapsed
    current_time = mixer.music.get_pos() // 1000
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Get currently playing song
    current_song = song_box.curselection()[0]
    # Grab song title
    song = song_box.get(current_song)
    song = f'C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/Audios/{song}.mp3'

    # Get song length with mutagen
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    # Displaying the info on the status bar
    status_bar.config(text=f'Time Elapsed:  {converted_current_time}  of  {converted_song_length}  ')

    # Update the slider position
    my_slider.config(value=int(current_time))
    # Update the time
    status_bar.after(1000, play_time)


# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir="./Audios", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    if song:
        # Strip out the Directory info and .mp3 extension from SONG NAME
        song = song.replace("C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/Audios/", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)
        global song_count
        song_count += 1


def add_songs():
    songs = filedialog.askopenfilenames(initialdir="./Audios", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    # Loop Through the songs and remove directory info and .mp3 extension
    for song in songs:
        song = song.replace("C:/Users/M K DE/PycharmProjects/tensorEnv/Tkinter_prac/Projects/Audios/", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)
        global song_count
        song_count += 1


# Remove a song from playlist
def remove_song():

    if not song_box.curselection():
        return

    global song_count

    mixer.music.stop()
    # Get the Current Anchor Index
    anchor_index = song_box.index(ANCHOR)
    song_box.delete(ANCHOR)
    # Set the previous song to be the anchor
    song_box.selection_set((anchor_index-1) % song_count)
    song_box.activate((anchor_index-1) % song_count)

    song_count -= 1


# Remove all songs from playlist
def remove_all_songs():
    global song_count

    mixer.music.stop()
    song_box.delete(0, END)

    song_count = 0


# Play Selected Song
def play():

    if not song_box.curselection():
        return

    song = song_box.get(ACTIVE)
    song = f'./Audios/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play(loops=0)

    play_time()

    # making slider configuration acc. to the song
    my_slider.config(to=song_length, value=0)


# Stop Playing Current Song
def stop():

    mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # Clear the Status Bar
    status_bar.config(text='')

    # Resetting the slider
    my_slider.set(0)


# Variable to know whether the song is already paused or not
paused = False


# Pause and Unpause the current song
def pause():

    global paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True


# Play the next song in playlist
def next_song():

    if not song_box.curselection():
        return

    cur_song = song_box.curselection()[0]
    next_one = (cur_song + 1) % song_count

    # Clearing the selected item
    song_box.selection_clear(0, END)
    # Setting the next one to be selected
    song_box.selection_set(next_one)
    # Activating the next one that was selected
    song_box.activate(next_one)

    play()


# Play the previous song in playlist
def prev_song():

    if not song_box.curselection():
        return

    cur_song = song_box.curselection()[0]
    prev_one = (cur_song - 1 + song_count) % song_count

    # Clearing the selected item
    song_box.selection_clear(0, END)
    # Setting the next one to be selected
    song_box.selection_set(prev_one)
    # Activating the next one that was selected
    song_box.activate(prev_one)

    play()


def slide(x):
    pass


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
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=prev_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=pause)
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
add_song_menu.add_command(label="Add many songs to Playlist", command=add_songs)

# Add DELETE Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Remove one song from Playlist", command=remove_song)
remove_song_menu.add_command(label="Remove all songs from Playlist", command=remove_all_songs)

# Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create a Music Position Slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, length=400, command=slide)
my_slider.pack(pady=20)


root.mainloop()
