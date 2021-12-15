from random import randrange
import os.path as path
#from types import prepare_class

def scanDistance():
    maxrand = 100
    dLeft  = randrange(maxrand)
    dFront = randrange(maxrand)
    dRight = randrange(maxrand)

    return(dLeft, dFront, dRight)

def evalDistance(dLeft, dFront, dRight):
    if dFront <= 20:
        return("back")
    if dFront >= 50:
        return("forward")
    else:
        if dFront <= 30:
            if dLeft <= dRight:
                return("spin_right")
            else:
                return("spin_left")
        else:
            if dLeft <= dRight:
                return("right")
            else:
                return("left")

def writeResult(dLeft, dFront, dRight, driveCommand):
    if not path.isfile('randomdrive.txt'):
        f = open("randomdrive.txt", "a")
        f.writelines(["left,front,right,command", "\n"])
    else:
        f = open("randomdrive.txt", "a")
    f.writelines([str(dLeft),",", str(dFront),",", str(dRight),",", driveCommand, "\n"])
    f.close()


def main():
    count = 400
    while count > 0:

        dLeft, dFront, dRight = scanDistance()
        driveCommand = evalDistance(dLeft, dFront, dRight)

        print(dLeft, dFront, dRight, driveCommand)
        writeResult(dLeft, dFront, dRight, driveCommand)
        count = count -1





if __name__ == "__main__":
    main()