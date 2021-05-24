import requests
import json
from tkinter import *
from tkinter import messagebox

# Getting Conversion Rate for two Particular Countries
# api_request = requests.get("https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=00c0c507c9cea5e2cfc3")
# api = json.loads(api_request.content)
# print(api)

# Getting All Currency Details
# api_request = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=00c0c507c9cea5e2cfc3")
# api = json.loads(api_request.content)
# print(api['results'])

api_countries_request = requests.get("https://free.currconv.com/api/v7/countries?apiKey=00c0c507c9cea5e2cfc3")
api = json.loads(api_countries_request.content)
# print(api['results'])

country_currency_dict = {}
country_list = []
for country_id in api['results']:
    country_currency_dict[api['results'][country_id]['name']] = api['results'][country_id]['currencyId']
    country_list.append(api['results'][country_id]['name'])

# print(country_list)
# print(country_currency_dict)

root = Tk()
root.title("Currency Converter App")
root.geometry("610x300")


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
            "https://free.currconv.com/api/v7/convert?q=" + search_option + "&compact=ultra&apiKey=00c0c507c9cea5e2cfc3")
        conversion_rate = json.loads(api_request.content)

        conversion_rate = str(round(float(conversion_rate[search_option]), 2))
        conv_rate_label.config(text=conversion_rate)


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


# Country Labels
country1_label = Label(root, text="Base Country:", font=('helvetica', 12))
country1_label.grid(row=0, column=0, padx=(20, 0), pady=(36, 0), sticky=E)
country2_label = Label(root, text="Conversion Country:", font=('helvetica', 12))
country2_label.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky=E)

# Entry Boxes
country1_entry = Entry(root, font=('helvetica', 12))
country1_entry.grid(row=0, column=1, pady=(36, 0), padx=(10, 0))
country2_entry = Entry(root, font=('helvetica', 12))
country2_entry.grid(row=1, column=1, pady=(20, 0), padx=(10, 0))

# Conversion Rate Button
conv_rate_button = Button(root, text="Conversion Rate", font=('helvetica', 12), command=conv_rate)
conv_rate_button.grid(row=2, column=0, columnspan=2, pady=(25, 0), ipadx=10)

# Conversion Rate Label
conv_rate_label = Button(root, text="", font=('helvetica', 12), bd=0)
conv_rate_label.grid(row=3, column=0, columnspan=2, pady=10)

# Create Frame
my_frame = LabelFrame(root, text="List Of Countries", font=("Helvetica", 11), bd=0)
my_frame.grid(row=0, column=2, rowspan=4, padx=(30, 0), pady=(15, 0))

# Create Listbox
my_list = Listbox(my_frame, font=("Helvetica", 10), width=24, height=12, bg="#ffe173",
                  fg="black", selectbackground="green", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH, pady=(8, 0))

# Create Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH, pady=(8, 0))

# Add Scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

update_listbox(country_list)

# Create a Binding on the ListBox onclick
my_list.bind("<<ListboxSelect>>", fill_out)

# Create a binding on the Entry Box
country1_entry.bind("<KeyRelease>", lambda event, obj=country1_entry: check(event, obj))
country2_entry.bind("<KeyRelease>", lambda event, obj=country2_entry: check(event, obj))

root.mainloop()
