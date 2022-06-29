from tkinter import W
import weatherhat
import time
import datetime
import csv

outPost = weatherhat.WeatherHAT()
file = open('test.csv', mode=W)
recorder = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
recorder.writerow(['Date/Time', 'Temp', 'Humid', "Rain"])
file.close()
while True:
    outPost.update(interval=5)
    print(datetime.datetime.now())
    print(f"Temp: {outPost.temperature} Degrees Celc")
    print(f"Humid: {outPost.humidity}%")
    print(f"Rain: {outPost.rain}")
    time.sleep(5)


