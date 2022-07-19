from influxdb import InfluxDBClient
import time
import pygame #I know, Trust me this is the best Libary for the GUI i want

def gen2dict(gen):
    #a lazy method just to convert generator to dictionary
    for i in gen:
        return i

pygame.init()
pygame.font.init()
pygame.display.set_caption('Scorchio!')
programFont=pygame.font.SysFont("Helvetica",20) 
client = InfluxDBClient('argon', 8086, database="Weather")
displaydm = (500,500) #width, height
screen = pygame.display.set_mode(displaydm)
rawArrow = pygame.image.load("arrow.png")
arrow = pygame.transform.scale(rawArrow, (50, 70))

Flag=True
while Flag:
    initresult = client.query('SELECT * FROM Shed ORDER BY DESC LIMIT 1;')
    result = initresult.get_points(measurement="Shed")
    dictresult = gen2dict(result)
    Temprature = dictresult["Temp"]
    Humidity = dictresult["Humidity"]
    Windspeed = dictresult["Windspeed"]

    screen.fill((255,255,255))
    rTemp=programFont.render(f"Temp: {Temprature}", True, "Black")
    rHumid=programFont.render(f"Humidity: {Humidity}", True, "Black")
    rWS=programFont.render(f"Windspeed: {Windspeed}", True, "Black")
    rWD=programFont.render(f"WindDir: {dictresult['WindDir']}", True, "Black")
    rDT=programFont.render(f"Datetime: {dictresult['Datetime']}", True, "Black")
    
    try:
        rArrow = pygame.transform.rotate(arrow,-dictresult["WindDir"])
        screen.blit(rArrow,(225,300))
    except:
        print(dictresult['WindDir'])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Flag = False
    screen.blit(rTemp,(20,10))
    screen.blit(rHumid,(20,30))
    screen.blit(rWS,(20,50 ))
    screen.blit(rWD,(20,70 ))
    screen.blit(rDT,(20,470 ))
    pygame.display.flip()