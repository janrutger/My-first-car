

class  Brain:
    def __init__(self):
        self.type = "algoritme"


    def getDirection(self, distances):
        dLeft  = distances[0]
        dFrontL= distances[1]
        dFront = distances[2]
        dFrontR= distances[3]
        dRight = distances[4]

        #dFront =(dFrontL+dFrontR+dFront)/3

        if dFront <= 30:
            return("back")

        # elif dFront <= 30:
        #     if dLeft <= dRight:
        #         return("spin_right")
        #     else:
        #         return("spin_left")

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



#############################################################
    def getDirectionV2(self, distances):
        dLeft  = distances[0]
        dFrontL= distances[1]
        dFront = distances[2]
        dFrontR= distances[3]
        dRight = distances[4]

        dFront =(dFrontL+dFrontR+dFront)/3

        if dFront <= 30:
            return("back")

        # elif dFront <= 30:
        #     if dLeft <= dRight:
        #         return("spin_right")
        #     else:
        #         return("spin_left")

        elif dFront <= 80:
            if dLeft <= dRight:
                return("spin_right")
            else:
                return("spin_left")
                
        elif dFront < 150:
            if dLeft <= dRight:
                return("right")
            else:
                return("left")
        else:
            return("forward")