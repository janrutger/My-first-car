

class  Brain:
    def __init__(self, brainType):
        self.brainType = brainType
        if self.brainType == "basic":
            pass
        elif self.brainType == "svm":
            import pandas as pd
            from sklearn.model_selection import train_test_split
            from sklearn.svm import SVC
            data = pd.read_csv('randomdrive.txt', header=0)
            X = data.drop(['command'], axis=1)
            y = data['command']
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
            self.svmModel = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
            accuracy = self.svmModel.score(X_test, y_test)
            print(accuracy)



    def getDirection(self, distances, manualCommand):
        if manualCommand == None:
            if self.brainType == "basic":
                direction = self.basicModel(distances)
            if self.brainType == "svm":
                direction = self.svmModel.predict([distances])
        else:
            direction = manualCommand

        return(direction)

    #this is the "basic" algoritme
    def basicModel(self, distances):
        dLeft  = distances[0]
        dFront = distances[1]
        dRight = distances[2]

        if dFront <= 30:
            return("back")

        elif dFront <= 80:
            high = max(dLeft, dRight)
            low  = min(dLeft, dRight)
            if (high* 0.9) > low:
                if dLeft < dRight:
                    return("spin_right")
                elif dLeft > dRight:
                    return("spin_left")
            else:
                return("spin_right")
            # if dLeft <= dRight:
            #     return("spin_right")
            # else:
            #     return("spin_left")
                
        
        elif dFront <= 100: 
            high = max(dLeft, dRight)
            low  = min(dLeft, dRight)
            if (high* 0.9) > low:
                if dLeft < dRight:
                    return("right")
                elif dLeft > dRight:
                    return("left")
            else:
                return("right")
            # if dLeft <= dRight:
            #     return("right")
            # else:
            #     return("left")
        else:
            high = max(dLeft, dRight)
            low  = min(dLeft, dRight)
            if (high* 0.3) > low:
                if dLeft < dRight:
                    return("right")
                elif dLeft > dRight:
                    return("left")
            else:
                return("forward")