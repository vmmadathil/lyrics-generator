import lyricsgenius
genius = lyricsgenius.Genius("uWEvIQkyw6XS0jKsuOP5U-yhuUdPlR8sNWAq1ESdrrWhEqGg9HQQr1vt3ZF5X1cw")
artist = genius.search_artist("The Weeknd")
print(artist.songs)
lyrics = artist.save_lyrics()