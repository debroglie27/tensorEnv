from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Opening File Dialog Box')
root.geometry("200x200")


def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/Users/M K DE/PycharmProjects/tensorEnv/Tech_with_tim/Tkinter_prac/ImageViewer_Images", title="Select a file", filetypes=(("jpg Files", "*.jpg"), ("all files", "*.*")))
    Label(root, text=root.filename).pack()
    my_img = PhotoImage(file=root.filename)
    Label(image=my_img).pack()


Button(root, text="Open Files", command=open).pack()

root.mainloop()
