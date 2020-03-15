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
    Exit_Code = -123
    
    
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
        
        self.guessedbox = QtWidgets.QListWidget(self.centralwidget)
        self.guessedbox.setGeometry(QtCore.QRect(1420, 660, 491, 371))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.guessedbox.setFont(font)
        self.guessedbox.setObjectName("guessedbox")
        
        self.wrongentrieslabel = QtWidgets.QLabel(self.centralwidget)
        self.wrongentrieslabel.setGeometry(QtCore.QRect(1420, 590, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.wrongentrieslabel.setFont(font)
        self.wrongentrieslabel.setTextFormat(QtCore.Qt.AutoText)
        self.wrongentrieslabel.setScaledContents(False)
        self.wrongentrieslabel.setAlignment(QtCore.Qt.AlignBottom)
        self.wrongentrieslabel.setWordWrap(True)
        self.wrongentrieslabel.setObjectName("wrongentrieslabel")
        
        self.inputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputbox.setGeometry(QtCore.QRect(210, 910, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.inputbox.setFont(font)
        self.inputbox.setText("")
        self.inputbox.setObjectName("inputbox")
        self.inputbox.setFocus(QtCore.Qt.MouseFocusReason)
        
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(970, 910, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.SubmitButtonClicked)
        # self.submitButton.setShortcut(QtGui.QKeySequence("Return")) Use at the main part of code, not here.
        
        self.submit_button_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.submitButton)
        self.submit_button_shortcut.activated.connect(self.SubmitButtonClicked)
        
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
            self.Update_List(letter)
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
            self.Update_List(random_word)
            self.CheckWinCondition()
            
    
    def SubmitButtonClicked(self):
        self.letter = self.inputbox.text()
        self.inputbox.clear()
        if len(self.letter) != 1 and len(self.letter) != len(self.HM_word):
            self.popup_wrongindex()
            return
        
        if len(self.letter) == len(self.HM_word):
            for a in self.guessed_words:
                if a == self.guessed_words:
                    self.popup_guessedwords()
                    return
            self.word_guess(self.letter)
        
        else:
            for x in self.guessed_letters:
                if x == self.letter:
                    self.popup_guessedletters()
                    return
            self.letter_guess(self.HM_word, self.letter)
        self.inputbox.setFocus(QtCore.Qt.MouseFocusReason)
            
    def popup_win(self):
        win_message = QtWidgets.QMessageBox()
        win_message.setWindowTitle("YOU WIN!")
        win_message.setText("Congratulations, You Win!")
        win_message.setInformativeText("Would you like to restart?")
        win_message.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        win_message.buttonClicked.connect(self.Restart)
        win_message.exec_()
    
    def popup_lose(self):
        lose_message = QtWidgets.QMessageBox()
        lose_message.setWindowTitle("YOU LOSE!")
        lose_message.setText("The correct word is '" + self.HM_word + "' \nTry harder next time :^)" )
        lose_message.setInformativeText("Would you like to restart?")
        lose_message.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        lose_message.setIcon(QtWidgets.QMessageBox.Critical)
        lose_message.buttonClicked.connect(self.Restart)
        lose_message.exec_()
        
    def popup_wrongindex(self):
        saytryagain = QtWidgets.QMessageBox()
        saytryagain.setWindowTitle("Oops")
        saytryagain.setText("Please enter only 1 letter or 1 word with the correct number of letters")
        saytryagain.setIcon(QtWidgets.QMessageBox.Warning)
        saytryagain.exec_()
        self.inputbox.setFocus(QtCore.Qt.MouseFocusReason)
        
    def popup_guessedletters(self):
        same_letter = QtWidgets.QMessageBox()
        same_letter.setWindowTitle("You guessed this before")
        same_letter.setText("The letter you guessed has already been guessed, please guess another letter or word")
        same_letter.setIcon(QtWidgets.QMessageBox.Warning)
        same_letter.exec_()
        self.inputbox.setFocus(QtCore.Qt.MouseFocusReason)
    
    def popup_guessedwords(self):
        same_word = QtWidgets.QMessageBox()
        same_word.setWindowTitle("You guessed this before")
        same_word.setText("The word you guessed has already been guessed, please guess another letter or word")
        same_word.setIcon(QtWidgets.QMessageBox.Warning)
        same_word.exec_()
        self.inputbox.setFocus(QtCore.Qt.MouseFocusReason)
    
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
            self.popup_lose()
            self.submitButton.setDisabled(True)
        
        if self.word_guessed == True:
            self.popup_win()
            self.submitButton.setDisabled(True)
        
        for x in self.word:
            if x == "_":
                return
        else:
            self.popup_win()
            self.submitButton.setDisabled(True)
            
    def Update_List(self, guess):
        self.guessedbox.addItem(guess)
        
    def Restart(self, i):
        if i.text() == "&Yes":
            QtWidgets.qApp.exit(Ui_MainWindow.Exit_Code)
        elif i.text() == "&No":
            sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.linesletters.setText(_translate("MainWindow", "LINES AND NUMBER LETTERS"))
        self.submitButton.setText(_translate("MainWindow", "SUBMIT"))
        self.wrongentrieslabel.setText(_translate("MainWindow", "Wrong Entries"))

if __name__ == "__main__":
    currentExitCode = Ui_MainWindow.Exit_Code
    while currentExitCode == Ui_MainWindow.Exit_Code:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        currentExitCode = app.exec_()
        app = None
        # sys.exit(app.exec_())


