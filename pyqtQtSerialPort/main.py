from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QVBoxLayout,QHBoxLayout,QComboBox
from PyQt5.QtSerialPort import QSerialPortInfo
import sys
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.listSerialPorts()

    def listSerialPorts(self):
        serialPortInfo=QSerialPortInfo()
        for serialPort in serialPortInfo.availablePorts():
            self.comboSeriPortList.addItem(serialPort.portName())

    def initUI(self):
        self.setGeometry(20,50,800,600)
        self.setWindowTitle("SeriPort Çalışması")
        vboxana=QVBox"Layout()
        hbox1=QHBoxLayout()
        self.comboSeriPortList=QComboBox()
        hbox1.addWidget(self.comboSeriPortList)
        hbox1.addStretch()
        vboxana.addLayout(hbox1)
        vboxana.addStretch()
        centralWidget=QWidget()
        centralWidget.setLayout(vboxana)
        self.setCentralWidget(centralWidget)


        
        



if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())