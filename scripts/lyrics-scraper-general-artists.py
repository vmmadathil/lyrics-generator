#import statements
import lyricsgenius
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

#After training the first iteration of the model, I recognized that I need more data for the model to make sense. Here, I'll begin augmenting the data set with some other R&B artists

#fetching the API key
API_KEY = os.getenv("API_KEY")

#progress messages
print('attempting to connect to Genius API')

try:
    #creating the genius client
    genius = lyricsgenius.Genius(API_KEY)
    print('successfully connected')
except:
    print('failed to connect!')

#a list of artists I'm interested in
artists = ['Frank Ocean', 'Bryson Tiller', 'Miguel', 'Usher', 'Tory Lanez', 'Trey Songz', 'dvsn', 'Rihanna', 'James Blake']

#iterate through all these artists, keep only their top 15 songs
for name in artists:
    try:
        artist = genius.search_artist(name, max_songs = 15)
        print('Saving the songs for {}'.format(name))
        artist.save_lyrics()
    except:
        print("failed to save lyrics for {}".format(name))

