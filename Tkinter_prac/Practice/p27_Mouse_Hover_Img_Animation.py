from tkinter import *

root = Tk()
root.title('Mouse Hover Image Animation')
root.geometry("500x300")


def change(event):
    my_label.config(image=my_img2)


def change_back(event):
    my_label.config(image=my_img1)


my_img1 = PhotoImage(file="../Projects/ImageViewer_Images/car.png")
my_img2 = PhotoImage(file="../Projects/ImageViewer_Images/bike.png")

my_label = Label(root, image=my_img1)
my_label.pack(pady=20)

my_label.bind('<Enter>', change)
my_label.bind('<Leave>', change_back)

root.mainloop()
