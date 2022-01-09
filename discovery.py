import os.path as path
import utils
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

sceneMap = utils.makeScene(None)
print(sceneMap)

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Map discovery")


run = True
while run:
    pygame.time.delay(10)

    manualCommand = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                manualCommand = "forward"
            if event.key == pygame.K_6:
                manualCommand = "right"
            if event.key == pygame.K_2:
                manualCommand = "back"
            if event.key == pygame.K_4:
                manualCommand = "left"


    ##Some more code here
  

    pygame.display.update() #update screen

pygame.quit()