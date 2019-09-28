import spacy
from analyzer.SentiWordNetScores import SentiWordNetScores
from analyzer.AnalysisResults import AnalysisResults
from analyzer.AdjectiveUse import AdjectiveUse
from analyzer.Tip import Tip

TAG_VERB_BASE = 'VB'
TAG_VERB_NON_3RD_PERSON_PRESENT = 'VBP'

ENGLISH_STATISTICAL_MODEL = 'en_core_web_sm'

ROOT = 'ROOT'
LEMMA_BE = 'be'

POS_PROPER_NOUN = 'PROPN'
POS_NOUN = 'NOUN'
POS_VERB = 'VERB'
POS_ADJECTIVE = 'ADJ'
DEP_NOMINAL_SUBJECT = 'nsubj'
DEP_NEGATION = 'neg'
TAG_POSSESIVE_ENDING = 'POS'
TAG_VERB_GERUND = 'VBG'
TAG_CONJ_PREP = 'IN'
TAG_NOUN = 'NN'
TAG_ADJECTIVE = 'JJ'
TAG_PERSONAL_PRONOUN = 'PRON'

service_words = ['service', 'staff', 'waiter', 'hostess', 'waitress', 'waiters']
decor_words = ['decor', 'decoration', 'lighting', 'atmosphere', 'ambiance']
food_words = ['food', 'drink', 'meal', 'portion', 'menu', 'cook', 'dish', 'lunch', 'dinner', 'breakfast', 'taste']
price_words = ['price', 'bill', 'money', 'expense']
categories_words = {'food': food_words, 'service': service_words, 'decor': decor_words, 'price': price_words}

sentspacy_to_sentiwordnet_pos_dict = {POS_ADJECTIVE: 'a', POS_VERB: 'v', POS_NOUN: 'n', POS_PROPER_NOUN: 'n'}

class NounNotFoundError(Exception):
    pass

def find_noun_of_adjective(adjective):
    if adjective.head.pos_ == POS_NOUN and adjective!=adjective.head:
        return adjective.head
    if adjective.head.pos_ == POS_ADJECTIVE and adjective.head != adjective:
        return find_noun_of_adjective(adjective.head)
    if adjective.head.pos_ == POS_VERB and adjective.head.lemma_ == LEMMA_BE:
        for child in adjective.head.children:
            if child.pos_ == POS_NOUN:
                return child
    raise NounNotFoundError

class SpaCyReviewAnalyzer:

    def __init__(self, review_list, word_list=categories_words):
        self.review_list = review_list
        self.nlp = spacy.load(ENGLISH_STATISTICAL_MODEL)
        self.sentiment_values = SentiWordNetScores()
        self.word_list = word_list
        self.multi_word_list = {}
        for categ, categ_word_list in word_list.items():
            for word in categ_word_list:
                if len(word.split()) > 1:
                    categ_word_list.remove(word)
                    if categ in self.multi_word_list:
                        self.multi_word_list[categ].append(word.split())
                    else:
                        self.multi_word_list[categ] = word.split()
        self.analysis_results = AnalysisResults(word_list.keys())

    def analyze(self, progress_signal=None):

        review_list_length = len(self.review_list)
        review_count = 0
        for review in self.review_list:
            review_count += 1
            text_to_analyze = review.title + '. ' + review.text
            doc = self.nlp(text_to_analyze)
            for sent in doc.sents:
                count = 0
                adverb_flag = False
                for token in sent:
                    for category, categ_specific_words in self.word_list.items():
                        if TAG_ADJECTIVE in token.tag_ or TAG_VERB_GERUND in token.tag_:
                            try:
                                noun = find_noun_of_adjective(token)

                                if noun.lemma_ in categ_specific_words or noun.text in categ_specific_words:

                                    sentim_val = self.sentiment_values.get_sentiment_value(token.text.lower(), self.spacy_to_sentiwordnet_pos(token))

                                    negated = False
                                    if self.is_token_negated(token):
                                        negated = True
                                        sentim_val /= -2

                                    adj = AdjectiveUse(token, noun, review.id, sent, sentim_val, negated=negated)
                                    self.analysis_results.add_adjective_use(category, adj)

                                elif noun.lemma_ in self.multi_word_list[category]:
                                    component_words = self.multi_word_list[category]

                                    # valid if sentence contains all words and one of the other words is among children of the word

                                    valid = all(word in sent.text for word in component_words)

                                    if valid:
                                        valid = any(child.text in component_words for child in noun.children)

                                    if valid:
                                        sentim_val = self.sentiment_values.get_sentiment_value(token.text.lower(), self.spacy_to_sentiwordnet_pos(token))
                                        negated = self.is_token_negated(token)
                                        if negated:
                                            sentim_val /= -2
                                        adj = AdjectiveUse(token, noun, review.id, sent, sentim_val, negated=negated)
                                        self.analysis_results.add_adjective_use(category, adj)

                            except NounNotFoundError:
                                continue
                            except KeyError:
                                continue

                    if len(sent)<5:
                        continue

                    if count > 2:
                        continue
                    else:
                        count += 1

                    if count == 1:
                        if 'will' in token.text.lower() or 'would' in token.text.lower() or 'thank' in token.text.lower() or 'let' in token.text.lower():
                            continue
                        if token.pos_ == 'ADV':
                            adverb_flag = True
                        if token.tag_ == TAG_VERB_BASE or token.tag_ == TAG_VERB_NON_3RD_PERSON_PRESENT:
                            tip = Tip(sent, review.id)
                            self.analysis_results.add_tip(tip)
                        continue
                    elif count == 2 and adverb_flag:
                        if token.tag_ == TAG_VERB_BASE or token.tag_ == TAG_VERB_NON_3RD_PERSON_PRESENT:
                            tip = Tip(sent, review.id)
                            self.analysis_results.add_tip(tip)

            if progress_signal != None:
                progress_signal.emit(100 * review_count / review_list_length)

        return self.analysis_results

    @staticmethod
    def is_token_negated(token):
        if token.head.pos_ == POS_NOUN and token.head.head.lemma_ == LEMMA_BE:
            token = token.head
        if token.head.pos_ == POS_VERB:
            return any(child.dep_ == DEP_NEGATION for child in token.head.children)
        return False

    @staticmethod
    def spacy_to_sentiwordnet_pos(token):
        try:
            return sentspacy_to_sentiwordnet_pos_dict[token.pos_]
        except KeyError as ke:
            raise ValueError(token.pos_ + ' is an invalid part of speech') from ke
