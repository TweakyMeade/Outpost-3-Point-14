from datetime import date
import json
import time
import weatherhat
import csv
def printData(dI,tI,tpI,hI,rI,wI):
    print(f'"Date":f{dI}, "Time":{tI}, "Temp":{tpI}, "Humidity":{hI}, "Rain":{rI}, "Windspeed":{wI}')
def payloadData(dI,tI,tpI,hI,rI,wI):
    jsonformat = f'"Date":{dI}, "Time":{tI}, "Temp":{tpI}, "Humidity":{hI}, "Rain":{rI}, Windspeed":{wI}'
    return jsonformat
        
outPost = weatherhat.WeatherHAT()
import paho.mqtt.client as mqtt
import time
import datetime
client=mqtt.Client("test")
client.connect(host="192.168.1.178", port=1883)

for i in range(1,3):
    dateATM = date.today()
    timeATM = time.strftime("%H:%M:%S")
    outPost.update(interval=5.0)
    tempR = outPost.temperature
    humidR = outPost.humidity
    windSpeedR = outPost.wind_speed
    windDirectionR = outPost.wind_direction
    rainR = outPost.rain
    payload ="{" + payloadData(dateATM,timeATM,tempR,humidR,rainR,windSpeedR) + "}"
    print(payload)
    print("{"+ payload + "}")
    #printData(dateATM,timeATM,tempR,humidR,rainR,windSpeedR)
    client.publish("Weather",f"{payload}")
    time.sleep(5)