from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mouse Press Event")
        
    
    def mousePressEvent(self,event):
        print("Tiklandi", event.x(), ",", event.y())
        
    def mouseReleaseEvent(self,event):
        print("Bırakıldı", event.x(), ",", event.y())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())
