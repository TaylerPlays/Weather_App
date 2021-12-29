from tkinter import *
from tkinter.font import BOLD
from dotenv import load_dotenv
import os
from PIL import ImageTk, Image
import requests

load_dotenv()

HEIGHT = 500
WIDTH = 600

app = Tk()
app.title("Tayler's Weather App")

def format_reponse(weather):
    try:
        name = (weather['name'])
        country = (weather['sys']['country'])
        desc = (weather['weather'][0]['description'])
        tempc = (weather['main']['temp'])
        tempf = (tempc) * 9 / 5 + 32
        humidity = (weather['main']['humidity'])

        finalstr = 'City: %s \nCountry: %s \nConditions: %s \nTemperature(C): %s \nTemperature(F): %s \nHumidity: %s' % (name,country, desc, tempc, tempf, humidity)
    
    except:
        finalstr = 'There was an error retrieving the information.'

    return finalstr

def get_weather(city):
    WEATHER_KEY = os.getenv('WEATHER_KEY')
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'appid': WEATHER_KEY, 'q': city, 'units' : 'metric'}
    response = requests.get(url, params = params)
    weather = response.json()

    label['text'] = format_reponse(weather)



canvas = Canvas(app, height= HEIGHT, width= WIDTH)
canvas.pack()

background_img = PhotoImage(file = 'landscape.png')
background_label = Label(app, image = background_img)
background_label.place(x = 0, y = 0, relwidth=1, relheight=1)

frame = Frame(app, bg = '#80c1ff', bd=5)
frame.place(relx=0.5 , rely = 0.1 ,relheight= 0.1, relwidth= 0.75, anchor='n')

entry = Entry(frame, font = ('Courier', 18))
entry.place(relwidth=0.67, relheight= 1)

button = Button(frame, text = "Get Weather", font = ('Courier', 12), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7,relwidth=0.3, relheight=1)

lower_frame = Frame(app, bg ='#80c1ff', bd=10)
lower_frame.place(relx =0.5, rely = 0.25, relwidth= 0.75, relheight= 0.6, anchor= 'n')

label = Label(lower_frame, font = ('Courier', 18), anchor= 'nw', justify = 'left', bd = 4, background='white')
label.place(relwidth= 1, relheight=1)


app.mainloop()

