
import sys
from PySide2.QtWidgets import QApplication, QLabel



app = QApplication(sys.argv)
label = QLabel("Merhaba")
label.show()
sys.exit(app.exec_())


