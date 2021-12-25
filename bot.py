import math

class  Bot:
    def __init__(self):
        self.botCenter = (50, 80)
        self.botHeight = 40
        self.botWidht  = 20

        self.frontLeft  = (self.botCenter[0] - int(self.botWidht/2), self.botCenter[1])
        self.frontRight = (self.botCenter[0] + int(self.botWidht/2), self.botCenter[1])
        self.backLeft   = (self.botCenter[0] - int(self.botWidht/2), self.botCenter[1] + self.botHeight)
        self.backRight  = (self.botCenter[0] + int(self.botWidht/2), self.botCenter[1] + self.botHeight)

        self.angle = -90 


    def botCoordinates(self):
        return([self.frontLeft, self.frontRight, self.backRight, self.backLeft])
    
    def botMove(self, move):
        X = 0
        Y = 1
        speed = 5

        if move == "up":
            self.angle_ = (self.angle + 0)%360 #do not change the direction, ony move up
            rads = math.radians(self.angle_)
            self.frontLeft  = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            self.frontRight = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            self.backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            self.backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))
             
        if move == "right":
            angle = 30
            self.angle = (self.angle + angle)%360
            rads = math.radians(self.angle)

            self.frontLeft   = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            self.frontRight  = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            self.backLeft    = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            self.backRight   = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))


        if move == "down":
            self.angle_ = (self.angle + 180)%360 #do not change the direction, ony move down
            rads = math.radians(self.angle_)
            self.frontLeft  = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            self.frontRight = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            self.backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            self.backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))

        if move == "left":
            angle = 330
            self.angle = (self.angle + angle)%360
            rads = math.radians(self.angle)

            self.frontLeft  = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            self.frontRight = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            self.backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            self.backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))  
        
        print(self.angle)