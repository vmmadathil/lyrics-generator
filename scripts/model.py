'''
This script trains the neural network
Author: Visakh Madathil
'''

#import statements
from __future__ import print_function
#Callbacks are used to view internal state and statistics of a model while training
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils.data_utils import get_file
from keras.utils import np_utils
import numpy as np
import random
import sys
import io 

#path to the file
path ='WeekndLyrics.txt'

#opening and reading the corpus
with io.open(path) as f:
    text = f.read().lower()

#making text all lowercase
text = text.lower()

#create mapping of unique chars to integers
chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

#summarize the loaded data
n_chars = len(text)
n_vocab = len(chars)
print('Corpus Length:', n_chars)
print("Total Vocab: ", n_vocab)

#prepare the dataset of input to output pairs encoded as integers
seq_length = 100 #roughly the number of character in every line(?)
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = text[i:i + seq_length]
	seq_out = text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print ("Total Patterns: ", n_patterns)


#reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (n_patterns, seq_length, 1))
#normalize
X = X / float(n_vocab)
#one hot encode the output variable
y = np_utils.to_categorical(dataY)


#define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

#define the checkpoint and saving it outside
filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

#training the model   
model.fit(X, y, epochs=1, batch_size=128, callbacks=callbacks_list)