# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Scott\Dev\TheNASA\client\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from detectorUI import Ui_DetectorWindow
from lastTen import Ui_TenWindow
import math


class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(600, 300)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        
        self.setMinimumSize(QtCore.QSize(600, 300))
        self.setMaximumSize(QtCore.QSize(600, 300))
        
        self.centralwidget = QtWidgets.QWidget(self)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(40, -10, 491, 91))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label")
        
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
        
        self.label_projectHeader = QtWidgets.QLabel(self.centralwidget)
        self.label_projectHeader.setGeometry(QtCore.QRect(220, 80, 161, 51))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        
        self.label_projectHeader.setFont(font)
        self.label_projectHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.label_projectHeader.setObjectName("label_projectHeader")
        
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
        
        self.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.setMenuBar(self.menubar)
        
        self.actionClickbait_Detector = QtWidgets.QAction(self)
        self.actionClickbait_Detector.setObjectName("actionClickbait_Detector")

        self.actionRecord = QtWidgets.QAction(self)
        self.actionRecord.setObjectName("actionRecord")

        self.menuFile.addAction(self.actionClickbait_Detector)
        self.menuFile.addAction(self.actionRecord)
        self.menuFile.triggered[QtWidgets.QAction].connect(self.displayDetector)
        
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.dialog = Ui_DetectorWindow()
        self.records = Ui_TenWindow()

        self.internalData = []

        self.records.setupUi(self)
        self.dialog.setupUi(self)

    def displayDetector(self, q):
            if not q or q.text() == "Clickbait Detector":
                self.dialog.show()
            elif q.text() == "Records":
                self.records.show()

    def logData(self, text, val):
        if len(self.internalData) > 10:
            del self.internalData[-1]
        self.internalData.insert(0, [text, val >= 0.5, math.trunc(val * 10000) / 100])
        print(self.internalData)
        self.records.updateView(self.internalData)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "The National Agile and Scrum Association"))
        self.label_projectHeader.setText(_translate("MainWindow", "Our Projects"))
        self.btnDetector.setText(_translate("MainWindow", "Clickbait Detector"))
        self.btnEmpty_1.setText(_translate("MainWindow", "Coming Soon"))
        self.btnEmpty_2.setText(_translate("MainWindow", "Coming Soon"))
        self.btnEmpty_3.setText(_translate("MainWindow", "Coming Soon"))
        self.menuFile.setTitle(_translate("MainWindow", "Pages"))
        self.actionRecord.setText(_translate("MainWindow", "Records"))
        self.actionClickbait_Detector.setText(_translate("MainWindow", "Clickbait Detector"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
