from PyQt5.QtWidgets import QDialog

from GUI.controller.AdjectiveUseDialog import AdjectiveUseDialog
from GUI.view.MyTipsDialog import Ui_TipsDialog
from DAO.MysqlReviewDao import MysqlReviewDao


class TipsDialog(QDialog, Ui_TipsDialog):
    def __init__(self, tip_list):
        super(TipsDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.tip_list = tip_list
        self.dialog = None
        self.setModal(True)

        self.close_button.mouseReleaseEvent = lambda e: self.accept()

        if len(tip_list)==0:
            self.tips_text_edit.setText('no tips found')
        else:
            html_to_insert = '<ul>\n'
            for tip in self.tip_list:
                html_to_insert += "<li>" + tip.sent.text + "</li>\n"
            html_to_insert += '</ul>\n'
            self.tips_text_edit.setHtml(html_to_insert)
        self.tips_text_edit.mouseReleaseEvent = lambda e: self.on_click_tips_textedit(e)

    def on_click_tips_textedit(self, e):
        cursor = self.tips_text_edit.cursorForPosition(e.pos())
        if cursor.blockNumber() < len(self.tip_list):
            review_id = self.tip_list[cursor.blockNumber()].review_id
            self.dialog = AdjectiveUseDialog(review_id, bold=cursor.block().text())
            self.dialog.show()
        else:
            return
