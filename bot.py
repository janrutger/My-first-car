

class  Bot:
    def __init__(self):
        self.botCenter = (50, 80)
        self.botHeight = 40
        self.botWidht  = 20

        self.frontLeft  = (self.botCenter[0] - self.botWidht/2, self.botCenter[1])
        self.frontRight = (self.botCenter[0] + self.botWidht/2, self.botCenter[1])

        self.backLeft   = (self.botCenter[0] - self.botWidht/2, self.botCenter[1] + self.botHeight)
        self.backRight  = (self.botCenter[0] + self.botWidht/2, self.botCenter[1] + self.botHeight)


    def botCoordinates(self):
        return([self.frontLeft, self.frontRight, self.backRight, self.backLeft])

    
    def botMove(self, move):
        X = 0
        Y = 1
        speed = 5

        if move == "up":
            self.frontLeft  = (self.frontLeft[X] +0,  self.frontLeft[Y] -speed)
            self.frontRight = (self.frontRight[X]+0, self.frontRight[Y] -speed)
            self.backLeft   = (self.backLeft[X]  +0,   self.backLeft[Y] -speed)
            self.backRight  = (self.backRight[X] +0,  self.backRight[Y] -speed) 
        if move == "right":
            self.frontLeft  = (self.frontLeft[X] +speed,  self.frontLeft[Y] -0)
            self.frontRight = (self.frontRight[X]+speed, self.frontRight[Y] -0)
            self.backLeft   = (self.backLeft[X]  +speed,   self.backLeft[Y] -0)
            self.backRight  = (self.backRight[X] +speed,  self.backRight[Y] -0)
        if move == "down":
            self.frontLeft  = (self.frontLeft[X] +0,  self.frontLeft[Y] +speed)
            self.frontRight = (self.frontRight[X]+0, self.frontRight[Y] +speed)
            self.backLeft   = (self.backLeft[X]  +0,   self.backLeft[Y] +speed)
            self.backRight  = (self.backRight[X] +0,  self.backRight[Y] +speed)
        if move == "left":
            self.frontLeft  = (self.frontLeft[X] -speed,  self.frontLeft[Y] -0)
            self.frontRight = (self.frontRight[X]-speed, self.frontRight[Y] -0)
            self.backLeft   = (self.backLeft[X]  -speed,   self.backLeft[Y] -0)
            self.backRight  = (self.backRight[X] -speed,  self.backRight[Y] -0)    