from db.transactions import Transactions

from PyQt4.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt

class TransactionTableModel(QAbstractTableModel):
    """ Represnts the Transaction List as a Table """

    def __init__(self):
        """ Build the Transactions Table """
        QAbstractTableModel.__init__(self)
        self.columns = ["Amount", "Description", "Type", "Date"]
        self.statusTips = ["The amount of money in the transaction.",
                           "Description of the transaction.",
                           "The Transaction type (Income/Expense).",
                           "The Date the Transaction occured."]
        self.roleResponses = {Qt.DisplayRole:self.getData,
                              Qt.EditRole:self.getData,
                              Qt.ToolTipRole:self.getTip,
                              Qt.StatusTipRole:self.getTip,
                              Qt.TextAlignmentRole:self.getTextAlignment}
        self.columnSetterFunctions = [self.setTransactionAmount,
                                      self.setTransactionDescription,
                                      self.setTransactionIncome,
                                      self.setTransactionDate]
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

    def flags(self, index):
        """ Return flags for the Transaction Table """
        return Qt.ItemIsEditable | Qt.ItemIsEnabled # | Qt.ItemIsSelectable

    def setData(self, index, value, role = Qt.EditRole):
        """ Set Data in the Transaction Table """
        column = index.column()
        if column < len(self.columnSetterFunctions):
            self.columnSetterFunctions[column](index, value)
            self.dataChanged(index, index)
            return True
        return False

    def getDataBasedOnRole(self, index, role):
        """ Get Data based on the role given """
        if role in self.roleResponses:
            return self.roleResponses[role](index)

    def getData(self, index):
        """ Return the actual Data """
        column = index.column()
        if column < len(self.columnPopulatorFunctions):
            return self.columnPopulatorFunctions[column](index)

    def getTip(self, index):
        """ Return Data for a Status or Tool Tip """
        column = index.column()
        if column < len(self.statusTips):
            return self.statusTips[column]

    def getTextAlignment(self, index):
        """ Return Text Alignment for the given cell """
        return int(Qt.AlignLeft|Qt.AlignVCenter)

    def getTransactionAmount(self, index):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None and transaction.amount is not None:
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
            if transaction.income is True:
                return QVariant("Income")
            elif transaction.income is False:
                return QVariant("Expense")

    def getTransactionDate(self, index):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            return QVariant("{0:%m/%d/%Y}".format(transaction.date))

    def setTransactionAmount(self, index, value):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None and transaction.amount is not None:
            amount = transaction.amount
            cents = amount%100
            dollars = amount/100
            return QVariant("${0}.{1:{fill}2}".format(dollars, cents, fill=0))

    def setTransactionDescription(self, index, value):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            transaction.description = str(value.toString())

    def setTransactionIncome(self, index, value):
        """ Return the amount for a particular transaction """
        transaction = self.getTransactionForRow(index)
        if transaction is not None:
            if transaction.income is True:
                return QVariant("Income")
            elif transaction.income is False:
                return QVariant("Expense")

    def setTransactionDate(self, index, value):
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