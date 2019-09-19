import lyricsgenius
genius = lyricsgenius.Genius("uWEvIQkyw6XS0jKsuOP5U-yhuUdPlR8sNWAq1ESdrrWhEqGg9HQQr1vt3ZF5X1cw")
artist = genius.search_artist("The Weeknd")
print(artist.songs)
lyrics = artist.save_lyrics() 

lyric_path = "lyrics.csv"
lyrics.keys()
songs = lyrics.get('songs')
lyric_df = pd.DataFrame(columns=['name', 'lyrics'])
for x in songs:
    lyric_df = lyric_df.append({
        'name': x.get('title'),
        'lyrics': x.get('lyrics')
    }, ignore_index=True)
lyric_df.to_csv(lyric_path, index=False)
lyric_df.iloc[0]