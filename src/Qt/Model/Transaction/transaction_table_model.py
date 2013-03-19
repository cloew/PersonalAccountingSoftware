from amount_column import AmountColumn
from balance_column import BalanceColumn
from category_column import CategoryColumn
from cleared_column import ClearedColumn
from date_column import DateColumn
from description_column import DescriptionColumn
from reconciled_column import ReconciledColumn
from type_column import TypeColumn

from db.accounts import Accounts
from db.transactions import Transactions
from PySide.QtCore import Qt
from Qt.Model.table_model import TableModel

import db.transaction_filters as TransactionFilters

class TransactionTableModel(TableModel):
    """ Reprsents the Transaction List as a Table """
    transaction_retrievers = {TransactionFilters.All:Transactions.allForAccount,
                              TransactionFilters.Uncleared:Transactions.allUnclearedTransactionsForAccount,
                              TransactionFilters.Unreconciled:Transactions.allUnreconciledTransactionsForAccount}
    default_retriever = transaction_retrievers[TransactionFilters.All]

    def __init__(self):
        """ Initialize the Table Model """
        self.account = Accounts.all()[0]
        self.retriever = self.default_retriever
        self.last_count = self.rowCount(self)
        TableModel.__init__(self)

    def getColumns(self):
        """ Get the Columns for the table """
        return [AmountColumn(self.account, self.retriever),
                DescriptionColumn(self.account, self.retriever),
                TypeColumn(self.account, self.retriever),
                CategoryColumn(self.account, self.retriever),
                DateColumn(self.account, self.retriever),
                BalanceColumn(self.account, self.retriever),
                ClearedColumn(self.account, self.retriever),
                ReconciledColumn(self.account, self.retriever)]

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(self.retriever(self.account))

    def setData(self, index, value, role = Qt.EditRole):
        """ Set Data in the Transaction Table """
        dataSet = TableModel.setData(self, index, value, role)
        if dataSet:
            self.checkCount()
        return dataSet

    def setTransactionRetriever(self, transactionFilter):
        """ Set the Transaction Retriever """
        if transactionFilter in self.transaction_retrievers:
            self.retriever = self.transaction_retrievers[transactionFilter]

            for column in self.columns:
                column.transactionRetriever = self.retriever
            self.checkCount()
            
    def setAccount(self, account):
        """ Set the Transaction Account """
        self.account = account
        if account is not None:
            for column in self.columns:
                column.account = self.account
            self.checkCount()

    def checkCount(self):
        """ Check if the number of records in the table has changed """
        count = self.rowCount(self)
        if self.last_count != -1:
            if count < self.last_count:
                self.removeRows(count, self.last_count-count)
            elif count > self.last_count:
                self.insertRows(self.last_count, count-self.last_count)
        self.last_count = count
        return count