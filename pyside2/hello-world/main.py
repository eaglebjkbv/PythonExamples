import sys
from PySide2.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)
#app.setStyle("fusion")
#label = QLabel("Hello World!")
#label = QLabel("<font color=red size=40>Hello World!</font>")
button = QPushButton("Merhaba")

button.show()
app.exec_()
