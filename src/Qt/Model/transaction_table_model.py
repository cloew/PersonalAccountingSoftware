from PyQt4.QtCore import QAbstractTableModel, QVariant, Qt

from db.transactions import Transactions

class TransactionTableModel(QAbstractTableModel):
    """ Represnts the Transaction List as a Table """

    def __init__(self):
        """ Build the Transactions Table """
        QAbstractTableModel.__init__(self)

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(Transactions.all())

    def columnCount(self, parent):
        """ Returns the number of columns in the table """
        return 4

    def data(self, index, role = Qt.DisplayRole):
        """ Return the data at the given index """
        if not index.isValid():
            return self.getDisplayRoleData(index)
        else:
            return self.getDataBasedOnRole(index, role)

    def getDataBasedOnRole(self, index, role):
        """ Get Data based on the role given """
        print "Getting Data Based on Role:", role

        if role == Qt.DisplayRole:
            return self.getDisplayRoleData(index)
        elif role == Qt.TextAlignmentRole:
            return self.getTextAlignmentRole(index)

    def getDisplayRoleData(self, index):
        """ Return Data for the Qt Display Role """
        return QVariant("Some Value")

    def getTextAlignmentRole(self, index):
        """ Return Text Alignment for the given cell """
        return int(Qt.AlignLeft|Qt.AlignVCenter)

    def headerData(self, section, orientation, role = Qt.DisplayRole):
        """ Return Header Data """
        if role != Qt.DisplayRole:
            return None
        if Qt.Horizontal == orientation:
            return QVariant("Horizontal Header")
        else:
            return QVariant("Vertical Header")