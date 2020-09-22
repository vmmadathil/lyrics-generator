import json

#list of artist names
artists = ['FrankOcean', 'BrysonTiller', 'Miguel', 'Usher', 'ToryLanez', 'TreySongz', 'dvsn', 'Rihanna', 'JamesBlake']

#looping through all the different artists
for name in artists:
    #reading in the json
    try:
        with open('../data/raw/Lyrics_{}.json'.format(name)) as f:
            data = json.load(f)
        print("Working on {}".format(name))
    except:
        print('unable to read in file for {}'.format(name))

    #appending the lyrics to a text file
    with open('../data/pre-processed/raw_additional_lyrics.txt', 'a', encoding="utf-8") as f:
        for element in data['songs']:
            f.write("{}\n".format(element['lyrics']))
    f.close()


