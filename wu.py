################################################################
# wu.py
# Get Weather Info using the Weather Underground's API
# Dipslay Weather in a Window created using Tkinter
#
# Set wu_api to your Weather Underground API Key
# Set wu_state and wu_city to pull weather for your location
#
# http://www.vhersey.com
#
################################################################
import base64
import time
import requests

try:
    # Linux/Raspberry Pi
    import Tkinter as tk
except ImportError:
    # Windows
    import tkinter as tk

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


# Weather Underground API 
# Get your API key here: https://www.wunderground.com/weather/api/?apiref=cfe61f63df094ac0
wu_api = "PUTYOURAPIKEYHERE"
wu_state = "VA"
wu_city = "Suffolk"

# API Delay in Milliseconds - Remember you only get 500 calls per day for free
# 600000 = 10 Minutes
api_delay = "600000"

# Build the url to get weather information
wu_uri = "http://api.wunderground.com/api/"+wu_api+"/conditions/q/"+wu_state+"/"+wu_city+".json"

# Use Tkinter to create the Window
root = tk.Tk()
root.title("Weather")
root.geometry("350x150+300+300")

# Create a frame
frame = tk.Frame(root)
frame.pack()

# Label laceholders in the frame
wuLocation = tk.Label(frame, text='Location')
wuLocation.pack()
wuTime = tk.Label(frame, text='Time')
wuTime.pack()
wuIcon = tk.Label(frame, image='')
wuIcon.pack()
wuConditions = tk.Label(frame, text='Conditions')
wuConditions.pack()
wuTempf = tk.Label(frame, text='Tempf')
wuTempf.pack()
wuHumidity = tk.Label(frame, text='Humidity')
wuHumidity.pack()

def wuGet():

    # Request the weather info from Weather Underground
    wu_req = requests.get(wu_uri)
    data = wu_req.json()

    # Pull out the useful info
    current_weather =  data['current_observation']['weather']
    obs_conditions = "Current Conditions: "+current_weather
    obs_location = "Weather for "+str(data['current_observation']['display_location']['full'])
    obs_time = str(data['current_observation']['observation_time'])
    current_tempf = str(data['current_observation']['temp_f'])
    obs_tempf = "Current Temperature: "+current_tempf+" F"
    obs_humidity = "Relative Humidity: "+str(data['current_observation']['relative_humidity'])
    icon_url = data['current_observation']['icon_url']

    # Get the weather icon from the icon_url
    image_byt = urlopen(icon_url).read()
    image_b64 = base64.encodestring(image_byt)
    photo = tk.PhotoImage(data=image_b64)

    # Update the Labels with the Weather
    wuLocation.config(text=obs_location)
    wuTime.config(text=obs_time)
    wuIcon.image = photo
    wuIcon.config(image=photo)
    wuConditions.config(text=obs_conditions)
    wuTempf.config(text=obs_tempf)
    wuHumidity.config(text=obs_humidity)

    # Wait for the delay, next verse same as the first
    frame.after(api_delay, wuGet)


# Call wuGet to get the first update
wuGet()

root.mainloop()
