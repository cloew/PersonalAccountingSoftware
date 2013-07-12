from db.accounts import Accounts
from db.transactions import Transactions

from Qt.GUI.Core.kao_table_widget import KaoTableWidget

from Qt.GUI.Transaction.transaction_category_delegate import TransactionCategoryDelegate
from Qt.GUI.Transaction.transaction_type_delegate import TransactionTypeDelegate

from Qt.GUI.Transaction.Columns.amount_column import AmountColumn
from Qt.GUI.Transaction.Columns.balance_column import BalanceColumn
from Qt.GUI.Transaction.Columns.category_column import CategoryColumn
from Qt.GUI.Transaction.Columns.cleared_column import ClearedColumn
from Qt.GUI.Transaction.Columns.date_column import DateColumn
from Qt.GUI.Transaction.Columns.description_column import DescriptionColumn
from Qt.GUI.Transaction.Columns.reconciled_column import ReconciledColumn
from Qt.GUI.Transaction.Columns.type_column import TypeColumn

class TransactionTableWidget(KaoTableWidget):
    """ The Transaction Table Widget View """
    
    def __init__(self):
        """ Initialize the Transaction Table Widget """
        self.account = Accounts.all()[0]
        self.columns = [AmountColumn(self), DescriptionColumn(), TypeColumn(), CategoryColumn(), DateColumn(), BalanceColumn(), ClearedColumn(), ReconciledColumn()]
        transactions = Transactions.allForAccount(self.account)
        KaoTableWidget.__init__(self, transactions, self.columns)
                    
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
            item.updateData()
        