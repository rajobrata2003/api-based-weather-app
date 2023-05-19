from tkinter import *
from tkinter import messagebox

import requests 
from configparser import ConfigParser

# config file
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']



# weather calculation
def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_k = json['main']['temp']
        temp_c = temp_k - 273.15
        temp_f = temp_c * 9 /5 + 32
        weather = json['weather'][0]['main']
        weather_desc = json['weather'][0]['description']
        final = (city, country, temp_c, temp_f,weather)
        return final
    else:
        return None

    

def search():
    city=city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = '{:.2f}C, {:.2f}F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[4]
    else:
        messagebox.showerror('Error', 'Cannot find specified city');



app = Tk()
app.title("Weather App")
app.geometry('800x400')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search city", width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold',20))
location_lbl.pack()

temp_lbl = Label(app, text='');
temp_lbl.pack()

weather_lbl = Label(app, text='');
weather_lbl.pack()        

app.mainloop()
