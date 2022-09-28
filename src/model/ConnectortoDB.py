import random

#attributes and lists
source = "src\model\possible_words.txt"
used= "src\model\\used_words.txt"
#find word:

#single line:
#randomword = random.choice(findWords(source))

#print(randomWord)
#compare to list:


#merged code:


def checkIfWordIsUsedInFile(txtfile,word):
    wordUsed=False    
    with  open(txtfile,"r") as file:
        
        lines=file.readlines()
        if(word in lines):
            wordUsed=True

    return wordUsed
    


def findWords(txtfile):

    with  open(txtfile,"r") as file:
        
        lines=file.readlines()
    
    
    
    return lines



def addWordIfNotExists(txtfile,word):
    if not(checkIfWordIsUsedInFile(txtfile=txtfile,word=word)):
        
        with  open(txtfile,"a") as file:
            file.write(word)
        print("word added:"+word)



def searchAndCompareRandomWordToGuess():
    wordlist = findWords(source)
    randomWord=random.choice(wordlist)
    print(checkIfWordIsUsedInFile(used,randomWord))
    #Add if not exists
    addWordIfNotExists(used,randomWord)

searchAndCompareRandomWordToGuess()









