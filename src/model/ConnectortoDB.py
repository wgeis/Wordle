import random

source = "src\model\possible_words.txt"
=

def checkIfWordIsUsedInFile(txtfile,word):
    
    
    file = open(txtfile,"r")
    lines = file.readlines()
    wordUsed = False
    if(word in lines):
        wordUsed=True
    return wordUsed
    

checkIfWordIsUsedInFile(source,"monke")


def findWords(txtfile):
    file = open(txtfile,"r")
    lines=file.readlines()
    file.close()
    return lines

wordlist = findWords(source)

randomWord=random.choice(wordlist)

print(randomWord)







