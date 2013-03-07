from db.categories import Categories
from Qt.Model.table_model import TableModel

class CategoryTableModel(TableModel):
    """ Represnts the Category List as a Table """

    def getColumns(self):
        """ Get the Columns for the table """
        return []

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(Categories.all())