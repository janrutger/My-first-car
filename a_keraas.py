import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


# load dataset
data = pandas.read_csv("randomdrive.txt", header=0)
X = data.drop(['command'], axis=1)
Y = data['command']
#dataset = dataframe.values
#print(dataset)
#X = dataset[:,0:2].astype(float)
#Y = dataset[:,3]


# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)



# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(9, input_dim=3, activation='relu'))
	model.add(Dense(6, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=1)
estimator.fit(X, dummy_y)

#kfold = KFold(n_splits=10, shuffle=True)
#results = cross_val_score(estimator, X, dummy_y, cv=kfold)
#print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))