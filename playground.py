import pygame
pygame.init()

import bot

win = pygame.display.set_mode((640,480))
pygame.display.set_caption("First Game")

# x = 50
# y = 80
# width = 20
# height = 40
# vel = 10

run = True

car = bot.Bot()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                car.botMove("up")
            if event.key == pygame.K_6:
                car.botMove("right")
            if event.key == pygame.K_2:
                car.botMove("down")
            if event.key == pygame.K_4:
                car.botMove("left")

    Coordinates = car.botCoordinates()
    win.fill((0,0,0))  # Fills the screen with black
    #pygame.draw.rect(win, (255,0,0), (x, y, width, height))  
    pygame.draw.polygon(win, (255,0,0), Coordinates, 0)
    pygame.display.update() 
    
pygame.quit()