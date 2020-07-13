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
        self.textEditGelenData.append(self.serialPort.readAll().data().decode())
        
    def portSendData(self):
        self.serialPort.write(self.lineEditGidenData.text().encode())

    def portDisconnect(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.pushButtonBaglan.setEnabled(True)
            self.pushButtonBaglantiKes.setEnabled(False)
            self.pushButtonGonder.setEnabled(False)
        
    def portConnect(self):
        
        self.serialPort.setPortName(self.comboSeriPortList.currentText())
        self.serialPort.setBaudRate(QSerialPort.Baud9600)
        self.serialPort.setDataBits(QSerialPort.Data8)
        self.serialPort.setParity(QSerialPort.EvenParity)
        self.serialPort.setStopBits(QSerialPort.OneStop)
        if not self.serialPort.isOpen():
            
            self.serialPort.open(QIODevice.ReadWrite)
            self.pushButtonBaglan.setEnabled(False)
            self.pushButtonBaglantiKes.setEnabled(True)
            self.pushButtonGonder.setEnabled(True)



    def initUI(self):
        self.serialPort=QSerialPort()
        self.setGeometry(20,50,320,200)
        self.setWindowTitle("SeriPort Çalışması")
        vboxana=QVBoxLayout()
        hbox1=QHBoxLayout()
        self.comboSeriPortList=QComboBox()
        hbox1.addWidget(self.comboSeriPortList)
        self.pushButtonBaglan=QPushButton("Bağlan")
        self.pushButtonBaglan.setEnabled(True)
        self.pushButtonBaglantiKes=QPushButton("Bağlantı Kes")
        self.pushButtonBaglantiKes.setEnabled(False)
        hbox1.addWidget(self.pushButtonBaglan)
        hbox1.addWidget(self.pushButtonBaglantiKes)
        hbox1.addStretch()
        hbox2=QHBoxLayout()
        self.textEditGelenData=QTextEdit()
        self.textEditGelenData.setFixedSize(300,100)
        hbox2.addWidget(self.textEditGelenData)
        hbox2.addStretch()
        hbox3=QHBoxLayout()
        self.lineEditGidenData=QLineEdit()
        self.lineEditGidenData.setFixedWidth(200)
        self.pushButtonGonder=QPushButton("Gönder")
        self.pushButtonGonder.setEnabled(False)
        self.pushButtonGonder.setFixedWidth(95)

        hbox3.addWidget(self.lineEditGidenData)
        hbox3.addWidget(self.pushButtonGonder)

        hbox3.addStretch()
        

        vboxana.addLayout(hbox1)
        vboxana.addLayout(hbox2)
        vboxana.addLayout(hbox3)
        vboxana.addStretch()
        centralWidget=QWidget()
        centralWidget.setLayout(vboxana)
        self.setCentralWidget(centralWidget)

        self.pushButtonBaglan.clicked.connect(self.portConnect)
        self.pushButtonBaglantiKes.clicked.connect(self.portDisconnect)
        self.pushButtonGonder.clicked.connect(self.portSendData)
        self.serialPort.readyRead.connect(self.dataReceived)


        
        



if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())