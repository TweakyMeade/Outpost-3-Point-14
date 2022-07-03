from datetime import date
import time, weatherhat, csv, os
def printData(dI,tI,tpI,hI,rI,wI,wdI):
    print(f"Date:{dI}, Time:{tI}, Temp:{tpI}, Humidity:{hI}, Rain:{rI}, Windspeed:{wI}, WindDir:{wdI}")
outPost = weatherhat.WeatherHAT()

while True:
    dateATM = date.today()
    timeATM = time.strftime("%H:%M:%S")
    outPost.update(interval=5.0)
    tempR = outPost.temperature
    humidR = outPost.humidity
    windSpeedR = outPost.wind_speed
    windDirectionR = outPost.wind_direction
    rainR = outPost.rain
    recorder = csv.writer(open(f"{dateATM}.csv", "a"), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    recorder.writerow([dateATM,timeATM,tempR,humidR,rainR,windSpeedR,windDirectionR])

    printData(dateATM,timeATM,tempR,humidR,rainR,windSpeedR,windDirectionR)
    time.sleep(5)