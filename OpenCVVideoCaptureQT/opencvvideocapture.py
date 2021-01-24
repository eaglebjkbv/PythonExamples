from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import cv2 as cv



class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.anaEkran()
        self.show()

    def anaEkran(self):

        self.setWindowTitle("Open CV Denemesi")
        self.VBoxAna=QVBoxLayout()
        self.Hbox1=QHBoxLayout()
        self.buttonGoster=QPushButton("Vi&deo Başlat")
        pixmap2=QPixmap("kamera.PNG")
        ButtonIcon=QIcon(pixmap2)
        self.buttonGoster.setIcon(ButtonIcon)
        self.buttonGoster.setIconSize(pixmap2.rect().size())
        self.Hbox1.addWidget(self.buttonGoster)
        self.Hbox1.addStretch()

        self.labelVideo=QLabel("Video Bekleniyor...")
        self.labelVideo.setFixedSize(600, 398)
        self.labelVideo.setFrameShape(QFrame.Box)
        self.labelVideo.setAlignment(Qt.AlignCenter)
        self.Hbox2 = QHBoxLayout()
        self.Hbox2.addWidget(self.labelVideo)
        self.Hbox2.addStretch()

        self.checkBoxYuz = QCheckBox("Yüzleri Yakala")
        self.checkBoxGoz = QCheckBox("Gözleri Yakala")
        self.comboYakalama=QComboBox()
        self.comboYakalama.addItem("haarcascade_frontalface_default.xml")
        self.comboYakalama.addItem("lbpcascade_frontalface.xml")
        self.Hbox3=QHBoxLayout()
        self.Hbox3.addWidget(self.checkBoxYuz)
        self.Hbox3.addWidget(self.comboYakalama)
        self.Hbox3.addStretch()

        self.Hbox3.addWidget(self.checkBoxGoz)



        self.VBoxAna.addLayout(self.Hbox1)
        self.VBoxAna.addLayout(self.Hbox2)
        self.VBoxAna.addLayout(self.Hbox3)

        self.setLayout(self.VBoxAna)

        self.buttonGoster.clicked.connect(self.kameraBaslat)
        self.comboYakalama.activated.connect(self.degistir)
    def degistir(self):
        self.yuzCascade = cv.CascadeClassifier(self.comboYakalama.currentText())

    def kameraBaslat(self):
        self.yuzCascade=cv.CascadeClassifier(self.comboYakalama.currentText())
        self.gozCascade=cv.CascadeClassifier("haarcascade_eye.xml")
        self.kamera = cv.VideoCapture(0)
        self.timer=QTimer()
        self.timer.timeout.connect(self.videoYakala)
        self.timer.start(10)

    def videoYakala(self):
        read, img= self.kamera.read()
        if read:
            griTon=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            if self.checkBoxYuz.isChecked():
                yuzler = self.yuzCascade.detectMultiScale(griTon, 1.2, 5)
                for (x, y, w, h) in yuzler:

                    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
            if self.checkBoxGoz.isChecked():
                gozler = self.gozCascade.detectMultiScale(griTon, 1.2, 5)
                for (x, y, w, h) in gozler:
                    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

            cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
            res = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
            resim = QPixmap.fromImage(res)
            resim = resim.scaled(self.labelVideo.width(), self.height(), Qt.KeepAspectRatio)
            self.labelVideo.setPixmap(resim)
            self.labelVideo.setAlignment(Qt.AlignCenter)
            #self.labelVideo.repaint()

def pencere():
    app=QApplication(sys.argv)
    pen=Pencere()
    sys.exit(app.exec())




if __name__ == '__main__':
    pencere()
