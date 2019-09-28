CATEGORY_HOTEL = 'Hotel'
CATEGORY_RESTAURANT = 'Restaurant'


class Place:

    def __init__(self, id='', name='', category='', location=''):
        self.id = id
        self.name = name
        self.category = category
        self.location = location

    def __str__(self):
        return 'id: ' + str(
            self.id) + '\n' + 'name: ' + self.name + '\n' + 'category: ' + self.category + '\n' + 'location: ' + self.location + '\n'
