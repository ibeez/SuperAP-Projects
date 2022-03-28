#attempts to create a list of valid anagrams, and then generate a 'crossword' of possible answers using the given set of letters

import random 
import enchant

#pyenchant is a python module used for spell checking that returns a true or false answer depending on if the given string is a valid english word 
dictionary = enchant.Dict("en_US")

#class to store the x and y values of letter on the crossword 
class Coord():
    def __init__(self,x,y,letter,wordstatus):
        self.x = x
        self.y = y
        self.letter = letter
        self.wordstatus = wordstatus
#allows input for a word to be turned into a crossword 
rootword = input("insert word:")
brokenword = []
#checks if the original word is a valid word 
firstword = dictionary.check(rootword)
if firstword:
    for i in range(len(rootword)):
        brokenword.append(rootword[i:i+1])
else:
    print("please choose a valid root word")
    quit()
#creates an array to hold the letters that have yet to be used to create a word and an array to hold the possible solutions 
holder = []
validanagrams = []

#gets a list of possible anagrams
for i in range(4,len(rootword)):
    for k in range(10000): 
        tempword = ''  
        holder = brokenword[:]
        #creates a word of a given length that uses each letter a maximum of the number of times it appears in the root word
        for j in range(i):
            templetter =  random.choice(holder)
            tempword = tempword +  templetter
            #comment out the line below to remove the 'each letter used a certain number of times' restriction 
            holder.remove(templetter)

        #adds word to the list of possible solutions if it is a valid word AND it does not yet exist in the list of valid solutions 
        if dictionary.check(tempword):
            duplicatexists = False 
            for l in validanagrams:
                if l == tempword: 
                    duplicatexists = True
            if duplicatexists is False:
                validanagrams.append(tempword) 
print(validanagrams)


rows, cols = (10,10)
arr = [[" " for i in range(cols)]for j in range(rows)]
#array to hold coordinates of spaces containing words 
usedcoords = []
#function to break a string into a list of characters 
def breakword(thingy):
    broken = []
    for i in range(len(thingy)):
        broken.append(thingy[i:i+1])
    return broken 

#holds spots in crossword containing letters 
coords = []
def startCrossword():
    wordpicker = random.choice(validanagrams)
    print(wordpicker)
    rowpicker = random.randint(0,len(arr))
    spotpicker = random.randint(0,len(arr) - len(wordpicker) - 1)
    wordToAdd = breakword(wordpicker)
    for i in range(len(wordToAdd)):
        xpicked = rowpicker
        ypicked = spotpicker -1 + i
        arr[xpicked][ypicked] = wordToAdd[i]
        coords.append(Coord(xpicked,ypicked,wordToAdd[i],'horizontal'))
    validanagrams.remove(wordpicker)


def addCrossWord():
    addTo = random.choice(coords)
    baseletter = addTo.letter 
    #print('base letter: ' + baseletter)
    nextWord = ""
    if addTo.wordstatus == 'horizontal':
        newWordStatus = 'vertical'
    else:
        newWordStatus = 'horizontal'
    while nextWord == "":   
        testWordUsable = False
        while testWordUsable == False:
            testWord = random.choice(validanagrams)
            if testWord.find(baseletter) != -1:
                testWordUsable = True
                testWordParts = testWord.split(baseletter,1)
        if newWordStatus == 'vertical':
            midRow = addTo.x
            if midRow - len(testWordParts[0]) > -1 and midRow + len(testWordParts[1]) < 10:
                nextWord = testWord
        else:
            midLetter = addTo.y
            if midLetter - len(testWordParts[0]) > -1 and midLetter + len(testWordParts[1]) < 10:
                nextWord = testWord
                coords.remove(addTo)
        if newWordStatus == 'vertical':
            lineUp = addTo.y
            nextWordLetters = breakword(nextWord)
            startingPoint = midRow - len(testWordParts[0])
            for i in range(len(nextWordLetters)):
                arr[startingPoint + i][lineUp] = nextWordLetters[i]
                coords.append(Coord(startingPoint + i, lineUp,nextWordLetters[i], 'vertical'))
        else: 
            row = addTo.x
            midLetter = addTo.y
            nextWordLetters = breakword(nextWord)
            startingPoint = midLetter - len(testWordParts[0])
            for i in range(len(nextWordLetters)):
                arr[row][startingPoint + i] = nextWordLetters[i]
                coords.append(Coord(row, startingPoint + i,nextWordLetters[i], 'horizontal'))
        print(nextWord)



startCrossword()
for i in range(0,3):
    addCrossWord()
for x in range(len(arr)):
    print(arr[x])
