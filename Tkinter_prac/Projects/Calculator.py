import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Calculator")

myfont = font.Font(size=20)
myfont2 = font.Font(size=25)

e = tk.Entry(root, width=20, font=myfont, justify="right", borderwidth=4)
e.grid(row=0, column=0, columnspan=4)

n = ''
math = ''
f_num = 0
s_num = 0


def button_num(num):
    global n
    n = e.get()
    e.delete(0, "end")
    e.insert(0, n + num)


def button_equal():
    global s_num
    try:
        s_num = float(e.get())
        e.delete(0, 'end')

        if math == 'addition':
            e.insert(0, str(f_num + s_num))
        elif math == 'subtraction':
            e.insert(0, str(f_num - s_num))
        elif math == 'multiplication':
            e.insert(0, str(f_num * s_num))
        elif math == 'division':
            e.insert(0, str(f_num / s_num))
        elif math == 'modulus':
            e.insert(0, str(f_num % s_num))
        else:
            e.delete(0, "end")
            e.config(foreground="red")
            e.insert(0, "Error!")

    except ValueError:
        e.delete(0, "end")
        e.config(foreground="red")
        e.insert(0, "Error!")


def button_clear():
    global n, math, f_num, s_num
    e.config(foreground="black")
    e.delete(0, "end")
    n = ''
    math = ''
    f_num = 0
    s_num = 0


def button_math(symbol):
    global f_num, math
    try:
        f_num = float(e.get())
        e.delete(0, "end")
    except ValueError:
        e.delete(0, "end")
        e.config(foreground="red")
        e.insert(0, "Error!")

    if symbol == '+':
        math = "addition"
    elif symbol == '-':
        math = "subtraction"
    elif symbol == '*':
        math = "multiplication"
    elif symbol == '/':
        math = "division"
    elif symbol == '%':
        math = "modulus"
    else:
        e.delete(0, "end")
        e.config(foreground="red")
        e.insert(0, 'Error!')


# creating the buttons
button_1 = tk.Button(root, text="1", padx=20, pady=7, font=myfont, command=lambda: button_num('1'))
button_2 = tk.Button(root, text="2", padx=20, pady=7, font=myfont, command=lambda: button_num('2'))
button_3 = tk.Button(root, text="3", padx=20, pady=7, font=myfont, command=lambda: button_num('3'))
button_4 = tk.Button(root, text="4", padx=20, pady=7, font=myfont, command=lambda: button_num('4'))
button_5 = tk.Button(root, text="5", padx=20, pady=7, font=myfont, command=lambda: button_num('5'))
button_6 = tk.Button(root, text="6", padx=20, pady=7, font=myfont, command=lambda: button_num('6'))
button_7 = tk.Button(root, text="7", padx=20, pady=7, font=myfont, command=lambda: button_num('7'))
button_8 = tk.Button(root, text="8", padx=20, pady=7, font=myfont, command=lambda: button_num('8'))
button_9 = tk.Button(root, text="9", padx=20, pady=7, font=myfont, command=lambda: button_num('9'))
button_0 = tk.Button(root, text="0", padx=20, pady=7, font=myfont, command=lambda: button_num('0'))

button_clears = tk.Button(root, text="Clear", padx=34, pady=5, bg="#add8e6", font=myfont, command=button_clear)
button_equals = tk.Button(root, text="=", padx=55, pady=5, bg="#ff4500", font=myfont, command=button_equal)

button_add = tk.Button(root, text="+", padx=15, pady=7, bg="#d3d3d3", font=myfont, command=lambda: button_math('+'))
button_sub = tk.Button(root, text="-", padx=15, bg="#d3d3d3", font=myfont2, command=lambda: button_math('-'))
button_mul = tk.Button(root, text="x", padx=17, pady=6.5, bg="#d3d3d3", font=myfont, command=lambda: button_math('*'))
button_div = tk.Button(root, text="/", padx=19, pady=7, bg="#d3d3d3", font=myfont, command=lambda: button_math('/'))
button_mod = tk.Button(root, text="%", padx=15, pady=6.5, bg="#d3d3d3", font=myfont, command=lambda: button_math('%'))
button_dot = tk.Button(root, text=".", padx=20, pady=1, font=myfont2, command=lambda: button_num('.'))

# putting the buttons on the screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_clears.grid(row=5, column=0, columnspan=2)
button_equals.grid(row=5, column=2, columnspan=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_mod.grid(row=4, column=2)
button_dot.grid(row=4, column=1)

root.mainloop()
