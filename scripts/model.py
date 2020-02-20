'''
This script trains the neural network
Author: Visakh Madathil
'''

#import statements
from __future__ import print_function
#Callbacks are used to view internal state and statistics of a model while training
from keras.callbacks import LambdaCallback #this callback supports creating simple, custom callbacks on the fly
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import io 

#path to the file
path ='WeekndLyrics.txt'

#opening and reading the corpus
with io.open(path) as f:
    text = f.read().lower()

#printing the length of the corpus
print('corpus length:', len(text))



