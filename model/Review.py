import locale

from datetime import date
from typing import Optional


class Review:
    """class to model the review from database

    Attributes:
        id              id in database, taken from website
        name            name of the reviewed place
        title           title of the review given by its reviewer
        text            text of the review excluding title
        review_date     date when the review was published
        rating          rating from 0 to 5 given by the reviewer
        experience_date date when the reviewer visited given place
        helpful         number of helpful votes given to the review by other users
        to_expand       boolean, if true the review text may not be complete, and have to be downloaded
        source_url      url of the website under which the review was present at the moment of downloading
        place_id        id in database of the reviewed place, assigned by program
        author_all      number of all the reviews ever written by the reviewer
        author_helpful  number of helpful votes given to all the reviews ever written by the author
    """
    nullables = ['id', 'experience_date']

    def __init__(self, id: Optional[int] = None, name: str = '', title: str = '', text: str = '',
                 review_date: date = date.today(), rating: int = 0, experience_date: Optional[date] = None,
                 helpful: int = 0, source_url: str = '', place_id: int = 0, author_all: int = 0, author_helpful: int = 0):
        self.id = id
        self.name = name
        self.title = title
        self.text = text
        self.review_date = review_date
        self.rating = rating
        self.experience_date = experience_date
        self.helpful = helpful
        self.to_expand = False
        self.source_url = source_url
        self.place_id = place_id
        self.author_all = author_all
        self.author_helpful = author_helpful

    def __str__(self):
        for k,v in self.__dict__.items():
            if k not in self.nullables and v is None:
                raise ValueError(f'the field {k} is of None type')
        return 'id: ' + str(self.id) + '\n' + \
               'title: ' + self.title + '\n' + \
               'text: ' + self.text + '\n' + \
               'name: ' + self.name + '\n' + \
               'review_date: ' + str(self.review_date) + '\n' + \
               'experience_date: ' + str(self.experience_date) + '\n' + \
               'rating: ' + str(self.rating) + '\n' + \
               'helpful: ' + str(self.helpful) + '\n' + \
               'author_all: ' + str(self.author_all) + '\n' + \
               'author_helpful: ' + str(self.author_helpful) + '\n'

