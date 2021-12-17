import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
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


Questions= { "left": [0.45, 0.4, 0.4, 0.375, 0.4, 0.4], 
 			"front": [0.15, 0.225, 0.4, 0.175, 0.125, 0.1],
 		    "right": [0.4, 0.1, 0.375, 0.4, 0.475, 0.375]}
toPredict = pandas.DataFrame(Questions)
Prediction = model.predict_classes(toPredict)
print(encoder.inverse_transform(Prediction))

