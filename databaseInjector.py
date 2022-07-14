import datetime 
import time
import weatherhat
import os
import dotenv
import paho.mqtt.client as mqtt
dotenv.load_dotenv()
waitingBuffTime = 5
userInterval = 30
mqttHost = str(os.getenv("mqttHost"))
mqttPort = int(os.getenv("mqttPort"))
outPost = weatherhat.WeatherHAT()
client=mqtt.Client()
client.connect(host=mqttHost, port=mqttPort)
print(f"Currently connecting to Database {mqttHost} on Port {mqttPort}. \nstart pumping weather data in {waitingBuffTime} seconds with {userInterval} second Intervals")
time.sleep(waitingBuffTime)
while True:
    outPost.update(interval=userInterval)
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
    time.sleep(30)