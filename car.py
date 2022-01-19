import math

X = 0
Y = 1

class  Car:
    def __init__(self, startSpot, witdht):
        self.botCenter = startSpot.center
        self.botHeight = 3 * witdht
        self.botWidht  = witdht
        self.botAngle  = math.degrees(math.atan2(self.botCenter[Y], self.botCenter[X]))
        
        self.botNewCoordinates()

    def botNewCoordinates(self):
        #X = 0
        #Y = 1
        rads = math.radians((self.botAngle-90)%360)
        self.frontLeft   = (int(self.botCenter[X] + (self.botWidht) * math.cos(rads)),  int(self.botCenter[Y] + (self.botWidht) * math.sin(rads)))
        rads = math.radians((self.botAngle+90)%360)
        self.frontRight  = (int(self.botCenter[X] + (self.botWidht) * math.cos(rads)),  int(self.botCenter[Y] + (self.botWidht) * math.sin(rads)))
        rads = math.radians((self.botAngle-180)%360)
        self.backLeft    = (int(self.frontLeft[X] + (self.botHeight) * math.cos(rads)),  int(self.frontLeft[Y] + (self.botHeight) * math.sin(rads)))
        rads = math.radians((self.botAngle+180)%360)
        self.backRight    = (int(self.frontRight[X] + (self.botHeight) * math.cos(rads)),  int(self.frontRight[Y] + (self.botHeight) * math.sin(rads)))

    def botCoordinates(self):
        return([self.frontLeft, self.frontRight, self.backRight, self.backLeft])

    
    def botNextStep(self, newStep):
        self.botAngle = math.degrees(math.atan2(newStep.center[Y]-self.botCenter[Y], newStep.center[X]-self.botCenter[X]))
        self.botCenter = newStep.center
        self.botNewCoordinates()