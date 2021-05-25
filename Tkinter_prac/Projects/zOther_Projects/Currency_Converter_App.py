import os
import json
import requests
from tkinter import *
from tkinter import messagebox, ttk
from pathlib import Path
from dotenv import load_dotenv


# Getting Conversion Rate for two Particular Countries
# api_request = requests.get("https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=" + API_KEY)
# api = json.loads(api_request.content)
# print(api)

# Getting All Currency Details
# api_request = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=" + API_KEY)
# api = json.loads(api_request.content)
# print(api['results'])


class CurrencyConverterApp:
    def __init__(self, master, title, geo):
        self.root = master
        self.root.title(title)
        self.root.geometry(geo)
        self.root.config(bg="#daff8c")

        # Loading the Environment Variables from .env file
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        self.API_KEY = os.environ.get('CURRENCY_CONVERTER_API_KEY')

        api_countries_request = requests.get("https://free.currconv.com/api/v7/countries?apiKey=" + self.API_KEY)
        api = json.loads(api_countries_request.content)

        self.country_currency_dict = {}
        self.country_list = []
        for country_id in api['results']:
            self.country_currency_dict[api['results'][country_id]['name']] = api['results'][country_id]['currencyId']
            self.country_list.append(api['results'][country_id]['name'])

        # Create Tabs
        self.my_notebook = ttk.Notebook(self.root)
        self.my_notebook.pack(pady=(0, 5), padx=5)

        # Create Two Frames
        self.conversion_rate_frame = Frame(self.my_notebook, width=620, height=460, bg="#daff8c")
        self.convert_frame = Frame(self.my_notebook, width=620, height=430)

        self.conversion_rate_frame.pack(fill=BOTH, expand=1)
        self.convert_frame.pack(fill=BOTH, expand=1)

        # Add our Tabs
        self.my_notebook.add(self.conversion_rate_frame, text="Conversion Rate")
        self.my_notebook.add(self.convert_frame, text="Convert", state=DISABLED)

        WinConversionRate(self.conversion_rate_frame, self.my_notebook,
                          self.country_currency_dict, self.country_list,
                          self.API_KEY)

    def find_conv_rate(self, country1, country2):
        country1_name = country1.lower().title()
        country2_name = country2.lower().title()

        if country1_name == '' or country2_name == '':
            messagebox.showwarning("Warning", "Please Select a Country Name", parent=root)
        elif country1_name == country2_name:
            messagebox.showwarning("Warning", "Please Select Different Country Names", parent=root)
        elif country1_name not in self.country_list or country2_name not in self.country_list:
            messagebox.showwarning("Warning", "Please Select Proper Country Names", parent=root)
        else:
            search_option = self.country_currency_dict[country1_name] + '_' + self.country_currency_dict[country2_name]
            api_request = requests.get(
                "https://free.currconv.com/api/v7/convert?q=" + search_option + "&compact=ultra&apiKey=" + self.API_KEY)
            conversion_rate = json.loads(api_request.content)

            conversion_rate = float(conversion_rate[search_option])

            return conversion_rate

        return -1


class WinConversionRate:
    def __init__(self, master, my_notebook, country_currency_dict, country_list, api_key):
        self.root = master
        self.label_frame_color = "#c7ff66"
        self.my_notebook = my_notebook
        self.country_list = country_list
        self.country_currency_dict = country_currency_dict
        self.API_KEY = api_key

        # Country1 LabelFrame
        self.country1_labelframe = LabelFrame(self.root, text="Base Country", font=("Helvetica", 11),
                                              bg=self.label_frame_color)
        self.country1_labelframe.grid(row=0, column=0, pady=(30, 0), padx=(25, 0))
        # Label
        self.country1_label = Label(self.country1_labelframe, text="Country of Currency which you want to Convert...",
                                    bg=self.label_frame_color)
        self.country1_label.pack(padx=20, pady=(10, 0))
        # Country1 Entry Box
        self.country1_entry = Entry(self.country1_labelframe, font=('helvetica', 15), width=25)
        self.country1_entry.pack(padx=20, pady=(10, 15))

        # Country2 LabelFrame
        self.country2_labelframe = LabelFrame(self.root, text="Conversion Country", font=("Helvetica", 11),
                                              bg=self.label_frame_color)
        self.country2_labelframe.grid(row=1, column=0, pady=(20, 0), padx=(25, 0))
        # Label
        self.country2_label = Label(self.country2_labelframe, text="Country of Currency which you want to Convert to...",
                                    bg=self.label_frame_color)
        self.country2_label.pack(padx=20, pady=(10, 0))
        # Country2 Entry Box
        self.country2_entry = Entry(self.country2_labelframe, font=('helvetica', 15), width=25)
        self.country2_entry.pack(padx=20, pady=(10, 0))
        # Label
        self.conversion_rate_label = Label(self.country2_labelframe, text="Current Conversion Rate...", bg=self.label_frame_color)
        self.conversion_rate_label.pack(padx=20, pady=(15, 0))
        # Readonly Entry box for Conversion rate
        self.conversion_rate_entry = Entry(self.country2_labelframe, state="readonly", font=('helvetica', 15), width=25)
        self.conversion_rate_entry.pack(padx=20, pady=(10, 15))

        # Button Frame
        self.button_frame = Frame(self.root, bg="#daff8c")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=(40, 0))

        # Unlock Button
        self.unlock_button = Button(self.button_frame, text="Unlock", font=('helvetica', 12), bg="#fd99ff", command=self.unlock)
        self.unlock_button.grid(row=0, column=0, ipadx=5, padx=(10, 30))
        # Conversion Rate Button
        self.conv_rate_button = Button(self.button_frame, text="Conversion Rate", font=('helvetica', 12), bg="#fd99ff",
                                       command=self.conv_rate)
        self.conv_rate_button.grid(row=0, column=1, ipadx=8, padx=(30, 0))

        # Create Frame
        self.my_frame = LabelFrame(self.root, text="List Of Countries", font=("Helvetica", 11),
                                   bg=self.label_frame_color)
        self.my_frame.grid(row=0, column=1, rowspan=2, pady=(30, 0), padx=(30, 10))

        # Create Listbox
        self.my_list = Listbox(self.my_frame, font=("Helvetica", 10), width=24, height=15, bg="#f9ff85",
                               fg="black", selectbackground="green", activestyle="none")
        self.my_list.pack(side=LEFT, fill=BOTH, pady=(10, 11), padx=(10, 0))

        # Create Scrollbar
        self.my_scrollbar = Scrollbar(self.my_frame)
        self.my_scrollbar.pack(side=RIGHT, fill=BOTH, pady=(10, 11), padx=(0, 10))

        # Add Scrollbar
        self.my_list.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_list.yview)

        self.update_listbox(country_list)

        # Create a Binding on the ListBox onclick
        self.my_list.bind("<<ListboxSelect>>", self.fill_out)

        # Create a binding on the Entry Box
        self.country1_entry.bind("<KeyRelease>", lambda event, obj=self.country1_entry: self.check(event, obj))
        self.country1_entry.bind("<Button-1>", lambda event, obj=self.country1_entry: self.check(event, obj))
        self.country2_entry.bind("<KeyRelease>", lambda event, obj=self.country2_entry: self.check(event, obj))
        self.country2_entry.bind("<Button-1>", lambda event, obj=self.country2_entry: self.check(event, obj))

    def conv_rate(self):
        country1_name = self.country1_entry.get().lower().title()
        country2_name = self.country2_entry.get().lower().title()

        if country1_name == '' or country2_name == '':
            messagebox.showwarning("Warning", "Please Select a Country Name", parent=root)
        elif country1_name == country2_name:
            messagebox.showwarning("Warning", "Please Select Different Country Names", parent=root)
        elif country1_name not in self.country_list or country2_name not in self.country_list:
            messagebox.showwarning("Warning", "Please Select Proper Country Names", parent=root)
        else:
            search_option = self.country_currency_dict[country1_name] + '_' + self.country_currency_dict[country2_name]
            api_request = requests.get(
                "https://free.currconv.com/api/v7/convert?q=" + search_option + "&compact=ultra&apiKey=" + self.API_KEY)
            conversion_rate = json.loads(api_request.content)

            conversion_rate = conversion_rate[search_option]
            self.conversion_rate_entry.config(state=NORMAL)
            self.conversion_rate_entry.insert(END, conversion_rate)
            self.conversion_rate_entry.config(state="readonly")

            # Locking the Country Entry Boxes
            self.country1_entry.config(state="readonly")
            self.country2_entry.config(state="readonly")

            # Unlocking our convert Tab
            self.my_notebook.tab(1, state=NORMAL)

    # Update the ListBox
    def update_listbox(self, data):
        # Clear the ListBox
        self.my_list.delete(0, END)

        # Add data to ListBox
        for item in data:
            self.my_list.insert(END, item)

    # Update Entry Box with ListBox clicked
    def fill_out(self, e):
        if root.focus_get() == self.country1_entry:
            # Delete whatever is in Entry Box
            self.country1_entry.delete(0, END)

            # Add clicked list item to entry box
            self.country1_entry.insert(END, self.my_list.get(ANCHOR))
        elif root.focus_get() == self.country2_entry:
            # Delete whatever is in Entry Box
            self.country2_entry.delete(0, END)

            # Add clicked list item to entry box
            self.country2_entry.insert(END, self.my_list.get(ANCHOR))

    # Create func to check entry with listbox
    def check(self, event, obj):
        if obj == self.country1_entry:
            # Grab what was typed
            typed = self.country1_entry.get()
        else:
            # Grab what was typed
            typed = self.country2_entry.get()

        if typed == '':
            data = self.country_list
        else:
            data = []
            for item in self.country_list:
                if typed.lower() in item.lower():
                    data.append(item)

        # Update our ListBox with selected items
        self.update_listbox(data)

    def unlock(self):
        self.conversion_rate_entry.config(state=NORMAL)
        self.conversion_rate_entry.delete(0, END)
        self.conversion_rate_entry.config(state="readonly")
        self.my_notebook.tab(1, state=DISABLED)

        self.country1_entry.config(state=NORMAL)
        self.country2_entry.config(state=NORMAL)


if __name__ == "__main__":
    root = Tk()
    env_file_path = "C:/Users/HP/Pycharm_Projects/openCV_venv/.env"
    CurrencyConverterApp(root, "Currency Converter App", "635x460+340+80")

    mainloop()
