from keras.models import Sequential

model = Sequential()

from keras.layers import Dense

#make model with two hidden layers of 21 neurons and a single output neuron
model.add(Dense(units=21, activation='relu', input_dim=7))
model.add(Dense(units=21, activation='relu'))
model.add(Dense(units=1, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
