from PyQt5.QtWidgets import QApplication, QComboBox, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.seriPortListele()

    def seriPortListele(self):
        seriPortBilgi = QSerialPortInfo()
        for seriPort in seriPortBilgi.availablePorts():
            print(seriPort.portName())
            self.comboBoxSeriPortlar.addItem(seriPort.portName())
            

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        VBoxAna = QVBoxLayout()
        HBox1 = QHBoxLayout()
        self.comboBoxSeriPortlar = QComboBox()
        HBox1.addWidget(self.comboBoxSeriPortlar)
        HBox1.addStretch()
        VBoxAna.addLayout(HBox1)
        VBoxAna.addStretch()

        centralWidget = QWidget()
        centralWidget.setLayout(VBoxAna)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())