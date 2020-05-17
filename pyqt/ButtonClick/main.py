from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
import sys

class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def buttonClicked(self):
        self.labelMerhaba.setText("Merhaba")

    def initUI(self):
        self.setGeometry(10, 10, 600, 400)
        self.setWindowTitle("Button Click Örneği")
        self.labelMerhaba = QLabel("", self)
        self.pushButtonSelamla = QPushButton("Tıkla", self)
        self.pushButtonSelamla.setGeometry(10, 20, 100, 50)
        self.pushButtonSelamla.clicked.connect(self.buttonClicked) # Tıklandığında çağırılacak Callback methodu belirtir
        self.show()
        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = win()
    sys.exit(app.exec_())




