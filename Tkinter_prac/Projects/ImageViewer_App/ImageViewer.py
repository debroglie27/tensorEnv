from tkinter import *

root = Tk()
root.title("Image Viewer App")
root.geometry("280x270+480+160")
root.config(bg="#ebffa8")

icon = PhotoImage(file='ImageViewer_Images/feather.png')
root.iconphoto(False, icon)

image1 = PhotoImage(file='ImageViewer_Images/car.png')
image2 = PhotoImage(file='ImageViewer_Images/bike.png')
image3 = PhotoImage(file='ImageViewer_Images/ship.png')
image4 = PhotoImage(file='ImageViewer_Images/plane.png')

image_list = [image1, image2, image3, image4]

i = 0

my_label = Label(image=image_list[i], bg="#ebffa8")
my_label.pack(pady=(25, 0))


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
    if i == 0:
        button_backward.config(state=DISABLED)

    status.config(text=f"Image {i + 1} of {len(image_list)}")
    my_label.config(image=image_list[i])


button_frame = Frame(root, bg="#ebffa8")
button_frame.pack(pady=(30, 0))

button_forward = Button(button_frame, text=">>", bg="#77fc65", font=("Helvetica", 10), command=forward)
button_exit = Button(button_frame, text="Exit Program", bg="#fcc265", font=("Helvetica", 10), command=root.quit)
button_backward = Button(button_frame, text="<<", bg="#77fc65", font=("Helvetica", 10), command=backward, state=DISABLED)

button_forward.grid(row=0, column=2)
button_exit.grid(row=0, column=1, padx=10)
button_backward.grid(row=0, column=0)

status = Label(root, text=f"Image {i+1} of {len(image_list)}", bg="#dfff75", bd=1, relief=SUNKEN, anchor=E)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
