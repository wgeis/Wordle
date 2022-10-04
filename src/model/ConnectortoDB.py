
import random

class Wordfinder:
    def __init__(self,source,used):
        self.source = "src\model\possible_words.txt"
        self.used= "src\model\\used_words.txt"

        

#attributes and lists
    def findWords(self,txtfile):
        with  open(txtfile,"r") as file:
          lines=file.readlines()
        return lines


    def checkIfWordIsUsedInFile(self,txtfile,word):
        wordUsed=False    
        with  open(txtfile,"r+") as file:
            
            lines=file.readlines()
            if(word in lines):
                wordUsed=True
            else:
                file.write(word)

        return wordUsed


    def addWordIfNotExists(self,txtfile,word):

        if not(self.checkIfWordIsUsedInFile(txtfile=txtfile,word=word)):
        
            with  open(txtfile,"a") as file:
               file.write(word)
            print("word added:"+word)


    def getRandomWordAndCompareToUsedWords(self):
        wordlist = self.findWords(self.source)
        
        randomWord=random.choice(wordlist)
        while (self.checkIfWordIsUsedInFile(self.used,randomWord)):
            #use a while loop to ensure that our word is not found in the list - and if it is, go back again.
            randomWord=random.choice(wordlist)
            #declare it to be new.
        else:
            return randomWord

       
        

#test = Wordfinder(source="",used="")

#singleword = test.getRandomWordAndCompareToUsedWords()
#print(singleword)













#find word:












