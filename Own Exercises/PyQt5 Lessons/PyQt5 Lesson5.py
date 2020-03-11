# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQT5 Lesson5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import resource #pyrcc5 <filename>.qrc -o <filename>.py

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(6, 3, 791, 431))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(":/com.airbnb.app.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.airbnb = QtWidgets.QPushButton(self.centralwidget)
        self.airbnb.setGeometry(QtCore.QRect(30, 470, 301, 51))
        self.airbnb.setObjectName("airbnb")
        self.misaka = QtWidgets.QPushButton(self.centralwidget)
        self.misaka.setGeometry(QtCore.QRect(410, 470, 361, 51))
        self.misaka.setObjectName("misaka")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.misaka.clicked.connect(self.show_misaka)
        self.airbnb.clicked.connect(self.show_airbnb)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.airbnb.setText(_translate("MainWindow", "Airbnb"))
        self.misaka.setText(_translate("MainWindow", "Misaka"))
        
    def show_misaka(self):
        self.photo.setPixmap(QtGui.QPixmap(":/Misaka.jpg"))

    def show_airbnb(self):
        self.photo.setPixmap(QtGui.QPixmap(":/com.airbnb.app.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
