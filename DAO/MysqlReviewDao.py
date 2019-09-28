import xml.etree.ElementTree, mysql.connector
from model.Review import Review


class MysqlReviewDaoError(Exception):
    pass


class MysqlReviewDao:
    def __init__(self):
        tree = xml.etree.ElementTree.parse('config/mysql_configuration.xml')
        root = tree.getroot()
        config = {}
        for elem in root:
            config[elem.tag] = elem.text

        self.db = mysql.connector.connect(user=config['user'], password=config['password'],
          host=config['host'],
          database=config['database'],
          charset=config['charset'])

    def add_review(self, review, place_id=None):
        """
        :param review:
        :param place_id:
        :return: rowcount
        """
        cursor = self.db.cursor()
        sql = 'REPLACE INTO reviews (review_id, name, title, review_text, review_date, rating, exp_date, helpful, SOURCE_URL, place_id, author_all, author_helpful) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (review.id, review.name, review.title, review.text, review.review_date, review.rating,
               review.experience_date, review.helpful, review.source_url, place_id, review.author_all, review.author_helpful)
        cursor.execute(sql, val)
        self.db.commit()
        return cursor.rowcount

    def get_all_by_name(self, name):
        cursor = self.db.cursor()
        sql = 'SELECT review_id, name, title, review_text, review_date, rating, exp_date, helpful, SOURCE_URL, ' \
              'place_id, author_all, author_helpful FROM reviews WHERE name = %s'
        val = (name,)
        cursor.execute(sql, val)
        reslist = cursor.fetchall()
        to_return = []
        if reslist != None:
            for x in reslist:
                to_return.append(Review(int(x[0]), str(x[1]), x[2].decode('utf-8'), x[3].decode('utf-8'), x[4], int(x[5]), x[6], int(x[7]), str(x[8]), int(x[9]), int(x[10]), int(x[11])))
            # print(int(x[10]))
        return to_return

    def get_review_by_id(self, id):
        cursor = self.db.cursor()
        sql = 'SELECT review_id, name, title, review_text, review_date, rating, exp_date, helpful, SOURCE_URL, ' \
              'place_id, author_all, author_helpful FROM reviews WHERE review_id = %s'
        val = (id,)
        cursor.execute(sql, val)
        review = cursor.fetchone()
        if review is None:
            raise MysqlReviewDaoError(f'review with id: {id} not found in database')
        return Review(int(review[0]), str(review[1]), review[2].decode('utf-8'), review[3].decode('utf-8'), review[4], int(review[5]), review[6], int(review[7]),
               str(review[8]), int(review[9]), int(review[10]), int(review[11]))