import datetime 
import time
import weatherhat
import os
import paho.mqtt.client as mqtt

"""
These Variables are configurable.
I personally like storing server information in .env files but its not required
Remove dotenv within the code below and plug the ip and port straight into mqttHost and mqttPort

"""
import dotenv
dotenv.load_dotenv()
waitingBuffTime = 5
userInterval = 30
mqttHost = str(os.getenv("mqttHost"))
mqttPort = int(os.getenv("mqttPort"))
mqttTopic = "Weather"

"""
Setting up the Weatherhat and MQTT as easily understandable Classes
"""
outPost = weatherhat.WeatherHAT()
client=mqtt.Client()
client.connect(host=mqttHost, port=mqttPort)
print(f"Currently connecting to Database {mqttHost} on Port {mqttPort}. \nstart pumping weather data in {waitingBuffTime} seconds with {userInterval} second Intervals")
time.sleep(waitingBuffTime)
"""
while Loop to push data to the server
"""
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
    client.publish(mqttTopic,payload)
    time.sleep(30)