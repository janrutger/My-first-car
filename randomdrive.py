from random import randrange
from types import prepare_class

def scanDistance():
    dLeft  = randrange(100)
    dFront = randrange(100)
    dRight = randrange(100)

    return(dLeft, dFront, dRight)

def evalDistance(dLeft, dFront, dRight):
    if dFront < 20:
        return("back")
    if dFront > 50:
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
    f = open("randomdrive/randomdrive.txt", "a")
    f.writelines([str(dLeft),",", str(dFront),",", str(dRight),",", driveCommand, "\n"])
    f.close()


def main():
    count = 2000
    while count > 0:

        dLeft, dFront, dRight = scanDistance()
        driveCommand = evalDistance(dLeft, dFront, dRight)

        print(dLeft, dFront, dRight, driveCommand)
        writeResult(dLeft, dFront, dRight, driveCommand)
        count = count -1





if __name__ == "__main__":
    main()