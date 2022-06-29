import weatherhat
import time
import datetime
import csv
flag = True
outPost = weatherhat.WeatherHAT()

while True:
    file = open('test.csv', "a")
    recorder = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if flag == True:
        recorder.writerow(['Date/Time', 'Temp', 'Humid', "Rain"])
        flag = False
    outPost.update(interval=5)
    recorder.writerow([datetime.datetime.now(), outPost.temperature, outPost.humidity, outPost.rain])
    #print(datetime.datetime.now())
    #print(f"Temp: {outPost.temperature} Degrees Celc")
    #print(f"Humid: {outPost.humidity}%")
    #print(f"Rain: {outPost.rain}")
    file.close()
    time.sleep(5)


