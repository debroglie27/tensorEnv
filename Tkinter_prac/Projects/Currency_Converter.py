import os
import json
import requests
from tkinter import *
from tkinter import messagebox, ttk
from pathlib import Path
from dotenv import load_dotenv


# # Environment File Path
# env_file_path = "C:/Users/HP/Pycharm_Projects/openCV_venv/.env"
#
# # Loading the Environment Variables from .env file
# env_path = Path(env_file_path)
# load_dotenv(dotenv_path=env_path)
#
# API_KEY = os.environ.get('CURRENCY_CONVERTER_API_KEY')

# # Getting Conversion Rate for two Particular Countries
# api_request = requests.get("https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=" + API_KEY)
# api = json.loads(api_request.content)
# print(api)

# # Getting All Currency Details
# api_request = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=" + API_KEY)
# api = json.loads(api_request.content)
# print(api['results'])

# # Getting All Country Details
# api_countries_request = requests.get("https://free.currconv.com/api/v7/countries?apiKey=" + API_KEY)
# api = json.loads(api_countries_request.content)
# print(api['results'])


class CurrencyConverterApp:
    def __init__(self, master=None, gui=False):
        # Loading the Environment Variables from .env file
        env_path = Path(env_file_path)
        load_dotenv(dotenv_path=env_path)

        # Getting our API KEY
        self.API_KEY = os.environ.get('CURRENCY_CONVERTER_API_KEY')

        # Requesting for Information
        api_countries_request = requests.get("https://free.currconv.com/api/v7/countries?apiKey=" + self.API_KEY)
        # Getting the Information
        api = json.loads(api_countries_request.content)

        # Storing only the Required Information
        self.country_currency_dict = {}
        self.country_list = []
        for country_id in api['results']:
            self.country_currency_dict[api['results'][country_id]['name'].lower()] = api['results'][country_id]['currencyId'], \
                                                                                     api['results'][country_id]['currencyName'], \
                                                                                     api['results'][country_id]['currencySymbol']
            self.country_list.append(api['results'][country_id]['name'])

        if gui:
            self.root = master
            self.root.title("Currency Converter App")
            self.root.geometry("635x460+320+80")
            self.root.config(bg="#daff8c")

            # Create Tabs
            self.my_notebook = ttk.Notebook(self.root)
            self.my_notebook.pack(pady=(0, 5), padx=5)

            # Create Two Frames
            self.conversion_rate_frame = Frame(self.my_notebook, width=620, height=460, bg="#daff8c")
            self.convert_frame = Frame(self.my_notebook, width=620, height=460, bg="#daff8c")

            self.conversion_rate_frame.pack(fill=BOTH, expand=1)
            self.convert_frame.pack(fill=BOTH, expand=1)

            # Add our Tabs
            self.my_notebook.add(self.conversion_rate_frame, text="Conversion Rate")
            self.my_notebook.add(self.convert_frame, text="Convert", state=DISABLED)

            # Binding My Notebook
            self.my_notebook.bind("<<NotebookTabChanged>>", self.handle_tab_changed)

            # Calling the ConversionRate class
            self.obj_WinConversionRate = WinConversionRate(self.conversion_rate_frame, self.my_notebook,
                                                           self.country_currency_dict, self.country_list,
                                                           self.API_KEY)

    def handle_tab_changed(self, event):
        selection = event.widget.select()
        tab = event.widget.tab(selection, "text")

        if tab == "Conversion Rate":
            self.root.geometry("635x460+340+80")
            for child in self.convert_frame.winfo_children():
                child.destroy()
        else:
            self.root.geometry("440x350+410+120")

            conversion_rate = float(self.obj_WinConversionRate.conversion_rate_entry.get())
            country1_name = self.obj_WinConversionRate.country1_entry.get().lower()
            country2_name = self.obj_WinConversionRate.country2_entry.get().lower()

            country1_currencyName = self.country_currency_dict[country1_name][1]
            country2_currencyName = self.country_currency_dict[country2_name][1]

            country1_currencySymbol = self.country_currency_dict[country1_name][2]
            country2_currencySymbol = self.country_currency_dict[country2_name][2]

            self.conversion_rate_frame.pack_forget()
            WinConvert(self.convert_frame, conversion_rate, country1_currencyName, country1_currencySymbol,
                       country2_currencyName, country2_currencySymbol)

    def find_conv_rate(self, country1, country2):
        country1_name = country1.lower()
        country2_name = country2.lower()

        if country1_name == '' or country2_name == '':
            return -1
        elif country1_name == country2_name:
            return -2
        elif country1_name not in [x.lower() for x in self.country_list] or \
                country2_name not in [x.lower() for x in self.country_list]:
            return -3
        else:
            # Making our search option
            search_option = self.country_currency_dict[country1_name][0] + '_' + self.country_currency_dict[country2_name][0]
            # Requesting for conversion rate information
            api_request = requests.get(
                "https://free.currconv.com/api/v7/convert?q=" + search_option + "&compact=ultra&apiKey=" + self.API_KEY)
            # Getting the Conversion Rate Information
            conversion_rate = json.loads(api_request.content)

            # Getting the actual value
            conversion_rate = float(conversion_rate[search_option])

            return conversion_rate

    def convert(self, val, country1, country2):
        conv_rate = self.find_conv_rate(country1, country2)

        if conv_rate == -1:
            raise ValueError("Please Provide Country Names")
        elif conv_rate == -2:
            raise ValueError("Please Provide Different Country Names")
        elif conv_rate == -3:
            raise ValueError("Please Provide Proper Country Names")
        else:
            try:
                result = conv_rate * float(val)
            except Exception:
                raise ValueError("Please Provide a Numeric Value")

            return result


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
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=(40, 25))

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
        self.my_frame.grid(row=0, column=1, rowspan=2, pady=(30, 0), padx=(30, 25))

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
        country1_name = self.country1_entry.get().lower()
        country2_name = self.country2_entry.get().lower()

        if country1_name == '' or country2_name == '':
            messagebox.showwarning("Warning", "Please Select a Country Name", parent=root)
        elif country1_name == country2_name:
            messagebox.showwarning("Warning", "Please Select Different Country Names", parent=root)
        elif country1_name not in [x.lower() for x in self.country_list] or \
                country2_name not in [x.lower() for x in self.country_list]:
            messagebox.showwarning("Warning", "Please Select Proper Country Names", parent=root)
        else:
            search_option = self.country_currency_dict[country1_name][0] + '_' + self.country_currency_dict[country2_name][0]
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
                if typed.lower() in item.lower()[0:len(typed)]:
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


class WinConvert:
    def __init__(self, master, conversion_rate, country1_currency_name, country1_currency_symbol,
                 country2_currency_name, country2_currency_symbol):
        self.root = master
        self.conversion_rate = conversion_rate
        self.country1_currencyName = country1_currency_name
        self.country2_currencyName = country2_currency_name
        self.country1_currencySymbol = country1_currency_symbol
        self.country2_currencySymbol = country2_currency_symbol

        self.label_frame_color = "#c7ff66"

        # Currency1 LabelFrame
        self.currency1_labelframe = LabelFrame(self.root, text="Amount in " + country1_currency_name, font=("Helvetica", 11),
                                               bg=self.label_frame_color)
        self.currency1_labelframe.pack(pady=(30, 0), padx=(25, 25))
        # Currency1 Entry Box
        self.currency1_entry = Entry(self.currency1_labelframe, font=('helvetica', 15), width=25)
        self.currency1_entry.pack(padx=20, pady=(10, 10))
        # Convert Button
        self.convert_button = Button(self.currency1_labelframe, text="Convert", font=('helvetica', 11), bg="#fd99ff", command=self.convert)
        self.convert_button.pack(padx=20, pady=(5, 15), ipadx=6)

        # Currency2 LabelFrame
        self.currency2_labelframe = LabelFrame(self.root, text="Equivalent Amount in " + country2_currency_name, font=("Helvetica", 11),
                                               bg=self.label_frame_color)
        self.currency2_labelframe.pack(pady=(24, 0), padx=(25, 25))
        # Currency2 Entry Box
        self.currency2_entry = Entry(self.currency2_labelframe, font=('helvetica', 15), width=25, state="readonly")
        self.currency2_entry.pack(padx=20, pady=(10, 15))

        # Clear Button
        clear_button = Button(self.root, text="Clear", font=("Helvetica", 11), bg="#fd99ff", command=self.clear)
        clear_button.pack(pady=(22, 0), ipadx=5)

    def clear(self):
        # Clearing the Entry Boxes
        self.currency1_entry.delete(0, END)
        self.currency2_entry.config(state=NORMAL)
        self.currency2_entry.delete(0, END)
        self.currency2_entry.config(state="readonly")

    def convert(self):
        try:
            result = self.conversion_rate * float(self.currency1_entry.get())
        except Exception:
            messagebox.showwarning("Warning", "Please Provide a Numeric Value")
            return

        # round() our result based on its value
        if result < 1:
            if result > 0.001:
                result = round(result, 4)
            else:
                result = round(result, 6)
        else:
            result = round(result, 2)

        # State of entry box to NORMAL then deleting the content
        self.currency2_entry.config(state=NORMAL)
        self.currency2_entry.delete(0, END)

        # Result formatted to have commas
        result = '{:,}'.format(result)
        # Symbol Added
        result = self.country2_currencySymbol + " " + result
        # Inserting the final result
        self.currency2_entry.insert(END, result)

        # Making State of the entry box to "readonly"
        self.currency2_entry.config(state="readonly")


if __name__ == "__main__":
    env_file_path = "C:/Users/HP/Pycharm_Projects/openCV_venv/.env"

    root = Tk()
    CurrencyConverterApp(root, gui=True)

    # obj = CurrencyConverterApp()
    # print(obj.convert(203, "United States of America", "India"))

    mainloop()
