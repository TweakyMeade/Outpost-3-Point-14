from influxdb import InfluxDBClient
client = InfluxDBClient(host='argon', port=8086)
print(client.get_list_database())
client.switch_database('weatherstation')
results = client.query('SELECT Temp FROM Shed ORDER BY DESC LIMIT 1')
for result in results:
    print("Result: {0}".format(result))