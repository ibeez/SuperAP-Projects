#attempts to create a list of valid anagrams, and then generate a 'crossword' of possible answers using the given set of letters

import random 
import enchant

#pyenchant is a python module used for spell checking that returns a true or false answer depending on if the given string is a valid english word 
dictionary = enchant.Dict("en_US")


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
for x in range(len(arr)):
    print(arr[x])

#function to break a string into a list of characters 
def breakword(thingy):
    broken = []
    for i in range(len(thingy)):
        broken.append(thingy[i:i+1])
    return broken 
def startCrossword():
    wordpicker = random.choice(validanagrams)
    print(wordpicker)
    rowpicker = random.randint(0,len(arr))
    spotpicker = random.randint(0,len(arr) - len(wordpicker) - 1)
    wordToAdd = breakword(wordpicker)
    for i in range(len(wordToAdd)):
        arr[rowpicker][spotpicker + i] = wordToAdd[i]
    

def addCrossWord(): 
    print("")


startCrossword()
for x in range(len(arr)):
    print(arr[x])