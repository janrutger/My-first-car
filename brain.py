

class  Brain:
    def __init__(self, brainType):
        self.brainType = brainType
        if self.brainType == "basic":
            pass


    def getDirection(self, distances):
        if self.brainType == "basic":
            direction = self.getBasic(distances)
            return(direction)


    def getBasic(self, distances):
        dLeft  = distances[0]
        dFront = distances[1]
        dRight = distances[2]

        if dFront <= 30:
            return("back")

        elif dFront <= 80:
            if dLeft <= dRight:
                return("spin_right")
            else:
                return("spin_left")
                
        elif dFront < 180:
            if dLeft <= dRight:
                return("right")
            else:
                return("left")
        else:
            return("forward")