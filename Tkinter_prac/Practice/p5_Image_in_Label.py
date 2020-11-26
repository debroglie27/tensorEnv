from tkinter import *
# from PIL import ImageTk, Image

root = Tk()
root.title("Nothing Much")
icon = PhotoImage(file='../ImageViewer_Images/feather.png')
root.iconphoto(False, icon)

car_img = PhotoImage(file="../ImageViewer_Images/car.png")
# car_img = ImageTk.PhotoImage(Image.open("car.png"))
my_label = Label(image=car_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
