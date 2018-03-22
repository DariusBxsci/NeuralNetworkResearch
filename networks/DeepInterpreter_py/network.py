from keras.models import Sequential
from training_data import generate_training_data
import numpy
from keras.utils import *
from keras.layers import Dense
numpy.set_printoptions(threshold=numpy.nan)

model = Sequential()

#make model with two hidden layers of 21 neurons and a single output neuron
model.add(Dense(units=7, activation='relu', input_dim=7))
model.add(Dense(units=7, activation='relu'))
model.add(Dense(units=7, activation='sigmoid'))
model.add(Dense(units=7, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

x_train, y_train = generate_training_data()

model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=10)

print model.predict_classes(numpy.array([[0.0,0.0,1.0,1.0,1.0,0.0,0.0]]))
