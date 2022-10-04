import sys
sys.path.append("src\model")
#Append the path.
import ConnectortoDB
# import the file

class gamestatecontroller:
    def __init__(self) -> None:
        self.numberattempts= 5
        getword = ConnectortoDB.Wordfinder("","")
        self.possiblewords= getword.findWords
        self.selectedword = getword.getRandomWordAndCompareToUsedWords()
        self.wordisguessed=False
        self.usedWords =[]
    def addGuessToUsedWordsList(self,guess):
        self.usedWords.append(guess)

Game = gamestatecontroller()

def validateGuess():
    guess = input()
    if(len(guess)==5 and guess in Game.possiblewords):
        print(guess)

#print(Game.numberattempts)


#logic for checking words.

