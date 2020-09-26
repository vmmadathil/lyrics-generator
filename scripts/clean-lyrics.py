#this script will clean up the lyrics
import re
import numpy as np

'''
TO DO:
    1. Remove all verses of features lyrics
    2. Remove all verse tags
    3. Change all words that end with "in'" to "ing" 
    4. Remove all ad-libs (for now)
'''


'''
Function: Remove features
This function will remove the featured verses and keep only the verses for the artist. In songs with multple artists, 
the verse tags will contain a colon followed by the artist name. If the verse tag doesn't have a colon, it is not a song with a feature.
Once that is complete, all the lyrics are joined and verse tags and ad libs are removed 
'''
def removeFeaturesAndTags(text, artist_name):
    #creating an array of lyrics chunks
    verses = text.split('[')

    #empty array
    confirmedVerses = []

    for verse in verses:

        if(":" in verse):
            if(artist_name in verse):
                verse = '[' + verse
                confirmedVerses.append(verse)
        else:
            verse = '[' + verse
            confirmedVerses.append(verse)
    
    print('removing repeated verses')
    confirmedVerses = list(set(confirmedVerses))
    
    #combining all the verses into one large string
    lyrics = " ".join(confirmedVerses)

    print('removing tags and ad-libs')
    #removing tags [] and ad libs ()
    lyrics = re.sub("[\(\[].*?[\)\]]", "", lyrics)

    #calling function to replace words
    replaceWords(lyrics)


'''
Function: Replace words
'''
def replaceWords(lyrics):
    
    lyrics = lyrics.replace("in' ", "ing ")
    lyrics = lyrics.replace('*', '')
    lyrics = lyrics.replace('(', '')
    lyrics = lyrics.replace(')', '')
    lyrics = lyrics.replace('=', '')
    lyrics = lyrics.replace(';', ',')
    lyrics = lyrics.replace('*', '')
    lyrics = lyrics.replace(']', '')
    lyrics = lyrics.replace('‘', "'")
    lyrics = lyrics.replace('‘', "’")
    lyrics = lyrics.replace('…', "...")
    lyrics = lyrics.replace('\n\n', "\n")

    lyrics = lyrics.replace('\xa0', "'")
    lyrics = lyrics.replace('\u2005', "'")
    lyrics = lyrics.replace('\u200e', "'")
    lyrics = lyrics.replace('\u205f', "'")
    lyrics = lyrics.replace('\ufeff', "'")
    

    lyrics = lyrics.lower()
    lyrics = lyrics.replace(' i ', ' I ')
    lyrics = lyrics.replace(" i'", " I'")

    lyrics = re.sub('\ntrodde.*?nej','',lyrics, flags=re.DOTALL)
    lyrics = re.sub('\nquand.*?17 ans','',lyrics, flags=re.DOTALL)
    lyrics = re.sub('\nseneler.*?günüm','',lyrics, flags=re.DOTALL)
    lyrics = re.sub('\nyalnız.*?yorgunum','',lyrics, flags=re.DOTALL)
    lyrics = re.sub('\nlaisse.*?jour-là\nje ne pleurerai pas\nje ne pleurerai pas','',lyrics, flags=re.DOTALL)
    lyrics = re.sub('\nmmm.*?...','',lyrics, flags=re.DOTALL)

    vocab = sorted(set(lyrics))
    print ('There are {} unique characters'.format(len(vocab)))
    

    file_path = '../data/processed/lyrics.txt'

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(lyrics)

    lyrics = lyrics.strip()
    
    print("finished writing lyrics")




'''
Function: Remove Ad-libs
'''


#main function
def main():
    #importing in all the lyrics
    with open('../data/pre-processed/raw_lyrics.txt', 'r',  encoding="utf-8") as f:
        text = f.read()
    
    print('read in lyrics, removing featured artists')

    artist_name = 'The Weeknd'
    removeFeaturesAndTags(text, artist_name)




if __name__ == "__main__":
    main()



#importing in all the lyrics
