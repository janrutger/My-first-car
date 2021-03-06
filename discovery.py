import utils
import astar
import os.path as path
import pygame
pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

maxX = 640 #width of scene/PNG
maxY = 480 #heiht of scene/PNG
sceneMap = utils.makeScene(None, maxX, maxY)

WIDTH  = 700 #canvas win X-ax
HEIGHT = 500 #canvas win Y-ax
width  = 5   #spot

listToDo = []
listDone = []

#CANVAS
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Map discovery")

#make Grid en find spot to start
grid = utils.makeGrid(WIDTH, HEIGHT, width)
startLocation = (360,240)
startSpot = utils.scanInit(sceneMap, startLocation, width, grid)
listToDo.append(startSpot)


gridReady = False
run = True

while run and not gridReady:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(listToDo) > 0:
        thisSpot = listToDo[0]
        listToDo.pop(0)
        
        neighborsStatus = utils.findNeigborsStatus(thisSpot, sceneMap, maxX, maxY)
        neighborSpots   = utils.setNeigbors(grid, thisSpot, neighborsStatus)
        for neighborSpot in neighborSpots:
            if neighborSpot not in listToDo and neighborSpot not in listDone:
                listToDo.append(neighborSpot)          
        #print(neighbors)
        listDone.append(thisSpot)
        #utils.showGrid(win, grid)
    else:
        print("Finished")
        gridReady = True
        utils.showGrid(win, grid)
        pygame.display.set_caption("A* Path Finding Algorithm")
        start = None
        end = None
        utils.traceNeigbors(grid)

utils.makeBorder(grid)

while run and gridReady:
    utils.showGrid(win, grid)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]: # LEFT
            pos = pygame.mouse.get_pos()
            row, col = utils.get_clicked_pos(pos, width)
            spot = grid[row][col]
            if not start and spot != end:
                start = spot
                #start.make_start()
                start.color = RED

            elif not end and spot != start:
                end = spot
                end.color = GREEN
                #end.make_end()

        elif pygame.mouse.get_pressed()[2]: # RIGHT
            pos = pygame.mouse.get_pos()
            row, col = utils.get_clicked_pos(pos, width)
            spot = grid[row][col]
            spot.color = WHITE
            #spot.reset()
            if spot == start:
                start = None
            elif spot == end:
                end = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start and end:
                #algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                #route = astar.algorithm(lambda: utils.showGrid(win, grid), grid, start, end)
                route = astar.algorithm(lambda: utils.showGridStub(), grid, start, end)


from car import Car

win = pygame.display.set_mode((maxX,maxY))
#win = pygame.make_surface(sceneMap)
pygame.display.set_caption("Drive the Car")

runRoute = True
index = 0
route.reverse()
car = Car(route[0], width)
while runRoute:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runRoute = False

    if index < len(route)-1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.time.delay(250)
        pygame.surfarray.blit_array(win, sceneMap)

        ## Get the Car coordinates & Draw the car

        #car.botNextStepNormal(route[index])
        car.botNextStepSmooth(route[index+1])
        Coordinates = car.botCoordinates() # 0=frontleft, 1=frontright
        #print(Coordinates)
        pygame.draw.polygon(win,(0,0,255), Coordinates, 0) #draw de car
        pygame.draw.circle(win, (255,0,0), Coordinates[0], 3, 0)
        pygame.draw.circle(win, (0,255,0), Coordinates[1], 3, 0)
        
        pygame.display.update() #update screen
    
    index = index +1
    if index == len(route)-1:
        index=0
        car.botCenter = route[0].center


        

    
    # for step in reversed(route):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()

    #     pygame.time.delay(250)
    #     pygame.surfarray.blit_array(win, sceneMap)
    #     ## Get the Car coordinates & Draw the car
    #     car.botNextStep(step)
    #     Coordinates = car.botCoordinates() # 0=frontleft, 1=frontright
    #     #print(Coordinates)
    #     pygame.draw.polygon(win,(0,0,255), Coordinates, 0) #draw de car
    #     pygame.draw.circle(win, (255,0,0), Coordinates[0], 3, 0)
    #     pygame.draw.circle(win, (0,255,0), Coordinates[1], 3, 0)
        
    #     pygame.display.update() #update screen

pygame.quit()


