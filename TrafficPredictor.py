# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrafficPredictor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt , QDateTime
from keras.models import load_model
import numpy as np
TrafficModel = load_model('70_50_60_elu_elu_elu_adam.hdf5')
dateTime = QDateTime()
dayNum = { "Monday":1,
			"Tuesday":2,
			"Wednesday":3,
			"Thursday":4,
			"Friday":5,
			"Saturday":6,
			"Sunday":7
}

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 296)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 170, 111, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 100, 221, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 221, 21))
        self.label.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 111, 20))
        self.label_2.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 241, 31))
        self.label_3.setStyleSheet("font: 87 20pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 100, 111, 31))
        self.pushButton.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 250, 371, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 121, 16))
        self.label_4.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select the Date and Time "))
        self.label_2.setText(_translate("Dialog", "Traffic Density"))
        self.label_3.setText(_translate("Dialog", "Traffic Forecast"))
        self.pushButton.setText(_translate("Dialog", "Predict"))
        self.label_4.setText(_translate("Dialog", "Traffic Status"))

    def TrafficStatus(self,Traffic):
        MaxCapacity = 150
        FilledPerc = (Traffic / MaxCapacity) * 100
        self.progressBar.setValue(FilledPerc)
		
    def handlePredictPress(self):
        global dateTime
        global dayNum
        #dateTime = self.dateTimeEdit.dateTime()
        dateTime = self.dateTimeEdit.dateTime()
        #print(dateTime.toString('MM dddd HH mm'))
        #print(dateTime.toString(Qt.DefaultLocaleLongDate))
        #dateName = dateTime.toString(Qt.DefaultLocaleLongDate)
        month = dateTime.toString('MM')
        Day = dateTime.toString('dddd')
        weekday = dayNum[Day]
        hr = dateTime.toString('HH')
        mm = dateTime.toString('mm')
        hour = int(hr)
        min = int(mm)
        minutes = hour*60 + min 
        print(minutes,weekday,month)
        self.predictTraffic(minutes,weekday,month)

    def predictTraffic(self,minutes,weekday,month):
        global TrafficModel
        Indata = np.array([[minutes,weekday,month]])
        Traffic = TrafficModel.predict(Indata)
        self.lcdNumber.display(int(Traffic))
        self.TrafficStatus(Traffic)
        print(Traffic)
		
        return Traffic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.pushButton.clicked.connect(lambda:ui.handlePredictPress())
    ui.TrafficStatus(0)
    Dialog.show()
    dateInput = dateTime.toString(Qt.DefaultLocaleLongDate)
	#weekday = 
    #month = int(dateTime[1])
    sys.exit(app.exec_())
