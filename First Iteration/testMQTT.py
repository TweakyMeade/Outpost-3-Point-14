import paho.mqtt.client as mqtt
import time
import datetime
import dotenv
import os
dotenv.load_dotenv()
client=mqtt.Client("test")

client.connect(host=os.getenv("mqttHost"), port=int(os.getenv("mqttPort")))
while True:
    strn = f"test {datetime.datetime.now()}"
    client.publish("Test",strn)
    print("sent")
    time.sleep(10)
