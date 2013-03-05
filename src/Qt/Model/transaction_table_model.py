from PyQt4 import QtCore

from db.transactions import Transactions

class TransactionTableModel(QtCore.QAbstractTableModel):
    """ Represnts the Transaction List as a Table """

    def __init__(self):
        """ Build the Transactions Table """
        QtCore.QAbstractTableModel.__init__(self)

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(Transactions.all())

    def columnCount(self, parent):
        """ Returns the number of columns in the table """
        return 4

    def data(self, index, role = QtCore.Qt.DisplayRole):
        """ Return the data at the given index """
        return QtCore.QVariant("Some Value")

    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        """ Return Header Data """
        if QtCore.Qt.Horizontal == orientation:
            return QtCore.QVariant("Horizontal Header")
        else:
            return QtCore.QVariant("Vertical Header")