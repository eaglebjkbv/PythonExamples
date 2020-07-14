from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLineEdit,QVBoxLayout,QHBoxLayout,QComboBox, QPushButton,QTextEdit
from PyQt5.QtSerialPort import QSerialPortInfo,QSerialPort
from PyQt5.QtCore import QIODevice
import sys
import array
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.listSerialPorts()

    def listSerialPorts(self):
        serialPortInfo=QSerialPortInfo()
        for serialPort in serialPortInfo.availablePorts():
            self.comboSeriPortList.addItem(serialPort.portName())

    def dataReceived(self):
        self.textEditReceiveData.append(self.serialPort.readAll().data().decode())
        
    def portSendData(self):
        self.serialPort.write(self.LineEditSendData.text().encode())

    def portDisconnect(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.pushButtonConnect.setEnabled(True)
            self.pushButtonDisconnect.setEnabled(False)
            self.pushButtonSend.setEnabled(False)
        
    def portConnect(self):
        
        self.serialPort.setPortName(self.comboSeriPortList.currentText())
        self.serialPort.setBaudRate(QSerialPort.Baud9600)
        self.serialPort.setDataBits(QSerialPort.Data8)
        self.serialPort.setParity(QSerialPort.EvenParity)
        self.serialPort.setStopBits(QSerialPort.OneStop)
        if not self.serialPort.isOpen():
            
            self.serialPort.open(QIODevice.ReadWrite)
            self.pushButtonConnect.setEnabled(False)
            self.pushButtonDisconnect.setEnabled(True)
            self.pushButtonSend.setEnabled(True)



    def initUI(self):
        self.serialPort=QSerialPort()
        self.setGeometry(20,50,320,200)
        self.setWindowTitle("SeriPort Çalışması")
        vboxana=QVBoxLayout()
        hbox1=QHBoxLayout()
        self.comboSeriPortList=QComboBox()
        hbox1.addWidget(self.comboSeriPortList)
        self.pushButtonConnect=QPushButton("Bağlan")
        self.pushButtonConnect.setEnabled(True)
        self.pushButtonDisconnect=QPushButton("Bağlantı Kes")
        self.pushButtonDisconnect.setEnabled(False)
        hbox1.addWidget(self.pushButtonConnect)
        hbox1.addWidget(self.pushButtonDisconnect)
        hbox1.addStretch()
        hbox2=QHBoxLayout()
        self.textEditReceiveData=QTextEdit()
        self.textEditReceiveData.setFixedSize(300,100)
        hbox2.addWidget(self.textEditReceiveData)
        hbox2.addStretch()
        hbox3=QHBoxLayout()
        self.LineEditSendData=QLineEdit()
        self.LineEditSendData.setFixedWidth(200)
        self.pushButtonSend=QPushButton("Gönder")
        self.pushButtonSend.setEnabled(False)
        self.pushButtonSend.setFixedWidth(95)

        hbox3.addWidget(self.LineEditSendData)
        hbox3.addWidget(self.pushButtonSend)

        hbox3.addStretch()
        

        vboxana.addLayout(hbox1)
        vboxana.addLayout(hbox2)
        vboxana.addLayout(hbox3)
        vboxana.addStretch()
        centralWidget=QWidget()
        centralWidget.setLayout(vboxana)
        self.setCentralWidget(centralWidget)

        self.pushButtonConnect.clicked.connect(self.portConnect)
        self.pushButtonDisconnect.clicked.connect(self.portDisconnect)
        self.pushButtonSend.clicked.connect(self.portSendData)
        self.serialPort.readyRead.connect(self.dataReceived)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())