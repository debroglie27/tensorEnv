from tkinter import *
import requests
import json

root = Tk()
root.title('Working with APIs')
root.geometry("634x240")

weather_color = {'O3': 'Gray', 'PM2.5': 'Gray', 'PM10': 'Gray'}

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=37824320-9FBD-49F4-8B22-AB9E4018218C


def look_zipcode():
    global weather_color
    zipcode = str(entry.get())

    weather_color = {'O3': 'Gray', 'PM2.5': 'Gray', 'PM10': 'Gray'}
    content = {'O3': 'AQI for O3 Not Available                  ', 'PM2.5': 'AQI for PM2.5 Not Available            ', 'PM10': 'AQI for PM10 Not Available                 '}

    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=37824320-9FBD-49F4-8B22-AB9E4018218C")
        api = json.loads(api_request.content)

        reporting_area = api[0]['ReportingArea']
        parameter = [api[i]['ParameterName'] for i in range(len(api))]
        aqi = {api[i]['ParameterName']: api[i]['AQI'] for i in range(len(api))}
        category_name = {api[i]['ParameterName']: api[i]['Category']['Name'] for i in range(len(api))}

        for param in parameter:
            if category_name[param] == 'Good':
                weather_color[param] = '#00E400'
            elif category_name[param] == 'Moderate':
                weather_color[param] = '#ffff00'
            elif category_name[param] == 'Unhealthy for Sensitive Groups':
                weather_color[param] = '#ff7e00'
            elif category_name[param] == 'Unhealthy':
                weather_color[param] = '#ff0000'
            elif category_name[param] == 'Very Unhealthy':
                weather_color[param] = '#8F3F97'
            else:
                weather_color[param] = '#7E0023'

            content[param] = reporting_area + ' -> ' + param + ', AQI: ' + str(str(aqi[param])) + ', Category: ' + category_name[param] + '           '

    except Exception:
        content['O3'] = "                                ERROR!!!                               "
        content['PM2.5'] = "                                ERROR!!!                               "
        content['PM10'] = "                                ERROR!!!                              "

    frame1.config(bg=weather_color['O3'])
    frame2.config(bg=weather_color['PM2.5'])
    frame3.config(bg=weather_color['PM10'])

    my_label1.config(text=content['O3'], background=weather_color['O3'])
    my_label2.config(text=content['PM2.5'], background=weather_color['PM2.5'])
    my_label3.config(text=content['PM10'], background=weather_color['PM10'])


frame1 = Frame(root, bg=weather_color['O3'])
frame1.grid(row=0, column=0, sticky=W + E)
frame2 = Frame(root, bg=weather_color['PM2.5'])
frame2.grid(row=1, column=0, sticky=W + E)
frame3 = Frame(root, bg=weather_color['PM10'])
frame3.grid(row=2, column=0, pady=(0, 10), sticky=W + E)

default_text = "                                                                              "

my_label1 = Label(frame1, text=default_text, background=weather_color['O3'], font=('Helvetica', 16))
my_label1.pack(padx=80, pady=10, anchor=W)
my_label2 = Label(frame2, text=default_text, background=weather_color['PM2.5'], font=('Helvetica', 16))
my_label2.pack(padx=80, pady=10, anchor=W)
my_label3 = Label(frame3, text=default_text, background=weather_color['PM10'], font=('Helvetica', 16))
my_label3.pack(padx=80, pady=10, anchor=W)

entry = Entry(root, justify='center')
entry.grid(row=3, column=0, pady=10, ipadx=30)

lookup_but = Button(root, text="Lookup Zipcode", command=look_zipcode)
lookup_but.grid(row=4, column=0, ipadx=15)

root.mainloop()
