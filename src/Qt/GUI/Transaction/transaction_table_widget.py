from db.accounts import Accounts
from db.transactions import Transactions

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

from PySide.QtGui import QTableWidget, QTableWidgetItem

class TransactionTableWidget(QTableWidget):
    """ The Transaction Tabel Widget View """
    
    def __init__(self):
        """ Initialize the Transaction Table Widget """
        self.account = Accounts.all()[0]
        self.columns = [AmountColumn(), DescriptionColumn(), TypeColumn(), CategoryColumn(), DateColumn(), BalanceColumn(), ClearedColumn(), ReconciledColumn()] #"Amount", "Description", "Type", "Category", "Date", "Balance", "Cleared", "Reconciled"]
        transactions = Transactions.allForAccount(self.account)
        QTableWidget.__init__(self, len(transactions), len(self.columns))
        
        self.setHorizontalHeaderLabels([column.HEADER for column in self.columns])
        self.verticalHeader().hide()
        
        self.populateTable(transactions)
        self.setColumnsDelegates()
        
    def populateTable(self, transactions):
        """ Load Transactions from the Database """
        for row in range(len(transactions)):
            for column in range(len(self.columns)):
                transaction = transactions[row]
                columnPopulator = self.columns[column]
                
                widget = columnPopulator.getWidgetForColumn(transaction)
                item = columnPopulator.getItemForColumn(transaction)
                
                if widget is not None:
                    self.setCellWidget(row, column, widget)
                elif item is not None:
                    self.setItem(row, column, item)
                    
    def setColumnsDelegates(self):
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
                    
    def setDelegateForColumn(self, delegate, columnClass):
        """ Set the Custom Delegate for a column """
        columnClasses = [column.__class__ for column in self.columns]
        index = columnClasses.index(columnClass)
        if index is not None:
            self.setItemDelegateForColumn(index, delegate)
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """
        