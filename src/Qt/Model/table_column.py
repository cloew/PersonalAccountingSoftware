from db.transactions import Transactions
from PySide.QtCore import QAbstractTableModel, QModelIndex, Qt

class TableColumn:
    """ Represents a column in a Table Model """
    header_name = "TODO: Replace with real name" # Should be overridden in Sub Class

    def getHorizontalHeader(self):
        """ Return Header Data """
        return self.header_name

    def flags(self, row):
        """ Return flags for the Column's Row """
        return Qt.ItemIsEditable | Qt.ItemIsEnabled # | Qt.ItemIsSelectable

    def getData(self, row):
        """ Return data for the transaction in the given row.
            Should be overridden in sub class. """

    def setData(self, row, value):
        """ Set the data in this column of the given transaction.
            Should be overridden in sub class. """

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row.
            Should be overridden in sub class. """