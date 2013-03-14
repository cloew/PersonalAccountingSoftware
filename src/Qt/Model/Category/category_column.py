from db.categories import Categories
from PySide.QtCore import QAbstractTableModel, QModelIndex, Qt
from Qt.Model.table_column import TableColumn

class CategoryColumn(TableColumn):
    """ Represents a column in the Categories Table """
    header_name = "TODO: Replace with real name" # Should be overridden in Sub Class

    def getData(self, row):
        """ Return data for the category in the given row """
        category = self.getCategoryForRow(row)
        if category is not None:
            return self.getDataForCategory(category)

    def getDataForCategory(self, category):
        """ Return data for the provided category.
            Should be overridden in sub class """

    def setData(self, row, value):
        """ Set the data in this column of the given category """
        category = self.getCategoryForRow(row)
        if category is not None:
            return self.setDataForCategory(category, value)

    def setDataForCategory(self, transaction, value):
        """ Set data for the provided category.
            Return whether the entry was set.
            Should be overridden in sub class. """

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row.
            Should be overridden in sub class. """

    def getCategoryForRow(self, row):
        """ Returns the Transaction in the given row """
        categories = Categories.all()
        if row < len(categories):
            return categories[row]