import datetime 
import time
import weatherhat
import paho.mqtt.client as mqtt

def printData(dtI,tpI,hI,rI,wI):
    print(f'"Datetime:{dtI}, "Temp":{tpI}, "Humidity":{hI}, "Rain":{rI}, "Windspeed":{wI}')

outPost = weatherhat.WeatherHAT()
client=mqtt.Client("test")
client.connect(host="192.168.1.178", port=1883)

while True:
    outPost.update(interval=5.0)
    datetimeATM= datetime.datetime.timestamp(datetime.datetime.now())
    tempR = outPost.temperature
    humidR = outPost.humidity
    windSpeedR = outPost.wind_speed
    windDirectionR = outPost.wind_direction
    rainR = outPost.rain
    payload = f'{{"Datetime":{datetimeATM}, "Temp":{tempR}, "Humidity":{humidR}, "Rain":{rainR}, "Windspeed":{windSpeedR}, "WindDir":{windDirectionR}}}'

    client.publish("Weather",payload)
    time.sleep(5)