# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hangman.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import hmresources
import sys
import numpy as np
import csv
import pandas as pd
import random
import io

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.linesletters = QtWidgets.QLabel(self.centralwidget)
        self.linesletters.setGeometry(QtCore.QRect(0, 660, 1491, 211))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(72)
        self.linesletters.setFont(font)
        self.linesletters.setTextFormat(QtCore.Qt.AutoText)
        self.linesletters.setScaledContents(False)
        self.linesletters.setAlignment(QtCore.Qt.AlignCenter)
        self.linesletters.setWordWrap(True)
        self.linesletters.setObjectName("linesletters")
        
        self.drawing = QtWidgets.QLabel(self.centralwidget)
        self.drawing.setGeometry(QtCore.QRect(500, 0, 661, 661))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.drawing.setFont(font)
        self.drawing.setText("")
        self.drawing.setPixmap(QtGui.QPixmap(":/images/Stage 0.png"))
        self.drawing.setScaledContents(True)
        self.drawing.setAlignment(QtCore.Qt.AlignCenter)
        self.drawing.setObjectName("drawing")
        
        self.guessedbox = QtWidgets.QListView(self.centralwidget)
        self.guessedbox.setGeometry(QtCore.QRect(1490, 660, 421, 371))
        self.guessedbox.setObjectName("guessedbox")
        
        self.inputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputbox.setGeometry(QtCore.QRect(210, 910, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.inputbox.setFont(font)
        self.inputbox.setText("")
        self.inputbox.setObjectName("inputbox")
        
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(970, 910, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.SubmitButtonClicked)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.englishwords = QtCore.QFile(":/csv/englishwords.csv")
        if self.englishwords.open(QtCore.QIODevice.ReadOnly):
            self.f = io.BytesIO(self.englishwords.readAll().data())
        self.file = pd.read_csv(self.f, sep = ';', skiprows=3)
        self.file = self.file.dropna(thresh=2)
        self.file = self.file.drop(self.file[self.file['word'].map(len) < 3].index)
        self.words = self.file['word']
        index = random.randint(0, len(self.words) - 1)
        self.HM_word = self.words[index]

        self.guessed_letters = {}
        self.guessed_words = {}
        
        lines = ''
        for number_of_letters in range(len(self.HM_word)):
            lines += "__ "
            self.linesletters.setText(lines)
        self.mistakes = 0
        self.word_guessed = False
        
    def letter_guess(self, random_word, letter):
        wrong = False
        for letters in random_word:
            if letters == letter:
                self.guessed_letters[letter] = True
                self.display(self.HM_word, self.guessed_letters)
                self.CheckWinCondition()
                return
        else:
            self.guessed_letters[letter] = False
            wrong = True
            self.mistakes += 1
            self.drawing.setPixmap(QtGui.QPixmap(":/images/Stage " + str(self.mistakes) + ".png"))
            self.display(self.HM_word, self.guessed_letters)
            self.CheckWinCondition()
            
    def word_guess(self, random_word):
        if str(random_word) == self.HM_word:
            self.linesletters.setText(self.HM_word)
            self.word_guessed = True
            self.CheckWinCondition()
        
        else:
            self.guessed_words[random_word] = False
            self.mistakes += 1
            self.drawing.setPixmap(QtGui.QPixmap(":/images/Stage " + str(self.mistakes) + ".png"))
            self.display(self.HM_word, self.guessed_letters)
            self.CheckWinCondition()
            
    
    def SubmitButtonClicked(self):
        ########include if statement for number of letters######## DONE
        self.letter = self.inputbox.text()
        self.inputbox.clear()
        if len(self.letter) != 1 and len(self.letter) != len(self.HM_word):
            print("try again")
            ##pop up to try again##
            return
        
        if len(self.letter) == len(self.HM_word):
            for a in self.guessed_words:
                if a == self.guessed_words:
                    print('The word you guessed has already been guessed, please guess another word or letter')
                    return
            self.word_guess(self.letter)
        
        else:
            for x in self.guessed_letters:
                if x == self.letter:
                    ######### label statement to replace ##########
                    print('The letter you guessed has already been guessed, please guess another letter or word')
                    return
            self.letter_guess(self.HM_word, self.letter)
    
    def display(self, random_word, guessed_letters):
        self.word = ''
        for x in random_word:
            for y in guessed_letters:
                if x == y:
                    self.word += y + " "
                    break
            else:
                self.word += "__ " 
        self.linesletters.setText(self.word)
        
    def CheckWinCondition(self):
        if self.mistakes >= 6:
            print('The correct word is "' + self.HM_word + '"') ###### pop up dialog #######
            print('Try harder next time :^)')
            self.submitButton.setDisabled(True)
        
        if self.word_guessed == True:
            print('Congratulations, You Win!')
            self.submitButton.setDisabled(True)
        
        for x in self.word:
            if x == "_":
                return
        else:
            print('Congratulations, You Win!')
            self.submitButton.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.linesletters.setText(_translate("MainWindow", "LINES AND NUMBER LETTERS"))
        self.submitButton.setText(_translate("MainWindow", "SUBMIT"))

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


