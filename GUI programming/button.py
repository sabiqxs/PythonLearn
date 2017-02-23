import sys
from PyQt5 import QtWidgets, QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)

    b.setText('Push Me')
    l.setText('Look at me')
    w.setWindowTitle('PyQt5 Learn Button')

    b.move(100, 50)
    l.move(110, 100)

    # geometry (x, y, width, height)
    w. setGeometry(100, 100, 300, 200)
    w.show()
    sys.exit(app.exec_())

Window()


