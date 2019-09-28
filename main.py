import sys

from PyQt5.QtWidgets import QApplication

from GUI.controller.PyQtApp import PyQtApp

if len(sys.argv) == 1:
    app = QApplication(sys.argv)
    form = PyQtApp()
    form.show()
    app.exec_()
else:
    raise ValueError('wrong number of arguments')
