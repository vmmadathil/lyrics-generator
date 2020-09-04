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
'''
def removeFeatures(text):
    #creating an array of lyrics chunks
    verses = text.split('[')

    #empty array
    confirmedVerses = []

    #for loop to loop through all the verses 
    for verse in verses:
        #seeing if the verse has a colon -- if it does, see if the verse is by The Weeknd
        if ((':' in verse) and ('The Weeknd' in verse)):
            confirmedVerses.append('[' + verse)
        else:
            confirmedVerses.append('[' + verse)
    
    print(confirmedVerses[0])

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
    removeFeatures(text)




if __name__ == "__main__":
    main()



#importing in all the lyrics
