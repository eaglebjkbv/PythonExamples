from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QTimer

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.setWindowTitle("Merhaba")
     

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())