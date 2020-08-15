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

#getting the name and lyric and saving it to a csv
lyric_path = "lyrics.csv"

#reading in all the lyrics


lyrics.keys()



songs = lyrics.get('songs')
lyric_df = pd.DataFrame(columns=['name', 'lyrics'])
for song in songs:
    print('Working on {}'.format(song))
    lyric_df = lyric_df.append({
        'name': song.get('title'),
        'lyrics': song.get('lyrics')
    }, ignore_index=True)
lyric_df.to_csv(lyric_path, index=False)
lyric_df.iloc[0]
