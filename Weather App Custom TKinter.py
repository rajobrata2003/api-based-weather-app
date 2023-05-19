from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

import customtkinter

import requests 
from configparser import ConfigParser




#icons


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
    print(weather)
    if weather:
        location_lbl.configure(text = '{}, {}'.format(weather[0], weather[1]))
        temp_lbl.configure(text = '{:.2f}C, {:.2f}F'.format(weather[2], weather[3]))
        weather_lbl.configure(text=weather[4])
        print(weather[4])
        if(weather[4]=="Clouds"):
            search_btn.configure(image=cloudy_image)
        elif(weather[4]=="Thunderstorm"):
            search_btn.configure(image=thunder_image)
        elif(weather[4]=="Drizzle"):
            search_btn.configure(image=drizzle_image)
        elif(weather[4]=="Rain"):
            search_btn.configure(image=rain_image)
        elif(weather[4]=="Clear"):
            search_btn.configure(image=clear_image)
        elif(weather[4]=="Haze"):
            search_btn.configure(image=haze_image)
        else:
             search_btn.configure(image=None)
        search_btn._draw()
        
        
    else:
        messagebox.showerror('Error', 'Cannot find specified city');




#customtkinter

customtkinter.set_appearance_mode("dark");
customtkinter.set_default_color_theme("dark-blue");


app = customtkinter.CTk()
app.title("Weather App")
app.geometry('480x600')


frame = customtkinter.CTkFrame(master=app)
#frame.pack(pady=20, padx=60, fill="both", expand=True)
frame.place(relx=.5, rely=.45, anchor= CENTER)

#IMAGES

cloudy_image = customtkinter.CTkImage(Image.open("Images/clouds.png"),size=(30, 30))
thunder_image = customtkinter.CTkImage(Image.open("Images/thunder.jpg"),size=(30, 25))
drizzle_image = customtkinter.CTkImage(Image.open("Images/drizzle.png"),size=(30, 30))
rain_image = customtkinter.CTkImage(Image.open("Images/rain.png"),size=(30, 30))
clear_image = customtkinter.CTkImage(Image.open("Images/clear.png"),size=(30, 30))
haze_image = customtkinter.CTkImage(Image.open("Images/haze.jpg"),size=(30, 30))


#Main UI

title = customtkinter.CTkLabel(master=frame, text="Welcome to Weather App",font=('Times', 24))
title.pack(pady=12, padx=10)

city_text = StringVar()
city_entry = customtkinter.CTkEntry(master=frame, textvariable=city_text, width=200)
city_entry.pack(pady=12, padx=10)





search_btn = customtkinter.CTkButton(master=frame, text="Search City",image=None, width=120, height=35, command=search)
search_btn.pack(pady=12, padx=10)

location_lbl = customtkinter.CTkLabel(master=frame, text='', font=('bold',20))
location_lbl.pack(pady=12, padx=10)

temp_lbl = customtkinter.CTkLabel(master=frame, text='') 
temp_lbl.pack(pady=12, padx=10)

weather_lbl = customtkinter.CTkLabel(master=frame, text='')
weather_lbl.pack(pady=12, padx=10)        

app.mainloop()
