from PyQt5.QtWidgets import QApplication, QComboBox, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget
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
        pushButtonClikMe.setFixedSize(100, 100)
        
        comboBoxDeneme.setFixedWidth(100)
        
        hbox.addWidget(comboBoxDeneme,1)
        hbox.addStretch()
        hbox.addWidget(pushButtonClikMe, 1)
        self.statusBar().addWidget(comboBoxDeneme)
        widget=QWidget()
        self.setCentralWidget(pushButtonClikMe)
        #widget.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()

    sys.exit(app.exec())