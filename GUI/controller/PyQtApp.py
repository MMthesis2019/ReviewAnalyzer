from PyQt5.QtCore import QThread, pyqtSignal, QDate, QDateTime
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import *

from GUI.controller import AdjectiveUseDialog
from GUI.controller.TipsDialog import TipsDialog
from GUI.view.MyMainWindow import Ui_MainWindow
from DAO.MysqlPlaceDao import MysqlPlaceDao
from DAO.MysqlReviewDao import MysqlReviewDao
from GUI.controller.ReviewFilter import ReviewFilter
from GUI.controller.SentimentResultWidget import SentimentResultWidget
from analyzer.AnalysisResults import WEIGHTED_MEAN, ONLY_USEFUL, ALL
from analyzer.SpaCyReviewAnalyzer import SpaCyReviewAnalyzer


class PyQtApp(QMainWindow, Ui_MainWindow):

    class AnalyzerThread(QThread):
        signal = pyqtSignal(object)
        progressSignal = pyqtSignal(int)

        def __init__(self, *args):
            super().__init__()
            self.args = args

        def __del__(self):
            self.wait()

        def run(self):
            """Creates spacy analyzer, performs analysis, changes results to text representation"""
            self.analyzer = SpaCyReviewAnalyzer(*self.args)
            results = self.analyzer.analyze(progress_signal=self.progressSignal)
            self.signal.emit(results)

    def __init__(self):
        super(PyQtApp, self).__init__()
        self.setWindowTitle("Review analyzer")

        self.results_on_screen = False
        self.analysis_results_dictionary = {}
        self.adjective_details_list =[]

        self.placeDao = MysqlPlaceDao()
        self.reviewDao = MysqlReviewDao()
        self.setupUi(self)
        self.retranslateUi(self)
        self.add_functions_to_gui()
        self.tips=[]

        self.dialog = None

        self.number_reviews_found = 0

    def add_functions_to_gui(self):
        #filling places list
        self.load_places_from_database()

        #adding functions to buttons
        self.categories_analysis_button_widget.mouseReleaseEvent = self.on_click_analyse
        self.custom_word_analysis_button_widget.mouseReleaseEvent = self.on_click_analyse_custom_word
        self.result_widget.mouseReleaseEvent = lambda e: self.on_click_result_widget(e)
        self.adjective_details_textedit.mouseReleaseEvent = lambda e: self.on_click_adjective_details(e)
        self.radioButtonMonthLimit.toggled.connect(lambda: self.on_toggle_radio_button(self.radioButtonMonthLimit))
        self.dismiss_button.mouseReleaseEvent = lambda e: self.adjective_details_frame.setVisible(False)
        self.tips_button.mouseReleaseEvent = lambda e: self.on_click_tips(e)
        self.result_widget.setReadOnly(True)
        self.date_limit.setDisabled(True)

        self.adjective_details_frame.setVisible(False)
        self.result_label.setVisible(False)
        self.progressBar.setVisible(False)
        self.tips_button.setVisible(False)

        self.date_limit.setMaximumDate(QDate.currentDate())
        self.date_limit.setDateTime(QDateTime.currentDateTime())
        self.progressBar.setProperty("value", 0)

        with open("GUI/results.css") as stylesheet:
            css = stylesheet.read()
            self.adjective_details_textedit.document().setDefaultStyleSheet(css)
            self.result_widget.document().setDefaultStyleSheet(css)

        self.sentiment_result_widgets=[]

    def load_places_from_database(self):
        self.places_list = self.placeDao.list_places()
        self.list_widget.clear()
        self.places_list.sort(key=lambda p: p.name)
        items = [f"{place.category[0].upper() if place.category else 'N'} {place.name.replace('_', ' ')}, " \
                     f"{place.location if place.location else 'N'}" for place in self.places_list]
        self.list_widget.addItems(items)

    def on_toggle_radio_button(self, rb):
        self.date_limit.setDisabled(not rb.isChecked())

    def on_click_analyse(self, event):
        self.on_click_analyse_custom_word(event, False)

    def on_click_analyse_custom_word(self, event, custom_words=True):
        self.adjective_details_frame.setVisible(False)
        index = self.list_widget.currentRow()
        if index == -1:
            self.clear_and_write_to_message_box('no place chosen')
            return
        rev_list = self.reviewDao.get_all_by_name(self.places_list[index].name)
        if self.radioButtonMonthLimit.isChecked():
            rev_list = ReviewFilter.filter_by_date(rev_list, self.date_limit.date().toPyDate())
        if self.useful_only_rb.isChecked():
            rev_list = ReviewFilter.filter_by_author_useful(rev_list)

        self.clear_and_write_to_message_box(str(len(rev_list)) + ' reviews found')
        self.number_reviews_found = len(rev_list)
        if custom_words:
            words = self.opinion_object_edit_widget.text()
            if words == '':
                self.clear_and_write_to_message_box('no word chosen')
                return
            custom_word_list = words.strip().split(';')
            words_to_analyze = {}
            for each in custom_word_list:
                words_to_analyze[each] = [each]
            analyzer_args = [rev_list, words_to_analyze]
        else:
            analyzer_args = [rev_list]
        self.thread = PyQtApp.AnalyzerThread(*analyzer_args)
        self.thread.signal.connect(self.on_signal_analysis_results)
        self.thread.progressSignal.connect(self.on_signal_progressBar_update)
        self.thread.start()
        self.progressBar.setVisible(True)
        self.progressBar.setProperty("value", 0)
        self.custom_word_analysis_button_widget.setEnabled(False)
        self.categories_analysis_button_widget.setEnabled(False)
        self.tips_button.setEnabled(False)

    def clear_and_write_to_message_box(self, text):
        self.result_widget.clear()
        self.result_widget.insertPlainText(text)

    def on_signal_progressBar_update(self, value):
        self.progressBar.setProperty("value", int(value))

    def on_signal_analysis_results(self, analysis_results):
        self.result_label.setVisible(True)
        self.progressBar.setVisible(False)
        self.custom_word_analysis_button_widget.setEnabled(True)
        self.categories_analysis_button_widget.setEnabled(True)
        self.tips_button.setEnabled(True)
        self.tips_button.setVisible(True)
        self.analysis_results_dictionary = analysis_results.adjective_occurence_dict
        self.results_on_screen = True

        html_to_insert= analysis_results.to_html()
        if self.number_reviews_found != 0:
            html_to_insert = str(self.number_reviews_found) + ' reviews analysed<br/><br/>' + html_to_insert
        self.result_widget.setHtml(html_to_insert)

        self.remove_sent_widgets()

        if self.weighted_mean_rb.isChecked():
            chosen_filter=WEIGHTED_MEAN
        elif self.useful_only_rb.isChecked():
            chosen_filter=ONLY_USEFUL
        else:
            chosen_filter=ALL

        only_non_zero=self.nonzero_sentiment_radio_button.isChecked()
        for category, value in analysis_results.get_sentiment_value_dict(only_non_zero=only_non_zero, filter=chosen_filter).items():
            widget_to_add = SentimentResultWidget(category, value*100)
            self.sentiment_value_layout.addWidget(widget_to_add)
            self.sentiment_result_widgets.append(widget_to_add)

        self.tips = analysis_results.tips

    def on_click_result_widget(self, e):
        cursor = self.result_widget.cursorForPosition(e.pos())
        cursor.select(QTextCursor.BlockUnderCursor)
        self.result_widget.setTextCursor(cursor)
        adj_end_pos = cursor.selectedText().find("(")
        word = cursor.selectedText()[:adj_end_pos].strip()
        cursor_pos = cursor.position()

        # determining position of categories names in textfield and putting them into list of tuples
        doc = self.result_widget.document()
        list = []
        for k, v in self.analysis_results_dictionary.items():
            cursor = doc.find(k)
            cursor.select(QTextCursor.WordUnderCursor)
            list.append((cursor.position(),k))
        list = sorted(list)

        if len(list) == 0:
            return
        elif len(list) == 1:
            found_category = list[0][1]
        else:
            for pos, category in list:
                if pos>cursor_pos:
                    break
                found_category = category
        self.adj_dict = self.analysis_results_dictionary[found_category]
        if word not in self.adj_dict.keys():
            self.adjective_details_frame.setVisible(False)
            return
        else:
            self.adjective_details_list.clear()
            self.adjective_details_frame.setVisible(True)
            html_to_insert = '<ul>\n'
            for adj in self.adj_dict[word]:
                self.adjective_details_list.append(adj)
                html_to_insert +="<li>"+adj.to_html()+"</li>\n"
            html_to_insert += '</ul>\n'
            self.adjective_details_textedit.setHtml(html_to_insert)

    def on_click_adjective_details(self, e):
        cursor = self.adjective_details_textedit.cursorForPosition(e.pos())
        if cursor.blockNumber() < len(self.adjective_details_list):
            review_id = self.adjective_details_list[cursor.blockNumber()].review_id
            chosen_sent = cursor.block().text()
            self.dialog = AdjectiveUseDialog.AdjectiveUseDialog(review_id, dao=self.reviewDao, bold=chosen_sent)
            self.dialog.show()
        else:
            return

    def on_click_tips(self, event):
        self.dialog = TipsDialog(self.tips)
        self.dialog.show()

    def remove_sent_widgets(self):
        for widget in self.sentiment_result_widgets:
            widget.deleteLater()
        self.sentiment_result_widgets.clear()

