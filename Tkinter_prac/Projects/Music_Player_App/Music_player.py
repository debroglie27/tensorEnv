from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pygame import mixer
import time
from mutagen.mp3 import MP3

root = Tk()
root.title('Music Player')
root.geometry("600x440+350+80")

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

    # Get currently playing song
    current_song = song_box.curselection()[0]
    # Grab song title
    song = song_box.get(current_song)
    song = f'./Audios/{song}.mp3'

    # Get song length with mutagen
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    if int(my_slider.get()) == int(song_length):
        # Displaying the info on the status bar
        status_bar.config(text=f'Time Elapsed:  {converted_song_length}  of  {converted_song_length}  ')
        # Making the slider value the end
        my_slider.set(int(song_length)+1)
    elif paused:
        pass
    elif int(my_slider.get()+1) == int(current_time):
        # Update the slider position
        my_slider.config(value=int(current_time))
        # converted current time
        converted_current_time = time.strftime('%M:%S', time.gmtime(my_slider.get()))
        # Displaying the info on the status bar
        status_bar.config(text=f'Time Elapsed:  {converted_current_time}  of  {converted_song_length}  ')
    else:
        # Update the slider position
        my_slider.config(value=int(my_slider.get()))
        # Change the converted current time
        converted_current_time = time.strftime('%M:%S', time.gmtime(my_slider.get()))
        # Displaying the info on the status bar
        status_bar.config(text=f'Time Elapsed:  {converted_current_time}  of  {converted_song_length}  ')
        # Update slider position by 1 second
        my_slider.config(value=int(my_slider.get()+1))

    # Update the time
    status_bar.after(1000, play_time)


# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir="./Audios", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    if song:
        # Strip out the Directory info and .mp3 extension from SONG NAME
        song = song.replace("C:/Users/HP/Pycharm_Projects/tensorEnv/Tkinter_prac/Projects/Music_Player_App/Audios/", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)
        global song_count
        song_count += 1


def add_songs():
    songs = filedialog.askopenfilenames(initialdir="./Audios", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    # Loop Through the songs and remove directory info and .mp3 extension
    for song in songs:
        song = song.replace("C:/Users/HP/Pycharm_Projects/tensorEnv/Tkinter_prac/Projects/Music_Player_App/Audios/", "")
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

    # Everything Stops after removing a song
    stop()


# Remove all songs from playlist
def remove_all_songs():
    global song_count

    mixer.music.stop()
    song_box.delete(0, END)

    song_count = 0

    # Everything Stops after removing a song
    stop()


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

    stop()

    # Setting the next one to be selected
    song_box.selection_set(next_one)
    # Activating the next one that was selected
    song_box.activate(next_one)

    song = song_box.get(ACTIVE)
    song = f'./Audios/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play(loops=0)


# Play the previous song in playlist
def prev_song():

    if not song_box.curselection():
        return

    cur_song = song_box.curselection()[0]
    prev_one = (cur_song - 1 + song_count) % song_count

    stop()

    # Setting the next one to be selected
    song_box.selection_set(prev_one)
    # Activating the next one that was selected
    song_box.activate(prev_one)

    song = song_box.get(ACTIVE)
    song = f'./Audios/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play(loops=0)


def slide(x):

    if not song_box.curselection():
        return

    song = song_box.get(ACTIVE)
    song = f'./Audios/{song}.mp3'

    mixer.music.load(song)
    mixer.music.play(loops=0, start=int(my_slider.get()))


# Create Volume Function
def volume(x):
    mixer.music.set_volume(volume_slider.get())
    current_volume = mixer.music.get_volume()*100
    volume_label.config(text=str(int(current_volume)))


# Create Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="green", width=40, font=("Helvetica", 15),
                   selectbackground="grey", selectforeground="black", activestyle="none")
song_box.grid(row=0, column=0)

# Define Player Control Images
back_btn_img = PhotoImage(file="Music_Player_Images/back50.png")
forward_btn_img = PhotoImage(file="Music_Player_Images/forward50.png")
play_btn_img = PhotoImage(file="Music_Player_Images/play50.png")
pause_btn_img = PhotoImage(file="Music_Player_Images/pause50.png")
stop_btn_img = PhotoImage(file="Music_Player_Images/stop50.png")

# Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=(20, 0))

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
add_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to Playlist", command=add_song)
add_song_menu.add_command(label="Add many songs to Playlist", command=add_songs)

# Add DELETE Song Menu
remove_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Remove one song from Playlist", command=remove_song)
remove_song_menu.add_command(label="Remove all songs from Playlist", command=remove_all_songs)

# Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create a Music Position Slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, length=430, command=slide)
my_slider.grid(row=2, column=0, pady=(20, 0))

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=(30, 0), rowspan=2)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, value=1, length=230, command=volume)
volume_slider.pack(padx=10, pady=10)

# Create Volume value label
volume_label = Label(volume_frame, text='100', font=('Helvetica', 15))
volume_label.pack(pady=5)

root.mainloop()
