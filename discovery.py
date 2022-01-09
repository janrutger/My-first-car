import os.path as path
import utils
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

sceneMap = utils.makeScene(None)

HEIGHT = 800
WIDTH  = 800
width  = 20

listToDo = []
listDone = []

win = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Map discovery")

grid = utils.makeGrid(HEIGHT, WIDTH, width)
sceneLocation = (100,150)
position, color = utils.scanInit(sceneMap, sceneLocation, width)
grid[position[0]][position[1]].color = color
grid[position[0]][position[1]].spotStatus = "open"
listToDo.append(position)



run = True
while run:
    pygame.time.delay(300)

    manualCommand = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if len(listToDo) > 0:
        thisSpot = listToDo[0]
        listToDo.pop(0)
        print(thisSpot)
        neighbors = utils.findNeigbors(thisSpot, sceneMap, width)
        neighborSpots = utils.updateNeigbors(grid, thisSpot, neighbors)
        for neighborSpot in neighborSpots:
            if neighborSpot not in listToDo and neighborSpot not in listDone:
                listToDo.append(neighborSpot)          
        print(neighbors)
        listDone.append(thisSpot)
    else:
        print("Finished")


    ##Some more code here
  
    utils.showGrid(win, grid, width)
    pygame.display.update() #update screen

pygame.quit()