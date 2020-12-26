from tkinter import *
from datetime import date


root = Tk()
root.title('Menu Bars')
root.geometry('500x350')

panic = Label(root, text="DON'T, PANIC!", font=("Helvetica", 40), bg="black", fg="green")
panic.pack(pady=10, ipadx=10, ipady=10)

# Get Today's Date
today = date.today()
# Format Date
f_today = today.strftime("%A - %B %d, %Y")

# Output Date
today_label = Label(root, text=f_today)
today_label.pack(pady=20)

# Countdown
days_in_year = 366
today_day_number = int(today.strftime("%j"))

# Calculate how many days are remaining
days_left = days_in_year - today_day_number

# Countdown Label
countdown_label = Label(root, text=f'There Are Only {days_left} Days\nLeft In 2020!!', font=("Helvetica", 20))
countdown_label.pack(pady=20)


root.mainloop()
