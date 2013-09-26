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
    
    def __init__(self, parent=None):
        """ Initialize the Transaction Table Widget """
        self.columns = self.getColumns()
        transactions = self.getTransactions()
        KaoTableWidget.__init__(self, transactions, self.columns, parent=parent)
        
        self.currentCellChanged.connect(self.updateOnSelectionChange)
        
    def updateTransactions(self):
        """ Update the Account for the table """
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
        
    def getColumns(self):
        """ Return the  """
        return []
    
    def getTransactions(self):
        """ Return the list of transactions with filters applied """
        return []
        
    def updateOnSelectionChange(self, currentRow, currentColumn, previousRow, previousColumn):
        """ Update the Transactions Widget when a row is selected """
        transaction = self.getCurrentTransaction(currentRow)
        self.updateTransactionOnSelectionChange(transaction)
        
    def updateTransactionOnSelectionChange(self, transaction):
        """ Update the Transactions Widget when a row is selected """
        self.updateToolbarOnCurrentSelectionChange(transaction)
        
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