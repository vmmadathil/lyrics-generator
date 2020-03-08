import pandas as pd
import numpy as np 
import sys

from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#loading ascii text 