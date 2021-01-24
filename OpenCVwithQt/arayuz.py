# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Deneme(object):
    def setupUi(self, Deneme):
        Deneme.setObjectName("Deneme")
        Deneme.resize(993, 577)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Deneme.sizePolicy().hasHeightForWidth())
        Deneme.setSizePolicy(sizePolicy)
        self.pushButtonVideoBaslat = QtWidgets.QPushButton(Deneme)
        self.pushButtonVideoBaslat.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pushButtonVideoBaslat.setObjectName("pushButtonVideoBaslat")
        self.label = QtWidgets.QLabel(Deneme)
        self.label.setGeometry(QtCore.QRect(30, 60, 941, 481))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")

        self.retranslateUi(Deneme)
        QtCore.QMetaObject.connectSlotsByName(Deneme)

    def retranslateUi(self, Deneme):
        _translate = QtCore.QCoreApplication.translate
        Deneme.setWindowTitle(_translate("Deneme", "Dialog"))
        self.pushButtonVideoBaslat.setText(_translate("Deneme", "Başlat"))
        self.label.setText(_translate("Deneme", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Deneme = QtWidgets.QDialog()
    ui = Ui_Deneme()
    ui.setupUi(Deneme)
    Deneme.show()
    sys.exit(app.exec_())

