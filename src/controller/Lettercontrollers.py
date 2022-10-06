import sys
from typing import List
sys.path.append("src\model")
from LetterDataClass import LetterThatCanBePainted as Letterclass


class Lettercontroller: 
  
    def __init__(self):
        self.alphabets_in_lowercase=[]
        self.letters =[]
        for i in range(97,123):
            self.alphabets_in_lowercase.append(chr(i))
            for letter in self.alphabets_in_lowercase:
                self.letters.append(Letterclass(letter))
                #ToDo: Make sure that the letters created can be updated later. This is just for initiating the letters.
    def updateLetterState(self,letterstate,letter=Letterclass):
        letter.setLetterState(letterstate)
    def getLettersArray(self):
        return self.letters
    #print(alphabets_in_lowercase)

Controller = Lettercontroller()
letters = Controller.getLettersArray()


for letterclass in letters:
    print (letterclass.getLetter())
    
fooo = List

#test

print ("Ah der")
    

    