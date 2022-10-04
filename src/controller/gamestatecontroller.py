import sys
sys.path.append("src\model")
#Append the path.
import ConnectortoDB
# import the file



class gamestatecontroller:
    def __init__(self) -> None:
        self.source = "src\model\possible_words.txt"
        self.used= "src\model\\used_words.txt"
        self.numberattempts= 5
        getword = ConnectortoDB.Wordfinder("","")
        
        self.selectedword= getword.getRandomWordAndCompareToUsedWords()
        self.possiblewordslist = getword.findWords(self.source) #2309 words
        #Returns a touple. First is a list of the possible words, the second is the word.
        self.wordisguessed=False
        self.usedguesseslist =[] #This is for already attempted guesses

    def addGuessToUsedWordsList(self,guess):
        self.usedguesseslist.append(guess)
    def validateGuess(self,guess):
        """Validate the guess before processing it by separate method."""
        guess = str.lower(guess)
        #Can the word be accepted and then evaluated??
        onlyLetters = guess.isalpha()
        length= len(guess)==5   
        wordExists=False
        for word in self.possiblewordslist:
            if guess in word:
                #Funky error - when I print it out as a list, it gives me the \n. Clonky workaround but it helps.
                #print("Found it")
                wordExists= True

        uniqueguess = guess not in self.usedguesseslist
        
        guessIsValid=onlyLetters and length and uniqueguess and wordExists==True
        if(guessIsValid):
            self.usedguesseslist.append(guess)
            #print(guess," exists in the list")
            #print(self.usedguesseslist)
            return guess


    def compareGuessToActualWord(guess):

        for letter in guess:
            print(letter)

                

Game = gamestatecontroller()


    
#Game.validateGuess(input("GÆT NU BLUETOOTH \n"))
print(Game.validateGuess("moron") )
print(Game.validateGuess("homer") )
print(Game.validateGuess("bully") )
print(Game.validateGuess("sully") )
print(len(Game.usedguesseslist))
#print(Game.numberattempts)


#logic for checking words.

