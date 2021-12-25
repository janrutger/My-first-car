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

    def botAlign(self, newPosition, position, angle):
        angle = math.radians(angle)
        temps = (newPosition[0]-position[0],newPosition[1]-position[1])
        temps = (temps[0]*math.cos(angle)-temps[1]*math.sin(angle), temps[0]*math.sin(angle)+temps[1]*math.cos(angle))
        temps = (temps[0]+position[0], temps[1]+position[1])
        return((int(temps[0]), int(temps[1])))
    
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

            new_frontLeft   = (self.frontLeft[X] + speed * math.cos(rads),  self.frontLeft[Y] + speed * math.sin(rads))
            new_frontRight  = (self.frontRight[X]+ speed * math.cos(rads),  self.frontRight[Y]+ speed * math.sin(rads))
            new_backLeft    = (self.backLeft[X]  + speed * math.cos(rads),  self.backLeft[Y]  + speed * math.sin(rads))
            new_backRight   = (self.backRight[X] + speed * math.cos(rads),  self.backRight[Y] + speed * math.sin(rads))

            self.frontleft  = self.botAlign(new_frontLeft, self.frontLeft, angle)
            self.frontRight = self.botAlign(new_frontRight, self.frontRight, angle)
            self.backLeft   = self.botAlign(new_backLeft, self.backLeft, angle)
            self.backRight  = self.botAlign(new_backRight, self.backRight, angle)

            

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

            new_frontLeft  = (self.frontLeft[X] + speed * math.cos(rads),  self.frontLeft[Y] + speed * math.sin(rads))
            self.frontleft = self.botAlign(new_frontLeft, self.frontLeft, angle)
            new_frontRight = (self.frontRight[X]+ speed * math.cos(rads),  self.frontRight[Y]+ speed * math.sin(rads))
            self.frontRight = self.botAlign(new_frontRight, self.frontRight, angle)
            new_backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            self.backLeft = self.botAlign(new_backLeft, self.backLeft, angle)
            new_backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))
            self.backRight = self.botAlign(new_backRight, self.backRight, angle)

            # self.frontLeft  = (int(self.frontLeft[X] + speed * math.cos(rads)),  int(self.frontLeft[Y] + speed * math.sin(rads)))
            # self.frontRight = (int(self.frontRight[X]+ speed * math.cos(rads)),  int(self.frontRight[Y]+ speed * math.sin(rads)))
            # self.backLeft   = (int(self.backLeft[X]  + speed * math.cos(rads)),  int(self.backLeft[Y]  + speed * math.sin(rads)))
            # self.backRight  = (int(self.backRight[X] + speed * math.cos(rads)),  int(self.backRight[Y] + speed * math.sin(rads)))  
        
        print(self.angle)