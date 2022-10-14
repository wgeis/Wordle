import sys
from tkinter.ttk import Style
from colorama import init, Fore, Back
init()


sys.path.append("src\model")
from LetterDataClass import LetterThatCanBePainted as Letter



class WordChecker:
    """This thingamabob is for checking a word after we've found it, made our letters etc. It doesn't generate words on it's own. Basically it's entire purpose is to give us a list
    of letter objects and their state, so we then can pass it on to a class that colors those letters."""
    def __init__(self):
        self.wordtobechecked = ""
        #Placeholder for a word. Can be replaced
        self.alphabets_in_lowercase=[]
        #In theory this COULD just be a global thing, but the array it returns, needs to be modified and unique.
        self.lettersList =[]
        #A list of objects.
        for i in range(97,123):
            self.alphabets_in_lowercase.append(chr(i))#create a list of lower case letters
            for letter in self.alphabets_in_lowercase: #For each of those, append the letterslist.
                self.lettersList.append(Letter(letter))
        self.guess =""
        #Needs to be unique for each instance of Wordchecker.
        #in theory, I should probably have a static wordchecker than can then check any guess with a selected word.
        #The current setup is more of a "make new WordChecker, with new word, and unique letter arrays"
    
    
    def setWord(self,wordToBeGuessed):
        #Allows for setting a new word.
        self.wordtobechecked=wordToBeGuessed
    

    def setLettersListToWorkWith(self,lettersToBeSet):
        self.lettersList=lettersToBeSet


    def getGuessAndAppendToGuessList(self,guess):
        #Only allow validated guesses - the guess must be long enough, no numbers etc, and actually be in the source material.
        self.guess=guess #Latest guess
        self.checkWord(guess)

    def checkWordAndReturnList(self,guess):
        showThisToUser=[Letter]
        for i in range(len(guess)):#Allows for variable lengths.
                       
            if(guess[i]==self.wordtobechecked[i]):
                #if the letter is a match, color the letter green in our list.
                color="green"
                    
            if(guess[i] in self.wordtobechecked):
                color="yellow"
            if(guess[i] not in self.wordtobechecked):
               pass 


def simpleWordChecker(guess,guessMe):
    #Only receive valid input
    listOfLettersTosHow =""
    for i in range(len(guess)):#Allows for variable lengths.
            listOfLettersTosHow=listOfLettersTosHow+guess[i] #make new string, append with old.

    for i in range(len(guess)):
        print(i)
        
        
                    
        if(guess[i]==guessMe[i]):
            #if the letter is a match, color the letter green in our list.
            color="green"
            print(color)

                
        elif(guess[i] in guessMe): #in it
            color="yellow"
            print(color)
            #listOfLettersTosHow=listOfLettersTosHow.replace(listOfLettersTosHow[i],"?",1)
        if(guess[i] not in guessMe): #Not in 
                color="gray"
                print(color)

            
                
    return listOfLettersTosHow



#print(simpleWordChecker("qqnqa"))

frabruger= input("Gæt et ord på 5 bogstaver:")
simpleWordChecker(frabruger,"banan")
#word = WordChecker()
