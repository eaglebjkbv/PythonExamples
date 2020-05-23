from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = 0
        self.y = 0

    def initUI(self):
        self.setWindowTitle("Mouse Press Event")
        self.setGeometry(100, 100, 600, 400)
        self.setMouseTracking(True)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Left:
            print("Sol Tuş")
        if e.key() == Qt.Key_Right:
            print("Sağ tuş")
        


    def mousePressEvent(self,event):
        print("Tiklandi", event.x(), ",", event.y())
        
    def mouseReleaseEvent(self,event):
        print("Bırakıldı", event.x(), ",", event.y())

    def mouseMoveEvent(self, event):
        
        self.x = event.x()  
        self.y = event.y()
        self.repaint()
    

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawRect(self.x, self.y, 20, 20)
        qp.end()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())
