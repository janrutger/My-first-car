import pygame
pygame.init()
win = pygame.display.set_mode((640,480))
pygame.display.set_caption("First Game")

import robot
car = robot.Car()

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                car.botMove("forward")
            if event.key == pygame.K_9:
                car.botMove("right")
            if event.key == pygame.K_6:
                car.botMove("spin_right")
            if event.key == pygame.K_2:
                car.botMove("back")
            if event.key == pygame.K_7:
                car.botMove("left")
            if event.key == pygame.K_4:
                car.botMove("spin_left")

    ## Create scene
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(win, (255,255,255), (20,20,600,440), 0)
    pygame.draw.rect(win, (0,0,0,0), (200,150,75,100), 0)
    scene = pygame.surfarray.array3d(win)
    
    sonarDistances, sonarLines, carCenter = car.botSonar(scene, (-45,-30,0,30, 45))
    print(sonarDistances, sonarLines)

    ## Draw the car
    Coordinates = car.botCoordinates() # 0=frontleft, 1=frontright
    #print(Coordinates)
    pygame.draw.polygon(win,(0,0,255), Coordinates, 0) #draw de car
    pygame.draw.circle(win, (255,0,0), Coordinates[0], 3, 0)
    pygame.draw.circle(win, (0,255,0), Coordinates[1], 3, 0)
    for sonarLine in sonarLines:
        pygame.draw.line(win, (0,0,0), carCenter, sonarLine, 1)
        pygame.draw.circle(win, (255,0,0), sonarLine, 1, 0)
    

    ##Update playground window
    pygame.display.update() #updte screen to show the car
    
pygame.quit()