from PyQt4 import QtCore

from db.transactions import Transactions

class TransactionTableModel(QtCore.QAbstractTableModel):
    """ Represnts the Transaction List as a Table """

    def __init__(self):
        """ Build the Transactions Table """
        QtCore.QAbstractTableModel.__init__(self)

    def rowCount(self):
        """ Returns the number of rows in the table """
        return len(Transactions.all())

    def columnCount(self):
        """ Returns the number of columns in the table """
        return 4

    def data(self, QtCore.QModelIndex index, int role = Qt.DisplayRole):
        """ Return the data at the given index """
        return "Some Value"