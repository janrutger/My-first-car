import os.path as path
import utils
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

maxX = 640 #width of scene/PNG
maxY = 480 #heiht of scene/PNG
sceneMap = utils.makeScene(None, maxX, maxY)

HEIGHT = 800 #canvas win
WIDTH  = 800 #canvas win
width  = 10  #spot

listToDo = []
listDone = []

#CANVAS
win = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Map discovery")

#make Grid en find spot to start
grid = utils.makeGrid(HEIGHT, WIDTH, width)
startLocation = (320,240)
startSpot = utils.scanInit(sceneMap, startLocation, width, grid)
listToDo.append(startSpot)


#mapping Scene to Grid and show Grid on Canvas
run = True
while run:
    #pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if len(listToDo) > 0:
        thisSpot = listToDo[0]
        listToDo.pop(0)
        
        neighborsStatus = utils.findNeigbors(thisSpot, sceneMap, maxX, maxY)
        neighborSpots   = utils.updateNeigbors(grid, thisSpot, neighborsStatus)
        for neighborSpot in neighborSpots:
            if neighborSpot not in listToDo and neighborSpot not in listDone:
                listToDo.append(neighborSpot)          
        #print(neighbors)
        listDone.append(thisSpot)
    else:
        print("Finished")
        #utils.showGrid(win, grid)


    ##Some more code here
  
    utils.showGrid(win, grid)
    pygame.display.update() #update screen

pygame.quit()