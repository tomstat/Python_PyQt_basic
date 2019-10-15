#!/usr/bin/env python
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("<h2><i>Hello</i> " "<font color=red>Qt!</font></h2>")
label.setSizeIncrement(100, 40) 
label.show()

app.exec_()
