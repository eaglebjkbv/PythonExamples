from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPushButton
import sys


class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def button1Clicked(self):
        result=QMessageBox.question(self,'Mesaj Kutusu',"Bir Cevap Seç",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if (result == QMessageBox.Yes):
            self.labelMesaj.setText("Yes Seçildi")
        elif (result == QMessageBox.No):
            self.labelMesaj.setText("No Seçildi")
        elif (result == QMessageBox.Cancel):
            self.labelMesaj.setText("Cancel Seçildi")
    
    
    def initUI(self):
        self.setWindowTitle("Message Box Deneme")
        self.button1 = QPushButton("Show Message Box", self)
        self.button1.setGeometry(0, 0, 200, 30)
        self.button1.clicked.connect(self.button1Clicked)
        self.labelMesaj = QLabel("Deneme", self)
        self.labelMesaj.setGeometry(10, 30, 150, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = win()
    sys.exit(app.exec())
