import pandas as pd
import pandas.io.json as pd_json
from pandas.io.json import json_normalize
import json
import os

#opening al 
for 
with open('lyrics_theweeknd_6inchheel.json', 'r') as read_file:
    data = json.load(read_file)


data = data['songs']

df = pd.io.json.json_normalize(data)
df = df[['title', 'lyrics', 'album']]

bigdf = 
print(df)