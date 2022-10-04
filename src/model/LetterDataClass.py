#pyQT comes in handy here, if possible. 

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

class LetterThatCanBePainted():

    def __init__(self,theLetter):
        self.colorOfLetter =""
        self.theLetter= theLetter
    def getLetter(self):
        return self.theLetter
    def getColor(self):
        return self.colorOfLetter