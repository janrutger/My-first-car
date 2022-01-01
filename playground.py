import pygame
pygame.init()
win = pygame.display.set_mode((640,480))
pygame.display.set_caption("Driving a ROBOTcar")

import robot
car = robot.Car()

import brain
carBrain = brain.Brain("svm") #Supported Brains "basic" of "svm"

run = True
while run:
    pygame.time.delay(200)

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
    pygame.draw.rect(win, (0,0,0), (80,125,75,100), 0)
    pygame.draw.rect(win, (0,0,0), (150,300,75,100), 0)
    pygame.draw.rect(win, (0,0,0), (430,120,75,100), 0)
    pygame.draw.rect(win, (0,0,0), (300,0,50,150), 0)
    pygame.draw.rect(win, (0,0,0), (380,375,125,30), 0)
    pygame.draw.rect(win, (0,0,0), (320, 240, 40,40), 0)
    sceneMap = pygame.surfarray.array3d(win)
    
    ## Get the Car coordinates & Draw the car
    Coordinates = car.botCoordinates() # 0=frontleft, 1=frontright
    #print(Coordinates)
    pygame.draw.polygon(win,(0,0,255), Coordinates, 0) #draw de car
    pygame.draw.circle(win, (255,0,0), Coordinates[0], 3, 0)
    pygame.draw.circle(win, (0,255,0), Coordinates[1], 3, 0)

    ##get distances & draw the sonar lines 
    sonarDistances, sonarLines, carCenter = car.botSonar(sceneMap, (-30,0,30))
    for sonarLine in sonarLines:
        pygame.draw.line(win, (0,0,0), carCenter, sonarLine, 1)
        pygame.draw.circle(win, (255,0,0), sonarLine, 1, 0)

    ##Update playground window
    pygame.display.update() #updte screen to show the car

    ## get move Command + perform move   
    carCommand = carBrain.getDirection(sonarDistances)
    print(sonarDistances, carCommand)
    car.botMove(carCommand)


pygame.quit()