from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Merhaba PYQT")
    win.setGeometry(100, 100, 600, 400)
    labelMerhaba = QLabel(win)
    labelMerhaba.setGeometry(50, 50, 200, 200)
    
    buttonDeneme = QPushButton("Click Me",win)
    buttonDeneme.setGeometry(10,30,200,100)
    
    labelMerhaba.setText("Merhaba Bu ilk Label")
    win.show()
    sys.exit(app.exec())

window()




