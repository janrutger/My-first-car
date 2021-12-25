import pygame
pygame.init()

import bot

win = pygame.display.set_mode((640,480))
pygame.display.set_caption("First Game")

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

    
    Coordinates = car.botCoordinates() # 0=frontleft, 1=frontright
    print(Coordinates)
    
    
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.polygon(win, (255,0,255), Coordinates, 0) #draw de car
    pygame.draw.circle(win, (255,0,0), Coordinates[0], 3, 0)
    pygame.draw.circle(win, (0,255,0), Coordinates[1], 3, 0)
    pygame.draw.circle(win, (0,0,255), Coordinates[2], 3, 0)
    pygame.draw.circle(win, (100,100,100), Coordinates[3], 3, 0)
    pygame.display.update() #updte screen to show the car
    
pygame.quit()