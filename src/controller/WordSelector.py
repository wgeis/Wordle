import sys
sys.path.append("src\model")
#Append the path.
import ConnectortoDB
# import the file

usefromoutside = ConnectortoDB.Wordfinder("","")
print(usefromoutside.getRandomWordAndCompareToUsedWords())

