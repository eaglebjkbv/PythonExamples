import sys
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
from PyQt5.QtCore import Qt

i=0

def initializeModel(model):
    model.setTable('ogrenci')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    # model.setFilter("id<10")
    model.select()

    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "Ad")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Soyad")


def refreshModel(model):
    model.select()

def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    view.horizontalHeader().setSortIndicatorShown(True)
    view.setMinimumSize(400,300)
    return view


def addrow():

    model.rowCount()
    ret = model.insertRows(model.rowCount(), 1)
    if ret:
        print ("Ekeleme Başarılı")



def removerow():
    model.removeRow(view1.currentIndex().row())
    refreshModel(model)

def sirala(i,sira):
    view1.sortByColumn(i,sira)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('deneme.db')
    model = QtSql.QSqlTableModel()

    delrow = -1
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)



    view1.horizontalHeader().sortIndicatorChanged.connect(sirala)


    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    button = QtWidgets.QPushButton("Satır Ekle")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtWidgets.QPushButton("Satır Sil")
    btn1.clicked.connect(removerow)
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Veritabanı Örneği")
    dlg.show()
    sys.exit(app.exec_())