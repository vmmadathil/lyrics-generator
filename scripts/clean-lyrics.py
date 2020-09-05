#this script will clean up the lyrics
import re

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
the verse tags will contain a colon followed by the artist name. If the verse tag doesn't have a colon, it is not a song with a feature
'''
def removeFeatures(text, artist_name):
    #creating an array of lyrics chunks
    verses = text.split('[')

    #empty array
    confirmedVerses = []

    for verse in verses:

        if(":" in verse):
            if('artist_name' in verse):
                verse = '[' + verse
                confirmedVerses.append(verse)
        else:
            verse = '[' + verse
            confirmedVerses.append(verse)
    
    print(confirmedVerses[0])


    '''
    #for loop to loop through all the verses 
    for verse in verses:
        print(verse)
        #seeing if the verse has a colon -- if it does, see if the verse is by The Weeknd
        if ((':' in verse) and ('The Weeknd' in verse)):
            confirmedVerses.append('[' + verse)
        else:
            confirmedVerses.append('[' + verse)

        break

    print(confirmedVerses[0])
    '''

    #calling function to remove verse tags
    #removeTags(confirmedVerses)


'''
Function: Remove tags
'''
def removeTags(verses):
    
    #print(type(verses[1]))
    print((verses[1]))

    count = 0
    #looping through all the verses
    for verse in verses:
        count = count + 1
        verse, *_ = verse.split(']')
        
        print(verse)
        
        if count == 10:
            break



'''
Function: Replace words
'''

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
    removeFeatures(text, artist_name)




if __name__ == "__main__":
    main()



#importing in all the lyrics
