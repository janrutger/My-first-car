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

def showGrid(win, grid, width):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            thisSpot = grid[i][j]
            pygame.draw.rect(win, thisSpot.color, (thisSpot.mapX, thisSpot.mapY, thisSpot.width, thisSpot.width))

    for i in range(len(grid)):
        pygame.draw.line(win, WHITE, (0, i*width), (len(grid)*width, i*width))
        for j in range(len(grid[i])):
            pygame.draw.line(win, WHITE, (j*width, 0), (j*width, len(grid[i])*width ))


def scanInit(sceneMap, location, width):
    row = location[X] // width
    col = location[Y] // width
    white = sceneMap[location] == WHITE
    if white.all():
        color = WHITE
    else:
        print("ERROR: starting point non white")
        color = GREY

    return((row, col), color)


def findNeigbors(thisSpot, sceneMap, width):
    result = []
    up    = (thisSpot[X]*width, thisSpot[Y]*width-width)
    right = (thisSpot[X]*width+width, thisSpot[Y]*width)
    down  = (thisSpot[X]*width, thisSpot[Y]*width+width)
    left  = (thisSpot[X]*width-width, thisSpot[Y]*width)

    print(up, right, down, left)

    for direction in [up, right, down, left]:
        white = sceneMap[direction] == WHITE
        black = sceneMap[direction] == BLACK

        color = sceneMap[direction]
        print(color)


        if white.all():
            result.append("open")
        elif black.all():
            result.append("blocked")
        else:
            print("COLOR MAPPING ERROR, blocked by default")
            #result.append("blocked")

    return(result)

def updateNeigbors(grid, thisSpot, neighbors):
    result = []
    thisSpot=grid[thisSpot[X]][thisSpot[Y]]
    print(thisSpot.row, thisSpot.col)
    if neighbors[0] == "open": #UP
        grid[thisSpot.row][thisSpot.col-1].color = WHITE
        grid[thisSpot.row][thisSpot.col-1].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row, thisSpot.col-1))
        result.append((thisSpot.row, thisSpot.col-1))
    if neighbors[0] == "blocked": #UP
        grid[thisSpot.row][thisSpot.col-1].color = BLACK
        grid[thisSpot.row][thisSpot.col-1].spotStatus = "blocked"

    if neighbors[1] == "open": #RIGHT
        grid[thisSpot.row+1][thisSpot.col].color = WHITE
        grid[thisSpot.row+1][thisSpot.col].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row+1, thisSpot.col))
        result.append((thisSpot.row+1, thisSpot.col))
    if neighbors[1] == "blocked": #RIGHT
        grid[thisSpot.row+1][thisSpot.col].color = BLACK
        grid[thisSpot.row+1][thisSpot.col].spotStatus = "blocked"

    if neighbors[2] == "open": #DOWN
        grid[thisSpot.row][thisSpot.col+1].color = WHITE
        grid[thisSpot.row][thisSpot.col+1].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row, thisSpot.col+1))
        result.append((thisSpot.row, thisSpot.col+1))
    if neighbors[2] == "blocked": #DOWN
        grid[thisSpot.row][thisSpot.col+1].color = BLACK
        grid[thisSpot.row][thisSpot.col+1].spotStatus = "blocked"

    if neighbors[3] == "open": #LEFT
        grid[thisSpot.row-1][thisSpot.col].color = WHITE
        grid[thisSpot.row-1][thisSpot.col].spotStatus = "open"
        grid[thisSpot.row][thisSpot.col].neighbors.append((thisSpot.row-1, thisSpot.col))
        result.append((thisSpot.row-1, thisSpot.col))
    if neighbors[3] == "blocked": #LEFT
        grid[thisSpot.row-1][thisSpot.col].color = BLACK
        grid[thisSpot.row-1][thisSpot.col].spotStatus = "blocked"
    return(result)    

def makeScene(fileName):
    pygame.init()
    win = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Create scenemap")

    run = True
    while run:
        win.fill((0,0,0))  # Fills the screen with black 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if path.isfile("images/cirkels1.png"):
            image = pygame.image.load("images/cirkels.png")
            win.blit(image, (0,0))
        else:
            #pygame.draw.rect(win, (255,255,255), (40,40,560,400), 0)
            pygame.draw.rect(win, (255,255,255), (20,20,600,440), 0)
            # pygame.draw.rect(win, (0,0,0), (80,125,40,100), 0)
            # pygame.draw.rect(win, (0,0,0), (150,300,40,100), 0)
            # pygame.draw.rect(win, (0,0,0), (430,120,30,100), 0)
            # pygame.draw.rect(win, (0,0,0), (300,0,50,150), 0)
            # pygame.draw.rect(win, (0,0,0), (380,375,125,30), 0)
            pygame.draw.rect(win, (0,0,0), (320, 250, 40,40), 0)
            pygame.draw.rect(win, (0,0,0), (180, 200, 40,40), 0)
            # pygame.draw.rect(win, (0,0,0), (500, 300, 20,20), 0)
            # pygame.draw.rect(win, (0,0,0), (500, 150, 20,20), 0)

        sceneMap = pygame.surfarray.array3d(win)
        pygame.display.update() #update screen
    pygame.quit()

    return(sceneMap)