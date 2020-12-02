from tkinter import *

root = Tk()
root.title('Frames')
root.geometry("300x300")

# frame = LabelFrame(root, text="This is a Frame", padx=40, pady=40)
frame = LabelFrame(root, text="Hi", padx=40, pady=40)
frame.pack(padx=10, pady=10)

b1 = Button(frame, text="Button1")
b2 = Button(frame, text="Button2")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
