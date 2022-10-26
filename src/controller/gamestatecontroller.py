
import sys
sys.path.append("src\model")
#Append the path.
import ConnectortoDB

# import the file

from colorama import init, Fore, Back
init()



class gamestatecontroller():
    def __init__(self) -> None:
        self.source = "src\model\possible_words.txt"
        self.used= "src\model\\used_words.txt"
       
        getword = ConnectortoDB.Wordfinder("","")
        
        self.selectedword= getword.getRandomWordAndCompareToUsedWords()
        self.possiblewordslist = getword.findWords(self.source) #2309 words
        #Returns a touple. First is a list of the possible words, the second is the word.
        self.wordisguessed=False
        self.usedguesseslist =[] #This is for already attempted guesses

    def addGuessToUsedWordsList(self,guess):
        self.usedguesseslist.append(guess)
    def validateGuess(self,guess : str):
        """Validate the guess before processing it by separate method."""
        guess = guess.lower()
        #Can the word be accepted and then evaluated??
        onlyLetters = guess.isalpha()
        length= len(guess)==5   
        wordExists=False
        for word in self.possiblewordslist:
            if guess in word:
                #Funky error - when I print it out as a list, it gives me the \n. Clonky workaround but it helps.
               
                wordExists= True

        uniqueguess = guess not in self.usedguesseslist
        
        guessIsValid=onlyLetters and length and uniqueguess and wordExists==True
        if(guessIsValid):
            self.usedguesseslist.append(guess)
            #print(guess," exists in the list")
            #print(self.usedguesseslist)
        elif not (wordExists):
            print("The word is not in the list :(")
        elif not (length):
            print("how dare you not enter a word with %d letters. Shame! 🔔 "% self.wordLength) #Just for shizzles and giggles 

        return guessIsValid
   
    def simpleWordChecker(self,guess):
        currentGuessThatIsShownToTheUser =""
        guessMe=self.selectedword
        # for i in range(len(guess)):#Allows for variable lengths.
        #         listOfLettersTosHow=listOfLettersTosHow+guess[i] #make new string, append with old.

        for i in range(len(guess)):
                   
                                   
            if(guess[i]==guessMe[i]):
                #if the letter is a match, color the letter green in our list.
                currentGuessThatIsShownToTheUser=currentGuessThatIsShownToTheUser+ Back.GREEN + guess[i] + Back.RESET
                    
            elif(guess[i] in guessMe): #in it
                
                currentGuessThatIsShownToTheUser=currentGuessThatIsShownToTheUser+ Back.YELLOW + guess[i] + Back.RESET
                #listOfLettersTosHow=listOfLettersTosHow.replace(listOfLettersTosHow[i],"?",1)
            if(guess[i] not in guessMe): #Not in 
                    currentGuessThatIsShownToTheUser=currentGuessThatIsShownToTheUser+ Back.RED + guess[i] + Back.RESET

                
                    
        return currentGuessThatIsShownToTheUser
  

                

game = gamestatecontroller()
gameIsRunning = True



while gameIsRunning:
        print("type exit to stop game and get the secret word")
        print("start a new game?y/n")
        action = input()
        if action =="n":
            gameIsRunning=False
        elif action=="y":
            numberOfGuesses =0
            print("Guess a word with 5 letters")

            
            while numberOfGuesses<6:
                currentGuessThatIsShownToTheUser =""
                guess = input()
                if(guess=="exit"):
                    print("Det hemmelige ord var "+game.selectedword)
                    break         

                
                if(game.validateGuess(guess)):
                    #check if its a valid guess):
                    currentGuessThatIsShownToTheUser=game.simpleWordChecker(guess)
                    print(currentGuessThatIsShownToTheUser)
                    numberOfGuesses=numberOfGuesses+1
                    print(str(numberOfGuesses)+" forsøg brugt")  
      

   



#Lets try making the game as a console version. The game will run while...


        




            
    
        

              
                






#Find a word 
