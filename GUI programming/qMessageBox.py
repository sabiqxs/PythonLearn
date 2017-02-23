import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from builtins import print


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.initUI()

    def initUI(self):

        answer = QMessageBox.question(self, 'Beverage', 'Do you like Coffee?', QMessageBox.Yes | QMessageBox.No)
        if answer == QMessageBox.Yes:
            print('yes')
        if answer == QMessageBox.No:
            print('no')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

