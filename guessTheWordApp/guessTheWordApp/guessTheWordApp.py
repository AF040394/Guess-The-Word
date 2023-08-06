import random
wordList = []
#open the file and save the items into a list
myFile = open("dictionary1.txt","r")
for line in myFile:
    words = line.strip()
    wordList.append(words)
myFile.close()
#pick a random lenght between 4 and 12
lenght = random.randint(4,12)
difficulty = False
#total number of guesses
numberGuess = lenght*2 
#display the secret word with underscores for how many letters
secret = ["_"]* lenght
#keep track of all guesses
allGuess = []
#chosen list that store the words that are in the game
chosenLenght = []
#counter to check if first turn
round = 0
#zero letter frequency
zeroWord = []
#one more letter frequency
oneWord = []
#more words letter frequency
moreWords=[]
#excluded words
excludedWords=[]
guessCounter = 0
#append all wrong guess
wrongGuess=[]
counter = 0 
endGame = False


#this method devides the wordlist into wordfamilies in the first iteration
#in the second iteration the method will divide the largest family into different list based on the occurency of the guess
def wordFamilies(list,secret, guess,excludedWords,zeroWord,oneWord,moreWords):
        for item in list: #chosenLenght
            if len(item) != len(secret):
                excludedWords.append(item)
            elif guess not in item and item not in zeroWord  and item not in excludedWords and item not in oneWord and item not in moreWords: 
                zeroWord.append(item)
            elif guess in item and item.count(guess) == 1 and item not in oneWord and item not in excludedWords and item not in zeroWord and item not in moreWords:
                oneWord.append(item)
            elif guess in item and item.count(guess) > 1 and item not in moreWords and item not in excludedWords and item not in oneWord and item not in zeroWord:
                moreWords.append(item)
#this method will return the largest family

def largestWordFamily(zeroWord,oneWord,moreWords):
        #this if statemente is >= because if the list are the same lenght, it will not give error
       if len(zeroWord) >= len(oneWord) and len(zeroWord) >= len(moreWords):
           return zeroWord
       elif len(oneWord) > len(zeroWord) and len(oneWord) >= len(moreWords):
           return oneWord
       elif len(moreWords) > len(zeroWord) and len(moreWords) > len(oneWord):
           return moreWords


#this method checks the position of the guess in the secret word and compare it to te position of the items of the largest family
def checRightWord(secret, chosenLenght,guess):
    #i need to convert the secret list into a string
    y = ''.join(secret)
    #since i remove the item from the list that is in loop 
    #the loop starts from the end of the list so to avoid jumping an item
    #i did this because if the loop starts at 0 it doesn't consider some item in the list
    for item in reversed(chosenLenght):

        if y.index(guess) != item.index(guess):

            chosenLenght.remove(item)
#this method will read the guess
def readGuess(guess):
    
        guess = input('Guess a character: ')
        #put the guess to lower case
        guess = guess.lower()
       #check if the letter has been used before
        if guess in allGuess and len(allGuess) != 0:
             print("You tried this letter before, please enter a new one!")
             #if the letter has been used, return the guess to a none value 
             #while program running if guess is set to none
             #the program prompt to user to choose another letter
             guess = None
        return guess
    #method for valid input
def checkGuess(guess):
    #check the llenght of the input, if one than more character, set guess to none
     if guess != None and len(guess) > 1:
        print("You entered a wrong value, please try again")
        guess = None
     return guess
#method for the hard mode
def hardMode(wordList,secret, guess,excludedWords,zeroWord):
   #exclude the words with different lenght
    for item in wordList:
        if len(item) != len(secret):
            excludedWords.append(item)
         #append all item that don't have a guess 
        elif guess not in item:
            zeroWord.append(item)
         #append all item that have one guess
        elif guess in item and item.count(guess) == 1:
            zeroWord.append(item)
    return zeroWord
#remove all words where there is a wrong letter used
def removeFailingWords(wrongGuess, chosenLenght):
    for item in wrongGuess:
        for element in reversed(chosenLenght):
            if item in element:
                chosenLenght.remove(element)
#hard mode change word
def changeWord(chosenLenght, guess):
    for item in reversed(chosenLenght):
        #make sure that the list has at least an item, otherwise the program break
        if guess in item and len(chosenLenght)>1:
            chosenLenght.remove(item)
#this method checks the words index with the secret index, if a letter is present in secret
def checRightWordHard(secret, chosenLenght,guess,excludedWords):
 
    y = ''.join(secret)

    for item in chosenLenght:

        if y.index(guess) != item.find(guess):
            excludedWords.append(item)
    for element in excludedWords:
        if element in chosenLenght:
            chosenLenght.remove(element)
#hard mode, check how many emprty spaces left
def checkEmptySpaces(secret):
    number = 0
    for item in secret:
        if item == '_':
            number = number+1
    #return the number of empty spaces
    return number
#check if the user input
while(difficulty == False):
    print("Choose the difficulty level:")
    print("1 Easy")
    print("2 Hard")
    #prompt the user the difficulty level
    userChoice = input("press 1 or 2: ")
    if(userChoice == '1' or userChoice == '2'):
        difficulty = True
    else:
        print('You entered a wrong input')
if userChoice == '1':
    while not endGame:
        #reset the guess each turn
        guess = None
        print(str(secret))
        #print the number of guesses left
        print("Number Of Guess Left: " + str(numberGuess))
        #print usd letters
        print("Used letters "+ str(allGuess))
    

        #this if statemen is needed to run the wordfamily list first 
        if round == 0: 
            while guess == None:
                #check if the guess is valid
                guess = readGuess(guess)
                guess = checkGuess(guess)
            #append the guess to allGuesss to display the letter used
            allGuess.append(guess)
            wordFamilies(wordList,secret, guess,excludedWords,zeroWord,oneWord,moreWords)
        
        else: 
            guess = None
            while guess == None:
                guess = readGuess(guess)
                guess = checkGuess(guess)
            allGuess.append(guess)
            print("excluded words : " + str(excludedWords))
            print(" words : " + str(chosenLenght))
            wordFamilies(chosenLenght,secret, guess,excludedWords,zeroWord,oneWord,moreWords)
       #return the largest family and save the list to a variable
        x = largestWordFamily(zeroWord,oneWord,moreWords)
        #i need to copy the list, otherwise when i reset the list at the end, the items in chosenLenght willl be lost
        chosenLenght = x.copy()
        print(chosenLenght)
        
        #select a random word in the largest list
        word = random.choice(chosenLenght)
        print(word)
    
   
        temp = 0
        round += 1
        #check if the guess is in the word
        if guess in word:

            #this will run until the end of the word
            while word.find(guess,temp) !=-1: 
                 #find the guess in the word and save it to a temporary variable
                temp = word.find(guess,temp)
                #pass the temporary index and insert the guess
                secret[temp] = guess
            
                #move one space
                temp += 1
                #check how many words are in the guess
                guessCounter+=1
            print("Your guess is correct")
            
       
        
            #check all the words that have same letter but in dfifferent position 
            #exclude the word that don't have the letter at the same index
            checRightWord(secret, chosenLenght,guess)
            #subctract one attempt
            numberGuess -=1
        
        
            #check if the user find the word and end game
            if len(word) == guessCounter:
                print(secret)
                print("You win! the secret word is:" + word)
            
                endGame = True
      
    
        
        if guess not in word:
    
            print("Your guess is wrong, please try again")
            numberGuess -=1
            #game ends if user finishes the attempts
            if numberGuess == 0:
                print(secret)
                print("You lost! the secret word was:" + word)
 
                endGame = True


        #clear the list at the end of each turn
        #there are new list each turn with different words
        zeroWord.clear()
        oneWord.clear()
        moreWords.clear()
#hard mode
if userChoice == '2':  
    while not endGame:
    
        guess = None
        print(str(secret))
    
        print("Used letters "+ str(allGuess))
        print("Number Of Guess Left: " + str(numberGuess))

        #this if statemen is needed to run the wordfamily list first and after the largest family
        if round == 0: 
            while guess == None:
                guess = readGuess(guess)
                guess = checkGuess(guess)
            allGuess.append(guess)
            #pass the list with zero word guess frequency
            x = hardMode(wordList,secret, guess,excludedWords,zeroWord)
            #copy the list
            chosenLenght = x.copy()
        else: 
            guess = None
            while guess == None:
                guess = readGuess(guess)
                guess = checkGuess(guess)
            allGuess.append(guess)
 
        
        print(chosenLenght)
        #check if the number of guesses left or the empty spaces of the secret word
        if (numberGuess<=10 and len(chosenLenght)>1 or counter < 7 and len(chosenLenght)>1 ):
            #given those condition the program will discard the words containing the guess
            #making the game harder
            changeWord(chosenLenght, guess)
            word = random.choice(chosenLenght)
        else:
            word = random.choice(chosenLenght)
        print(word)
    
   
        temp = 0
        round += 1
        if guess in word:

        
            while word.find(guess,temp) !=-1: 
            
                temp = word.find(guess,temp)
                secret[temp] = guess
                temp += 1
                guessCounter+=1
            print("Your guess is correct")
            
            checRightWordHard(secret, chosenLenght,guess,excludedWords)
            numberGuess -=1
        
        

            if len(word) == guessCounter:
                print(secret)
                print("You win! the secret word is:" + word)
            
                endGame = True
      
    
    
        if guess not in word:
    
            print("Your guess is wrong, please try again")
            #append the wrong guesses
            wrongGuess.append(guess)
            #remove the words with wrong letters
            removeFailingWords(wrongGuess, chosenLenght)
            numberGuess -=1
            if numberGuess == 0:
                print(secret)
                print("You lost! the secret word was:" + word)
 
                endGame = True
    #count how many empty spaces there are and save it to a counter
    counter = checkEmptySpaces(secret)


