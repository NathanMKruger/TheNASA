# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Scott\Dev\TheNASA\client\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, -10, 441, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 801, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 80, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.btnDetector = QtWidgets.QPushButton(self.centralwidget)
        self.btnDetector.setGeometry(QtCore.QRect(190, 140, 221, 23))
        self.btnDetector.setObjectName("pushButton")
        self.btnDetector.clicked.connect(self.displayDetector)
        
        self.btnEmpty_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnEmpty_1.setEnabled(False)
        self.btnEmpty_1.setGeometry(QtCore.QRect(190, 170, 221, 23))
        self.btnEmpty_1.setObjectName("btnEmpty_1")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 120, 801, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnEmpty_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnEmpty_2.setEnabled(False)
        self.btnEmpty_2.setGeometry(QtCore.QRect(190, 200, 221, 23))
        self.btnEmpty_2.setObjectName("btnEmpty_2")
        self.btnEmpty_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnEmpty_3.setEnabled(False)
        self.btnEmpty_3.setGeometry(QtCore.QRect(190, 230, 221, 23))
        self.btnEmpty_3.setObjectName("btnEmpty_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionClickbait_Detector = QtWidgets.QAction(MainWindow)
        self.actionClickbait_Detector.setObjectName("actionClickbait_Detector")
        self.menuFile.addAction(self.actionHome)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClickbait_Detector)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def displayDetector(self):
        print("Placeholder!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "The National Agile and Scrum Association"))
        self.label_2.setText(_translate("MainWindow", "Our Projects"))
        self.btnDetector.setText(_translate("MainWindow", "Clickbait Detector"))
        self.btnEmpty_1.setText(_translate("MainWindow", "Coming Soon"))
        self.btnEmpty_2.setText(_translate("MainWindow", "Coming Soon"))
        self.btnEmpty_3.setText(_translate("MainWindow", "Coming Soon"))
        self.menuFile.setTitle(_translate("MainWindow", "Pages"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionClickbait_Detector.setText(_translate("MainWindow", "Clickbait Detector"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())