from category_column import CategoryColumn

from db.categories import Categories
from PySide.QtCore import Qt

class DeleteColumn(CategoryColumn):
    """ Represents the Category Delete Column """
    header_name = None

    def flags(self, row):
        """ Return flags for the Column's Row """
        return Qt.ItemIsEnabled

    def getDataForCategory(self, category):
        """ Return data for the provided category """
        return None # No Data, just a button

    def setDataForCategory(self, category, value):
        """ Set data for the provided category """
        if value:
            Categories.delete(category)
        return False

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Delete the Category."