import random

#attributes and lists
source = "src\model\possible_words.txt"
used= "src\model\\used_words.txt"



def checkIfWordIsUsedInFile(txtfile,word):
    wordUsed=False    
    with  open(txtfile,"r") as file:
        
        lines=file.read()
        if(word in lines):
            wordUsed=True

    return wordUsed
    


print(check)


def findWords(txtfile):
    file = open(txtfile,"r")
    lines=file.readlines()
    file.close()
    return lines

wordlist = findWords(source)


#find word:
randomWord=random.choice(wordlist)
check =checkIfWordIsUsedInFile(used,randomWord)
#compare to list:








