import datetime

class ReviewFilter:

    @staticmethod
    def filter_by_date(review_list, earliest_date):
        result = []
        for review in review_list:
            if review.review_date > earliest_date:
                result.append(review)
        return result

    @staticmethod
    def filter_by_useful(review_list):
        result = []
        for review in review_list:
            if review.helpful > 0:
                result.append(review)
        return result

    @staticmethod
    def filter_by_author_useful(review_list):
        result = []
        for review in review_list:
            if review.author_helpful > 0:
                result.append(review)
        return result