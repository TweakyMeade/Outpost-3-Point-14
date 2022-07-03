import datetime 
import time
import weatherhat
import os
import dotenv
import paho.mqtt.client as mqtt
dotenv.load_dotenv()

outPost = weatherhat.WeatherHAT()
client=mqtt.Client()
client.connect(host=os.getenv("mqttHost"), port=int(os.getenv("mqttPort")))

while True:
    outPost.update(interval=5.0)
    datetimeATM= datetime.datetime.timestamp(datetime.datetime.now())
    tempR = outPost.temperature
    humidR = outPost.humidity
    presureR = outPost.pressure
    windSpeedR = outPost.wind_speed
    windDirectionR = outPost.wind_direction
    rainR = outPost.rain
    lightR = outPost.lux
    dewR = outPost.dewpoint
    totalRainR = outPost.rain_total
    payload = f'{{"Datetime":{datetimeATM}, "Temp":{tempR}, "Humidity":{humidR}, "Rain":{rainR}, "Windspeed":{windSpeedR}, "WindDir":{windDirectionR}, "DewPoint":{dewR}, "Light":{lightR}, "Presure":{presureR}}}'
    client.publish("Weather",payload)
    time.sleep(5)