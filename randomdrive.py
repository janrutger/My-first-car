from random import randrange
import os.path as path
#from types import prepare_class

maxDistance = 200
normFactor = 1 # 1 means no normalisation, 

def scanDistance():
    
    dLeft  = randrange(maxDistance)/normFactor
    dFront = randrange(maxDistance)/normFactor
    dRight = randrange(maxDistance)/normFactor

    return(dLeft, dFront, dRight)

def evalDistance(dLeft, dFront, dRight):
    if dFront <= 20/normFactor:
        return("back")
    elif dFront <= 30/normFactor:
        if dLeft <= dRight:
            return("spin_right")
        else:
            return("spin_left")
    elif dFront <= 50/normFactor:
        if dLeft <= dRight:
            return("right")
        else:
            return("left")
    elif dFront > 50/normFactor:
        return("forward")


def writeResult(dLeft, dFront, dRight, driveCommand):
    if not path.isfile('randomdrive.txt'):
        f = open("randomdrive.txt", "a")
        f.writelines(["left,front,right,command", "\n"])
    else:
        f = open("randomdrive.txt", "a")
    f.writelines([str(dLeft),",", str(dFront),",", str(dRight),",", driveCommand, "\n"])
    f.close()


def main():
    count = 1000
    while count > 0:

        dLeft, dFront, dRight = scanDistance()
        driveCommand = evalDistance(dLeft, dFront, dRight)

        print(dLeft, dFront, dRight, driveCommand)
        writeResult(dLeft, dFront, dRight, driveCommand)
        count = count -1





if __name__ == "__main__":
    main()