
from influxdb import InfluxDBClient
import time

def gen2dict(gen):
    #a lazy method just to convert generator to dictionary
    for i in gen:
        return i

client = InfluxDBClient('argon', 8086, database="Weather")
    #client.switch_database('Weather')
while True:
    initresult = client.query('SELECT * FROM Shed ORDER BY DESC LIMIT 1;')
    result = initresult.get_points(measurement="Shed")
    dictresult = gen2dict(result)
    print(dictresult["Temp"])
    print(dictresult["Windspeed"])
    time.sleep(3)