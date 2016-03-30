#!/usr/bin/python
#
# Returns temperature and humidity reading of home lab closet
# using Adafruit_DHT library and DHT22 Sensor
#
# Usage: getlabtemp.py
#
# Displays Date/time, Temperature in Celsius, Tempature in Fahrenheit, and % Humidity
#
import Adafruit_DHT
import time

# Define Sensor Type
sensor = Adafruit_DHT.DHT22
# GPIO Pin Temperature Sensor is connected to
pin = 4
# High Temp Alert (F)
danger = 90

#Get Humidity and Temperature Reading
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#Did we get it?
if humidity is not None and temperature is not None:
   #convert to F
   tempfh = temperature * 1.8 + 32
   #Check to see if over danger temp
   if tempfh > danger:
      print("It's getting hot in here")
   #Date/Time
   dt = time.strftime("%m-%m-%Y %H:%M")
   print dt + ' - Temp={0:0.1f}*C Temp={1:0.1f}*F Humidity={2:0.1f}%'.format(temperature, tempfh, humidity)
else:
   print 'Failed to get reading from sensor. Try running this again!'
