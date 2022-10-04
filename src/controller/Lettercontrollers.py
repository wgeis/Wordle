import sys
sys.path.append("src\model")
import LetterDataClass

alphabets_in_lowercase=[]
for i in range(97,123):
    alphabets_in_lowercase.append(chr(i))
#print(alphabets_in_lowercase)

letters=[]#Letter container
for letter in alphabets_in_lowercase:
    
    letters.append(LetterDataClass.LetterThatCanBePainted(letter))

for Letter in letters:
    print(Letter)

    