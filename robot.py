import math

class  Car:
    def __init__(self):
        self.botCenter = (50, 80)
        self.botHeight = 40
        self.botWidht  = 20
        self.botAngle  = 5

        self.botNewCoordinates(self.botCenter, self.botAngle)

    def botNewCoordinates(self, botCenter, botAngele):
        X = 0
        Y = 1
        rads = math.radians((botAngele-90)%360)
        self.frontLeft   = (int(botCenter[X] + (self.botWidht/2) * math.cos(rads)),  int(botCenter[Y] + (self.botWidht/2) * math.sin(rads)))
        rads = math.radians((botAngele+90)%360)
        self.frontRight  = (int(botCenter[X] + (self.botWidht/2) * math.cos(rads)),  int(botCenter[Y] + (self.botWidht/2) * math.sin(rads)))
        rads = math.radians((botAngele-180)%360)
        self.backLeft    = (int(self.frontLeft[X] + (self.botHeight) * math.cos(rads)),  int(self.frontLeft[Y] + (self.botHeight) * math.sin(rads)))
        rads = math.radians((botAngele+180)%360)
        self.backRight    = (int(self.frontRight[X] + (self.botHeight) * math.cos(rads)),  int(self.frontRight[Y] + (self.botHeight) * math.sin(rads)))

    def botCoordinates(self):
        return([self.frontLeft, self.frontRight, self.backRight, self.backLeft])
    
    def botMove(self, move):
        X = 0
        Y = 1
        speed = 5

        if move == "forward":
            speed = speed
            self.angle_ = (self.botAngle + 0)%360 #do not change the direction, ony move up
            rads = math.radians(self.angle_)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)
             
        if move == "right":
            angle = 5
            speed = speed  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        if move == "spin_right":
            angle = 47
            speed = 2  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)


        if move == "back":
            speed = speed*2
            self.angle_ = (self.botAngle + 180)%360 #do not change the direction, ony move down
            rads = math.radians(self.angle_)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        if move == "left":
            angle = -5
            speed = speed  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        if move == "spin_left":
            angle = -47
            speed = 2  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        #print(self.botAngle, self.botCoordinates())

    def botSonar(self, scene, offsets):
        X = 0
        Y = 1
        sonarDistances = []
        sonarCoordinates = []
        maxLenght = 200

        for offset in offsets:
            sonarAngle = (self.botAngle + offset)%360
            rads = math.radians(sonarAngle)
            for n in range(1,maxLenght+1):
                sonarProbe = (int(self.botCenter[X] + n * math.cos(rads)),  int(self.botCenter[Y] + n * math.sin(rads)))
                probe = scene[sonarProbe] == (0,0,0) #is black
                if probe.all() or n == maxLenght:
                     sonarDistances.append(n)
                     sonarCoordinates.append(sonarProbe)
                     break
        
        return(sonarDistances, sonarCoordinates, self.botCenter)