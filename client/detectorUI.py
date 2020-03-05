# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Scott\Dev\TheNASA\client\detector.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras.models import Sequential
import math


class Ui_DetectorWindow(QtWidgets.QMainWindow):
    def setupUi(self, rootUI):
        self.root = rootUI
        self.setObjectName("MainWindow")
        self.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(400, 280))
        self.setMaximumSize(QtCore.QSize(400, 280))
        self.centralwidget = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(110, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 60, 261, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_prompt = QtWidgets.QLabel(self.centralwidget)
        self.label_prompt.setGeometry(QtCore.QRect(80, 90, 111, 16))
        self.label_prompt.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_prompt.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 90, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 120, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.displayName)
		
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 150, 261, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(106, 170, 191, 21))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_3")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(56, 200, 301, 20))
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_4")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(70, 220, 261, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("label_result")
        self.label_correctionPrompt = QtWidgets.QLabel(self.centralwidget)
        self.label_correctionPrompt.setGeometry(QtCore.QRect(110, 240, 80, 21))
        self.label_correctionPrompt.setObjectName("label_5")
        self.btn_correction = QtWidgets.QPushButton(self.centralwidget)
        self.btn_correction.setGeometry(QtCore.QRect(211, 240, 121, 23))
        self.btn_correction.setObjectName("pushButton_2")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def displayName(self):
        _translate = QtCore.QCoreApplication.translate
        inText = self.lineEdit.text()
        if inText != "":
            self.label_name.setText(_translate("MainWindow", inText))
            self.lineEdit.clear()
            data = self.runPredict(inText)
            if data >= 0.8:
                output = "is CLICKBAIT"
            else:
                output = "is NOT CLICKBAIT"
            readableData = math.trunc(data * 10000) / 100
            self.label_result.setText(output + " (" + str(readableData) + "%)")
            if self.root is not None:
                self.root.logData(inText, data)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Clickbait Detector"))
        self.label_prompt.setText(_translate("MainWindow", "Enter a title or URL:"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_name.setText(_translate("MainWindow", "{Name}"))
        self.label_result.setText(_translate("MainWindow", "is {CLICKBAIT/NOT CLICKBAIT (%)}"))
        self.label_correctionPrompt.setText(_translate("MainWindow", "Is this wrong?"))
        self.btn_correction.setText(_translate("MainWindow", "Submit Correction"))

    def runPredict(self, tex):
        model = load_model('../predictor.h5')
        tokenizer = Tokenizer(num_words=500)
        tokenizer.fit_on_texts(tex)
        input = tokenizer.texts_to_sequences(tex)
        input = pad_sequences(input, padding='post', maxlen=150)
        prediction = model.predict(input)
        val = numpy.sum(prediction[0])
        print(prediction)
        return val/len(prediction[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_DetectorWindow()
    ui.setupUi(None)
    ui.show()
    sys.exit(app.exec_())
