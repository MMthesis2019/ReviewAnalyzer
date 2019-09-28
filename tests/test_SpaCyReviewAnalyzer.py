import unittest
from datetime import date

import spacy

from analyzer.SpaCyReviewAnalyzer import ENGLISH_STATISTICAL_MODEL, SpaCyReviewAnalyzer, find_noun_of_adjective
from model.Review import Review


class TestAnalyser(unittest.TestCase):
    def test_find_noun_of_adjective(self):
        nlp = spacy.load(ENGLISH_STATISTICAL_MODEL)
        sentence1 = "This was a tasty meal."
        doc1 = nlp(sentence1)
        for token in doc1:
            if token.text == "tasty":
                noun_token = find_noun_of_adjective(token)
                self.assertEqual("meal", noun_token.text)

        sentence2 = "This meal was really tasty."
        doc2 = nlp(sentence2)
        for token in doc2:
            if token.text == "tasty":
                noun_token = find_noun_of_adjective(token)
                self.assertEqual("meal", noun_token.text)

        sentence3 = "This was a warm and tasty meal."
        doc3 = nlp(sentence3)
        for token in doc3:
            if token.text == "tasty":
                noun_token = find_noun_of_adjective(token)
                self.assertEqual("meal", noun_token.text)

        sentence4 = "This meal was nice and tasty."
        doc4 = nlp(sentence4)
        for token in doc4:
            if token.text == "tasty":
                noun_token = find_noun_of_adjective(token)
                self.assertEqual("meal", noun_token.text)

        sentence5 = "This meal was cold but tasty."
        doc5 = nlp(sentence5)
        for token in doc5:
            if token.text == "tasty":
                noun_token = find_noun_of_adjective(token)
                self.assertEqual("meal", noun_token.text)

    def test_is_token_negated(self):
        nlp = spacy.load(ENGLISH_STATISTICAL_MODEL)
        negated_sentence_string1 = "This sentence isn't affirmative."
        negated_sentence_doc1 = nlp(negated_sentence_string1)
        for token in negated_sentence_doc1:
            if token.text == "affirmative":
                self.assertTrue(SpaCyReviewAnalyzer.is_token_negated(token))

        negated_sentence_string2 = "This sentence is not affirmative."
        negated_sentence_doc2 = nlp(negated_sentence_string2)
        for token in negated_sentence_doc2:
            if token.text == "affirmative":
                self.assertTrue(SpaCyReviewAnalyzer.is_token_negated(token))

        negated_sentence_string3 = "This is not an affirmative sentence."
        negated_sentence_doc3 = nlp(negated_sentence_string3)
        for token in negated_sentence_doc3:
            if token.text == "affirmative":
                self.assertTrue(SpaCyReviewAnalyzer.is_token_negated(token))

    def test_analyze(self):
        review1 = Review(1, "restaurantX", "Good for lunch",
                         "No English speaking but friendly staff. Good choice if you are visiting the nearby museum. The food was good but not great. The prices were fair.",
                         date.today(), 4, None, 0, '', 1, 1)

        review2 = Review(2, "restaurantX", "Eating out with family", "Fabulous food. Fair prices, excellent value for money. We would highly recommend this restaurant. Right in the centre of the town and a great atmosphere always busy. ",
                         date.today(),  5, None, 0, '',1,1)
        review_list = [review1, review2]
        analyzer = SpaCyReviewAnalyzer(review_list)
        results = analyzer.analyze()
        sentiment_dict = results.get_sentiment_value_dict()
        for category, sentiment_val in sentiment_dict.items():
            self.assertTrue(sentiment_val>0)

        adjective_use_dict1 = results.adjective_occurence_dict['food']
        self.assertEqual(len(adjective_use_dict1['good']), 1)

        adjective_use_dict2 = results.adjective_occurence_dict['price']
        self.assertEqual(len(adjective_use_dict2['fair']), 2)

        use_of_good = adjective_use_dict1['good'][0]
        self.assertEqual(use_of_good.noun.text, "food")
        self.assertEqual(use_of_good.sentence.text, "The food was good but not great.")
        self.assertEqual(use_of_good.review_id, 1)
        self.assertTrue(use_of_good.sentiment_value>0)

if __name__ == '__main__':
    unittest.main()
