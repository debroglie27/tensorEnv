from tkinter import *

root = Tk()
root.title("Image Viewer")
icon = PhotoImage(file='./ImageViewer_Images/feather.png')
root.iconphoto(False, icon)

initial = 0
i = initial - 1

image1 = PhotoImage(file='./ImageViewer_Images/car.png')
image2 = PhotoImage(file='./ImageViewer_Images/bike.png')
image3 = PhotoImage(file='./ImageViewer_Images/ship.png')
image4 = PhotoImage(file='./ImageViewer_Images/plane.png')

image_list = [image1, image2, image3, image4]

status = Label(root, text=f"Image {i+1} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_label = Label(image=image_list[i])
my_label.grid(row=0, column=0, columnspan=3)


def forward():
    global i
    button_backward.config(state=NORMAL)
    i += 1
    status.config(text=f"Image {i+1} of {len(image_list)}")
    if i == len(image_list)-1:
        button_forward.config(state=DISABLED)
    my_label.config(image=image_list[i])


def backward():
    global i
    button_forward.config(state=NORMAL)
    i -= 1
    status.config(text=f"Image {i+1} of {len(image_list)}")
    if i == 0:
        button_backward.config(state=DISABLED)
    my_label.config(image=image_list[i])


button_forward = Button(root, text=">>", command=forward)
button_exit = Button(root, text="Exit Program", command=root.quit)
if initial == 1:
    button_backward = Button(root, text="<<", command=backward, state=DISABLED)
else:
    button_backward = Button(root, text="<<", command=backward)


button_forward.grid(row=1, column=2, pady=4)
button_exit.grid(row=1, column=1)
button_backward.grid(row=1, column=0)

root.mainloop()
