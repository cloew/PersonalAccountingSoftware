from Qt.GUI.Transaction.Table.transaction_table_widget import TransactionTableWidget

from Qt.GUI.Transaction.Table.Columns.account_column import AccountColumn
from Qt.GUI.Transaction.Table.Columns.amount_column import AmountColumn
from Qt.GUI.Transaction.Table.Columns.category_column import CategoryColumn
from Qt.GUI.Transaction.Table.Columns.date_column import DateColumn
from Qt.GUI.Transaction.Table.Columns.description_column import DescriptionColumn
from Qt.GUI.Transaction.Table.Columns.remove_subtransaction_column import RemoveSubtransactionColumn
from Qt.GUI.Transaction.Table.Columns.type_column import TypeColumn

class SubTransactionTableWidget(TransactionTableWidget):
    """ The Transaction Table Widget View for a single account """
    
    def __init__(self, transaction, parentForm, parent=None):
        """ Initialize the Transaction Table Widget """
        self.parent_transaction = transaction
        self.currentSubtransaction = None
        self.parentForm = parentForm
        TransactionTableWidget.__init__(self, parent=parent)
    
    def getColumns(self):
        """ Return the columns for use in the table """
        return [AccountColumn(callbacks=[self.updateCoreTransactionTable]),
                AmountColumn(callbacks=[self.updateCoreTransactionTable]),
                DescriptionColumn(callbacks=[self.updateCoreTransactionTable]),
                TypeColumn(callbacks=[self.updateCoreTransactionTable]),
                #CategoryColumn(callbacks=[self.updateCoreTransactionTable]),
                DateColumn(callbacks=[self.updateCoreTransactionTable])]
                #RemoveSubtransactionColumn(self)]
        
    def getTransactions(self):
        """ Return the list of transactions with filters applied """
        transactions = []
        if self.parent_transaction is not None and self.parent_transaction.subtransaction_set is not None:
            transactions = list(self.parent_transaction.subtransaction_set.transactions)
            transactions.remove(self.parent_transaction)
        return transactions
        
    def updateCoreTransactionTable(self):
        self.parentForm.table.updateTransactions()
        
    def updateTransactionOnSelectionChange(self, transaction):
        """ Update the Transactions Widget when a row is selected """
        self.currentSubtransaction = transaction
        self.parentForm.updateSubtransactionDetails()