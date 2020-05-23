from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtCore import QRect, QTimer


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.y=0
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerTick)
        self.timer.start(17)
    
    def timerTick(self):
        self.y = self.y + 1
        self.repaint()

    
    def initUI(self):
        self.setWindowTitle("Merhaba")
        self.setGeometry(100,100,600,400)
     

    def paintEvent(self, e):
        qp = QPainter()
        image = QPixmap("./ball.png",)
        qp.begin(self)
        qp.drawPixmap(10,self.y,image.width(),image.height(),image)
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())