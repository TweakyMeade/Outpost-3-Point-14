from influxdb import InfluxDBClient
import time
import pygame #I know, Trust me this is the best Libary for the GUI i want

def gen2dict(gen):
    #a lazy method just to convert generator to dictionary
    for i in gen:
        return i
def textRender(iDict,w,h):
    hOffset = h
    for i in iDict.keys():
        screen.blit(programFont.render(f"{i}: {dictresult[i]}", True, "Red"),(w,hOffset))
        hOffset += 20

        
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
    dictresult = gen2dict(initresult.get_points(measurement="Shed"))
    screen.fill((255,255,255))
    try:
        rArrow = pygame.transform.rotate(arrow,-dictresult["WindDir"])
        screen.blit(rArrow,(225,300))
    except:
        pass
    dictresult.pop("WindDir")
    textRender(dictresult,10,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Flag = False
    pygame.display.flip()