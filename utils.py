import pygame
import os.path as path

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

X=0
Y=1

class Spot:
    def __init__(self, row, col, width):
        self.width =  width
        self.row = row
        self.col = col
        self.mapX = self.row * self.width
        self.mapY = self.col * self.width

        self.location = None
        self.color = GREY
        self.spotStatus = None
        self.neighbors = []


def makeGrid(HEIGHT, WIDTH, width):
    grid = []
    for row in range(0, HEIGHT // width):
        grid.append([])
        for col in range(0, WIDTH // width):
            spot = Spot(row, col, width)
            grid[row].append(spot)
    return(grid)

def showGrid(win, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            thisSpot = grid[i][j]
            pygame.draw.rect(win, thisSpot.color, (thisSpot.mapX, thisSpot.mapY, thisSpot.width, thisSpot.width))

    width = thisSpot.width
    for i in range(len(grid)):
        pygame.draw.line(win, WHITE, (0, i*width), (len(grid)*width, i*width))
        for j in range(len(grid[i])):
            pygame.draw.line(win, WHITE, (j*width, 0), (j*width, len(grid[i])*width ))


def scanInit(sceneMap, location, width, grid):
    row = location[X] // width
    col = location[Y] // width
    startSpot = grid[row][col]
    white = sceneMap[location] == WHITE
    if white.all():
        startSpot.color = WHITE
        startSpot.spotStatus = "open"
    else:
        print("ERROR: starting point non white")

    return(startSpot)


def findNeigbors(thisSpot, sceneMap, maxX, maxY):
    result = []
    width = thisSpot.width
    # up    = (thisSpot[X]*width, thisSpot[Y]*width-width)
    # right = (thisSpot[X]*width+width, thisSpot[Y]*width)
    # down  = (thisSpot[X]*width, thisSpot[Y]*width+width)
    # left  = (thisSpot[X]*width-width, thisSpot[Y]*width)
    up    = (thisSpot.mapX, thisSpot.mapY-width)
    right = (thisSpot.mapX+width, thisSpot.mapY)
    down  = (thisSpot.mapX, thisSpot.mapY+width)
    left  = (thisSpot.mapX-width, thisSpot.mapY)

    print("All new>>: ", up, right, down, left)

    for direction in [up, right, down, left]:
        white = sceneMap[direction] == WHITE
        black = sceneMap[direction] == BLACK

        #if white.all():
        #    result.append("open")
        if direction[X] - width < 0 or direction[X] + width >= maxX or direction[Y] - width < 0 or direction[Y] + width  >= maxY:
                result.append("blocked")
        elif white.all():
                result.append("open")
        elif black.all():
            result.append("blocked")
        else:
            print("COLOR MAPPING ERROR, blocked by default")
            result.append("blocked")
            print("current: ", thisSpot.row, thisSpot.col)
            print("current: ", thisSpot.mapX, thisSpot.mapY)
            print("All new: ", up, right, down, left)
            print("Result : ", result)
            color = sceneMap[direction]
            print("Color  : ", color)

    return(result)

def updateNeigbors(grid, thisSpot, neighbors):
    result = []

    #Direction is UP
    if neighbors[0] == "open": #UP
        grid[thisSpot.row][thisSpot.col-1].color = WHITE
        grid[thisSpot.row][thisSpot.col-1].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row, thisSpot.col-1))
        #result.append((thisSpot.row, thisSpot.col-1))
        result.append(grid[thisSpot.row][thisSpot.col-1])
    if neighbors[0] == "blocked": #UP
        grid[thisSpot.row][thisSpot.col-1].color = BLACK
        grid[thisSpot.row][thisSpot.col-1].spotStatus = "blocked"

    #Direction is RIGHT
    if neighbors[1] == "open": #RIGHT
        grid[thisSpot.row+1][thisSpot.col].color = WHITE
        grid[thisSpot.row+1][thisSpot.col].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row+1, thisSpot.col))
        #result.append((thisSpot.row+1, thisSpot.col))
        result.append(grid[thisSpot.row+1][thisSpot.col])
    if neighbors[1] == "blocked": #RIGHT
        grid[thisSpot.row+1][thisSpot.col].color = BLACK
        grid[thisSpot.row+1][thisSpot.col].spotStatus = "blocked"

    #Direction is DOWN
    if neighbors[2] == "open": #DOWN
        grid[thisSpot.row][thisSpot.col+1].color = WHITE
        grid[thisSpot.row][thisSpot.col+1].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row, thisSpot.col+1))
        #result.append((thisSpot.row, thisSpot.col+1))
        result.append(grid[thisSpot.row][thisSpot.col+1])
    if neighbors[2] == "blocked": #DOWN
        grid[thisSpot.row][thisSpot.col+1].color = BLACK
        grid[thisSpot.row][thisSpot.col+1].spotStatus = "blocked"

    #Direction is LEFT
    if neighbors[3] == "open": #LEFT
        grid[thisSpot.row-1][thisSpot.col].color = WHITE
        grid[thisSpot.row-1][thisSpot.col].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row-1, thisSpot.col))
        #result.append((thisSpot.row-1, thisSpot.col))
        result.append(grid[thisSpot.row-1][thisSpot.col])
    if neighbors[3] == "blocked": #LEFT
        grid[thisSpot.row-1][thisSpot.col].color = BLACK
        grid[thisSpot.row-1][thisSpot.col].spotStatus = "blocked"
    return(result)    

def makeScene(fileName, maxX, maxY):
    pygame.init()
    win = pygame.display.set_mode((maxX,maxY))
    pygame.display.set_caption("Create scenemap")

    if path.isfile("images/cirkelsGG.png"):
        image = pygame.image.load("images/cirkels.png")
    else:
        image = None

    run = True
    while run:
        win.fill((0,0,0))  # Fills the screen with black 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if image != None:
            win.blit(image, (0,0))
        else:
            #pygame.draw.rect(win, (255,255,255), (40,40,560,400), 0)
            pygame.draw.rect(win, (255,255,255), (20,20,600,440), 0)
            pygame.draw.rect(win, (0,0,0), (80,125,40,100), 0)
            pygame.draw.rect(win, (0,0,0), (150,300,40,100), 0)
            pygame.draw.rect(win, (0,0,0), (430,120,30,100), 0)
            pygame.draw.rect(win, (0,0,0), (300,0,50,150), 0)
            pygame.draw.rect(win, (0,0,0), (380,375,125,30), 0)
            pygame.draw.rect(win, (0,0,0), (320, 250, 40,40), 0)
            pygame.draw.rect(win, (0,0,0), (180, 200, 40,40), 0)
            pygame.draw.rect(win, (0,0,0), (500, 300, 20,20), 0)
            pygame.draw.rect(win, (0,0,0), (500, 150, 20,20), 0)

        sceneMap = pygame.surfarray.array3d(win)
        pygame.display.update() #update screen
    pygame.quit()

    return(sceneMap)