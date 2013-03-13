from category_column import CategoryColumn

class NameColumn(CategoryColumn):
    """ Represents the Category Name Column """
    header_name = "Name"

    def getDataForCategory(self, category):
        """ Return data for the provided category """
        if category.name is not None:
            return category.name

    def setDataForCategory(self, category, value):
        """ Set data for the provided category """
        category.name = value
        return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Name of the category."