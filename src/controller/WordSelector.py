import random

words ="banan","mango","pærer","æbler","melon","water"
selectedword =""
def select_randomword(list):
    word = random.choice(list)
    print("From select:",word)

    return word

print("before line 12",selectedword)
selectedword=select_randomword(words)
print("after line 12,",selectedword)

