import json

#reading in the json
try:
    with open('../data/raw/Lyrics_TheWeeknd.json') as f:
        data = json.load(f)
except:
    print('unable to read in file')

#writing the lyrics to a text file
with open('../data/pre-processed/raw_lyrics.txt', 'w', encoding="utf-8") as f:
    for element in data['songs']:
        f.write("{}\n".format(element['lyrics']))
f.close()
