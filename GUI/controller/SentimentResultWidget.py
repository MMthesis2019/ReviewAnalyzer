from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget

from GUI.view.MyWidget import Ui_Form

class SentimentResultWidget(QWidget, Ui_Form):
    def __init__(self, label, value):
        super(SentimentResultWidget, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.progressBar.setProperty("value", abs(int(value)))
        self.label.setText(label)
        palette = QPalette(self.palette())
        if value>0:
            palette.setColor(QPalette.Highlight, QColor(0, 255, 0))
        elif value<0:
            palette.setColor(QPalette.Highlight,QColor(255,0,0))
        self.progressBar.setPalette(palette)
