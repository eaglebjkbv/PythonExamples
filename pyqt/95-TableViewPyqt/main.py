from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton
from PyQt5 import QtCore
import sys
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractItemModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(10, 10, 800, 600)
        self.setWindowTitle("TableView Denemesi")
        self.tableViewVeriler = QTableView()
        self.pushButtonKaydet = QPushButton()
        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]
        self.model=TableModel(data)
        self.tableViewVeriler.setModel(self.model)
        self.setCentralWidget(self.tableViewVeriler)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec())
    