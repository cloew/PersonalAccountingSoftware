from db.accounts import Accounts
from db.transactions import Transactions

from Qt.GUI.Core.kao_table_widget import KaoTableWidget

from Qt.GUI.Transaction.Table.transaction_category_delegate import TransactionCategoryDelegate
from Qt.GUI.Transaction.Table.transaction_type_delegate import TransactionTypeDelegate

from Qt.GUI.Transaction.Table.Columns.amount_column import AmountColumn
from Qt.GUI.Transaction.Table.Columns.balance_column import BalanceColumn
from Qt.GUI.Transaction.Table.Columns.category_column import CategoryColumn
from Qt.GUI.Transaction.Table.Columns.cleared_column import ClearedColumn
from Qt.GUI.Transaction.Table.Columns.date_column import DateColumn
from Qt.GUI.Transaction.Table.Columns.description_column import DescriptionColumn
from Qt.GUI.Transaction.Table.Columns.reconciled_column import ReconciledColumn
from Qt.GUI.Transaction.Table.Columns.type_column import TypeColumn

from PySide.QtCore import Qt
from PySide.QtGui import QAction

class TransactionTableWidget(KaoTableWidget):
    """ The Transaction Table Widget View """
    
    def __init__(self, transactionMenu, parent=None):
        """ Initialize the Transaction Table Widget """
        self.account = Accounts.all()[0]
        self.filters = {}
        self.columns = [AmountColumn(self), DescriptionColumn(), TypeColumn(self), CategoryColumn(), DateColumn(self), BalanceColumn(self.account), ClearedColumn(self), ReconciledColumn(self)]
        transactions = self.getTransactions()
        self.transactionMenu = transactionMenu
        KaoTableWidget.__init__(self, transactions, self.columns, parent=parent)
        
        self.currentCellChanged.connect(self.updateOnSelectionChange)
        
    def updateTransactions(self, account=None, filters=None):
        """ Update the Account for the table """
        if account is not None:
            self.account = account
        if filters is not None:
            self.filters = filters
        
        balanceColumn = self.getColumn(BalanceColumn)
        balanceColumn.account = self.account
            
        transactions = self.getTransactions()
        self.setRowCount(len(transactions))
        self.populateTable(transactions)
        
        transaction = self.getCurrentTransaction(self.currentRow())
        self.updateToolbarOnCurrentSelectionChange(transaction)
                    
    def setColumnDelegates(self):
        """ Set Column Delegates """
        self.setCategoryDelegate()
        self.setTypeDelegate()
                    
    def setCategoryDelegate(self):
        """ Set the Category Delegate """
        self.categoryDelegate = TransactionCategoryDelegate()
        self.setDelegateForColumn(self.categoryDelegate, CategoryColumn)
        
    def setTypeDelegate(self):
        """ Set the Type Delegate """
        self.typeDelegate = TransactionTypeDelegate()
        self.setDelegateForColumn(self.typeDelegate, TypeColumn)
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """
        
    def updateBalanceColumn(self):
        """ Update the Running Balance """
        balanceColumnIndex = self.getColumnIndex(BalanceColumn)
        
        for row in range(self.rowCount()):
            item = self.item(row, balanceColumnIndex)
            item.account = self.account
            item.updateData()
        
    def getTransactions(self):
        """ Return the list of transactions with filters applied """
        return Transactions.allForAccount(self.account, filters=self.filters)
        
    def updateOnSelectionChange(self, currentRow, currentColumn, previousRow, previousColumn):
        """ Update the Transactions Widget when a row is selected """
        transaction = self.getCurrentTransaction(currentRow)
        self.updateToolbarOnCurrentSelectionChange(transaction)
        self.transactionMenu.updateOnTransactionChange(transaction)
        
    def updateToolbarOnCurrentSelectionChange(self, transaction):
        """ Update the Toolbar Transfer section so it reflects the current Transaction """
        self.toolbar.updateTransfers(transaction)
        
    def getCurrentTransaction(self, currentRow):
        """ Return the currently selected Transaction """
        transactions = self.getTransactions()
        transaction = None
        if currentRow in range(len(transactions)):
            transaction = transactions[currentRow]
        return transaction