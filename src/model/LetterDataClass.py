#pyQT comes in handy here, if possible. 

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

class LetterThatCanBePainted():
   

    def __init__(self,theLetter):
        self.letterState = 0
        self.theLetter= theLetter
    def getLetter(self):
        return self.theLetter
    def setLetterState(self,letterstate):
        self.letterState=letterstate
        #starts as 0, but if its 1, it appears in the word. If it is a match, make it 2.
    def getLetterState(self):
        return self.letterState
    

    
        