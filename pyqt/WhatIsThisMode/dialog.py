from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QMessageBox
from PyQt5.QtCore import QEvent
import sys

class win(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(10, 10, 600, 400)          
        self.setWindowTitle("Merhaba Dünya")
        self.label1=QLabel("Selamlar...",self)
        self.installEventFilter(self)
        
        
        self.show()
    def eventFilter(self, a0, a1):
        if (a1.type()==QEvent.EnterWhatsThisMode):
            result=QMessageBox.question(self,'Mesaj Kutusu',"What is This Moduna Geçildi",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        return super().eventFilter(a0, a1)
   
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = win()
    sys.exit(app.exec_())