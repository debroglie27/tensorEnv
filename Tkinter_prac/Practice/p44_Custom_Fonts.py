from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Custom Fonts')
root.geometry("400x400")

big_font = Font(family="Helvetica",
                size=25,
                weight="bold",
                slant="roman",
                underline=1,
                overstrike=0)

head_label = Label(root, text="Welcome to Database", bg='#A0E170', font=big_font)
head_label.pack(pady=(0, 20), ipadx=28, ipady=10)

my_label = Label(root, text="Address Database", font=big_font, bg="orange")
my_label.pack(pady=20)

root.mainloop()
