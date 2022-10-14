import PyQt5
import sys
sys.path.append("src\view")
import demo
#uses the materials in the demo-class to do stuff. We're aiming to see if we can get stuff in the console when a gamer presses a button.



class gameLogic:
    def __init__(self) -> None:
    
        pass


    
    def setButtonListeners(self):
        self.BUTTONTEXT=self.pushButton.text()
        self.pushButton.clicked.connect(lambda ch, buttonThatWasPressed=self.pushButton,buttontext=self.BUTTONTEXT:self.getButtonText(buttonThatWasPressed,buttontext))
        

    def getButtonText(self, buttonThatWasPressed,text):
        print("du har trykket på mig!",str(text))
    def enterButton(self):
        #valider om vores gæt er okay - send en string afsted med alle de aktuelle gæt.
        pass
    
