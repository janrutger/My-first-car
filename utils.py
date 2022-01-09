import pygame
import os.path as path

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

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
    for row in range(0, HEIGHT-1, width):
        grid.append([])
        for col in range(0, WIDTH-1, width):
            spot = Spot(row, col, width)
            grid[col].append(spot)
            

def makeScene(fileName):
    pygame.init()
    win = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Create scenemap")

    if path.isfile("images/filename.png"):
        image = pygame.image.load("images/filename.png")
    else:
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
    return(sceneMap)