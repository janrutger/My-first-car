#import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def readFile():
    data = pd.read_csv('randomdrive.txt', header=0)
    return(data)

def procesData(data):
    X = data.drop(['command'], axis=1)
    y = data['command']
    return(X, y)

def makeModel(type, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    if type == "svc":
        thisModel = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
        #svm_predictions = thisModel.predict(X_test)
        #print(svm_predictions)
        accuracy = thisModel.score(X_test, y_test)
        print(accuracy)
    else:
        thisModel = KNeighborsClassifier(n_neighbors = 21).fit(X_train, y_train)
        # accuracy on X_test
        accuracy = thisModel.score(X_test, y_test)
        print(accuracy)
    
    return(thisModel)

def plotData(data):
    fig = plt.figure(figsize=(16,16))
    ax = fig.add_subplot(111, projection='3d')
    xax = data['right']
    yax = data['left']
    zax = data['front']
    command = data['command']

    for n in range(len(command)):
        if command[n] == 'spin_left':
            ax.scatter(xax[n], yax[n], zax[n], color='c')
        if command[n] == 'left':
            ax.scatter(xax[n], yax[n], zax[n], color='b')
        if command[n] == 'forward':
            ax.scatter(xax[n], yax[n], zax[n], color='r')
        if command[n] == 'right':
            ax.scatter(xax[n], yax[n], zax[n], color='g')
        if command[n] == 'spin_right':
            ax.scatter(xax[n], yax[n], zax[n], color='y') 
        if command[n] == 'back':
            ax.scatter(xax[n], yax[n], zax[n], color='k')
    plt.show()

def main():
    data = readFile()
    print(data.info())
    X, y = procesData(data)

    My_Model = makeModel("svc", X, y)
    My_test = [[75, 30, 80], [80, 55, 20], [80, 20, 75], [88, 40, 75]]
    My_predictions = My_Model.predict(My_test)
    print(My_test)
    print(My_predictions)
    #plotData(data)

    
if __name__ == "__main__":
    main()