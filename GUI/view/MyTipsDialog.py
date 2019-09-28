# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyTipsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TipsDialog(object):
    def setupUi(self, TipsDialog):
        TipsDialog.setObjectName("TipsDialog")
        TipsDialog.resize(470, 370)
        self.verticalLayout = QtWidgets.QVBoxLayout(TipsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(TipsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tips_text_edit = QtWidgets.QTextEdit(TipsDialog)
        self.tips_text_edit.setObjectName("tips_text_edit")
        self.verticalLayout.addWidget(self.tips_text_edit)
        self.widget = QtWidgets.QWidget(TipsDialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(TipsDialog)
        QtCore.QMetaObject.connectSlotsByName(TipsDialog)

    def retranslateUi(self, TipsDialog):
        _translate = QtCore.QCoreApplication.translate
        TipsDialog.setWindowTitle(_translate("TipsDialog", "Tips"))
        self.label.setText(_translate("TipsDialog", "Click on a tip for context:"))
        self.close_button.setText(_translate("TipsDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TipsDialog = QtWidgets.QDialog()
    ui = Ui_TipsDialog()
    ui.setupUi(TipsDialog)
    TipsDialog.show()
    sys.exit(app.exec_())

