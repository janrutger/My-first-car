import math

class  Car:
    def __init__(self):
        self.botCenter = (50, 80)
        self.botHeight = 40
        self.botWidht  = 20
        self.botAngle = 330

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
            self.angle_ = (self.botAngle + 0)%360 #do not change the direction, ony move up
            rads = math.radians(self.angle_)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)
             
        if move == "right":
            angle = 30
            speed = 1  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        if move == "spin_right":
            angle = 90
            speed = 1  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)


        if move == "back":
            self.angle_ = (self.botAngle + 180)%360 #do not change the direction, ony move down
            rads = math.radians(self.angle_)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        if move == "left":
            angle = -30
            speed = 1  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        if move == "spin_left":
            angle = -90
            speed = 1  #just change direction, do not move
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.botAngle)

        print(self.botAngle)