from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QWidget, QTableWidgetItem
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(10, 10, 800, 600)
        self.setWindowTitle("TableWidget Deneme")
        vbox = QVBoxLayout()
        tableWidgetPersons = QTableWidget()
        tableWidgetPersons.setRowCount(5)
        tableWidgetPersons.setColumnCount(3)

        tableWidgetPersons.setColumnWidth(1, 500)

        tableWidgetPersons.setHorizontalHeaderItem(0, QTableWidgetItem("Ad"))
        tableWidgetPersons.setHorizontalHeaderItem(
            1, QTableWidgetItem("Soyad"))
        tableWidgetPersons.setHorizontalHeaderItem(2, QTableWidgetItem("Yaş"))

        tableWidgetPersons.setItem(0, 0, QTableWidgetItem("Suzuki"))
        tableWidgetPersons.setItem(0, 1, QTableWidgetItem("Yamashita"))
        tableWidgetPersons.setItem(0, 2, QTableWidgetItem("58"))

        vbox.addWidget(tableWidgetPersons)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
