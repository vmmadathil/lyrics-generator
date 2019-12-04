#this script will keep only lyrics from The Weeknd's songs

import pandas as pd
import re

lyricsraw = pd.read_csv('the-weeknd-lyrics-complete.csv')

#keeping only songs on The Weeknd's albums
lyricsraw = lyricsraw.loc[lyricsraw['album'].notnull()]

#removing things in brackets
lyricsraw['lyrics'] = lyricsraw['lyrics'].str.replace(r'\[[.*]\]','')

lyricsraw.to_csv('processed-weeknd-lyrics.csv')