import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Bar Denemesi")
        menubar = self.menuBar()
        menu = QMenu('Dosya', self)
        menuDosyaGonder = QMenu('Gönder', self)
        actionGonderMail = QAction("Mail", self)
        actionGonderMessage = QAction("Mesaj", self)

        menuDosyaGonder.addAction(actionGonderMail)
        menuDosyaGonder.addAction(actionGonderMessage)
        menu.addMenu(menuDosyaGonder)

        actionDosyaCikis = QAction("Çıkış", self)
        actionDosyaCikis.setStatusTip("Programdan Çıkış")
        actionDosyaCikis.triggered.connect(self.cikis)
        menu.addSeparator()
        menu.addAction(actionDosyaCikis)
        menubar.addMenu(menu)
        self.statusBar().showMessage("Hazır")

    def cikis(self):
        print("Cikis")
        result = QMessageBox.question(self, "Çıkış",
                                      "Çıkılsın mı ?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()

    sys.exit(app.exec())
