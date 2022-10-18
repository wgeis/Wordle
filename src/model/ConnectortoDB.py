
import random

class Wordfinder:
    """This class is used to find a possible word - also contains logic to make sure it doesn't choose duplicates. """
    def __init__(self,source,used):
        self.source = "src\model\possible_words.txt"
        self.used= "src\model\\used_words.txt"

        

#attributes and lists
    def findWords(self,txtfile):
        """GLobal method for getting a list of words from a textifle. """
        with  open(txtfile,"r") as file:
          lines=file.readlines()
          for line in lines:
            line = line.strip("\n")
            
            #strip it of newline symbols.

        return lines
    def findWordsFromStandardFile(self):
        
        #For use if you don't have a standard file
        with  open(self.source,"r") as file:
          lines=file.readlines()
        return lines

#Works fine
    def addWordIfNotUsedInFile(self,txtfile,word):
        """Appends the file if the chosen word is not found in it. Used as a separate function to keep things untangled. But it violates DRY."""
        wordUsed=False    
        with  open(txtfile,"r+") as file:
            
            lines=file.readlines()
            if(word in lines):
                wordUsed=True
            else:
                file.write(word)

        return wordUsed



#Randomword works
    def getRandomWordAndCompareToUsedWords(self):
        """"this makes sure to generate a word not used previously. It utilizes the FindWords and AddWordNotUsed """
        wordlist = self.findWords(self.source)
        
       # print("from getrandoms",wordlist)
        randomWord=random.choice(wordlist)
        while (self.addWordIfNotUsedInFile(self.used,randomWord)):
            #use a while loop to ensure that our word is not found in the list - and if it is, go back again.
            randomWord=random.choice(wordlist)
            #declare it to be new.
        else:
           
            return randomWord

       
        

# test = Wordfinder(source="",used="")
# for i in range(1,100):
#     singleword = test.getRandomWordAndCompareToUsedWords()
#     print(singleword)

