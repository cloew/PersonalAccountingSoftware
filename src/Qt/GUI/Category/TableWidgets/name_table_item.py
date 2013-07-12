from db.categories import Categories
from Qt.GUI.Core.kao_table_item import KaoTableItem

class NameTableItem(KaoTableItem):
    """ Represents a Table Widget Item for a Category Name """
    
    def __init__(self, category):
        """ Initialize the Name Item """
        self.category = category
        KaoTableItem.__init__(self)
        
    def getData(self):
        """ Return the item's data as a string """
        return self.category.name
        
    def saveData(self, value):
        """ Save Data """
        self.category.name = value
        Categories.save()