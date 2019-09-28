# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Review(object):
    def setupUi(self, Review):
        Review.setObjectName("Review")
        Review.resize(470, 370)
        self.verticalLayout = QtWidgets.QVBoxLayout(Review)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Review)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.date_le = QtWidgets.QLineEdit(self.widget_2)
        self.date_le.setReadOnly(True)
        self.date_le.setObjectName("date_le")
        self.gridLayout.addWidget(self.date_le, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.title_label = QtWidgets.QLabel(self.widget_2)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.upvote_le = QtWidgets.QLineEdit(self.widget_2)
        self.upvote_le.setReadOnly(True)
        self.upvote_le.setObjectName("upvote_le")
        self.gridLayout.addWidget(self.upvote_le, 2, 1, 1, 1)
        self.title_le = QtWidgets.QLineEdit(self.widget_2)
        self.title_le.setReadOnly(True)
        self.title_le.setObjectName("title_le")
        self.gridLayout.addWidget(self.title_le, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.full_review = QtWidgets.QTextEdit(Review)
        self.full_review.setReadOnly(True)
        self.full_review.setObjectName("full_review")
        self.verticalLayout.addWidget(self.full_review)
        self.widget = QtWidgets.QWidget(Review)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_button = QtWidgets.QPushButton(self.widget)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Review)
        QtCore.QMetaObject.connectSlotsByName(Review)

    def retranslateUi(self, Review):
        _translate = QtCore.QCoreApplication.translate
        Review.setWindowTitle(_translate("Review", "Full review"))
        self.label.setText(_translate("Review", "Date:"))
        self.title_label.setText(_translate("Review", "Title:"))
        self.label_2.setText(_translate("Review", "Upvotes:"))
        self.close_button.setText(_translate("Review", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Review = QtWidgets.QDialog()
    ui = Ui_Review()
    ui.setupUi(Review)
    Review.show()
    sys.exit(app.exec_())

