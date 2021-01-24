from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget
import sys
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadImage()

    def loadImage(self):
        img=cv2.imread("sushi.JPG")
        cv2.cvtColor(img,cv2.COLOR_BGR2RGB,img)
        height,width,channel=img.shape
        image=QImage(img.data,width,height,width*3,QImage.Format_RGB888)
        image=QPixmap.fromImage(image)
        image=image.scaled(self.labelImage.width(),self.labelImage.height(),Qt.KeepAspectRatio)
        self.labelImage.setPixmap(image)
        self.labelImage.setAlignment(Qt.AlignCenter)

    def initUI(self):
        self.setGeometry(10,50,800,600)
        self.setWindowTitle("PyQt ile OpenCV çalışaması")
        vBoxAna=QVBoxLayout()
        hBox1=QHBoxLayout()
        self.labelImage=QLabel()
        self.labelImage.setText("Resim Bekleniyor...")
        self.labelImage.setFixedSize(780,580)
        hBox1.addWidget(self.labelImage)
        vBoxAna.addLayout(hBox1)
        centralWidget=QWidget()
        centralWidget.setLayout(vBoxAna)
        self.setCentralWidget(centralWidget)



if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainWindow=MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())