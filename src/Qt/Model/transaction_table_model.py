from db.transactions import Transactions

from PyQt4.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt

class TransactionTableModel(QAbstractTableModel):
    """ Represnts the Transaction List as a Table """

    def __init__(self):
        """ Build the Transactions Table """
        QAbstractTableModel.__init__(self)
        self.columns = ["Amount", "Description", "Type", "Date"]
        self.columnPopulatorFunctions = [self.getTransactionAmount,
                                         self.getTransactionDescription,
                                         self.getTransactionIncome,
                                         self.getTransactionDate]

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(Transactions.all())

    def columnCount(self, parent):
        """ Returns the number of columns in the table """
        return 4

    def insertRows(self, row, count, parent=QModelIndex()):
        """ Insert Rows """
        self.beginInsertRows(parent, row, row+count-1)
        self.endInsertRows()
        return True

    def data(self, index, role = Qt.DisplayRole):
        """ Return the data at the given index """
        if not index.isValid():
            return self.getDisplayRoleData(index)
        else:
            return self.getDataBasedOnRole(index, role)

    def getDataBasedOnRole(self, index, role):
        """ Get Data based on the role given """
        if role == Qt.DisplayRole:
            return self.getDisplayRoleData(index)
        elif role == Qt.TextAlignmentRole:
            return self.getTextAlignmentRole(index)

    def getDisplayRoleData(self, index):
        """ Return Data for the Qt Display Role """
        column = index.column()
        if column < len(self.columnPopulatorFunctions):
            return self.columnPopulatorFunctions[column](index)

    def getTextAlignmentRole(self, index):
        """ Return Text Alignment for the given cell """
        return int(Qt.AlignLeft|Qt.AlignVCenter)

    def getTransactionAmount(self, index):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            amount = transaction.amount
            cents = amount%100
            dollars = amount/100
            return QVariant("${0}.{1:{fill}2}".format(dollars, cents, fill=0))

    def getTransactionDescription(self, index):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            return QVariant(transaction.description)

    def getTransactionIncome(self, index):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            if transaction.income:
                return QVariant("Income")
            else:
                return QVariant("Expense")

    def getTransactionDate(self, index):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            return QVariant("{0:%m/%d/%Y}".format(transaction.date))

    def getTransactionForRow(self, index):
        """ Returns the Transaction in the given row """
        row = index.row()
        transactions = Transactions.all()
        if row < len(transactions):
            return transactions[row]

    def headerData(self, section, orientation, role = Qt.DisplayRole):
        """ Return Header Data """
        if role != Qt.DisplayRole:
            return None
        if Qt.Horizontal == orientation:
            if section < len(self.columns):
                return QVariant(self.columns[section])    
            return QVariant("Horizontal Header")