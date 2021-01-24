from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import QTimer
import sys
from PyQt5.QtGui import QColor, QPainter, QPixmap


class MyLabel(QLabel):
    def __init__(self, parent, text):
        QLabel.__init__(self, text, parent)
        self.refresh = True
        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshLabel)
        self.timer.start(10000)

    def refreshLabel(self):
        self.refresh = True

    def paintEvent(self, event):
        if(self.refresh == True):
            print("Refreshed")
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(0, 0, 200))
            qp.setBrush(QColor(200, 0, 0))
            for i in range(1, 500000):
                qp.drawRect(0, 0, 10, 10)
            self.refresh = False
            qp.end()


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def pushButtonSelamla_Clicked(self, mesaj):
        print(mesaj)

    def initUI(self):
        self.setGeometry(10, 10, 600, 400)
        self.setWindowTitle("Merhaba My Label")
        self.myLabel = MyLabel(self, "Merhaba")
        self.myLabel.setStyleSheet("background-color: black")
        self.myLabel.setGeometry(50, 10, 500, 400)
        self.pushButtonSelamla = QPushButton("Tıkla", self)
        self.pushButtonSelamla.setGeometry(1, 1, 50, 30)
        self.pushButtonSelamla.clicked.connect(
            lambda: self.pushButtonSelamla_Clicked("Naber .."))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec())
