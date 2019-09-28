import xml, mysql.connector
from model.Place import Place

FIELD_PLACE_ID = 'place_id'

FIELD_NAME = 'name'


class MysqlPlaceDaoError(Exception):
    pass


class MysqlPlaceDao:

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

    def get_place_by_field(self, field_name, field_value):
        if field_name not in [FIELD_NAME, FIELD_PLACE_ID]:
            raise ValueError('incorrect field name')
        cursor = self.db.cursor()
        sql = f'SELECT place_id, name, category, location FROM places WHERE {field_name} = %s'
        val = (field_value,)
        cursor.execute(sql, val)
        el = cursor.fetchone()
        if el is None:
            raise MysqlPlaceDaoError
        return Place(id=el[0], name=el[1], category=el[2], location=el[3])

    def add_place(self, place):
        if place.name == None:
            raise ValueError
        cursor = self.db.cursor()
        sql = 'INSERT INTO places (name, category, location) VALUES (%s, %s, %s)'
        val = (place.name, place.category, place.location)
        cursor.execute(sql, val)
        self.db.commit()
        return cursor.lastrowid

    def list_places(self):
        cursor = self.db.cursor()
        sql = 'SELECT place_id, name, category, location from places ORDER BY name ASC'
        cursor.execute(sql)
        reslist = cursor.fetchall()
        return [Place(id=el[0], name=el[1], category=el[2], location=el[3]) for el in reslist or []]
