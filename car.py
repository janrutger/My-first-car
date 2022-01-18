import math

class  Car:
    def __init__(self, startSpot, witdht):
        self.botCenter = startSpot.center
        self.botHeight = 3 * witdht
        self.botWidht  = witdht
        self.botAngle  = math.degrees(math.atan2(self.botCenter[1], self.botCenter[0]))
        
        self.botNewCoordinates(self.botCenter, self.botAngle)

    def botNewCoordinates(self, botCenter, botAngele):
        X = 0
        Y = 1
        rads = math.radians((botAngele-90)%360)
        self.frontLeft   = (int(botCenter[X] + (self.botWidht) * math.cos(rads)),  int(botCenter[Y] + (self.botWidht) * math.sin(rads)))
        rads = math.radians((botAngele+90)%360)
        self.frontRight  = (int(botCenter[X] + (self.botWidht) * math.cos(rads)),  int(botCenter[Y] + (self.botWidht) * math.sin(rads)))
        rads = math.radians((botAngele-180)%360)
        self.backLeft    = (int(self.frontLeft[X] + (self.botHeight) * math.cos(rads)),  int(self.frontLeft[Y] + (self.botHeight) * math.sin(rads)))
        rads = math.radians((botAngele+180)%360)
        self.backRight    = (int(self.frontRight[X] + (self.botHeight) * math.cos(rads)),  int(self.frontRight[Y] + (self.botHeight) * math.sin(rads)))

    def botCoordinates(self):
        return([self.frontLeft, self.frontRight, self.backRight, self.backLeft])

    
    def botNextStep(self, newStep):
        self.botAngle = math.degrees(math.atan2(newStep.center[1]-self.botCenter[1], newStep.center[0]-self.botCenter[0]))
        self.botCenter = newStep.center
        self.botNewCoordinates(self.botCenter, self.botAngle)