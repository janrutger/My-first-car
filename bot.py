import math

class  Bot:
    def __init__(self):
        self.botCenter = (50, 80)
        self.botHeight = 40
        self.botWidht  = 20
        self.botAngle = 330


        self.botNewCoordinates(self.botCenter, self.botAngle)

        # self.frontLeft  = (self.botCenter[0] - int(self.botWidht/2), self.botCenter[1])
        # self.frontRight = (self.botCenter[0] + int(self.botWidht/2), self.botCenter[1])
        #self.backLeft   = (self.botCenter[0] - int(self.botWidht/2), self.botCenter[1] + self.botHeight)
        #self.backRight  = (self.botCenter[0] + int(self.botWidht/2), self.botCenter[1] + self.botHeight)

         

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

        if move == "up":
            self.angle_ = (self.botAngle + 0)%360 #do not change the direction, ony move up
            rads = math.radians(self.angle_)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.angle_)

            # self.frontLeft  = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            # self.frontRight = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            # self.backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            # self.backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))
             
        if move == "right":
            angle = 30
            speed = 1
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.angle_)

            # self.frontLeft   = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            # self.frontRight  = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            # self.backLeft    = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            # self.backRight   = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))


        if move == "down":
            self.angle_ = (self.botAngle + 180)%360 #do not change the direction, ony move down
            rads = math.radians(self.angle_)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.angle_)

            # self.frontLeft  = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            # self.frontRight = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            # self.backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            # self.backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))

        if move == "left":
            angle = 330
            speed = 1
            self.botAngle = (self.botAngle + angle)%360
            rads = math.radians(self.botAngle)
            self.botCenter  = (int(self.botCenter[X] + speed * math.cos(rads)),  int(self.botCenter[Y] + speed * math.sin(rads))) 
            self.botNewCoordinates(self.botCenter, self.angle_)

            # self.frontLeft  = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            # self.frontRight = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            # self.backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            # self.backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))  
        
        print(self.botAngle)