import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("Hello Qt!")
label.setSizeIncrement(100, 40)     #prompted by Eclipse-PyDev
label.show()

app.exec_()

# sys.exit(app.exec_()) 
