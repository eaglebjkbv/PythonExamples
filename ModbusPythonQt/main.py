from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QComboBox, \
    QPushButton, QLineEdit, QListWidget

from PyQt5.QtCore import Qt,QTimer

import sys
import serial
import serial.tools.list_ports as listport

port=serial.Serial()


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.arayuz()
        self.show()


    def arayuz(self): # UI design
        self.setWindowTitle("Modbus RTU by Python")
        vboxAna=QVBoxLayout()
        hbox1=QHBoxLayout()
        grid1=QGridLayout()
        labelComport=QLabel("COM Port")
        grid1.addWidget(labelComport,1,1,Qt.AlignLeft)
        self.comboboxComPort = QComboBox()
        grid1.addWidget(self.comboboxComPort,2,1,Qt.AlignLeft)
        labelBaudrate=QLabel("Baudrate")
        grid1.addWidget(labelBaudrate, 1, 2, Qt.AlignLeft)
        self.comboboxBaudrate = QComboBox()
        grid1.addWidget(self.comboboxBaudrate, 2, 2, Qt.AlignLeft)
        labelAyarlar = QLabel("Ayarlar")
        grid1.addWidget(labelAyarlar, 1, 3, Qt.AlignLeft)
        self.comboboxAyarlar = QComboBox()
        grid1.addWidget(self.comboboxAyarlar, 2, 3, Qt.AlignLeft)
        self.pushbuttonBaglan = QPushButton("Bağlan")
        grid1.addWidget(self.pushbuttonBaglan, 1, 4, Qt.AlignLeft)
        self.pushbuttonBaglantiKes = QPushButton("Bağlantı Kes") # Close Connection Button
        grid1.addWidget(self.pushbuttonBaglantiKes, 2, 4, Qt.AlignLeft)

        hbox1.addLayout(grid1)

        vboxAna.addLayout(hbox1)
        vboxAna.addSpacing(40)
        hbox2=QHBoxLayout()
        grid2= QGridLayout()

        labelAdres = QLabel("Adres")
        grid2.addWidget(labelAdres, 1, 1, Qt.AlignLeft)
        self.lineeditAdres = QLineEdit()
        self.lineeditAdres.setText("01")
        self.lineeditAdres.setFixedWidth(40)
        grid2.addWidget(self.lineeditAdres, 2, 1, Qt.AlignLeft)

        labelKomut = QLabel("Komut ?")
        labelKomut.setToolTip("01- Tek Bobin Durumu Oku \n" +
                "02- Giriş Durumu Oku\n03- Tutucu Registerleri Oku \n" +
                "04- Giriş Registerleri Oku \n" +
                "05- Sadece Bir bobin durumu değiştir \n" +
                "06- Sadece Bir Register durumunu değiştir \n" +
                "0F- Birden fazla Bobin içeriği değiştir \n" +
                "10- Birden fazla Registere Değer atamak ")
        grid2.addWidget(labelKomut, 1, 2, Qt.AlignLeft)
        self.lineeditKomut = QLineEdit()
        self.lineeditKomut.setText("06")
        self.lineeditKomut.setFixedWidth(40)
        grid2.addWidget(self.lineeditKomut, 2, 2, Qt.AlignLeft)
        labelParametre = QLabel("Parametre")
        grid2.addWidget(labelParametre, 1, 3, Qt.AlignLeft)
        self.lineeditParametre = QLineEdit()
        self.lineeditParametre.setText("20010DAC")
        self.lineeditParametre.setFixedWidth(160)
        grid2.addWidget(self.lineeditParametre, 2, 3, Qt.AlignLeft)
        labelCrc = QLabel("CRC")
        grid2.addWidget(labelCrc, 1, 4, Qt.AlignLeft)
        self.lineeditCrc = QLineEdit()
        self.lineeditCrc.setFixedWidth(40)
        grid2.addWidget(self.lineeditCrc, 2, 4, Qt.AlignLeft)
        hbox2.addLayout(grid2)

        vboxAna.addLayout(hbox2)
        vbox1 = QVBoxLayout()
        self.pushbuttonGonder = QPushButton("Gönder")
        self.listCevap = QListWidget()
        labelCevap=QLabel("Gelen Cevap")
        vbox1.addWidget(self.pushbuttonGonder) # Send Data
        vbox1.addWidget(labelCevap)
        vbox1.addWidget(self.listCevap)
        vboxAna.addLayout(vbox1)

        self.setLayout(vboxAna)
        self.ilkdurum()
        self.olaylar()

    def ilkdurum(self): #initialize
        portlar=listport.comports()
        # Put all serial interfaces in combobox
        for cp in portlar:
            self.comboboxComPort.addItem(str(cp.device))
        ayarliste= ["8,O,1","8,E,1","8,N,2"]
        liste=["9600","14400", "19200", "38400", "57600", "115200"]
        self.comboboxBaudrate.addItems(liste)
        self.comboboxAyarlar.addItems(ayarliste)
        self.pushbuttonBaglantiKes.setEnabled(False)
        self.pushbuttonGonder.setEnabled(False)

    def olaylar(self): #Events
        self.pushbuttonBaglan.clicked.connect(self.baglan) #open serialport
        self.pushbuttonBaglantiKes.clicked.connect(self.baglantikes) #close serialport
        self.pushbuttonGonder.clicked.connect(self.gonder) # send data
        

    def baglan(self):

        port.baudrate = int(self.comboboxBaudrate.currentText())
        ayar=self.comboboxAyarlar.currentText() # take settings from setting combobox

        port.bytesize = serial.EIGHTBITS

        if ayar[2] == "E":
            port.parity = serial.PARITY_EVEN
        if ayar[2] == "O":
            port.parity = serial.PARITY_ODD
        if ayar[2] == "N":
            port.parity = serial.PARITY_NONE
        if ayar[4] == "1":
            port.stopbits = serial.STOPBITS_ONE
        if ayar[4] == "2":
            port.stopbits = serial.STOPBITS_TWO
        port.port = self.comboboxComPort.currentText()
        if not port.is_open:
            port.open()
            if port.is_open:
                self.pushbuttonBaglan.setEnabled(False)
                self.pushbuttonGonder.setEnabled(True)
                self.pushbuttonBaglantiKes.setEnabled(True)
                self.timer=QTimer()
                self.timer.timeout.connect(self.verial)
                self.timer.start(100)




    def baglantikes(self): #close connection

        if port.is_open:
            port.close()
            if not port.is_open:
                self.pushbuttonBaglan.setEnabled(True)
                self.pushbuttonGonder.setEnabled(False)
                self.pushbuttonBaglantiKes.setEnabled(False)
                self.timer.stop()

    def verial(self): #read data from serialport
        veri=""
        if port.is_open:
            gelenVeri = port.read(port.in_waiting)

            if not gelenVeri==b'':
                for a in gelenVeri:
                    if len(str(hex(a))[2:4].upper())==1:
                        veri+="0"+str(hex(a))[2:4].upper()+"-"

                    else:
                        veri+= str(hex(a))[2:4].upper()+"-"

                self.listCevap.insertItem(0, veri)



    def gonder(self): #send data from serialport
        data=self.lineeditAdres.text()+self.lineeditKomut.text()+self.lineeditParametre.text()

        data1=[]

        for a in range(0,len(data), 2):
            data1.append(int(data[a:a+2],16))
        msbyte, lsbyte =self.crc16(data1)
        self.lineeditCrc.setText(str(hex(msbyte))[2:4].upper()+str(hex(lsbyte))[2:4].upper())

        data1.append(msbyte)
        data1.append(lsbyte)


        port.write(data1)

    #calculation of crc16
    def crc16(self,data: bytes, poly=0xA001):

        crc = 0xFFFF
        for b in data:

            cur_byte = 0xFF & b

            for _ in range(0, 8):
                if (crc & 0x0001) ^ (cur_byte & 0x0001):
                    crc = (crc >> 1) ^ poly
                else:
                    crc >>= 1
                cur_byte >>= 1

        crc = (crc << 8) | ((crc >> 8) & 0xFF)
        msbyte = crc >> 8
        lsbyte = crc & 0x00FF
        #returns tupple
        return msbyte & 0xFF, lsbyte & 0xFF

#main

if __name__=="__main__":
    app=QApplication(sys.argv)
    pen=Pencere()
    sys.exit(app.exec())