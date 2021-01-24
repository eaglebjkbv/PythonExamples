from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import arayuz
import cv2 as cv
import numpy as np

class Pencere(QWidget,arayuz.Ui_Deneme):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.pushButtonVideoBaslat.clicked.connect(self.videoBaslat)

        self.show()

    def tick(self):

        read, img = self.video.read()
        if read:
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            yuzler = self.yuz_cascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in yuzler:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                print("deneme")

            cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
            res = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
            resim = QPixmap.fromImage(res)
            resim = resim.scaled(self.label.width(), self.height(), Qt.KeepAspectRatio)
            self.label.setPixmap(resim)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.repaint()

    def videoBaslat(self):


        self.video = cv.VideoCapture(0)
        self.yuz_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

        self.timer = QTimer()
        self.timer.start(20)
        self.timer.timeout.connect(self.tick)






def window():
    app = QApplication(sys.argv)
    pen = Pencere()
    sys.exit(app.exec_())



if __name__=="__main__":
    window()
