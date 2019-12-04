import pandas as pd
import pandas.io.json as pd_json
from pandas.io.json import json_normalize
import json
import glob

bigdf = pd.DataFrame(columns  = ['title', 'lyrics', 'album'])

counter = 1

#opening all the files in the directory
for filename in glob.glob("*.json"):
    print("Currently processing " + filename)
    with open(filename, 'r') as f:
        data = json.load(f)

    data = data['songs']

    df = pd.io.json.json_normalize(data)
    df = df[['title', 'lyrics', 'album']]

    bigdf = pd.concat([bigdf, df])

    print('Done with ' + str(counter) + ' lyrics files!')
    counter = counter + 1

bigdf.to_csv('the-weeknd-lyrics-complete.csv')