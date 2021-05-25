import os
import json
import requests
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from dotenv import load_dotenv

env_file_path = "C:/Users/HP/Pycharm_Projects/openCV_venv/.env"

# Loading the Environment Variables from .env file
env_path = Path(env_file_path)
load_dotenv(dotenv_path=env_path)

API_KEY = os.environ.get('CURRENCY_CONVERTER_API_KEY')


# Getting Conversion Rate for two Particular Countries
# api_request = requests.get("https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=" + API_KEY)
# api = json.loads(api_request.content)
# print(api)

# Getting All Currency Details
# api_request = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=" + API_KEY)
# api = json.loads(api_request.content)
# print(api['results'])

api_countries_request = requests.get("https://free.currconv.com/api/v7/countries?apiKey=" + API_KEY)
api = json.loads(api_countries_request.content)

country_currency_dict = {}
country_list = []
for country_id in api['results']:
    country_currency_dict[api['results'][country_id]['name']] = api['results'][country_id]['currencyId']
    country_list.append(api['results'][country_id]['name'])

root = Tk()
root.title("Currency Converter App")
root.geometry("620x430+340+100")
root.config(bg="#daff8c")


def conv_rate():
    country1_name = country1_entry.get()
    country2_name = country2_entry.get()

    if country1_name == "Select..." or country2_name == "Select...":
        messagebox.showwarning("Warning", "Please Select Both the Countries", parent=root)
    elif country1_name == country2_name:
        messagebox.showwarning("Warning", "Please Select Different Country Names", parent=root)
    else:
        search_option = country_currency_dict[country1_name] + '_' + country_currency_dict[country2_name]
        api_request = requests.get(
            "https://free.currconv.com/api/v7/convert?q=" + search_option + "&compact=ultra&apiKey=" + API_KEY)
        conversion_rate = json.loads(api_request.content)

        conversion_rate = conversion_rate[search_option]
        conversion_rate_entry.insert(END, conversion_rate)


# Update the ListBox
def update_listbox(data):
    # Clear the ListBox
    my_list.delete(0, END)

    # Add data to ListBox
    for item in data:
        my_list.insert(END, item)


# Update Entry Box with ListBox clicked
def fill_out(e):
    if root.focus_get() == country1_entry:
        # Delete whatever is in Entry Box
        country1_entry.delete(0, END)

        # Add clicked list item to entry box
        country1_entry.insert(END, my_list.get(ANCHOR))
    elif root.focus_get() == country2_entry:
        # Delete whatever is in Entry Box
        country2_entry.delete(0, END)

        # Add clicked list item to entry box
        country2_entry.insert(END, my_list.get(ANCHOR))


# Create func to check entry with listbox
def check(event, obj):
    if obj == country1_entry:
        # Grab what was typed
        typed = country1_entry.get()
    else:
        # Grab what was typed
        typed = country2_entry.get()

    if typed == '':
        data = country_list
    else:
        data = []
        for item in country_list:
            if typed.lower() in item.lower():
                data.append(item)

    # Update our ListBox with selected items
    update_listbox(data)


label_frame_color = "#c7ff66"

# Country1 LabelFrame
country1_labelframe = LabelFrame(root, text="Base Country", font=("Helvetica", 11), bg=label_frame_color)
country1_labelframe.grid(row=0, column=0, pady=(30, 0), padx=(25, 0))
# Label
country1_label = Label(country1_labelframe, text="Country of Currency which you want to Convert...", bg=label_frame_color)
country1_label.pack(padx=20, pady=(10, 0))
# Country1 Entry Box
country1_entry = Entry(country1_labelframe, font=('helvetica', 15), width=25)
country1_entry.pack(padx=20, pady=(10, 15))

# Country2 LabelFrame
country2_labelframe = LabelFrame(root, text="Conversion Country", font=("Helvetica", 11), bg=label_frame_color)
country2_labelframe.grid(row=1, column=0, pady=(20, 0), padx=(25, 0))
# Label
country2_label = Label(country2_labelframe, text="Country of Currency which you want to Convert to...", bg=label_frame_color)
country2_label.pack(padx=20, pady=(10, 0))
# Country2 Entry Box
country2_entry = Entry(country2_labelframe, font=('helvetica', 15), width=25)
country2_entry.pack(padx=20, pady=(10, 0))
# Label
conversion_rate_label = Label(country2_labelframe, text="Current Conversion Rate...", bg=label_frame_color)
conversion_rate_label.pack(padx=20, pady=(15, 0))
# Readonly Entry box for Conversion rate
conversion_rate_entry = Entry(country2_labelframe, state="readonly", font=('helvetica', 15), width=25)
conversion_rate_entry.pack(padx=20, pady=(10, 15))

# Conversion Rate Button
conv_rate_button = Button(root, text="Conversion Rate", font=('helvetica', 12), bg="#fd99ff", command=conv_rate)
conv_rate_button.grid(row=2, column=0, columnspan=2, pady=(35, 0), ipadx=8)

# Create Frame
my_frame = LabelFrame(root, text="List Of Countries", font=("Helvetica", 11), bg=label_frame_color)
my_frame.grid(row=0, column=1, rowspan=2, pady=(30, 0), padx=(30, 0))

# Create Listbox
my_list = Listbox(my_frame, font=("Helvetica", 10), width=24, height=15, bg="#f9ff85",
                  fg="black", selectbackground="green", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH, pady=(10, 11), padx=(10, 0))

# Create Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH, pady=(10, 11), padx=(0, 10))

# Add Scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

update_listbox(country_list)

# Create a Binding on the ListBox onclick
my_list.bind("<<ListboxSelect>>", fill_out)

# Create a binding on the Entry Box
country1_entry.bind("<KeyRelease>", lambda event, obj=country1_entry: check(event, obj))
country1_entry.bind("<Button-1>", lambda event, obj=country1_entry: check(event, obj))
country2_entry.bind("<KeyRelease>", lambda event, obj=country2_entry: check(event, obj))
country2_entry.bind("<Button-1>", lambda event, obj=country2_entry: check(event, obj))


root.mainloop()
