# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(907, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list_widget = QtWidgets.QListWidget(self.widget_2)
        self.list_widget.setObjectName("list_widget")
        self.horizontalLayout.addWidget(self.list_widget)
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.categories_analysis_button_widget = QtWidgets.QPushButton(self.frame)
        self.categories_analysis_button_widget.setObjectName("categories_analysis_button_widget")
        self.verticalLayout_3.addWidget(self.categories_analysis_button_widget)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.month_limit_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.month_limit_label.sizePolicy().hasHeightForWidth())
        self.month_limit_label.setSizePolicy(sizePolicy)
        self.month_limit_label.setObjectName("month_limit_label")
        self.verticalLayout_3.addWidget(self.month_limit_label)
        self.widget_5 = QtWidgets.QWidget(self.frame)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.opinion_object_edit_widget = QtWidgets.QLineEdit(self.widget_5)
        self.opinion_object_edit_widget.setObjectName("opinion_object_edit_widget")
        self.horizontalLayout_3.addWidget(self.opinion_object_edit_widget)
        self.custom_word_analysis_button_widget = QtWidgets.QPushButton(self.widget_5)
        self.custom_word_analysis_button_widget.setObjectName("custom_word_analysis_button_widget")
        self.horizontalLayout_3.addWidget(self.custom_word_analysis_button_widget)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButtonMonthLimit = QtWidgets.QCheckBox(self.widget_3)
        self.radioButtonMonthLimit.setObjectName("radioButtonMonthLimit")
        self.horizontalLayout_4.addWidget(self.radioButtonMonthLimit)
        self.date_limit = QtWidgets.QDateEdit(self.widget_3)
        self.date_limit.setDateTime(QtCore.QDateTime(QtCore.QDate(2004, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_limit.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.date_limit.setObjectName("date_limit")
        self.horizontalLayout_4.addWidget(self.date_limit)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.all_reviews_rb = QtWidgets.QRadioButton(self.widget_4)
        self.all_reviews_rb.setChecked(True)
        self.all_reviews_rb.setObjectName("all_reviews_rb")
        self.horizontalLayout_2.addWidget(self.all_reviews_rb)
        self.useful_only_rb = QtWidgets.QRadioButton(self.widget_4)
        self.useful_only_rb.setObjectName("useful_only_rb")
        self.horizontalLayout_2.addWidget(self.useful_only_rb)
        self.weighted_mean_rb = QtWidgets.QRadioButton(self.widget_4)
        self.weighted_mean_rb.setObjectName("weighted_mean_rb")
        self.horizontalLayout_2.addWidget(self.weighted_mean_rb)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.nonzero_sentiment_radio_button = QtWidgets.QCheckBox(self.frame)
        self.nonzero_sentiment_radio_button.setObjectName("nonzero_sentiment_radio_button")
        self.verticalLayout_3.addWidget(self.nonzero_sentiment_radio_button)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.widget_6)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_label = QtWidgets.QLabel(self.frame_2)
        self.result_label.setObjectName("result_label")
        self.verticalLayout.addWidget(self.result_label)
        self.result_widget = QtWidgets.QTextEdit(self.frame_2)
        self.result_widget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result_widget.setObjectName("result_widget")
        self.verticalLayout.addWidget(self.result_widget)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.adjective_details_frame = QtWidgets.QFrame(self.widget_6)
        self.adjective_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adjective_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adjective_details_frame.setObjectName("adjective_details_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.adjective_details_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.adjective_details_label = QtWidgets.QLabel(self.adjective_details_frame)
        self.adjective_details_label.setObjectName("adjective_details_label")
        self.verticalLayout_4.addWidget(self.adjective_details_label)
        self.adjective_details_textedit = QtWidgets.QTextEdit(self.adjective_details_frame)
        self.adjective_details_textedit.setStyleSheet("font: 9pt \"Sans Serif\";")
        self.adjective_details_textedit.setObjectName("adjective_details_textedit")
        self.verticalLayout_4.addWidget(self.adjective_details_textedit)
        self.dismiss_button = QtWidgets.QPushButton(self.adjective_details_frame)
        self.dismiss_button.setObjectName("dismiss_button")
        self.verticalLayout_4.addWidget(self.dismiss_button)
        self.horizontalLayout_5.addWidget(self.adjective_details_frame)
        self.sentiment_value_widget = QtWidgets.QWidget(self.widget_6)
        self.sentiment_value_widget.setObjectName("sentiment_value_widget")
        self.sentiment_value_layout = QtWidgets.QVBoxLayout(self.sentiment_value_widget)
        self.sentiment_value_layout.setObjectName("sentiment_value_layout")
        self.horizontalLayout_5.addWidget(self.sentiment_value_widget)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.tips_button = QtWidgets.QPushButton(self.centralwidget)
        self.tips_button.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tips_button.setFont(font)
        self.tips_button.setObjectName("tips_button")
        self.verticalLayout_2.addWidget(self.tips_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 907, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Review Analyzer"))
        self.label.setText(_translate("MainWindow", "Analyze opinions about food, price, decor, staff:"))
        self.categories_analysis_button_widget.setText(_translate("MainWindow", "Analyze"))
        self.month_limit_label.setText(_translate("MainWindow", "Analyze opinions about a thing of your choice:"))
        self.custom_word_analysis_button_widget.setText(_translate("MainWindow", "Analyze"))
        self.radioButtonMonthLimit.setText(_translate("MainWindow", "Skip reviews older than:"))
        self.label_2.setText(_translate("MainWindow", "Treating of useful reviews (by other users\' feedback)"))
        self.all_reviews_rb.setText(_translate("MainWindow", "All reviews"))
        self.useful_only_rb.setText(_translate("MainWindow", "Useful only"))
        self.weighted_mean_rb.setText(_translate("MainWindow", "Useful with greater weight"))
        self.nonzero_sentiment_radio_button.setText(_translate("MainWindow", "Count only adjectives with non-zero sentiment value"))
        self.result_label.setText(_translate("MainWindow", "Click on an adjective to see the context:"))
        self.result_widget.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Choose a place and click the &quot;Analyze&quot; button to see the analysis of the reviews</span></p></body></html>"))
        self.adjective_details_label.setText(_translate("MainWindow", "Click on a sentence to see the full review:"))
        self.dismiss_button.setText(_translate("MainWindow", "Dismiss"))
        self.tips_button.setText(_translate("MainWindow", "See tips"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

