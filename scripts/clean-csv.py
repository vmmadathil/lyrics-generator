#this script will keep only lyrics from The Weeknd's songs

import pandas as pd
import re

lyricsraw = pd.read_csv('the-weeknd-lyrics-complete.csv')

#keeping only songs on The Weeknd's albums
lyricsraw = lyricsraw.loc[lyricsraw['album'].notnull()]

#removing things in brackets
lyricsraw['lyrics'] = lyricsraw['lyrics'].str.replace(r"(\s*\[.*?\]\s*)", " ").str.strip()

print("finished processing!")

#lyricsraw.to_csv('processed-weeknd-lyrics.csv')

#now converting the df to a concatenated .txt file

print("converting to .txt file")

lyricsString = lyricsraw['lyrics'].str.cat()

print(len(lyricsString))
'''
txtfile = open('WeekndLyrics.txt', 'w', encoding='utf-8')
txtfile.write(lyricsString)
txtfile.close()
'''