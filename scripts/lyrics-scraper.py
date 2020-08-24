#import statements
import lyricsgenius
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

#fecthing the API key
API_KEY = os.getenv("API_KEY")

#creating the genius client
genius = lyricsgenius.Genius(API_KEY)

#fetching all the songs for the weeknd
artist = genius.search_artist("The Weeknd")

print('saving all the lyrics files')

#creating a json of the lyrics data 
artist.save_lyrics() 
