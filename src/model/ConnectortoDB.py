
import random

class Wordfinder:
    def __init__(self,source,used):
        self.source = "src\model\possible_words.txt"
        self.used= "src\model\\used_words.txt"

        

#attributes and lists
    def findWords(self,txtfile):
        
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
        """"this finds a random word and returns the list, THEN the word."""
        wordlist = self.findWords(self.source)
        
       # print("from getrandoms",wordlist)
        randomWord=random.choice(wordlist)
        while (self.addWordIfNotUsedInFile(self.used,randomWord)):
            #use a while loop to ensure that our word is not found in the list - and if it is, go back again.
            randomWord=random.choice(wordlist)
            #declare it to be new.
        else:
           
            return randomWord

       
        

#test = Wordfinder(source="",used="")

#singleword = test.getRandomWordAndCompareToUsedWords()
#print(singleword)













#find word:












