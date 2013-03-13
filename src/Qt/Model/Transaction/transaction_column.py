from db.transactions import Transactions
#from PySide.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt
from PySide.QtCore import QAbstractTableModel, QModelIndex, Qt

class TransactionColumn:
    """ Represents a column in the Transaction Table """
    header_name = "TODO: Replace with real name" # Should be overridden in Sub Class

    def getHorizontalHeader(self):
        """ Return Header Data """
        #return QVariant(self.header_name)
        return self.header_name

    def getData(self, row):
        """ Return data for the transaction in the given row """
        transaction = self.getTransactionForRow(row)
        if transaction is not None:
            return self.getDataForTransaction(transaction)

    def getDataForTransaction(self, transaction):
        """ Return data for the provided transaction.
            Should be overridden in sub class """

    def setData(self, row, value):
        """ Set the data in this column of the given transaction """
        transaction = self.getTransactionForRow(row)
        if transaction is not None:
            return self.setDataForTransaction(transaction, value)

    def setDataForTransaction(self, transaction, value):
        """ Set data for the provided transaction.
            Return whether the entry was set.
            Should be overridden in sub class. """

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row.
            Should be overridden in sub class. """

    def getTransactionForRow(self, row):
        """ Returns the Transaction in the given row """
        transactions = Transactions.all()
        if row < len(transactions):
            return transactions[row]