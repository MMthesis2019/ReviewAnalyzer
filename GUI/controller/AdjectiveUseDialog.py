from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog

from GUI.view.MyDialog import Ui_Review
from DAO.MysqlReviewDao import MysqlReviewDao


class AdjectiveUseDialog(QDialog, Ui_Review):
    def __init__(self, review_id, dao=None, bold=''):
        super(AdjectiveUseDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.setModal(True)

        if dao is None:
            self.reviewDao = MysqlReviewDao()
        else:
            self.reviewDao = dao
        review = self.reviewDao.get_review_by_id(review_id)
        if review.review_date is None:
            self.date_le.setText('unknown')
        else:
            self.date_le.setText(str(review.review_date))

        index_in_review=review.text.find(bold.strip())
        if index_in_review != -1:
            text_to_insert = review.text[:index_in_review]+'<b>'+\
                            review.text[index_in_review:index_in_review+len(bold)]+'</b>'+\
                            review.text[index_in_review+len(bold):]
            self.full_review.insertHtml(text_to_insert)
        elif review.title in bold or bold in review.title:
            font = QFont()
            font.setBold(True)
            self.title_le.setFont(font)
            self.full_review.insertPlainText(review.text)
        else:
            self.full_review.insertPlainText(review.text)

        self.upvote_le.setText(str(review.helpful))
        self.title_le.setText(str(review.title))
        self.close_button.mouseReleaseEvent=lambda e: self.accept()