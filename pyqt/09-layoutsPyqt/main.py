from PyQt5.QtWidgets import QApplication, QComboBox, QHBoxLayout, QMainWindow, QPushButton, QWidget
import sys
from PyQt5.QtCore import Qt

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        comboBoxDeneme = QComboBox()
        comboBoxDeneme.addItems(["item 1", "item2", "item3"])
        pushButtonClikMe = QPushButton("Click Me")
        pushButtonClikMe.setFixedWidth(100)
        
        
        
        
        #hbox.addWidget(comboBoxDeneme,1)
        hbox.addStretch()
        hbox.addWidget(pushButtonClikMe)
        widget=QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()

    sys.exit(app.exec())