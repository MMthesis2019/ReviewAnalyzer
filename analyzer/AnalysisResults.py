from typing import Dict, List
from DAO.MysqlReviewDao import MysqlReviewDao
from analyzer.AdjectiveUse import AdjectiveUse

ALL = 0
ONLY_USEFUL = 1
WEIGHTED_MEAN = 2


class AnalysisResults:
    def __init__(self, category_names: List[str]):
        if not category_names:
            raise ValueError('category_names list is empty')

        self.adjective_occurence_dict: Dict[str, Dict[str, List[AdjectiveUse]]] = {}
        for category_name in category_names:
            self.adjective_occurence_dict[category_name] = {}

        self.tips = []

    def to_html(self) -> str:
        result_as_str_list=[]
        for category, adjective_dict in self.adjective_occurence_dict.items():
            if len(adjective_dict) == 0:
                continue
            result_as_str_list += f'{category} is described as:'
            pos_adj_list = []
            neg_adj_list = []
            neu_adj_list = []
            for adj_text, adj_obj_list in adjective_dict.items():
                if adj_obj_list[0].sentiment_value > 0:
                    pos_adj_list.append((adj_text,adj_obj_list))
                elif adj_obj_list[0].sentiment_value < 0:
                    neg_adj_list.append((adj_text,adj_obj_list))
                else:
                    neu_adj_list.append((adj_text,adj_obj_list))
            pos_adj_list = sorted(pos_adj_list, key=lambda x: len(x[1]), reverse=True)
            neg_adj_list = sorted(neg_adj_list, key=lambda x: len(x[1]), reverse=True)
            neu_adj_list = sorted(neu_adj_list, key=lambda x: len(x[1]), reverse=True)

            result_as_str_list += '<ul class="positive">'
            for adj_text, adj_obj_list in pos_adj_list:
                result_as_str_list+= f'<li>{adj_text} ({len(adj_obj_list)} times),</li>'
            result_as_str_list += '</ul><ul class="negative">'
            for adj_text, adj_obj_list in neg_adj_list:
                result_as_str_list+= f'<li>{adj_text} ({len(adj_obj_list)} times),</li>'
            result_as_str_list+="</ul><ul>"
            for adj_text, adj_obj_list in neu_adj_list:
                result_as_str_list+= f'<li>{adj_text} ({len(adj_obj_list)} times),</li>'
            result_as_str_list += "\n</ul><br/>\n"

        if not result_as_str_list:
            return 'no results'
        else:
            return ''.join(result_as_str_list)

    def add_adjective_use(self, category: str, adjective: AdjectiveUse):
        """add adjective in the form of AdjectiveUse object to the list of adjectives used to describe the category"""
        adjective_dict = self.adjective_occurence_dict[category]
        key = adjective.adjective_text
        if key in adjective_dict:
            adjective_dict[key].append(adjective)
        else:
            adjective_dict[key] = [adjective]

    def get_sentiment_value_dict(self, only_non_zero=False, filter=ALL) -> Dict[str, float]:
        if filter == ONLY_USEFUL or filter == WEIGHTED_MEAN:
            reviewDao= MysqlReviewDao()
        sentiment_dict = {}
        for category, adj_dict in self.adjective_occurence_dict.items():
            sentiment_value_sum = 0
            count = 0
            for adj_text, adj_list in adj_dict.items():
                sentiment_value = adj_list[0].sentiment_value
                if only_non_zero and sentiment_value == 0:
                    continue
                else:
                    if filter == ALL:
                        sentiment_value_sum += sentiment_value * len(adj_list)
                        count += len(adj_list)
                    else:
                        for each in adj_list:
                            author_helpful = reviewDao.get_review_by_id(each.review_id).author_helpful
                            author_all = reviewDao.get_review_by_id(each.review_id).author_all
                            if filter == ONLY_USEFUL:
                                if author_helpful > 0:
                                    sentiment_value_sum += sentiment_value
                                    count += 1
                            elif filter == WEIGHTED_MEAN:
                                if author_helpful > 0:
                                    sentiment_value_sum += (author_helpful+1)*sentiment_value
                                    count += (author_helpful+1)
                                else:
                                    sentiment_value_sum += sentiment_value
                                    count+=1
            if count > 0:
                sentiment_dict[category] = sentiment_value_sum/count
            else:
                continue

        return sentiment_dict

    def get_adjective_dict(self, category) -> Dict[str, List[AdjectiveUse]]:
        """returns dictionary of k:adjective_text, v: adjective object list"""
        return self.adjective_occurence_dict[category]

    def add_tip(self, tip):
        self.tips.append(tip)
