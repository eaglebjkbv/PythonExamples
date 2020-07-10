from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QMessageBox, QPushButton, QTableView, QTextEdit, QVBoxLayout, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtSql

class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        
        if self.CreateDb():
            query = QtSql.QSqlQuery()
            query.exec_("create table todo(id INTEGER PRIMARY KEY AUTOINCREMENT, todo varchar(20), description varchar(50))")
        else:
            print("Veritabanı Problemi")

        self.initUI()
    
    def initModel(self):
        self.model.setTable('todo')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Todo")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Description")


    def initUI(self):
        self.setWindowTitle("Merhaba")
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        labelTodo = QLabel("Todo : ")
        self.textTodo = QTextEdit()
        self.textTodo.setFixedHeight(30)
        labelDesc = QLabel("Description : ")
        self.textDesc = QTextEdit()
        self.textDesc.setFixedHeight(30)

        hbox.addWidget(labelTodo)
        hbox.addWidget(self.textTodo)
        hbox.addWidget(labelDesc)
        hbox.addWidget(self.textDesc)
        hbox.addStretch()
        vbox.addLayout(hbox)
        pushSave = QPushButton("Kaydet")
        pushSave.setFixedHeight(40)
        vbox.addWidget(pushSave)
        
        self.tableData = QTableView()
        self.tableData.setModel(self.model)
        vbox.addWidget(self.tableData)
        vbox.addStretch()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbox)

        pushSave.clicked.connect(self.saveData)

    def saveData(self):
        query = QtSql.QSqlQuery(self.db)
        todo = self.textTodo.toPlainText()
        todoDesc=self.textDesc.toPlainText()
        query.exec_("insert into todo values (NULL,'"+todo+"','"+todoDesc+"')")
        self.model.select()

    def CreateDb(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("todos.db")
        self.model = QtSql.QSqlTableModel()
        self.initModel()
        if not self.db.open():
            QMessageBox.critical(self,QtGui.qApptr("Uyarı"),"Veri Tabanı Dosyası Açılamadı/Oluşturulamadı !",QMessageBox.Cancel)
            return False
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())