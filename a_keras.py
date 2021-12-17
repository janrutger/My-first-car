import pandas
from random import randrange
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# load dataset
data = pandas.read_csv("randomdrive.txt", header=0)
X = data.drop(['command'], axis=1)
X=X/200  #Normalize dataset maxdistance=200
Y = data['command']

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, random_state = 0)

# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(9, input_dim=3, activation='relu'))
	model.add(Dense(6, activation='relu'))
	model.add(Dense(6, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


model = baseline_model()
model.fit(X_train, y_train, epochs=150, batch_size=5, verbose=1)

a, accuracy = model.evaluate(X_test, y_test, verbose=1)
print(a)
print (accuracy)

#My_test = [[90, 30, 80], [80, 45, 20], [80, 80, 75], [75, 35, 80], [80, 25, 95], [80, 20, 75], [randrange(200),randrange(200),randrange(200)]]

Questions= { "left": [90, 80, 80, 75, 80, 80, randrange(200)], 
 			"front": [30, 45, 80, 35, 25, 75, randrange(200)],
 		    "right": [80, 20, 75, 80, 95, 75, randrange(200)]}
toPredict = pandas.DataFrame(Questions)
print(toPredict)
Prediction = model.predict_classes(toPredict/200) #normalizing inputdata
print(encoder.inverse_transform(Prediction))

