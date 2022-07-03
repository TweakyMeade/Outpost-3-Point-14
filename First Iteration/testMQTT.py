import paho.mqtt.client as mqtt
import time
import datetime
client=mqtt.Client("test")
client.connect(host="192.168.1.178", port=1883)
while True:
    strn = f"test {datetime.datetime.now()}"
    client.publish("Weather",strn)
    print("sent")
    time.sleep(10)
