from typing import Dict

from nltk.corpus import sentiwordnet as swn


class SentiWordNetScores:

    def __init__(self):
        self.exception_sentim_values: Dict[str, float] = {
            'expensive':-0.75,
            'high':     -0.5,
            'cheap':    0.5,
            'low':      0.75,
            'fresh':    0.75,
            'other':    0.0,
            'open':     0.5,
            'delicate': 0.25,
            'quiet':    0.25,
            'surprising': 0,
            'early':    0,
            'average':  -0.25,
            'late':     0,
            'huge':     0.25,
            'outstanding': 0.75,
            'cheapest': 0.75,
            'inexpensive':0.25,
            'higher':   -0.25,
            'free':     0.5,
            'main':     0,
            'exact':    0,
            'generous':  0.5,
            'comfy':    0.5,
            'wide':     0.25
        }
        # for word, sentim_value in exceptional_sentim_vals_to_add.items():
        #     for synonym in list(swn.senti_synsets(word)): #word synonyms
        #         full_synset_name = synonym.synset.name()
        #         first_dot_position = full_synset_name.index('.')
        #         if full_synset_name[first_dot_position+1] == 'a': #synonym is also adjective
        #             key=full_synset_name[:first_dot_position]
        #             self.exception_sentim_values[key] = sentim_value

    def get_sentiment_value(self, word, partofspeech):
        try:
            return self.exception_sentim_values[word]
        except KeyError:
            sets_count = 0
            sentiment_value = 0
            for sentisynset in swn.senti_synsets(word, partofspeech):
                sets_count += 1
                sentiment_value += sentisynset.pos_score() # * sentisynset.obj_score()
                sentiment_value -= sentisynset.neg_score() # * sentisynset.obj_score()
            if sets_count == 0:
                return 0
            else:
                return sentiment_value/sets_count
