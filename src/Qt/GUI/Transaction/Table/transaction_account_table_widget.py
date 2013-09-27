from db.accounts import Accounts
from db.transactions import Transactions

from Qt.GUI.Transaction.Table.transaction_table_widget import TransactionTableWidget

from Qt.GUI.Transaction.Table.Columns.amount_column import AmountColumn
from Qt.GUI.Transaction.Table.Columns.balance_column import BalanceColumn
from Qt.GUI.Transaction.Table.Columns.category_column import CategoryColumn
from Qt.GUI.Transaction.Table.Columns.cleared_column import ClearedColumn
from Qt.GUI.Transaction.Table.Columns.date_column import DateColumn
from Qt.GUI.Transaction.Table.Columns.description_column import DescriptionColumn
from Qt.GUI.Transaction.Table.Columns.reconciled_column import ReconciledColumn
from Qt.GUI.Transaction.Table.Columns.type_column import TypeColumn


class TransactionAccountTableWidget(TransactionTableWidget):
    """ The Transaction Table Widget View for a single account """
    
    def __init__(self, transactionMenu, parent=None):
        """ Initialize the Transaction Table Widget """
        self.account = Accounts.all()[0]
        self.filters = {}
        self.transactionMenu = transactionMenu
        TransactionTableWidget.__init__(self, parent=parent)
        
    def updateTransactions(self, account=None, filters=None):
        """ Update the Account for the table """
        if account is not None:
            self.account = account
        if filters is not None:
            self.filters = filters
        
        balanceColumn = self.getColumn(BalanceColumn)
        balanceColumn.account = self.account
            
        TransactionTableWidget.updateTransactions(self)
        
        transaction = self.getCurrentTransaction(self.currentRow())
        self.updateTransactionOnSelectionChange(transaction)
        
    def updateBalanceColumn(self):
        """ Update the Running Balance """
        balanceColumnIndex = self.getColumnIndex(BalanceColumn)
        
        for row in range(self.rowCount()):
            item = self.item(row, balanceColumnIndex)
            item.account = self.account
            item.updateData()
    
    def getColumns(self):
        """ Return the columns for use in the table """
        return [AmountColumn(callbacks=[self.updateBalanceColumn]), DescriptionColumn(), 
                TypeColumn(self.account, callbacks=[self.updateBalanceColumn]), CategoryColumn(),
                DateColumn(callbacks=[self.updateTransactions]), BalanceColumn(self.account),
                ClearedColumn(callbacks=[self.updateTransactions]), ReconciledColumn(callbacks=[self.updateTransactions])]
        
    def getTransactions(self):
        """ Return the list of transactions with filters applied """
        return Transactions.allForAccount(self.account, filters=self.filters)
        
    def updateTransactionOnSelectionChange(self, transaction):
        """ Update the Transactions Widget when a row is selected """
        self.updateToolbarOnCurrentSelectionChange(transaction)
        self.transactionMenu.updateOnTransactionChange(transaction)
        
    def updateToolbarOnCurrentSelectionChange(self, transaction):
        """ Update the Toolbar Transfer section so it reflects the current Transaction """
        self.toolbar.updateTransfers(transaction)