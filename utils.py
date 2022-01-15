import pygame
import os.path as path

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

X=0
Y=1

class Spot:
    def __init__(self, row, col, width):
        self.width =  width
        self.row = row
        self.col = col
        self.mapX = self.row * self.width
        self.mapY = self.col * self.width
        self.center = (self.mapX + self.width//2, self.mapY + self.width//2)

        self.color = GREY
        self.spotStatus = None
        self.neighbors = []


def makeGrid(WIDTH,HEIGHT, width):
    grid = []
    for row in range(0, WIDTH // width):
        grid.append([])
        for col in range(0, HEIGHT // width):
            spot = Spot(row, col, width)
            grid[row].append(spot)
    return(grid)

def showGrid(win, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            thisSpot = grid[i][j]
            pygame.draw.rect(win, thisSpot.color, (thisSpot.mapX, thisSpot.mapY, thisSpot.width, thisSpot.width))

    width = thisSpot.width
    lenRow = len(grid)  #this code is just working, it not correct i think
    for row in range(lenRow):
        lenHeight = len(grid[row])
        pygame.draw.line(win, WHITE, (0, row*width), ((lenRow*width, row*width))) #Horizental
    for col in range(lenRow):
        pygame.draw.line(win, WHITE, ( col*width, 0), ( col*width, lenHeight*width+width) ) #Vertikaal
            
    pygame.display.update() #update screen



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


def findNeigborsStatus(thisSpot, sceneMap, maxX, maxY):
    result = []
    width = thisSpot.width
    up    = (thisSpot.mapX, thisSpot.mapY-width)
    right = (thisSpot.mapX+width, thisSpot.mapY)
    down  = (thisSpot.mapX, thisSpot.mapY+width)
    left  = (thisSpot.mapX-width, thisSpot.mapY)

    lUp    = (thisSpot.mapX-width, thisSpot.mapY-width)
    rUp    = (thisSpot.mapX+width, thisSpot.mapY-width)
    rDown  = (thisSpot.mapX+width, thisSpot.mapY+width)
    lDown  = (thisSpot.mapX-width, thisSpot.mapY+width)

    print("All new>>: ", up, right, down, left, lUp, rUp, rDown, lDown)

    for direction in [up, right, down, left, lUp, rUp, rDown, lDown]:
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

def getNeigbors(grid, thisSpot):
    upSpot    = grid[thisSpot.row][thisSpot.col-1]
    rightSpot = grid[thisSpot.row+1][thisSpot.col]
    downSpot  = grid[thisSpot.row][thisSpot.col+1]
    leftSpot  = grid[thisSpot.row-1][thisSpot.col]

    lUpSpot    = grid[thisSpot.row-1][thisSpot.col-1]
    rUpSpot    = grid[thisSpot.row+1][thisSpot.col-1]
    rDwnSpot   = grid[thisSpot.row+1][thisSpot.col+1]
    lDownSpot  = grid[thisSpot.row-1][thisSpot.col+1]
    return((upSpot, rightSpot, downSpot, leftSpot, lUpSpot, rUpSpot, rDwnSpot, lDownSpot))

def traceNeigbors(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            thisSpot = grid[row][col]
            if thisSpot.spotStatus == "open":
                thisSpot.neighbors = []
                thatSpots = getNeigbors(grid,thisSpot)
                for thatSpot in thatSpots:
                    if thatSpot.spotStatus == "open":
                        thisSpot.neighbors.append(thatSpot)

def makeBorder(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            thisSpot = grid[row][col]
            if thisSpot.spotStatus == "open":
                if len(thisSpot.neighbors) < 8:
                    thisSpot.color = YELLOW
                    thisSpot.spotStatus = "blocked"

    traceNeigbors(grid)


def setSpot(thatSpot, thisSpot, neighborsStatus, neighborSpots):
    if neighborsStatus == "open":
        thatSpot.spotStatus = "open"
        thatSpot.color = WHITE
        thisSpot.neighbors.append(thatSpot)
        neighborSpots.append(thatSpot)
    elif neighborsStatus == "blocked":
        thatSpot.spotStatus = "blocked"
        thatSpot.color = BLACK
    return(neighborSpots)



def setNeigbors(grid, thisSpot, neighborsStatus):
    neighborSpots = []
    spots = getNeigbors(grid, thisSpot)

    for i in range(len(spots)):
    #for i in range(4):
       neighborSpots = setSpot(spots[i], thisSpot, neighborsStatus[i], neighborSpots) 


    # neighborSpots = setSpot(spots[0], thisSpot, neighborsStatus[0], neighborSpots)
    # neighborSpots = setSpot(spots[1], thisSpot, neighborsStatus[1], neighborSpots)
    # neighborSpots = setSpot(spots[2], thisSpot, neighborsStatus[2], neighborSpots)
    # neighborSpots = setSpot(spots[3], thisSpot, neighborsStatus[3], neighborSpots)
    return(neighborSpots)



def makeScene(fileName, maxX, maxY):
    pygame.init()
    win = pygame.display.set_mode((maxX,maxY))
    pygame.display.set_caption("Create scenemap")

    if path.isfile("images/JR-Straat.png"):
        image = pygame.image.load("images/JR-Straat.png")
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


def get_clicked_pos(pos, width):
    y, x = pos

    row = y // width
    col = x // width

    return row, col