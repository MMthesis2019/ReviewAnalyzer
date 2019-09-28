from analyzer.SentiWordNetScores import SentiWordNetScores

ADJECTIVE_CLASS_NAME = "adjective"
POSITIVE_CLASS_NAME = "positive"
NEGATIVE_CLASS_NAME = "negative"
NOUN_CLASS_NAME = "noun"


class AdjectiveUse:
    """contains information about an adjective, what it refers to and the context in which it is used"""

    sentiwordnet_scores=SentiWordNetScores

    def __init__(self, adjective_token, noun, review_id, sentence, sentiment_value, negated=False):
        self.adjective_token = adjective_token
        if negated:
            self.adjective_text = 'not '+ adjective_token.text.lower()
        else:
            self.adjective_text = adjective_token.text.lower()
        self.noun = noun
        self.sentence = sentence
        self.review_id = review_id
        self.sentiment_value = sentiment_value

    def to_html(self):
        html_sentence = self.sentence.text
        try:
            adjective_all_lowercase = self.adjective_token.text.lower()
            adj_start = html_sentence.lower().index(adjective_all_lowercase)
            adj_end = adj_start + len(adjective_all_lowercase)
            if self.sentiment_value>0:
                span_tag=self.open_span_tag(ADJECTIVE_CLASS_NAME, POSITIVE_CLASS_NAME)
            elif self.sentiment_value<0:
                span_tag = self.open_span_tag(ADJECTIVE_CLASS_NAME, NEGATIVE_CLASS_NAME)
            else:
                span_tag = self.open_span_tag(ADJECTIVE_CLASS_NAME)
            html_sentence = html_sentence[:adj_start] + span_tag + \
                            html_sentence[adj_start:adj_end] + self.close_span_tag() + html_sentence[adj_end:]

            noun_start = self.find_token_position(self.sentence, self.noun, html_sentence)
            noun_end = noun_start + len(self.noun)

            html_sentence = html_sentence[:noun_start] + self.open_span_tag(NOUN_CLASS_NAME) + \
                            html_sentence[noun_start:noun_end] + self.close_span_tag() + html_sentence[noun_end:]
            return html_sentence
        except ValueError:
            raise ValueError("noun or adjective not found in the sentence")

    @staticmethod
    def open_span_tag(*span_classes):
        classes = ""
        for span_class in span_classes:
            classes += span_class+" "
        return '<span class="'+classes+'">'

    def find_word_end_position(self, sentence, word):
        pass

    @staticmethod
    def close_span_tag():
        return "</span>"

    def find_token_position(self, noun_sent, noun, html_sent):
        occurence = 0
        for token in noun_sent:
            if noun.text in token.text:
                occurence+=1
                if token == noun:
                    break
        if occurence==0:
            raise ValueError('noun not found')

        from_index=0
        while occurence!=0:
            from_index = html_sent.find(noun.text, from_index+1)
            occurence-=1
        return from_index
