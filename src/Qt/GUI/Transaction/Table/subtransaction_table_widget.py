from db.transactions import Transactions
from db.subtransactions import SubTransactions

from Qt.GUI.Transaction.Table.transaction_table_widget import TransactionTableWidget

from Qt.GUI.Transaction.Table.Columns.amount_column import AmountColumn
from Qt.GUI.Transaction.Table.Columns.category_column import CategoryColumn
from Qt.GUI.Transaction.Table.Columns.date_column import DateColumn
from Qt.GUI.Transaction.Table.Columns.description_column import DescriptionColumn
from Qt.GUI.Transaction.Table.Columns.type_column import TypeColumn

class SubTransactionTableWidget(TransactionTableWidget):
    """ The Transaction Table Widget View for a single account """
    
    def __init__(self, transaction, parent=None):
        """ Initialize the Transaction Table Widget """
        self.parent_transaction = transaction
        TransactionTableWidget.__init__(self, parent=parent)
    
    def getColumns(self):
        """ Return the columns for use in the table """
        return [AmountColumn(self), DescriptionColumn(), TypeColumn(self), CategoryColumn(), DateColumn(self)]
        
    def getTransactions(self):
        """ Return the list of transactions with filters applied """
        transactions = []
        if self.parent_transaction is not None and self.parent_transaction.subtransaction_set is not None:
            transactions = list(self.parent_transaction.subtransaction_set.transactions)
            transactions.remove(self.parent_transaction)
        return transactions