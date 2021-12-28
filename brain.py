

class  Brain:
    def __init__(self):
        self.type = "algoritme"


    def getDirection(self, distances):
        dLeft  = distances[0]
        dFront = distances[1]
        dRight = distances[2]

        if dFront <= 20:
            return("back")
        elif dFront <= 30:
            if dLeft <= dRight:
                return("spin_right")
            else:
                return("spin_left")
        elif dFront <= 80:
            if dLeft <= dRight:
                return("right")
            else:
                return("left")
        elif dFront > 80:
            return("forward")