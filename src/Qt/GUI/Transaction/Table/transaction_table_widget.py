from Qt.GUI.Core.kao_table_widget import KaoTableWidget

from Qt.GUI.Transaction.Table.Columns.Delegates.transaction_category_delegate import TransactionCategoryDelegate
from Qt.GUI.Transaction.Table.Columns.Delegates.transaction_type_delegate import TransactionTypeDelegate

from Qt.GUI.Transaction.Table.Columns.category_column import CategoryColumn
from Qt.GUI.Transaction.Table.Columns.type_column import TypeColumn

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
        
    def getCurrentTransaction(self, currentRow):
        """ Return the currently selected Transaction """
        transactions = self.getTransactions()
        transaction = None
        if currentRow in range(len(transactions)):
            transaction = transactions[currentRow]
        return transaction