import sys
from PyQt5 import QtWidgets, QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    l1 = QtWidgets.QLabel(w)
    l1.setText('Hello Guys')

    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap('phone-outline.png'))

    w.setWindowTitle('PyQt5 Learn 1')

    # geometry (x, y, width, height)
    w. setGeometry(100, 100, 300, 200)
    l1.move(w.width()/2, w.height()/2)
    l2.move(w.width()/2, w.height()/2 + 20)

    w.show()
    sys.exit(app.exec_())

Window()


