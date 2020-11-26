from tkinter import *

root = Tk()
root.title('Paned Windows')
root.geometry("400x400")

panel1 = PanedWindow(bd=4, relief="raised", bg="red")
panel1.pack(fill=BOTH, expand=1)

frame1 = Frame(panel1)
panel1.add(frame1)

left_label = Label(frame1, text="Left Panel")
left_label.pack()
click_button = Button(frame1, text="HI")
click_button.pack()

panel2 = PanedWindow(panel1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
panel1.add(panel2)

top = Label(panel2, text="Top Panel")
panel2.add(top)

bottom = Label(panel2, text="Bottom Panel")
panel2.add(bottom)

root.mainloop()
