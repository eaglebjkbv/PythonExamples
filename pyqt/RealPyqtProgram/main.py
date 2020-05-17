from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import sys

class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(10, 10, 600, 400)          
        self.setWindowTitle("Merhaba Dünya")
        self.label1=QLabel("Selamlar...",self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = win()
    sys.exit(app.exec_())
