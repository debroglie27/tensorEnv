from tkinter import *


class Win1:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("400x400")
        self.but_new("Open Window2", '2', Win2)
        self.but_new("Open Window3", '3', Win3)

    def but_new(self, text, num, _class):
        Button(self.root, text=text, command=lambda: self.new_window(_class, num)).pack()

    '''def new_window(self, _class, num):
        global level
        level = Tk()
        title="Window"+num
        _class(level, title)
        self.root.destroy()'''

    def new_window(self, _class, num):
        level = Toplevel(self.root)
        title = "Window"+num
        _class(level, title)


class Win2:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("400x400")
        self.but_exit("Exit Window")

    def but_exit(self, text):
        Button(self.root, text=text, command=self.close_window).pack()

    '''def close_window(self):
        global root
        root = Tk()
        Win1(root, "Window1")
        self.root.destroy()'''

    def close_window(self):
        self.root.destroy()


class Win3:

    def __init__(self, master, title):
        self.root = master
        self.root.title(title)
        self.root.geometry("400x400")
        self.but_exit("Exit Window")

    def but_exit(self, text):
        Button(self.root, text=text, command=self.close_window).pack()

    '''def close_window(self):
        global root
        root = Tk()
        Win1(root, "Window1")
        self.root.destroy()'''

    def close_window(self):
        self.root.destroy()


root = Tk()
Win1(root, "Window1")

mainloop()
