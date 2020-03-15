# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hangman.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import hmresources

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
        font.setPointSize(36)
        self.linesletters.setFont(font)
        self.linesletters.setTextFormat(QtCore.Qt.AutoText)
        self.linesletters.setScaledContents(False)
        self.linesletters.setAlignment(QtCore.Qt.AlignCenter)
        self.linesletters.setWordWrap(True)
        self.linesletters.setObjectName("linesletters")
        
        self.drawing = QtWidgets.QLabel(self.centralwidget)
        self.drawing.setGeometry(QtCore.QRect(720, 0, 661, 661))
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
        font.setPointSize(36)
        self.inputbox.setFont(font)
        self.inputbox.setText("")
        self.inputbox.setObjectName("inputbox")
        
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(970, 910, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.linesletters.setText(_translate("MainWindow", "LINES AND NUMBER LETTERS"))
        self.submitButton.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
