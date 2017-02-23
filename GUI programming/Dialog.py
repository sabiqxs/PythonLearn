import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot



class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 example Dialog'
        self.left = 20
        self.top = 30
        self.width = 640
        self.height = 400

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # age = self.getAge()
        # print(age)
        self.show()
        self.getChoice()
    # def getAge(self):
    #     # dengan format QInputDialog.getInt(self, 'window title', 'label', default, min, max, increment)
    #     age, okPressed = QInputDialog.getInt(self, 'get Integer', 'age:', 18, 16, 130, 1)
    #     if okPressed:
    #         return age

    def getChoice(self):
        items = ('Red', 'Blue', 'Green')
        # dengan format QInputDialog.getItem(self, 'window title', 'label', list, ,editable)
        item, okPress = QInputDialog.getItem(self, 'get Item', 'Color:', items, 0, False)
        if okPress and item:
            print(item)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())