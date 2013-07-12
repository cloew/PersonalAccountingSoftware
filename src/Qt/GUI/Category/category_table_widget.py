from db.categories import Categories

class CategoryTableWidget:
    """ The Category Table Widget View """
    
    def __init__(self):
        """ Initalize the Category Table """
        categories = Catgeories.all()